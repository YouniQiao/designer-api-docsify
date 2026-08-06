# @ohos.app.form.FormExtensionAbility

The **FormExtensionAbility** module provides lifecycle callbacks invoked when a widget is created, destroyed, or
 updated.
 > **NOTE**
 > - The formExtensionAbility is cleared after 10 seconds of inactivity.
 > - The following modules cannot be referenced in the FormExtensionAbility, as doing so may cause the program to exit
 >  abnormally:
 >   - @ohos.ability.particleAbility (ParticleAbility)
 >   - @ohos.multimedia.audio (Audio Management)
 >   - @ohos.multimedia.camera (Camera Management)
 >   - @ohos.multimedia.media (Media)
 >   - @ohos.resourceschedule.backgroundTaskManager (Background Task Management)


## Summary

### Classes

| Name | Description |
| --- | --- |
| [FormExtensionAbility](arkts-form-app-form-formextensionability-formextensionability-c.md) | Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed. |

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [FormExtensionAbility](arkts-form-app-form-formextensionability-formextensionability-c-sys.md) | Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [OnAcquireFormStateFn](arkts-form-onacquireformstatefn-t.md) | Called to return a \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ object.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_You must override this callback if you want this ability to return the actual form state. Otherwise,this method returns \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ by default.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_3\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ |
| [OnStopFn](arkts-form-onstopfn-t.md) | Called when this ability breaks the last link, notifying the provider that the provider process is about to stop. |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [OnAcquireFormDataFn](arkts-form-onacquireformdatafn-t-sys.md) | Called when the system acquire the form data. |
| [OnShareFormFn](arkts-form-onshareformfn-t-sys.md) | Called when the system shares the form. |
<!--DelEnd-->

