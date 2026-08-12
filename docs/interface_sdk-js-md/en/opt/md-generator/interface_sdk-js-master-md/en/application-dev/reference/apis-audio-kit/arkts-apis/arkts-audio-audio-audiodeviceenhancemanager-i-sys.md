# AudioDeviceEnhanceManager

Provides enhanced audio device management capabilities.

**Since:** 26.0.0

<!--Device-audio-interface AudioDeviceEnhanceManager--><!--Device-audio-interface AudioDeviceEnhanceManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.DeviceEnhance

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## getSoundCardInfo

```TypeScript
getSoundCardInfo(): Promise<SoundCardInfo>
```

Obtains the sound card information. This method uses a Promise to return the query result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioDeviceEnhanceManager-getSoundCardInfo(): Promise<SoundCardInfo>--><!--Device-AudioDeviceEnhanceManager-getSoundCardInfo(): Promise<SoundCardInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.DeviceEnhance

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SoundCardInfo](arkts-audio-audio-soundcardinfo-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
