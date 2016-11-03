//
// Created by austin on 10/30/16.
//

#include <X11/Xlib.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    Display *display;

    /* open the connection to the display "simey:0". */
    display = XOpenDisplay("simey:0");
    if (display == NULL)
    {
        fprintf(stderr, "Cannot connect to X server %s\n", "simey:0");
        exit(-1);
    }
    else
    {
        printf("Success!");
    }
}