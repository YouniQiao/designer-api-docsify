# @ohos.app.form.FormExtensionAbility

## Modules to Import

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [FormExtensionAbility](arkts-form-app-form-formextensionability-formextensionability-c.md) | Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed. |

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [FormExtensionAbility](arkts-form-app-form-formextensionability-formextensionability-c-sys.md) | Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [OnAcquireFormStateFn](arkts-form-onacquireformstatefn-t.md) | Called to return a FormState object. <p>You must override this callback if you want this ability to return the actual form state. Otherwise, this method returns DEFAULT by default.</p> |
| [OnStopFn](arkts-form-onstopfn-t.md) | Called when this ability breaks the last link, notifying the provider that the provider process is about to stop. |

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [OnAcquireFormDataFn](arkts-form-onacquireformdatafn-t-sys.md) | Called when the system acquire the form data. |
| [OnShareFormFn](arkts-form-onshareformfn-t-sys.md) | Called when the system shares the form. |
<!--DelEnd-->

