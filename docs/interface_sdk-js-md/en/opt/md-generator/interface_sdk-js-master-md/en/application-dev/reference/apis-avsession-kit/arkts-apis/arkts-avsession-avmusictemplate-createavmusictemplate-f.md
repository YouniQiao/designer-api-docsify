# createAVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from '@kit.AVSessionKit';
```

## createAVMusicTemplate

```TypeScript
function createAVMusicTemplate(accessType: AVMusicTemplateType): AVMusicTemplate
```

Create an AVMusicTemplate instance.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-function createAVMusicTemplate(accessType: AVMusicTemplateType): AVMusicTemplate--><!--Device-avMusicTemplate-function createAVMusicTemplate(accessType: AVMusicTemplateType): AVMusicTemplate-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [accessType](../../apis-telephony-kit/arkts-apis/arkts-telephony-esim-accessrule-i.md) | [AVMusicTemplateType](arkts-avsession-avmusictemplate-avmusictemplatetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AVMusicTemplate](arkts-avsession-avmusictemplate-avmusictemplate-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000001-audio-template-creation-failure) |
