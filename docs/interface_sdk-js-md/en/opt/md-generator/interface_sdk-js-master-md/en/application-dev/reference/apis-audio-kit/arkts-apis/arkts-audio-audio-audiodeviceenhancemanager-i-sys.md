# AudioDeviceEnhanceManager

Provides enhanced audio device management capabilities.

**Since:** 26.0.0

<!--Device-audio-interface AudioDeviceEnhanceManager--><!--Device-audio-interface AudioDeviceEnhanceManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.DeviceEnhance

## Modules to Import

```TypeScript
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
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioManager = audio.getAudioManager();
let deviceEnhanceManager = audioManager.getDeviceEnhanceManager();

deviceEnhanceManager.getSoundCardInfo().then((soundCardInfo: audio.SoundCardInfo) => {
  console.info(`Successfully obtained sound card info: ${JSON.stringify(soundCardInfo, null, 2)}`);
})
.catch((err: BusinessError) => {
  console.error(`Failed to get sound card info. Code: ${err.code}, Message: ${err.message}`);
});
```
