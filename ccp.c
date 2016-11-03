#include <Xm/Xm.h> 
#include <Xm/PushB.h>
#include <stdlib.h>


void push(Widget , XtPointer ,
               XmPushButtonCallbackStruct *);


int main(int argc, char **argv)
{
    Widget top_wid, button;
    XtAppContext  app;

    top_wid = XtVaAppInitialize(&app, "Push", NULL, 0,
                                &argc, argv, NULL, NULL);

    button = XmCreatePushButton(top_wid, "Run Python", NULL, 0);
    XtManageChild(button);

    XtAddCallback(button, XmNactivateCallback, push, NULL);

    XtRealizeWidget(top_wid);
    XtAppMainLoop(app);

}

void push(Widget w, XtPointer client_data,
               XmPushButtonCallbackStruct *cbs)
{
    system("./pydraw.pyo");
}