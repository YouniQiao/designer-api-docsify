# createAVMusicTemplateController (System API)

## Modules to Import

```TypeScript
import { avMusicTemplate } from '@kit.AVSessionKit';
```

## createAVMusicTemplateController

```TypeScript
function createAVMusicTemplateController(sessionId: string): AVMusicTemplateController
```

Create AVMusicTemplate controller instance.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-function createAVMusicTemplateController(sessionId: string): AVMusicTemplateController--><!--Device-avMusicTemplate-function createAVMusicTemplateController(sessionId: string): AVMusicTemplateController-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AVMusicTemplateController](arkts-avsession-avmusictemplate-avmusictemplatecontroller-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000002-audio-template-controller-creation-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
