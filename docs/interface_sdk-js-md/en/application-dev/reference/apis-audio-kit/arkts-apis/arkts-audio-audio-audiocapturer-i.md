# AudioCapturer

This interface provides APIs for audio capture.Before calling any API in AudioCapturer, you must use [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md) to create an AudioCapturer instance.

> **NOTE：**&gt;
> - The initial APIs of this interface are supported since API version 8.

**Since:** 23

<!--Device-audio-interface AudioCapturer--><!--Device-audio-interface AudioCapturer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## getAudioStreamId

```TypeScript
getAudioStreamId(callback: AsyncCallback<long>): void
```

Obtains the stream ID of this audio capturer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioCapturer-getAudioStreamId(callback: AsyncCallback<long>): void--><!--Device-AudioCapturer-getAudioStreamId(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the stream ID obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioStreamId((err: BusinessError, streamId: number) => {
  console.info(`audioCapturer GetStreamId: ${streamId}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioStreamId().then((streamId: number) => {
  console.info(`audioCapturer getAudioStreamId: ${streamId}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioStreamId((err: BusinessError, streamId: number) => {
  console.info(`Renderer GetStreamId: ${streamId}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioStreamId().then((streamId: number) => {
  console.info(`Renderer getAudioStreamId: ${streamId}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## getAudioStreamId

```TypeScript
getAudioStreamId(): Promise<long>
```

Obtains the stream ID of this audio capturer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioCapturer-getAudioStreamId(): Promise<long>--><!--Device-AudioCapturer-getAudioStreamId(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the stream ID. |

**Examples**

See [getAudioStreamId](#getaudiostreamid)

## getAudioStreamIdSync

```TypeScript
getAudioStreamIdSync(): long
```

Obtains the stream ID of this audio capturer. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioCapturer-getAudioStreamIdSync(): long--><!--Device-AudioCapturer-getAudioStreamIdSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| long | Stream ID. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let streamId: number = audioCapturer.getAudioStreamIdSync();
  console.info(`audioCapturer getAudioStreamIdSync: ${streamId}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let streamId: number = audioRenderer.getAudioStreamIdSync();
  console.info(`Renderer getAudioStreamIdSync: ${streamId}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

## getAudioTime

```TypeScript
getAudioTime(callback: AsyncCallback<long>): void
```

Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1, 1970). This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioCapturer-getAudioTime(callback: AsyncCallback<long>): void--><!--Device-AudioCapturer-getAudioTime(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the number of nanoseconds obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioTime((err: BusinessError, timestamp: number) => {
  console.info(`Current timestamp: ${timestamp}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioTime().then((audioTime: number) => {
  console.info(`AudioFrameworkRecLog: AudioCapturer getAudioTime : Success ${audioTime}`);
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRecLog: AudioCapturer Created : ERROR : ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioTime((err: BusinessError, timestamp: number) => {
  console.info(`Current timestamp: ${timestamp}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioTime().then((timestamp: number) => {
  console.info(`Current timestamp: ${timestamp}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## getAudioTime

```TypeScript
getAudioTime(): Promise<long>
```

Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1, 1970). This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioCapturer-getAudioTime(): Promise<long>--><!--Device-AudioCapturer-getAudioTime(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return a timestamp representing the number of nanoseconds elapsed since the Unix epoch (January 1, 1970). <br>The timestamp unit is nanoseconds. |

**Examples**

See [getAudioTime](#getaudiotime)

## getAudioTimestampInfo

```TypeScript
getAudioTimestampInfo(): Promise<AudioTimestampInfo>
```

Obtains the timestamp and position information of an input audio stream.This API obtains the actual recording position (specified by **framePos**) of the audio channel and the timestamp when recording to that position (specified by **timestamp**, in nanoseconds).

**Since:** 23

<!--Device-AudioCapturer-getAudioTimestampInfo(): Promise<AudioTimestampInfo>--><!--Device-AudioCapturer-getAudioTimestampInfo(): Promise<AudioTimestampInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md)&gt; | Promise used to return the timestamp and position information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permit at current state. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioTimestampInfo().then((audioTimestampInfo: audio.AudioTimestampInfo) => {
  console.info(`Current timestamp: ${audioTimestampInfo.timestamp}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioTimestampInfo().then((audioTimestampInfo: audio.AudioTimestampInfo) => {
  console.info(`Current timestamp: ${audioTimestampInfo.timestamp}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## getAudioTimestampInfoSync

```TypeScript
getAudioTimestampInfoSync(): AudioTimestampInfo
```

Obtains the timestamp and position information of an input audio stream. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioCapturer-getAudioTimestampInfoSync(): AudioTimestampInfo--><!--Device-AudioCapturer-getAudioTimestampInfoSync(): AudioTimestampInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md) | Information about the timestamp and position information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permit at current state. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioTimestampInfo: audio.AudioTimestampInfo = audioCapturer.getAudioTimestampInfoSync();
  console.info(`Current timestamp: ${audioTimestampInfo.timestamp}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioTimestampInfo: audio.AudioTimestampInfo = audioRenderer.getAudioTimestampInfoSync();
  console.info(`Current timestamp: ${audioTimestampInfo.timestamp}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

## getAudioTimeSync

```TypeScript
getAudioTimeSync(): long
```

Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1, 1970). This API returns the result synchronously.

**Since:** 23

<!--Device-AudioCapturer-getAudioTimeSync(): long--><!--Device-AudioCapturer-getAudioTimeSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| long | Timestamp. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioTime: number = audioCapturer.getAudioTimeSync();
  console.info(`AudioFrameworkRecLog: AudioCapturer getAudioTimeSync : Success ${audioTime}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`AudioFrameworkRecLog: AudioCapturer getAudioTimeSync : ERROR : ${error}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let timestamp: number = audioRenderer.getAudioTimeSync();
  console.info(`Current timestamp: ${timestamp}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

## getBufferSize

```TypeScript
getBufferSize(callback: AsyncCallback<long>): void
```

Obtains a reasonable minimum buffer size in bytes for capturing. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioCapturer-getBufferSize(callback: AsyncCallback<long>): void--><!--Device-AudioCapturer-getBufferSize(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the minimum buffer size obtained; otherwise, **err** is an error object.<br>The unit is bytes. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getBufferSize((err: BusinessError, bufferSize: number) => {
  if (err) {
    console.error(`Failed to get buffer size. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting buffer size, BufferSize: ${bufferSize}.`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getBufferSize().then((bufferSize: number) => {
  console.info(`Succeeded in getting buffer size, BufferSize: ${bufferSize}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get buffer size. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bufferSize: number;

audioRenderer.getBufferSize((err: BusinessError, data: number) => {
  if (err) {
    console.error('getBufferSize error');
  } else {
    console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
    bufferSize = data;
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bufferSize: number;

audioRenderer.getBufferSize().then((data: number) => {
  console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
  bufferSize = data;
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}`);
});
```

## getBufferSize

```TypeScript
getBufferSize(): Promise<long>
```

Obtains a reasonable minimum buffer size in bytes for capturing. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioCapturer-getBufferSize(): Promise<long>--><!--Device-AudioCapturer-getBufferSize(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the buffer size. <br>The unit is bytes. |

**Examples**

See [getBufferSize](#getbuffersize)

## getBufferSizeSync

```TypeScript
getBufferSizeSync(): long
```

Obtains a reasonable minimum buffer size in bytes for capturing. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioCapturer-getBufferSizeSync(): long--><!--Device-AudioCapturer-getBufferSizeSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| long | Buffer size, in bytes. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bufferSize = audioCapturer.getBufferSizeSync();
  console.info(`Succeeded in getting buffer size, BufferSize: ${bufferSize}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get buffer size. Code: ${error.code}, message: ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bufferSize: number = 0;

try {
  bufferSize = audioRenderer.getBufferSizeSync();
  console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${bufferSize}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${error}`);
}
```

## getCapturerInfo

```TypeScript
getCapturerInfo(callback: AsyncCallback<AudioCapturerInfo>): void
```

Obtains the audio capturer information. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioCapturer-getCapturerInfo(callback: AsyncCallback<AudioCapturerInfo>): void--><!--Device-AudioCapturer-getCapturerInfo(callback: AsyncCallback<AudioCapturerInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the capturer information obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getCapturerInfo((err: BusinessError, capturerInfo: audio.AudioCapturerInfo) => {
  if (err) {
    console.error('Failed to get capture info');
  } else {
    console.info('Capturer getCapturerInfo:');
    console.info(`Capturer source: ${capturerInfo.source}`);
    console.info(`Capturer flags: ${capturerInfo.capturerFlags}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getCapturerInfo().then((audioParamsGet: audio.AudioCapturerInfo) => {
  if (audioParamsGet != undefined) {
    console.info('AudioFrameworkRecLog: Capturer CapturerInfo:');
    console.info(`AudioFrameworkRecLog: Capturer SourceType: ${audioParamsGet.source}`);
    console.info(`AudioFrameworkRecLog: Capturer capturerFlags: ${audioParamsGet.capturerFlags}`);
  } else {
    console.info(`AudioFrameworkRecLog: audioParamsGet is : ${audioParamsGet}`);
    console.info('AudioFrameworkRecLog: audioParams getCapturerInfo are incorrect');
  }
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRecLog: CapturerInfo :ERROR: ${err}`);
})
```

## getCapturerInfo

```TypeScript
getCapturerInfo(): Promise<AudioCapturerInfo>
```

Obtains the audio capturer information. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioCapturer-getCapturerInfo(): Promise<AudioCapturerInfo>--><!--Device-AudioCapturer-getCapturerInfo(): Promise<AudioCapturerInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)&gt; | Promise used to return the audio capturer information. |

**Examples**

See [getCapturerInfo](#getcapturerinfo)

## getCapturerInfoSync

```TypeScript
getCapturerInfoSync(): AudioCapturerInfo
```

Obtains the audio capturer information. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioCapturer-getCapturerInfoSync(): AudioCapturerInfo--><!--Device-AudioCapturer-getCapturerInfoSync(): AudioCapturerInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) | Audio capturer information. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioParamsGet: audio.AudioCapturerInfo = audioCapturer.getCapturerInfoSync();
  console.info(`AudioFrameworkRecLog: Capturer SourceType: ${audioParamsGet.source}`);
  console.info(`AudioFrameworkRecLog: Capturer capturerFlags: ${audioParamsGet.capturerFlags}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`AudioFrameworkRecLog: CapturerInfo :ERROR: ${error}`);
}
```

## getCurrentAudioCapturerChangeInfo

```TypeScript
getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo
```

Obtains the configuration changes of the current audio capturer. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioCapturer-getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo--><!--Device-AudioCapturer-getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| [AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md) | Configuration changes of the audio capturer. |

**Examples**

```TypeScript
let info: audio.AudioCapturerChangeInfo = audioCapturer.getCurrentAudioCapturerChangeInfo();
console.info(`Info streamId: ${info.streamId}`);
console.info(`Info source: ${info.capturerInfo.source}`);
console.info(`Info capturerFlags: ${info.capturerInfo.capturerFlags}`);
console.info(`Info muted: ${info.muted}`);
console.info(`Info type: ${info.deviceDescriptors[0].deviceType}`);
console.info(`Info role: ${info.deviceDescriptors[0].deviceRole}`);
console.info(`Info name: ${info.deviceDescriptors[0].name}`);
console.info(`Info address: ${info.deviceDescriptors[0].address}`);
console.info(`Info samplerates: ${info.deviceDescriptors[0].sampleRates[0]}`);
console.info(`Info channelcounts: ${info.deviceDescriptors[0].channelCounts[0]}`);
console.info(`Info channelmask: ${info.deviceDescriptors[0].channelMasks[0]}`);
if (info.deviceDescriptors[0].encodingTypes) {
  console.info(`Device encodingTypes: ${info.deviceDescriptors[0].encodingTypes[0]}`);
}
```

## getCurrentInputDevices

```TypeScript
getCurrentInputDevices(): AudioDeviceDescriptors
```

Obtains the information of the current input devices. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioCapturer-getCurrentInputDevices(): AudioDeviceDescriptors--><!--Device-AudioCapturer-getCurrentInputDevices(): AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) | An array of the audio device descriptors. |

**Examples**

```TypeScript
let deviceDescriptors: audio.AudioDeviceDescriptors = audioCapturer.getCurrentInputDevices();
console.info(`Device id: ${deviceDescriptors[0].id}`);
console.info(`Device type: ${deviceDescriptors[0].deviceType}`);
console.info(`Device role: ${deviceDescriptors[0].deviceRole}`);
console.info(`Device name: ${deviceDescriptors[0].name}`);
console.info(`Device address: ${deviceDescriptors[0].address}`);
console.info(`Device samplerates: ${deviceDescriptors[0].sampleRates[0]}`);
console.info(`Device channelcounts: ${deviceDescriptors[0].channelCounts[0]}`);
console.info(`Device channelmask: ${deviceDescriptors[0].channelMasks[0]}`);
if (deviceDescriptors[0].encodingTypes) {
  console.info(`Device encodingTypes: ${deviceDescriptors[0].encodingTypes[0]}`);
}
```

## getNoiseReductionMode

```TypeScript
getNoiseReductionMode(): NoiseReductionMode
```

Gets the noise reduction mode for current audio capturer. The mode will only consider the default and setted status, audio input device and stream concurrency will not be considered.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-getNoiseReductionMode(): NoiseReductionMode--><!--Device-AudioCapturer-getNoiseReductionMode(): NoiseReductionMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| [NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md) | The noise reduction mode for current audio capturer, the default value is { |

## getOverflowCount

```TypeScript
getOverflowCount(): Promise<long>
```

Obtains the number of overflow audio frames in the audio stream that is being captured. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioCapturer-getOverflowCount(): Promise<long>--><!--Device-AudioCapturer-getOverflowCount(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the number of overflow audio frames. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getOverflowCount().then((value: number) => {
  console.info(`Get overflow count Success! ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Get overflow count Fail: ${err}`);
});
```

## getOverflowCountSync

```TypeScript
getOverflowCountSync(): long
```

Obtains the number of overflow audio frames in the audio stream that is being captured. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioCapturer-getOverflowCountSync(): long--><!--Device-AudioCapturer-getOverflowCountSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| long | Number of overflow audio frames. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioCapturer.getOverflowCountSync();
  console.info(`Get overflow count Success! ${value}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get overflow count Fail: ${error}`);
}
```

## getStreamInfo

```TypeScript
getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void
```

Obtains the stream information of this audio capturer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioCapturer-getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void--><!--Device-AudioCapturer-getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the stream information obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getStreamInfo((err: BusinessError, streamInfo: audio.AudioStreamInfo) => {
  if (err) {
    console.error('Failed to get stream info');
  } else {
    console.info('Capturer GetStreamInfo:');
    console.info(`Capturer sampling rate: ${streamInfo.samplingRate}`);
    console.info(`Capturer channel: ${streamInfo.channels}`);
    console.info(`Capturer format: ${streamInfo.sampleFormat}`);
    console.info(`Capturer encoding type: ${streamInfo.encodingType}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getStreamInfo().then((audioParamsGet: audio.AudioStreamInfo) => {
  console.info('getStreamInfo:');
  console.info(`sampleFormat: ${audioParamsGet.sampleFormat}`);
  console.info(`samplingRate: ${audioParamsGet.samplingRate}`);
  console.info(`channels: ${audioParamsGet.channels}`);
  console.info(`encodingType: ${audioParamsGet.encodingType}`);
}).catch((err: BusinessError) => {
  console.error(`getStreamInfo :ERROR: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getStreamInfo((err: BusinessError, streamInfo: audio.AudioStreamInfo) => {
  console.info('Renderer GetStreamInfo:');
  console.info(`Renderer sampling rate: ${streamInfo.samplingRate}`);
  console.info(`Renderer channel: ${streamInfo.channels}`);
  console.info(`Renderer format: ${streamInfo.sampleFormat}`);
  console.info(`Renderer encoding type: ${streamInfo.encodingType}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getStreamInfo().then((streamInfo: audio.AudioStreamInfo) => {
  console.info('Renderer GetStreamInfo:');
  console.info(`Renderer sampling rate: ${streamInfo.samplingRate}`);
  console.info(`Renderer channel: ${streamInfo.channels}`);
  console.info(`Renderer format: ${streamInfo.sampleFormat}`);
  console.info(`Renderer encoding type: ${streamInfo.encodingType}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## getStreamInfo

```TypeScript
getStreamInfo(): Promise<AudioStreamInfo>
```

Obtains the stream information of this audio capturer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioCapturer-getStreamInfo(): Promise<AudioStreamInfo>--><!--Device-AudioCapturer-getStreamInfo(): Promise<AudioStreamInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)&gt; | Promise used to return the stream information. |

**Examples**

See [getStreamInfo](#getstreaminfo)

## getStreamInfoSync

```TypeScript
getStreamInfoSync(): AudioStreamInfo
```

Obtains the stream information of this audio capturer. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioCapturer-getStreamInfoSync(): AudioStreamInfo--><!--Device-AudioCapturer-getStreamInfoSync(): AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Stream information. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioParamsGet: audio.AudioStreamInfo = audioCapturer.getStreamInfoSync();
  console.info(`sampleFormat: ${audioParamsGet.sampleFormat}`);
  console.info(`samplingRate: ${audioParamsGet.samplingRate}`);
  console.info(`channels: ${audioParamsGet.channels}`);
  console.info(`encodingType: ${audioParamsGet.encodingType}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`getStreamInfo :ERROR: ${error}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let streamInfo: audio.AudioStreamInfo = audioRenderer.getStreamInfoSync();
  console.info(`Renderer sampling rate: ${streamInfo.samplingRate}`);
  console.info(`Renderer channel: ${streamInfo.channels}`);
  console.info(`Renderer format: ${streamInfo.sampleFormat}`);
  console.info(`Renderer encoding type: ${streamInfo.encodingType}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

## getSupportedNoiseReductionModes

```TypeScript
getSupportedNoiseReductionModes(): Array<NoiseReductionMode>
```

Gets all the supported noise reduction modes for current device platform. Currently the noise reduction effect is only supported when using [SOURCE_TYPE_VOICE_MESSAGE](arkts-audio-audio-sourcetype-e.md#source_type_voice_message), other supported usage may be extened later. The supported modes will only consider the audio format and device platform, audio input device and stream concurrency will not be considered.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-getSupportedNoiseReductionModes(): Array<NoiseReductionMode>--><!--Device-AudioCapturer-getSupportedNoiseReductionModes(): Array<NoiseReductionMode>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md)&gt; | The supported noise reduction mode array, at least { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800301](../errorcode-audio.md#6800301-system-error) | Audio server process died. |

## off('audioCapturerChange')

```TypeScript
off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void
```

Unsubscribes from the audio capturer configuration change event. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioCapturer-off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void--><!--Device-AudioCapturer-off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioCapturerChange' | Yes | Event type. The event **'audioCapturerChange'** is triggered when the audio capturer configuration is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md)&gt; | No | Callback used for unsubscription. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt'): void
```

Unsubscribes from the audio interruption event.

**Since:** 10

<!--Device-AudioCapturer-off(type: 'audioInterrupt'): void--><!--Device-AudioCapturer-off(type: 'audioInterrupt'): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | Yes | Event type. The event **'audioInterrupt'** is triggered when the audio focus is changed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('inputDeviceChange')

```TypeScript
off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void
```

Unsubscribes from the audio input device change event. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioCapturer-off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioCapturer-off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputDeviceChange' | Yes | Event type. The event **'inputDeviceChange'** is triggered when an audio input device is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | No | Callback used to return the information about the audio input device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('markReach')

```TypeScript
off(type: 'markReach', callback?: Callback<long>): void
```

Unsubscribes from the mark reached event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-off(type: 'markReach', callback?: Callback<long>): void--><!--Device-AudioCapturer-off(type: 'markReach', callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'markReach' | Yes | Event type. The event **'markReach'** is triggered when the number of frames captured reaches the value of the **frame** parameter. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | No | Callback used to return the value of the **frame** parameter.<br>**Since:** 18 |

## off('periodReach')

```TypeScript
off(type: 'periodReach', callback?: Callback<long>): void
```

Unsubscribes from the period reached event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-off(type: 'periodReach', callback?: Callback<long>): void--><!--Device-AudioCapturer-off(type: 'periodReach', callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'periodReach' | Yes | Event type. The event **'periodReach'** is triggered each time the number of frames captured reaches the value of the **frame** parameter. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | No | Callback used to return the value of the **frame** parameter.<br>**Since:** 18 |

## off('readData')

```TypeScript
off(type: 'readData', callback?: Callback<ArrayBuffer>): void
```

Unsubscribes from the audio data read event. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioCapturer-off(type: 'readData', callback?: Callback<ArrayBuffer>): void--><!--Device-AudioCapturer-off(type: 'readData', callback?: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'readData' | Yes | Event type. The event **'readData'** is triggered when audio stream data needs to be read. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | No | Callback used to return the buffer from which the data is read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: Callback<AudioState>): void
```

Unsubscribes from the audio capturer state change event. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-AudioCapturer-off(type: 'stateChange', callback?: Callback<AudioState>): void--><!--Device-AudioCapturer-off(type: 'stateChange', callback?: Callback<AudioState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'stateChange' | Yes | Event type. The event **'stateChange'** is triggered when the listening for audio capturer state change event is canceled. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | No | Callback used to return the audio status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offAudioCapturerChange

```TypeScript
offAudioCapturerChange(callback?: Callback<AudioCapturerChangeInfo>): void
```

Unsubscribes audio capturer info change event callback.

**Since:** 23

<!--Device-AudioCapturer-offAudioCapturerChange(callback?: Callback<AudioCapturerChangeInfo>): void--><!--Device-AudioCapturer-offAudioCapturerChange(callback?: Callback<AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md)&gt; | No | Callback used in subscribe. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offAudioInterrupt

```TypeScript
offAudioInterrupt(): void
```

UnSubscribes to audio interrupt events.

**Since:** 23

<!--Device-AudioCapturer-offAudioInterrupt(): void--><!--Device-AudioCapturer-offAudioInterrupt(): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

## offInputDeviceChange

```TypeScript
offInputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void
```

Unsubscribes input device change event callback.

**Since:** 23

<!--Device-AudioCapturer-offInputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioCapturer-offInputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | No | Callback used in subscribe. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offMarkReach

```TypeScript
offMarkReach(callback?: Callback<long>): void
```

Unsubscribes from the mark reached events.

**Since:** 23

<!--Device-AudioCapturer-offMarkReach(callback?: Callback<long>): void--><!--Device-AudioCapturer-offMarkReach(callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | No | Callback invoked when the event is triggered. |

## offPeriodReach

```TypeScript
offPeriodReach(callback?: Callback<long>): void
```

Unsubscribes from period reached events.

**Since:** 23

<!--Device-AudioCapturer-offPeriodReach(callback?: Callback<long>): void--><!--Device-AudioCapturer-offPeriodReach(callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | No | Callback invoked when the event is triggered. |

## offReadData

```TypeScript
offReadData(callback?: Callback<ArrayBuffer>): void
```

Unsubscribes audio data callback.

**Since:** 23

<!--Device-AudioCapturer-offReadData(callback?: Callback<ArrayBuffer>): void--><!--Device-AudioCapturer-offReadData(callback?: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | No | Callback used in subscribe. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offStateChange

```TypeScript
offStateChange(callback?: Callback<AudioState>): void
```

Unsubscribes audio state change event callback.

**Since:** 23

<!--Device-AudioCapturer-offStateChange(callback?: Callback<AudioState>): void--><!--Device-AudioCapturer-offStateChange(callback?: Callback<AudioState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | No | Callback used to listen for the audio state change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('audioCapturerChange')

```TypeScript
on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void
```

Subscribes to the audio capturer configuration change event, which is triggered when the audio recording stream status or device is changed. This API uses an asynchronous callback to return the result. The subscription is implemented asynchronously and the callback, which is triggered when the audio capturer configuration changes, may fail to reflect the actual condition.

**Since:** 11

<!--Device-AudioCapturer-on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void--><!--Device-AudioCapturer-on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioCapturerChange' | Yes | Event type. The event **'audioCapturerChange'** is triggered when the audio recording stream status or device is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md)&gt; | Yes | Callback used to return the current configuration and status information of the audio capturer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void
```

Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an asynchronous callback to return the result.The AudioCapturer instance proactively gains the focus when the **start** event occurs and releases the focus when the **pause** or **stop** event occurs. Therefore, you do not need to request to gain or release the focus.After this API is called, an [InterruptEvent](arkts-audio-audio-interruptevent-i.md) is received when the AudioCapturer instance fails to obtain the focus or an audio interruption event occurs (for example, the audio stream is interrupted by others). It is recommended that the application perform further processing based on the **InterruptEvent** information. For details, see [Introduction to Audio Focus](../../../media/audio/audio-playback-concurrency.md).

**Since:** 10

<!--Device-AudioCapturer-on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void--><!--Device-AudioCapturer-on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | Yes | Event type. The event **'audioInterrupt'** is triggered when the audio focus is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | Yes | Callback used to return the event information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('inputDeviceChange')

```TypeScript
on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void
```

Subscribes to the audio input device change event, which is triggered when an audio input device is changed. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioCapturer-on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioCapturer-on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputDeviceChange' | Yes | Event type. The event **'inputDeviceChange'** is triggered when an audio input device is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to return the updated information about the audio input device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('markReach')

```TypeScript
on(type: 'markReach', frame: long, callback: Callback<long>): void
```

Subscribes to the mark reached event, which is triggered (only once) when the number of frames captured reaches the value of the **frame** parameter. This API uses an asynchronous callback to return the result.For example, if **frame** is set to **100**, the callback is invoked when the number of captured frames reaches the 100th frame.

**Since:** 8

<!--Device-AudioCapturer-on(type: 'markReach', frame: long, callback: Callback<long>): void--><!--Device-AudioCapturer-on(type: 'markReach', frame: long, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'markReach' | Yes | Event type. The event **'markReach'** is triggered when the number of frames captured reaches the value of the **frame** parameter. |
| frame | long | Yes | Number of frames to trigger the event. The value must be greater than **0**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | Callback used to return the value of the **frame** parameter. |

## on('periodReach')

```TypeScript
on(type: 'periodReach', frame: long, callback: Callback<long>): void
```

Subscribes to the period reached event, which is triggered each time the number of frames captured reaches the value of the **frame** parameter. In other words, the information is reported periodically. This API uses an asynchronous callback to return the result.For example, if **frame** is set to **10**, the callback is invoked each time 10 frames are captured, for example, when the number of frames captured reaches the 10th frame, 20th frame, and 30th frame.

**Since:** 8

<!--Device-AudioCapturer-on(type: 'periodReach', frame: long, callback: Callback<long>): void--><!--Device-AudioCapturer-on(type: 'periodReach', frame: long, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'periodReach' | Yes | Event type. The event **'periodReach'** is triggered each time the number of frames captured reaches the value of the **frame** parameter. |
| frame | long | Yes | Number of frames to trigger the event. The value must be greater than **0**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | Callback used to return the value of the **frame** parameter. |

## on('readData')

```TypeScript
on(type: 'readData', callback: Callback<ArrayBuffer>): void
```

Subscribes to the audio data read event, which is triggered when audio stream data needs to be read. This API uses an asynchronous callback to return the result.The callback function is used only to read audio data. Do not call AudioCapturer APIs in it.To eliminate power-on noise caused by the microphone hardware design, the first 100 ms of data after recording starts is typically muted.

**Since:** 11

<!--Device-AudioCapturer-on(type: 'readData', callback: Callback<ArrayBuffer>): void--><!--Device-AudioCapturer-on(type: 'readData', callback: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'readData' | Yes | Event type. The event **'readData'** is triggered when audio stream data needs to be read. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | Yes | Callback used to return the buffer from which the data is read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: Callback<AudioState>): void
```

Subscribes to the audio capturer state change event, which is triggered when the state of the audio capturer is changed. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioCapturer-on(type: 'stateChange', callback: Callback<AudioState>): void--><!--Device-AudioCapturer-on(type: 'stateChange', callback: Callback<AudioState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'stateChange' | Yes | Event type. The event **'stateChange'** is triggered when the state of the audio capturer is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | Yes | Callback used to return the audio status. |

## onAudioCapturerChange

```TypeScript
onAudioCapturerChange(callback: Callback<AudioCapturerChangeInfo>): void
```

Subscribes audio capturer info change event callback. The event is triggered when input device change for this stream.

**Since:** 23

<!--Device-AudioCapturer-onAudioCapturerChange(callback: Callback<AudioCapturerChangeInfo>): void--><!--Device-AudioCapturer-onAudioCapturerChange(callback: Callback<AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md)&gt; | Yes | Callback used to listen device change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onAudioInterrupt

```TypeScript
onAudioInterrupt(callback: Callback<InterruptEvent>): void
```

Listens for audio interrupt events. This method uses a callback to get interrupt events. The interrupt event is triggered when audio recording is interrupted.

**Since:** 23

<!--Device-AudioCapturer-onAudioInterrupt(callback: Callback<InterruptEvent>): void--><!--Device-AudioCapturer-onAudioInterrupt(callback: Callback<InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | Yes | Callback used to listen for interrupt callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onInputDeviceChange

```TypeScript
onInputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void
```

Subscribes input device change event callback. The event is triggered when input device change for this stream.

**Since:** 23

<!--Device-AudioCapturer-onInputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioCapturer-onInputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to listen device change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onMarkReach

```TypeScript
onMarkReach(frame: long, callback: Callback<long>): void
```

Subscribes to mark reached events. When the number of frames captured reaches the value of the frame parameter, the callback is invoked.

**Since:** 23

<!--Device-AudioCapturer-onMarkReach(frame: long, callback: Callback<long>): void--><!--Device-AudioCapturer-onMarkReach(frame: long, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frame | long | Yes | Number of frames to trigger the event. The value must be greater than 0. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | Callback invoked when the event is triggered. |

## onPeriodReach

```TypeScript
onPeriodReach(frame: long, callback: Callback<long>): void
```

Subscribes to period reached events. When the period of frame capturing reaches the value of frame parameter, the callback is invoked.

**Since:** 23

<!--Device-AudioCapturer-onPeriodReach(frame: long, callback: Callback<long>): void--><!--Device-AudioCapturer-onPeriodReach(frame: long, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frame | long | Yes | Period during which frame capturing is listened. The value must be greater than 0. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | Callback invoked when the event is triggered. |

## onReadData

```TypeScript
onReadData(callback: Callback<ArrayBuffer>): void
```

Subscribes audio data callback. The event is triggered when audio buffer is available for reading more data.

**Since:** 23

<!--Device-AudioCapturer-onReadData(callback: Callback<ArrayBuffer>): void--><!--Device-AudioCapturer-onReadData(callback: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | Yes | Callback with the buffer to read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onStateChange

```TypeScript
onStateChange(callback: Callback<AudioState>): void
```

Subscribes audio state change event callback.

**Since:** 23

<!--Device-AudioCapturer-onStateChange(callback: Callback<AudioState>): void--><!--Device-AudioCapturer-onStateChange(callback: Callback<AudioState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | Yes | Callback used to listen for the audio state change event. |

## read

```TypeScript
read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void
```

Reads the buffer from the audio capturer. This method uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** readData

<!--Device-AudioCapturer-read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void--><!--Device-AudioCapturer-read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | Number of bytes to read. |
| isBlockingRead | boolean | Yes | Whether to block the read operation. **true** to block, **false** otherwise. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the buffer read; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getBufferSize().then((bufferSize: number) => {
  console.info('Succeeded in doing getBufferSize.');
  audioCapturer.read(bufferSize, true, (err: BusinessError, buffer: ArrayBuffer) => {
    if (err) {
      console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in doing read.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to getBufferSize. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getBufferSize().then((bufferSize: number) => {
  console.info('Succeeded in doing getBufferSize.');
  audioCapturer.read(bufferSize, true).then((buffer: ArrayBuffer) => {
    console.info('Succeeded in doing read.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to getBufferSize. Code: ${err.code}, message: ${err.message}`);
});
```

## read

```TypeScript
read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>
```

Reads the buffer. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** readData

<!--Device-AudioCapturer-read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>--><!--Device-AudioCapturer-read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | Number of bytes to read. |
| isBlockingRead | boolean | Yes | Whether to block the read operation. **true** to block, **false** otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the data read from the buffer. |

**Examples**

See [read](#read)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this audio capturer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioCapturer-release(callback: AsyncCallback<void>): void--><!--Device-AudioCapturer-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

tonePlayer.release((err: BusinessError) => {
  if (err) {
    console.error(`callback call release failed error: ${err.message}`);
    return;
  } else {
    console.info('callback call release success ');
  }
});
```

```TypeScript
tonePlayer.release().then(() => {
  console.info('promise call release');
}).catch(() => {
  console.error('promise call release fail');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.release((err: BusinessError) => {
  if (err) {
    console.error('capturer release failed');
  } else {
    console.info('capturer released.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.release().then(() => {
  console.info('AudioFrameworkRecLog: ---------RELEASE RECORD---------');
  console.info('AudioFrameworkRecLog: Capturer release : SUCCESS');
  console.info(`AudioFrameworkRecLog: AudioCapturer : STATE : ${audioCapturer.state}`);
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRecLog: Capturer stop: ERROR: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.release((err: BusinessError) => {
  if (err) {
    console.error('Renderer release failed');
  } else {
    console.info('Renderer released.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.release().then(() => {
  console.info('Renderer released successfully');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## release

```TypeScript
release(): Promise<void>
```

Releases this audio capturer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioCapturer-release(): Promise<void>--><!--Device-AudioCapturer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [release](#release)

## requestPlaybackCaptureStart

```TypeScript
requestPlaybackCaptureStart(callback: Callback<PlaybackCaptureStartState>): void
```

Asynchronously request to start the playback capture stream. This function is non-blocking, which means system will continue to process user authorization and stream starting when receiving the start request. And the final result will be returned by callback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-requestPlaybackCaptureStart(callback: Callback<PlaybackCaptureStartState>): void--><!--Device-AudioCapturer-requestPlaybackCaptureStart(callback: Callback<PlaybackCaptureStartState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PlaybackCaptureStartState](arkts-audio-audio-playbackcapturestartstate-e.md)&gt; | Yes | Callback function used to receive the final result of start request. |

## setIndependentAudioSessionStrategy

```TypeScript
setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void
```

Sets the independent audio session strategy and behavior parameters.

> **NOTE：**&gt;
> If this API is called while an audio capturer is running, you must call the
> [start](#start) API again for
> the settings to take effect.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void--><!--Device-AudioCapturer-setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| strategy | [AudioSessionStrategy](arkts-audio-audio-audiosessionstrategy-i.md) | Yes | Audio session strategy. |
| behavior | int | Yes | Specifies the audio session behavior.<br>This can be a single flag or a bitwise OR combination of multiple flags.<br>For details about the supported audio session behaviors, see [AudioSessionBehaviorFlags](arkts-audio-audio-audiosessionbehaviorflags-e.md). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permit at current state. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mute | boolean | Yes | Use true if application recording stream muted by application if self. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permitted at current state, stream is not running. |

## setNoiseReductionMode

```TypeScript
setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void
```

Sets noise reduction mode for current audio capturer. The supported mode should be obtained by [getSupportedNoiseReductionModes](#getsupportednoisereductionmodes). The actual effect may vary from different audio devices, and will be invalid when there are multiple recording streams running simultaneously. The mode can only be changed in created and stopped state.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturer-setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void--><!--Device-AudioCapturer-setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| noiseReductionMode | [NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md) | Yes | The noise reduction mode to set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Illegal state, audio capturer is in running or released state. |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) | The setted mode is not supported. |
| [6800301](../errorcode-audio.md#6800301-system-error) | Audio server process died. |

## setWillMuteWhenInterrupted

```TypeScript
setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>
```

Sets whether to [mute the current audio recording stream when an audio interruption occurs](../../../media/audio/using-audiocapturer-for-recording.md#setting-the-mute-interruption-mode). This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioCapturer-setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>--><!--Device-AudioCapturer-setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| muteWhenInterrupted | boolean | Yes | Whether to mute the current audio recording stream during an audio interruption. **true** to mute, **false** otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permitted at current state. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.setWillMuteWhenInterrupted(true).then(() => {
  console.info('setWillMuteWhenInterrupted Success!');
}).catch((err: BusinessError) => {
  console.error(`setWillMuteWhenInterrupted Fail: ${err}`);
});
```

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts this audio capturer to start capturing audio data. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioCapturer-start(callback: AsyncCallback<void>): void--><!--Device-AudioCapturer-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. If the operation fails, an error object with the following error code is returned:<br>Error code 6800301: indicates abnormal status, focus preemption failure, and abnormal system processing. For details, see system logs. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

tonePlayer.start((err: BusinessError) => {
  if (err) {
    console.error(`callback call start failed error: ${err.message}`);
    return;
  } else {
    console.info('callback call start success');
  }
});
```

```TypeScript
tonePlayer.start().then(() => {
  console.info('promise call start');
}).catch(() => {
  console.error('promise call start fail');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.start((err: BusinessError) => {
  if (err) {
    console.error('Capturer start failed.');
  } else {
    console.info('Capturer start success.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.start().then(() => {
  console.info('Succeeded in doing start.');
  if (audioCapturer.state == audio.AudioState.STATE_RUNNING) {
    console.info('AudioFrameworkRecLog: AudioCapturer is in Running State');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to start. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.start((err: BusinessError) => {
  if (err) {
    console.error('Renderer start failed.');
  } else {
    console.info('Renderer start success.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.start().then(() => {
  console.info('Renderer started');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## start

```TypeScript
start(): Promise<void>
```

Starts this audio capturer to start capturing audio data. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioCapturer-start(): Promise<void>--><!--Device-AudioCapturer-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise object, which indicates that the capturer is started successfully. If the operation fails, an error object with the following error code is returned: <br>Error code 6800301: indicates abnormal status, focus preemption failure, and abnormal system processing. For details, see system logs. |

**Examples**

See [start](#start)

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops this audio capturer, ceasing the input audio stream. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioCapturer-stop(callback: AsyncCallback<void>): void--><!--Device-AudioCapturer-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

tonePlayer.stop((err: BusinessError) => {
  if (err) {
    console.error(`callback call stop error: ${err.message}`);
    return;
  } else {
    console.error('callback call stop success ');
  }
});
```

```TypeScript
tonePlayer.stop().then(() => {
  console.info('promise call stop finish');
}).catch(() => {
  console.error('promise call stop fail');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.stop((err: BusinessError) => {
  if (err) {
    console.error('Capturer stop failed');
  } else {
    console.info('Capturer stopped.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.stop().then(() => {
  console.info('Succeeded in doing stop.');
  if (audioCapturer.state == audio.AudioState.STATE_STOPPED){
    console.info('AudioFrameworkRecLog: State is Stopped:');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to stop. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.stop((err: BusinessError) => {
  if (err) {
    console.error('Renderer stop failed');
  } else {
    console.info('Renderer stopped.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.stop().then(() => {
  console.info('Renderer stopped successfully');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## stop

```TypeScript
stop(): Promise<void>
```

Stops this audio capturer, ceasing the input audio stream. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioCapturer-stop(): Promise<void>--><!--Device-AudioCapturer-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [stop](#stop)

## state

```TypeScript
readonly state: AudioState
```

Audio capturer state.

**Type:** AudioState

**Since:** 23

<!--Device-AudioCapturer-readonly state: AudioState--><!--Device-AudioCapturer-readonly state: AudioState-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

