# onAVMusicTemplateCreate (System API)

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## onAVMusicTemplateCreate

```TypeScript
function onAVMusicTemplateCreate(callback: Callback<AVMusicTemplateDescriptor>): void
```

注册音频模板创建的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-function onAVMusicTemplateCreate(callback: Callback<AVMusicTemplateDescriptor>): void--><!--Device-avMusicTemplate-function onAVMusicTemplateCreate(callback: Callback<AVMusicTemplateDescriptor>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVMusicTemplateDescriptor&gt; | Yes | 回调函数，参数为音频模板描述。用于监听音频模板创建事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onAVMusicTemplateCreate can not work correctly due to limited device capabilities. |
| 201 | Permission verify failed. |
| 202 | Not System App. |

