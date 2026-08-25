# createAsrProcessingController (System API)

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## createAsrProcessingController

```TypeScript
function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController
```

Create ASR processing controller on one audio capturer.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| audioCapturer | [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AsrProcessingController](arkts-audio-audio-asrprocessingcontroller-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |
