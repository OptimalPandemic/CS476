set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Werror")

set(SOURCE_FILES draw.c ccp.c)

add_executable(draw ${SOURCE_FILES})

target_link_libraries(draw "-lX11 -lXm -lXt")