# offAVMusicTemplateDestroy (System API)

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'avMusicTemplate';
```

## offAVMusicTemplateDestroy

```TypeScript
function offAVMusicTemplateDestroy(callback?: Callback<AVMusicTemplateDescriptor>): void
```

UnRegister session destroy event

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-function offAVMusicTemplateDestroy(callback?: Callback<AVMusicTemplateDescriptor>): void--><!--Device-avMusicTemplate-function offAVMusicTemplateDestroy(callback?: Callback<AVMusicTemplateDescriptor>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVMusicTemplateDescriptor](arkts-avsession-avmusictemplate-avmusictemplatedescriptor-i-sys.md)&gt; | No | Used to handle 'sessionDestroy' command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.function offAVMusicTemplateDestroy can not work correctly due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verify failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

