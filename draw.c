//
// Created by austin on 10/30/16.
//

#include <X11/Xlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <X11/Xutil.h>
#include <memory.h>
#include <math.h>

#define PI 3.14159265

void close(Display *display, Window window)
{
    XDestroyWindow(display, window);
    XCloseDisplay(display);
}

int run()
{
    Display *display;
    Window root, window;
    unsigned long fgcolor, bgcolor;
    int screen, pointx, pointy;
    int x1, y1, x2, y2;
    int firstclick = 1;
    //double val = PI / 180;
    long eventmask = ButtonPressMask | KeyPressMask;
    XEvent event;
    XGCValues gcval;
    GC draw, drawBlack;
    Colormap cmap;
    XColor color, ignore;
    char* colorname = "red";

    char buffer[20];
    int bufsize=20;
    KeySym keysym;
    XComposeStatus statinout;
    int charcount, radius;

    if(!(display = XOpenDisplay(NULL)))
    {
        perror("XOpenDisplay");
        return 1;
    }

    root = RootWindow(display, screen = DefaultScreen(display));

    fgcolor = BlackPixel(display, screen);
    bgcolor = WhitePixel(display, screen);

    window = XCreateSimpleWindow(display, root, 0, 0, 200, 200, 2, fgcolor, bgcolor);

    cmap = DefaultColormap(display, screen);
    XAllocNamedColor(display, cmap, colorname, &color, &ignore);
    fgcolor = color.pixel;
    gcval.foreground = fgcolor;
    gcval.background = bgcolor;
    draw = XCreateGC(display, window, GCForeground|GCBackground, &gcval);

    gcval.foreground = BlackPixel(display, screen);
    gcval.background = WhitePixel(display, screen);
    drawBlack = XCreateGC(display, window, GCForeground|GCBackground, &gcval);

    XSelectInput(display, window, eventmask);
    XMapWindow(display, window);

    for(;;)
    {
        XWindowEvent(display, window, eventmask, &event);


        switch (event.type) {
            case Expose:
                XClearWindow(display, window);
                break;
            case ButtonPress:
                pointx = event.xbutton.x;
                pointy = event.xbutton.y;

                XFillArc(display, window, drawBlack, pointx - 2, pointy - 2, (unsigned int)(2 * 2), (unsigned int)(2 * 2), 0, 360 * 64);
                if(firstclick)
                {
                    firstclick = 0;
                    x1 = pointx;
                    y1 = pointy;
                }
                else
                {
                    x2 = pointx;
                    y2 = pointy;
                    radius = (int) sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));
                    XDrawArc(display, window, draw, x1-(radius), y1-(radius), radius*2, radius*2, 0, 360*64);
                    firstclick = 1;

                    XPoint points[5];
                    for( int i=0; i<5; ++i )
                    {
                        points[i].x = x1 + radius * sin(2 * PI * i / 5 + PI / 5);
                        points[i].y = y1 - radius * cos(2 * PI * i / 5 + PI / 5);
                    }
                    /*points[0].x = x1 + sin(36*val) / radius;
                    points[0].y = y1 - cos(36*val) / radius;
                    points[1].x =
                    points[1].x =
                    points[2].x = x1 + radius;
                    points[2].y = y1 + radius;*/


                    XFillPolygon(display, window, draw, points, 5, Complex, CoordModePrevious);
                    XDrawLines(display, window, drawBlack, points, 5, CoordModePrevious);
                }

                break;
            case KeyPress:
                charcount = XLookupString(&(event.xkey), buffer, bufsize, &keysym, &statinout);
                buffer[charcount] = '\0';
                if(strcmp(buffer, "c") == 0)
                {
                    XClearWindow(display, window);
                    break;
                }
                if(strcmp(buffer, "q") == 0)
                {
                    close(display, window);
                    return 0;
                }
            default:
                fprintf(stderr, "Unexpected event: %d\n", event.type);
        }
    }
}