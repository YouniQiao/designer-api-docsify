# AudioCapturer

This interface provides APIs for audio capture.

Before calling any API in AudioCapturer, you must use  
[createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md#createaudiocapturer)to create an AudioCapturer instance.

> **NOTE：**
> 
> - The initial APIs of this interface are supported since API version 8.

**Since:** 8

<!--Device-audio-interface AudioCapturer--><!--Device-audio-interface AudioCapturer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## offReadMicInData

```TypeScript
offReadMicInData(callback?: Callback<AudioCapturerMicInData>): void
```

Unsubscribes from micIn audio data callback.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-offReadMicInData(callback?: Callback<AudioCapturerMicInData>): void--><!--Device-AudioCapturer-offReadMicInData(callback?: Callback<AudioCapturerMicInData>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioCapturerMicInData&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onReadMicInData

```TypeScript
onReadMicInData(callback: Callback<AudioCapturerMicInData>): void
```

Subscribes to micIn audio data callback. This callback has higher priority than 'readData' callback.If this callback and 'readData' callback are both subscribed, only this callback will be triggered.See {@link #onReadData} for more details.The event is triggered when an audio buffer is available for reading more data.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-onReadMicInData(callback: Callback<AudioCapturerMicInData>): void--><!--Device-AudioCapturer-onReadMicInData(callback: Callback<AudioCapturerMicInData>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioCapturerMicInData&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setInputDeviceToAccessory

```TypeScript
setInputDeviceToAccessory(): void
```

Sets default input device of this Capturer to DEVICE_TYPE_ACCESSORY.Other capturers' devices will not be affected by this method.This method can only be used before the capture stream starts. Besides,if audio accessory is not connected, this method will report fail. After calling this function, the input device of this capturer will not be affected by other interfaces.

**Since:** 19

<!--Device-AudioCapturer-setInputDeviceToAccessory(): void--><!--Device-AudioCapturer-setInputDeviceToAccessory(): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
