# createAVMusicTemplateController (System API)

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## createAVMusicTemplateController

```TypeScript
function createAVMusicTemplateController(sessionId: string): AVMusicTemplateController
```

创建音频模板控制器，返回音频模板控制器对象。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-function createAVMusicTemplateController(sessionId: string): AVMusicTemplateController--><!--Device-avMusicTemplate-function createAVMusicTemplateController(sessionId: string): AVMusicTemplateController-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | AVSession对象唯一的会话标识。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AVMusicTemplateController](arkts-avsession-avmusictemplate-avmusictemplatecontroller-c.md) | 音频模板控制器实例，用于与接入音频模板的媒体应用进行数据交互。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function createAVMusicTemplateController can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000002 | Failed to create the AVMusicTemplate controller. |
| 201 | Permission verify failed. |
| 202 | Not System App. |

