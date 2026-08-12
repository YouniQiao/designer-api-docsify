# createAVAdsController

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## createAVAdsController

```TypeScript
function createAVAdsController(player: AVPlayer): Promise<AVAdsController | undefined>
```

Create an ad playback controller associated with the player instance.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-media-function createAVAdsController(player: AVPlayer): Promise<AVAdsController | undefined>--><!--Device-media-function createAVAdsController(player: AVPlayer): Promise<AVAdsController | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| player | [AVPlayer](arkts-media-media-avplayer-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVAdsController](arkts-media-media-avadscontroller-i.md) \| undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400108](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |
