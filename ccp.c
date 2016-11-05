#include <Xm/Xm.h> 
#include <Xm/Separator.h>
#include <Xm/PushB.h>
#include <Xm/BulletinB.h>
#include <stdlib.h>

#include "draw.h"


void push(Widget , XtPointer ,
               XmPushButtonCallbackStruct *);
void pushC(Widget w, XtPointer client_data, XmPushButtonCallbackStruct *cbs);


int main(int argc, char **argv)
{
    Widget top_wid, button, button2, bb;
    Arg al[10];
    XtAppContext app;
    int ac;

    top_wid = XtVaAppInitialize(&app, "Push", NULL, 0,
                                &argc, argv, NULL, NULL);

    /* create a bulletin board to hold widgets */
    ac=0;
    bb = XtCreateManagedWidget("bb",xmBulletinBoardWidgetClass,
                             top_wid, al, ac);
    ac = 0;
    button = XmCreatePushButton(bb, "Run Python", NULL, 0);

    ac = 0;
    button2 = XmCreatePushButton(bb, "Run C", NULL, 0);

    XtManageChild(button);
    XtManageChild(button2);
    XtAddCallback(button, XmNactivateCallback, (XtCallbackProc) push, NULL);
    XtAddCallback(button2, XmNactivateCallback, (XtCallbackProc) pushC, NULL);

    ac=0;
    XtSetArg(al[ac],XmNx,10); ac++;
    XtSetArg(al[ac],XmNy,10); ac++;
    XtSetValues(button, al, ac);

    ac=0;
    XtSetArg(al[ac],XmNx,10); ac++;
    XtSetArg(al[ac],XmNy,150); ac++;
    XtSetValues(button2, al, ac);

    XtRealizeWidget(top_wid);
    XtAppMainLoop(app);

}

void push(Widget w, XtPointer client_data,
               XmPushButtonCallbackStruct *cbs)
{
    system("./draw.pyo");
}

void pushC(Widget w, XtPointer client_data, XmPushButtonCallbackStruct *cbs)
{
    run();
}