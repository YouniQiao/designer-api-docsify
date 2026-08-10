# offAVMusicTemplateCreate (System API)

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## offAVMusicTemplateCreate

```TypeScript
function offAVMusicTemplateCreate(callback?: Callback<AVMusicTemplateDescriptor>): void
```

注销音频模板创建监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-function offAVMusicTemplateCreate(callback?: Callback<AVMusicTemplateDescriptor>): void--><!--Device-avMusicTemplate-function offAVMusicTemplateCreate(callback?: Callback<AVMusicTemplateDescriptor>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVMusicTemplateDescriptor&gt; | No | 回调函数，返回音频模板描述。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offAVMusicTemplateCreate can not work correctly due to limited device capabilities. |
| 201 | Permission verify failed. |
| 202 | Not System App. |

