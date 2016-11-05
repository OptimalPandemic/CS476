cmake_minimum_required(VERSION 3.6)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "/home/austin/CS476/A3")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Werror")
set(SOURCE_FILES draw.c ccp.c)

execute_process(COMMAND python -O -m compileall /home/austin/ClionProjects/CS476 && mv /home/austin/ClionProjects/CS476/draw.pyo /home/austin/CS476/A3/draw.pyo && chmod +x /home/austin/CS476/A3/draw.pyo)

add_executable(ccp ${SOURCE_FILES})
target_link_libraries(ccp "-lX11 -lXm -lXt -lm")

