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


## 导入模块

```TypeScript
import { FormExtensionAbility } from 'kits/@kit.FormKit';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [FormExtensionAbility](arkts-form-app-form-formextensionability-formextensionability-c.md) | Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed. |

<!--Del-->
### 类（系统接口）

| 名称 | 说明 |
| --- | --- |
| [FormExtensionAbility](arkts-form-app-form-formextensionability-formextensionability-c-sys.md) | Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed. |
<!--DelEnd-->

### 类型

| 名称 | 说明 |
| --- | --- |
| [OnAcquireFormStateFn](arkts-form-onacquireformstatefn-t.md) | Called to return a {@link FormState} object.&lt;p&gt;You must override this callback if you want this ability to return the actual form state. Otherwise,this method returns {@link FormState#DEFAULT} by default.&lt;/p&gt; |
| [OnStopFn](arkts-form-onstopfn-t.md) | Called when this ability breaks the last link, notifying the provider that the provider process is about to stop. |

<!--Del-->
### 类型（系统接口）

| 名称 | 说明 |
| --- | --- |
| [OnAcquireFormDataFn](arkts-form-onacquireformdatafn-t-sys.md) | Called when the system acquire the form data. |
| [OnShareFormFn](arkts-form-onshareformfn-t-sys.md) | Called when the system shares the form. |
<!--DelEnd-->

