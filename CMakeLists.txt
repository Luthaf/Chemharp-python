cmake_minimum_required(VERSION 3.16)

# Prevent CMake from looking for a C and a C++ compilers, as we might not
# need them. They will be found by cmake if we are using the internal chemfiles
project(chemfiles-python NONE)

option(CHFL_PY_INTERNAL_CHEMFILES "Use the internal version of chemfiles" OFF)

if(NOT ${CHFL_PY_INTERNAL_CHEMFILES})
    find_package(chemfiles CONFIG QUIET 0.10)
endif()

file(REMOVE ${PROJECT_SOURCE_DIR}/chemfiles/external.py)

if(${chemfiles_FOUND})
    set(CHEMFILES_VERSION "${chemfiles_VERSION}")
    get_target_property(CHEMFILES_TYPE chemfiles TYPE)
    if (NOT "${CHEMFILES_TYPE}" STREQUAL "SHARED_LIBRARY")
        message(FATAL_ERROR
            "We can only use a shared library build of chemfiles.\n"
            "Found a ${CHEMFILES_TYPE} build at ${CHEMFILES_LOCATION}\n"
            "Define CHFL_PY_INTERNAL_CHEMFILES=ON to use use the internal build instead."
        )
    endif()

    # Get the path to the chemfiles library. Instead of using the actual full
    # path to the library, we want to use the path to the symlink containing
    # only the SONAME/SOVERSION. For example, instead of the actual file
    # `/usr/local/lib/libchemfiles.0.11.3.dylib`, we want the symlink
    # `/usr/local/lib/libchemfiles.0.11.dylib`. This allows the same python
    # package to load different bugfix versions of chemfiles when loading an
    # external library.
    get_target_property(CHEMFILES_FULL_LOCATION chemfiles LOCATION)
    get_target_property(CHEMFILES_SONAME chemfiles IMPORTED_SONAME)
    if(NOT "${CHEMFILES_SONAME}" STREQUAL "CHEMFILES_SONAME-NOTFOUND")
        get_filename_component(CHEMFILES_SOLINK ${CHEMFILES_SONAME} NAME)
        get_filename_component(CHEMFILES_DIR ${CHEMFILES_FULL_LOCATION} DIRECTORY)
        set(CHEMFILES_LOCATION ${CHEMFILES_DIR}/${CHEMFILES_SOLINK})
    else()
        # if chemfiles does not define a SONAME (chemfiles <0.10.2 or on windows)
        # then use the full path
        set(CHEMFILES_LOCATION ${CHEMFILES_FULL_LOCATION})
    endif()

    if (EXISTS ${CHEMFILES_LOCATION})
        message(STATUS "Using external chemfiles ${CHEMFILES_VERSION} at ${CHEMFILES_LOCATION}")
    else()
        message(FATAL_ERROR "Missing symbolic link to ${CHEMFILES_FULL_LOCATION}, expected it at ${CHEMFILES_LOCATION}")
    endif()

    file(WRITE ${PROJECT_SOURCE_DIR}/src/chemfiles/external.py
        "EXTERNAL_CHEMFILES = \"${CHEMFILES_LOCATION}\"\n"
    )

    install(CODE "message(STATUS \"nothing to install\")")
else()
    # Use the git submodule
    if(NOT EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/lib/CMakeLists.txt")
        message(FATAL_ERROR
            "The git submodule for chemfiles is not initalized.\n"
            "Please run `git submodule update --init`"
        )
    endif()

    if (MSVC)
        set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /LTCG")
        set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} /LTCG")
        set(CMAKE_SHARED_LINKER_FLAGS_RELEASE "${CMAKE_SHARED_LINKER_FLAGS_RELEASE} /LTCG")
    endif()

    message(STATUS "Using internal chemfiles from ${CMAKE_CURRENT_SOURCE_DIR}/lib")
    set(BUILD_SHARED_LIBS ON CACHE BOOL "Build shared libraries instead of static ones" FORCE)
    add_subdirectory(lib EXCLUDE_FROM_ALL)

    add_custom_target(build_chemfiles ALL)
    add_dependencies(build_chemfiles chemfiles)

    # unset VERSION and SOVERSION to make sure only one copy of libchemfiles
    # is included in the wheels
    set_property(TARGET chemfiles PROPERTY VERSION)
    set_property(TARGET chemfiles PROPERTY SOVERSION)

    install(TARGETS chemfiles
        LIBRARY DESTINATION "chemfiles"
        RUNTIME DESTINATION "chemfiles"
    )
endif()
