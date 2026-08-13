# getAllAVMusicTemplateDescriptors (System API)

## Modules to Import

```TypeScript
import { avMusicTemplate } from '@kit.AVSessionKit';
```

## getAllAVMusicTemplateDescriptors

```TypeScript
function getAllAVMusicTemplateDescriptors(userId?: number): AVMusicTemplateDescriptor[]
```

Get all AVMusicTemplate descriptors.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-function getAllAVMusicTemplateDescriptors(userId?: int): AVMusicTemplateDescriptor[]--><!--Device-avMusicTemplate-function getAllAVMusicTemplateDescriptors(userId?: int): AVMusicTemplateDescriptor[]-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AVMusicTemplateDescriptor](arkts-avsession-avmusictemplate-avmusictemplatedescriptor-i-sys.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
