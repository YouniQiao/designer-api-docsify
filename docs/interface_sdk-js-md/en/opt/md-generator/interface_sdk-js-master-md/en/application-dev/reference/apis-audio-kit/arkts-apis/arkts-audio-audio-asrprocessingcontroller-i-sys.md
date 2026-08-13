# AsrProcessingController (System API)

ASR processing controller.

**Since:** 23

**Deprecated since:** -1

<!--Device-audio-interface AsrProcessingController--><!--Device-audio-interface AsrProcessingController-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## getAsrAecMode

```TypeScript
getAsrAecMode(): AsrAecMode
```

Get ASR AEC mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-AsrProcessingController-getAsrAecMode(): AsrAecMode--><!--Device-AsrProcessingController-getAsrAecMode(): AsrAecMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AsrAecMode](arkts-audio-audio-asraecmode-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |

## Examples

```TypeScript
let mode = asrProcessingController.getAsrAecMode();
```

## getAsrNoiseSuppressionMode

```TypeScript
getAsrNoiseSuppressionMode(): AsrNoiseSuppressionMode
```

Get ASR noise suppression mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-AsrProcessingController-getAsrNoiseSuppressionMode(): AsrNoiseSuppressionMode--><!--Device-AsrProcessingController-getAsrNoiseSuppressionMode(): AsrNoiseSuppressionMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AsrNoiseSuppressionMode](arkts-audio-audio-asrnoisesuppressionmode-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |

## Examples

```TypeScript
let mode = asrProcessingController.getAsrNoiseSuppressionMode();
```

## getAsrWhisperDetectionMode

```TypeScript
getAsrWhisperDetectionMode(): AsrWhisperDetectionMode
```

Get ASR whisper detection mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-AsrProcessingController-getAsrWhisperDetectionMode(): AsrWhisperDetectionMode--><!--Device-AsrProcessingController-getAsrWhisperDetectionMode(): AsrWhisperDetectionMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AsrWhisperDetectionMode](arkts-audio-audio-asrwhisperdetectionmode-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |

## Examples

```TypeScript
let mode = asrProcessingController.getAsrWhisperDetectionMode();
```

## isWhispering

```TypeScript
isWhispering(): boolean
```

Query whether user is whispering.

**Since:** 23

**Deprecated since:** -1

<!--Device-AsrProcessingController-isWhispering(): boolean--><!--Device-AsrProcessingController-isWhispering(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |

## Examples

```TypeScript
let flag = asrProcessingController.isWhispering();
```

## setAsrAecMode

```TypeScript
setAsrAecMode(mode: AsrAecMode): boolean
```

Set ASR AEC mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-AsrProcessingController-setAsrAecMode(mode: AsrAecMode): boolean--><!--Device-AsrProcessingController-setAsrAecMode(mode: AsrAecMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AsrAecMode](arkts-audio-audio-asraecmode-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |

## Examples

```TypeScript
let flag = asrProcessingController.setAsrAecMode(audio.AsrAecMode.BYPASS);
```

## setAsrNoiseSuppressionMode

```TypeScript
setAsrNoiseSuppressionMode(mode: AsrNoiseSuppressionMode): boolean
```

Set ASR noise suppression mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-AsrProcessingController-setAsrNoiseSuppressionMode(mode: AsrNoiseSuppressionMode): boolean--><!--Device-AsrProcessingController-setAsrNoiseSuppressionMode(mode: AsrNoiseSuppressionMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AsrNoiseSuppressionMode](arkts-audio-audio-asrnoisesuppressionmode-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |

## Examples

```TypeScript
let flag = asrProcessingController.setAsrNoiseSuppressionMode(audio.AsrNoiseSuppressionMode.BYPASS);
```

## setAsrVoiceControlMode

```TypeScript
setAsrVoiceControlMode(mode: AsrVoiceControlMode, enable: boolean): boolean
```

Set ASR voice control mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-AsrProcessingController-setAsrVoiceControlMode(mode: AsrVoiceControlMode, enable: boolean): boolean--><!--Device-AsrProcessingController-setAsrVoiceControlMode(mode: AsrVoiceControlMode, enable: boolean): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AsrVoiceControlMode](arkts-audio-audio-asrvoicecontrolmode-e-sys.md) | Yes |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |

## Examples

```TypeScript
let flag = asrProcessingController.setAsrVoiceControlMode(audio.AsrVoiceControlMode.AUDIO_2_VOICE_TX, true);
```

## setAsrVoiceMuteMode

```TypeScript
setAsrVoiceMuteMode(mode: AsrVoiceMuteMode, enable: boolean): boolean
```

Set ASR voice mute mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-AsrProcessingController-setAsrVoiceMuteMode(mode: AsrVoiceMuteMode, enable: boolean): boolean--><!--Device-AsrProcessingController-setAsrVoiceMuteMode(mode: AsrVoiceMuteMode, enable: boolean): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AsrVoiceMuteMode](arkts-audio-audio-asrvoicemutemode-e-sys.md) | Yes |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |

## Examples

```TypeScript
let flag = asrProcessingController.setAsrVoiceMuteMode(audio.AsrVoiceMuteMode.OUTPUT_MUTE, true);
```

## setAsrWhisperDetectionMode

```TypeScript
setAsrWhisperDetectionMode(mode: AsrWhisperDetectionMode): boolean
```

Set ASR whisper detection mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-AsrProcessingController-setAsrWhisperDetectionMode(mode: AsrWhisperDetectionMode): boolean--><!--Device-AsrProcessingController-setAsrWhisperDetectionMode(mode: AsrWhisperDetectionMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AsrWhisperDetectionMode](arkts-audio-audio-asrwhisperdetectionmode-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |

## Examples

```TypeScript
let flag = asrProcessingController.setAsrWhisperDetectionMode(audio.AsrWhisperDetectionMode.BYPASS);
```
