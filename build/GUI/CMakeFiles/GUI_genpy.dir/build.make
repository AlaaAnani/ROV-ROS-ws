# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/alaa/rov_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/alaa/rov_ws/build

# Utility rule file for GUI_genpy.

# Include the progress variables for this target.
include GUI/CMakeFiles/GUI_genpy.dir/progress.make

GUI_genpy: GUI/CMakeFiles/GUI_genpy.dir/build.make

.PHONY : GUI_genpy

# Rule to build all files generated by this target.
GUI/CMakeFiles/GUI_genpy.dir/build: GUI_genpy

.PHONY : GUI/CMakeFiles/GUI_genpy.dir/build

GUI/CMakeFiles/GUI_genpy.dir/clean:
	cd /home/alaa/rov_ws/build/GUI && $(CMAKE_COMMAND) -P CMakeFiles/GUI_genpy.dir/cmake_clean.cmake
.PHONY : GUI/CMakeFiles/GUI_genpy.dir/clean

GUI/CMakeFiles/GUI_genpy.dir/depend:
	cd /home/alaa/rov_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/alaa/rov_ws/src /home/alaa/rov_ws/src/GUI /home/alaa/rov_ws/build /home/alaa/rov_ws/build/GUI /home/alaa/rov_ws/build/GUI/CMakeFiles/GUI_genpy.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : GUI/CMakeFiles/GUI_genpy.dir/depend

