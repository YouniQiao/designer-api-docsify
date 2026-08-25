# createMicInAudioCapturer (System API)

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## createMicInAudioCapturer

```TypeScript
function createMicInAudioCapturer(config: AudioCapturerMicInConfig): Promise<AudioCapturer | null>
```

Obtains a special [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) instance. This method uses a promise to return the capturer instance. This capture can be used to record both Mic-In audio data and echo reference signal, for application to process algorithm. Mic-In audio data and echo reference signal will be put in one buffer or multiple buffers according to configuration set by application. Capturer is also not allowed to be created when application is in background.

**Since:** 23

**Required permissions:** ohos.permission.MICROPHONE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [AudioCapturerMicInConfig](arkts-audio-audio-audiocapturermicinconfig-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioCapturer](arkts-audio-audio-audiocapturer-i.md) \| null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |
| [6800301](../errorcode-audio.md#6800301-system-error) |
