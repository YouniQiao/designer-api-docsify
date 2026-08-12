# AudioCapturer

This interface provides APIs for audio capture.

Before calling any API in AudioCapturer, you must use  
[createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md#createAudioCapturer)to create an AudioCapturer instance.

> **NOTE：**
> 
> - The initial APIs of this interface are supported since API version 8.

**Since:** 8

<!--Device-audio-interface AudioCapturer--><!--Device-audio-interface AudioCapturer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## getAudioStreamId

```TypeScript
getAudioStreamId(callback: AsyncCallback<number>): void
```

Obtains the stream ID of this audio capturer. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-AudioCapturer-getAudioStreamId(callback: AsyncCallback<long>): void--><!--Device-AudioCapturer-getAudioStreamId(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getAudioStreamId

```TypeScript
getAudioStreamId(): Promise<number>
```

Obtains the stream ID of this audio capturer. This API uses a promise to return the result.

**Since:** 9

<!--Device-AudioCapturer-getAudioStreamId(): Promise<long>--><!--Device-AudioCapturer-getAudioStreamId(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getAudioStreamIdSync

```TypeScript
getAudioStreamIdSync(): number
```

Obtains the stream ID of this audio capturer. This API returns the result synchronously.

**Since:** 10

<!--Device-AudioCapturer-getAudioStreamIdSync(): long--><!--Device-AudioCapturer-getAudioStreamIdSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getAudioTime

```TypeScript
getAudioTime(callback: AsyncCallback<number>): void
```

Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1,1970). This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-getAudioTime(callback: AsyncCallback<long>): void--><!--Device-AudioCapturer-getAudioTime(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getAudioTime

```TypeScript
getAudioTime(): Promise<number>
```

Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1,1970). This API uses a promise to return the result.

**Since:** 8

<!--Device-AudioCapturer-getAudioTime(): Promise<long>--><!--Device-AudioCapturer-getAudioTime(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getAudioTimeSync

```TypeScript
getAudioTimeSync(): number
```

Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1,1970). This API returns the result synchronously.

**Since:** 10

<!--Device-AudioCapturer-getAudioTimeSync(): long--><!--Device-AudioCapturer-getAudioTimeSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getAudioTimestampInfo

```TypeScript
getAudioTimestampInfo(): Promise<AudioTimestampInfo>
```

Obtains the timestamp and position information of an input audio stream.

This API obtains the actual recording position (specified by **framePos**) of the audio channel and the timestamp when recording to that position (specified by **timestamp**, in nanoseconds).

**Since:** 19

<!--Device-AudioCapturer-getAudioTimestampInfo(): Promise<AudioTimestampInfo>--><!--Device-AudioCapturer-getAudioTimestampInfo(): Promise<AudioTimestampInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800103-unsupported-state) |

## getAudioTimestampInfoSync

```TypeScript
getAudioTimestampInfoSync(): AudioTimestampInfo
```

Obtains the timestamp and position information of an input audio stream. This API returns the result synchronously.

**Since:** 19

<!--Device-AudioCapturer-getAudioTimestampInfoSync(): AudioTimestampInfo--><!--Device-AudioCapturer-getAudioTimestampInfoSync(): AudioTimestampInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800103-unsupported-state) |

## getBufferSize

```TypeScript
getBufferSize(callback: AsyncCallback<number>): void
```

Obtains a reasonable minimum buffer size in bytes for capturing. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-getBufferSize(callback: AsyncCallback<long>): void--><!--Device-AudioCapturer-getBufferSize(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getBufferSize

```TypeScript
getBufferSize(): Promise<number>
```

Obtains a reasonable minimum buffer size in bytes for capturing. This API uses a promise to return the result.

**Since:** 8

<!--Device-AudioCapturer-getBufferSize(): Promise<long>--><!--Device-AudioCapturer-getBufferSize(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getBufferSizeSync

```TypeScript
getBufferSizeSync(): number
```

Obtains a reasonable minimum buffer size in bytes for capturing. This API returns the result synchronously.

**Since:** 10

<!--Device-AudioCapturer-getBufferSizeSync(): long--><!--Device-AudioCapturer-getBufferSizeSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCapturerInfo

```TypeScript
getCapturerInfo(callback: AsyncCallback<AudioCapturerInfo>): void
```

Obtains the audio capturer information. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-getCapturerInfo(callback: AsyncCallback<AudioCapturerInfo>): void--><!--Device-AudioCapturer-getCapturerInfo(callback: AsyncCallback<AudioCapturerInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)&gt; | Yes |

## getCapturerInfo

```TypeScript
getCapturerInfo(): Promise<AudioCapturerInfo>
```

Obtains the audio capturer information. This API uses a promise to return the result.

**Since:** 8

<!--Device-AudioCapturer-getCapturerInfo(): Promise<AudioCapturerInfo>--><!--Device-AudioCapturer-getCapturerInfo(): Promise<AudioCapturerInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)&gt; |

## getCapturerInfoSync

```TypeScript
getCapturerInfoSync(): AudioCapturerInfo
```

Obtains the audio capturer information. This API returns the result synchronously.

**Since:** 10

<!--Device-AudioCapturer-getCapturerInfoSync(): AudioCapturerInfo--><!--Device-AudioCapturer-getCapturerInfoSync(): AudioCapturerInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) |

## getCurrentAudioCapturerChangeInfo

```TypeScript
getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo
```

Obtains the configuration changes of the current audio capturer. This API returns the result synchronously.

**Since:** 11

<!--Device-AudioCapturer-getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo--><!--Device-AudioCapturer-getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md) |

## getCurrentInputDevices

```TypeScript
getCurrentInputDevices(): AudioDeviceDescriptors
```

Obtains the information of the current input devices. This API returns the result synchronously.

**Since:** 11

<!--Device-AudioCapturer-getCurrentInputDevices(): AudioDeviceDescriptors--><!--Device-AudioCapturer-getCurrentInputDevices(): AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) |

## getNoiseReductionMode

```TypeScript
getNoiseReductionMode(): NoiseReductionMode
```

Gets the noise reduction mode for current audio capturer.The mode will only consider the default and setted status, audio input device and stream concurrency will not be considered.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-getNoiseReductionMode(): NoiseReductionMode--><!--Device-AudioCapturer-getNoiseReductionMode(): NoiseReductionMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md) |

## getOverflowCount

```TypeScript
getOverflowCount(): Promise<number>
```

Obtains the number of overflow audio frames in the audio stream that is being captured. This API uses a promise to return the result.

**Since:** 12

<!--Device-AudioCapturer-getOverflowCount(): Promise<long>--><!--Device-AudioCapturer-getOverflowCount(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getOverflowCountSync

```TypeScript
getOverflowCountSync(): number
```

Obtains the number of overflow audio frames in the audio stream that is being captured. This API returns the result synchronously.

**Since:** 12

<!--Device-AudioCapturer-getOverflowCountSync(): long--><!--Device-AudioCapturer-getOverflowCountSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getStreamInfo

```TypeScript
getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void
```

Obtains the stream information of this audio capturer. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void--><!--Device-AudioCapturer-getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)&gt; | Yes |

## getStreamInfo

```TypeScript
getStreamInfo(): Promise<AudioStreamInfo>
```

Obtains the stream information of this audio capturer. This API uses a promise to return the result.

**Since:** 8

<!--Device-AudioCapturer-getStreamInfo(): Promise<AudioStreamInfo>--><!--Device-AudioCapturer-getStreamInfo(): Promise<AudioStreamInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)&gt; |

## getStreamInfoSync

```TypeScript
getStreamInfoSync(): AudioStreamInfo
```

Obtains the stream information of this audio capturer. This API returns the result synchronously.

**Since:** 10

<!--Device-AudioCapturer-getStreamInfoSync(): AudioStreamInfo--><!--Device-AudioCapturer-getStreamInfoSync(): AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) |

## getSupportedNoiseReductionModes

```TypeScript
getSupportedNoiseReductionModes(): Array<NoiseReductionMode>
```

Gets all the supported noise reduction modes for current device platform.Currently the noise reduction effect is only supported when using[SOURCE_TYPE_VOICE_MESSAGE](arkts-audio-audio-sourcetype-e.md#SOURCE_TYPE_VOICE_MESSAGE), other supported usage may be extened later.The supported modes will only consider the audio format and device platform,audio input device and stream concurrency will not be considered.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-getSupportedNoiseReductionModes(): Array<NoiseReductionMode>--><!--Device-AudioCapturer-getSupportedNoiseReductionModes(): Array<NoiseReductionMode>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800301-system-error) |

## off('markReach')

```TypeScript
off(type: 'markReach', callback?: Callback<number>): void
```

Unsubscribes from the mark reached event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-off(type: 'markReach', callback?: Callback<long>): void--><!--Device-AudioCapturer-off(type: 'markReach', callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'markReach' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## off('periodReach')

```TypeScript
off(type: 'periodReach', callback?: Callback<number>): void
```

Unsubscribes from the period reached event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-off(type: 'periodReach', callback?: Callback<long>): void--><!--Device-AudioCapturer-off(type: 'periodReach', callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'periodReach' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: Callback<AudioState>): void
```

Unsubscribes from the audio capturer state change event. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-AudioCapturer-off(type: 'stateChange', callback?: Callback<AudioState>): void--><!--Device-AudioCapturer-off(type: 'stateChange', callback?: Callback<AudioState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt'): void
```

Unsubscribes from the audio interruption event.

**Since:** 10

<!--Device-AudioCapturer-off(type: 'audioInterrupt'): void--><!--Device-AudioCapturer-off(type: 'audioInterrupt'): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioInterrupt' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |

## off('inputDeviceChange')

```TypeScript
off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void
```

Unsubscribes from the audio input device change event. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioCapturer-off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioCapturer-off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'inputDeviceChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |

## off('audioCapturerChange')

```TypeScript
off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void
```

Unsubscribes from the audio capturer configuration change event. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioCapturer-off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void--><!--Device-AudioCapturer-off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioCapturerChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |

## off('readData')

```TypeScript
off(type: 'readData', callback?: Callback<ArrayBuffer>): void
```

Unsubscribes from the audio data read event. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioCapturer-off(type: 'readData', callback?: Callback<ArrayBuffer>): void--><!--Device-AudioCapturer-off(type: 'readData', callback?: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'readData' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |

## on('markReach')

```TypeScript
on(type: 'markReach', frame: number, callback: Callback<number>): void
```

Subscribes to the mark reached event, which is triggered (only once) when the number of frames captured reaches the value of the **frame** parameter. This API uses an asynchronous callback to return the result.

For example, if **frame** is set to **100**, the callback is invoked when the number of captured frames reaches the 100th frame.

**Since:** 8

<!--Device-AudioCapturer-on(type: 'markReach', frame: long, callback: Callback<long>): void--><!--Device-AudioCapturer-on(type: 'markReach', frame: long, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'markReach' | Yes |
| [frame](../../apis-arkui/arkts-apis/arkts-arkui-rendernode-c.md) | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('periodReach')

```TypeScript
on(type: 'periodReach', frame: number, callback: Callback<number>): void
```

Subscribes to the period reached event, which is triggered each time the number of frames captured reaches the value of the **frame** parameter. In other words, the information is reported periodically. This API uses an asynchronous callback to return the result.

For example, if **frame** is set to **10**, the callback is invoked each time 10 frames are captured, for example, when the number of frames captured reaches the 10th frame, 20th frame, and 30th frame.

**Since:** 8

<!--Device-AudioCapturer-on(type: 'periodReach', frame: long, callback: Callback<long>): void--><!--Device-AudioCapturer-on(type: 'periodReach', frame: long, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'periodReach' | Yes |
| [frame](../../apis-arkui/arkts-apis/arkts-arkui-rendernode-c.md) | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: Callback<AudioState>): void
```

Subscribes to the audio capturer state change event, which is triggered when the state of the audio capturer is changed. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-on(type: 'stateChange', callback: Callback<AudioState>): void--><!--Device-AudioCapturer-on(type: 'stateChange', callback: Callback<AudioState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | Yes |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void
```

Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an asynchronous callback to return the result.

The AudioCapturer instance proactively gains the focus when the **start** event occurs and releases the focus when the **pause** or **stop** event occurs. Therefore, you do not need to request to gain or release the focus.

After this API is called, an [InterruptEvent](arkts-audio-audio-interruptevent-i.md#InterruptEvent) is received when the AudioCapturer instance fails to obtain the focus or an audio interruption event occurs (for example, the audio stream is interrupted by others). It is recommended that the application perform further processing based on the **InterruptEvent** information. For details, see  
[Introduction to Audio Focus](../../../media/audio/audio-playback-concurrency.md).

**Since:** 10

<!--Device-AudioCapturer-on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void--><!--Device-AudioCapturer-on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioInterrupt' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |

## on('inputDeviceChange')

```TypeScript
on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void
```

Subscribes to the audio input device change event, which is triggered when an audio input device is changed. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioCapturer-on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioCapturer-on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'inputDeviceChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |

## on('audioCapturerChange')

```TypeScript
on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void
```

Subscribes to the audio capturer configuration change event, which is triggered when the audio recording stream status or device is changed. This API uses an asynchronous callback to return the result. The subscription is implemented asynchronously and the callback, which is triggered when the audio capturer configuration changes,may fail to reflect the actual condition.

**Since:** 11

<!--Device-AudioCapturer-on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void--><!--Device-AudioCapturer-on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioCapturerChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |

## on('readData')

```TypeScript
on(type: 'readData', callback: Callback<ArrayBuffer>): void
```

Subscribes to the audio data read event, which is triggered when audio stream data needs to be read. This API uses an asynchronous callback to return the result.

The callback function is used only to read audio data. Do not call AudioCapturer APIs in it.

To eliminate power-on noise caused by the microphone hardware design, the first 100 ms of data after recording starts is typically muted.

**Since:** 11

<!--Device-AudioCapturer-on(type: 'readData', callback: Callback<ArrayBuffer>): void--><!--Device-AudioCapturer-on(type: 'readData', callback: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'readData' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |

## read

```TypeScript
read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void
```

Reads the buffer from the audio capturer. This method uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [readData](ohos.multimedia.audio.AudioCapturer#event:readData)

<!--Device-AudioCapturer-read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void--><!--Device-AudioCapturer-read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |
| isBlockingRead | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | Yes |

## read

```TypeScript
read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>
```

Reads the buffer. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [readData](ohos.multimedia.audio.AudioCapturer#event:readData)

<!--Device-AudioCapturer-read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>--><!--Device-AudioCapturer-read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |
| isBlockingRead | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this audio capturer. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-release(callback: AsyncCallback<void>): void--><!--Device-AudioCapturer-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## release

```TypeScript
release(): Promise<void>
```

Releases this audio capturer. This API uses a promise to return the result.

**Since:** 8

<!--Device-AudioCapturer-release(): Promise<void>--><!--Device-AudioCapturer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## requestPlaybackCaptureStart

```TypeScript
requestPlaybackCaptureStart(callback: Callback<PlaybackCaptureStartState>): void
```

Asynchronously request to start the playback capture stream.This function is non-blocking, which means system will continue to process user authorization and stream starting when receiving the start request. And the final result will be returned by callback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-requestPlaybackCaptureStart(callback: Callback<PlaybackCaptureStartState>): void--><!--Device-AudioCapturer-requestPlaybackCaptureStart(callback: Callback<PlaybackCaptureStartState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PlaybackCaptureStartState](arkts-audio-audio-playbackcapturestartstate-e.md)&gt; | Yes |

## setIndependentAudioSessionStrategy

```TypeScript
setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: number): void
```

Sets the independent audio session strategy and behavior parameters.

> **NOTE：**
> 
> If this API is called while an audio capturer is running, you must call the
> [start](#start) API again for
> the settings to take effect.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void--><!--Device-AudioCapturer-setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [AudioSessionStrategy](arkts-audio-audio-audiosessionstrategy-i.md) | Yes |
| behavior | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800103-unsupported-state) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |

## setMuteHint

```TypeScript
setMuteHint(mute: boolean): Promise<void>
```

Set mute hint for this capturer, this method is used as a hint for power optimization it does not mute the recording stream, only affects internal processing strategy.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-setMuteHint(mute: boolean): Promise<void>--><!--Device-AudioCapturer-setMuteHint(mute: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mute | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800103-unsupported-state) |

## setNoiseReductionMode

```TypeScript
setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void
```

Sets noise reduction mode for current audio capturer.The supported mode should be obtained by [getSupportedNoiseReductionModes](#getSupportedNoiseReductionModes).The actual effect may vary from different audio devices, and will be invalid when there are multiple recording streams running simultaneously.The mode can only be changed in created and stopped state.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void--><!--Device-AudioCapturer-setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| noiseReductionMode | [NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800103-unsupported-state) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800301-system-error) |
| [6800104](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800104-unsupported-parameter-value) |

## setWillMuteWhenInterrupted

```TypeScript
setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>
```

Sets whether to  
[mute the current audio recording stream when an audio interruption occurs](../../../media/audio/using-audiocapturer-for-recording.md#setting-the-mute-interruption-mode). This API uses a promise to return the result.

**Since:** 20

<!--Device-AudioCapturer-setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>--><!--Device-AudioCapturer-setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| muteWhenInterrupted | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800103-unsupported-state) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts this audio capturer to start capturing audio data. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-start(callback: AsyncCallback<void>): void--><!--Device-AudioCapturer-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## start

```TypeScript
start(): Promise<void>
```

Starts this audio capturer to start capturing audio data. This API uses a promise to return the result.

**Since:** 8

<!--Device-AudioCapturer-start(): Promise<void>--><!--Device-AudioCapturer-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops this audio capturer, ceasing the input audio stream. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-stop(callback: AsyncCallback<void>): void--><!--Device-AudioCapturer-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## stop

```TypeScript
stop(): Promise<void>
```

Stops this audio capturer, ceasing the input audio stream. This API uses a promise to return the result.

**Since:** 8

<!--Device-AudioCapturer-stop(): Promise<void>--><!--Device-AudioCapturer-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## state

```TypeScript
readonly state: AudioState
```

Audio capturer state.

**Type:** AudioState

**Since:** 8

<!--Device-AudioCapturer-readonly state: AudioState--><!--Device-AudioCapturer-readonly state: AudioState-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer
