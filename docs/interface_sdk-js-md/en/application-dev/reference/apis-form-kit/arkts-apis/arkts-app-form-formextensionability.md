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


## Modules to Import

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FormExtensionAbility](arkts-form-app-form-formextensionability-formextensionability-c.md) |

<!--Del-->
### Classes(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FormExtensionAbility](arkts-form-app-form-formextensionability-formextensionability-c-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [OnAcquireFormStateFn](arkts-form-onacquireformstatefn-t.md) |
| [OnStopFn](arkts-form-onstopfn-t.md) |

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [OnAcquireFormDataFn](arkts-form-onacquireformdatafn-t-sys.md) |
| [OnShareFormFn](arkts-form-onshareformfn-t-sys.md) |
<!--DelEnd-->
