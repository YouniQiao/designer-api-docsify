# AudioCapturer

提供音频采集的相关接口。

在使用AudioCapturer的接口之前，需先通过[createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md#createaudiocapturer)获取AudioCapturer实例。

> **说明：**
> 
> - 本Interface首批接口从API version 8开始支持。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

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

取消订阅micIn音频数据回调。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-offReadMicInData(callback?: Callback<AudioCapturerMicInData>): void--><!--Device-AudioCapturer-offReadMicInData(callback?: Callback<AudioCapturerMicInData>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioCapturerMicInData&gt; | No | 用于读取缓冲的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800103 | Operation not permitted at running state. |
| 6800101 | Parameter verification failed. |
| 202 | Caller is not a system application. |

## onReadMicInData

```TypeScript
onReadMicInData(callback: Callback<AudioCapturerMicInData>): void
```

订阅micIn音频数据回调。此回调的优先级高于“readData”回调。如果此回调和'readData'回调都被订阅，则仅此回调将被调用。有关更多详细信息，请参见{@link #onReadData}。当有音频缓冲可用于读取更多数据时，触发该事件。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-onReadMicInData(callback: Callback<AudioCapturerMicInData>): void--><!--Device-AudioCapturer-onReadMicInData(callback: Callback<AudioCapturerMicInData>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioCapturerMicInData&gt; | Yes | 读取缓冲的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800103 | Operation not permitted at running state. |
| 202 | Caller is not a system application. |

## setInputDeviceToAccessory

```TypeScript
setInputDeviceToAccessory(): void
```

Sets default input device of this Capturer to DEVICE_TYPE_ACCESSORY.Other capturers' devices will not be affected by this method.This method can only be used before the capture stream starts. Besides,if audio accessory is not connected, this method will report fail. After calling this function, the input device of this capturer will not be affected by other interfaces.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-AudioCapturer-setInputDeviceToAccessory(): void--><!--Device-AudioCapturer-setInputDeviceToAccessory(): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800103 | Operation not permit at current state. |
| 202 | Caller is not a system application. |

