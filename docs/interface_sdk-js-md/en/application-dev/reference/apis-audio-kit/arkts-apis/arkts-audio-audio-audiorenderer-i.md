# AudioRenderer

This interface provides APIs for audio rendering.Before calling any API in AudioRenderer, you must use [createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md) to create an AudioRenderer instance.

> **NOTE：**&gt;
> - The initial APIs of this interface are supported since API version 8.

**Since:** 23

<!--Device-audio-interface AudioRenderer--><!--Device-audio-interface AudioRenderer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## drain

```TypeScript
drain(callback: AsyncCallback<void>): void
```

Drains the playback buffer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-drain(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-drain(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.drain((err: BusinessError) => {
  if (err) {
    console.error('Renderer drain failed');
  } else {
    console.info('Renderer drained.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.drain().then(() => {
  console.info('Renderer drained successfully');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## drain

```TypeScript
drain(): Promise<void>
```

Drains the playback buffer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-drain(): Promise<void>--><!--Device-AudioRenderer-drain(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [drain](#drain)

## flush

```TypeScript
flush(): Promise<void>
```

Flushes the buffer. This API is available when [AudioState](arkts-audio-audio-audiostate-e.md) is **STATE_RUNNING**, **STATE_PAUSED**, or **STATE_STOPPED**. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-flush(): Promise<void>--><!--Device-AudioRenderer-flush(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permit at current state. Return by promise. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.flush().then(() => {
  console.info('Renderer flushed successfully');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## getAudioEffectMode

```TypeScript
getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void
```

Obtains the audio effect mode in use. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void--><!--Device-AudioRenderer-getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio effect mode obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioEffectMode((err: BusinessError, effectMode: audio.AudioEffectMode) => {
  if (err) {
    console.error('Failed to get params');
  } else {
    console.info(`getAudioEffectMode: ${effectMode}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioEffectMode().then((effectMode: audio.AudioEffectMode) => {
  console.info(`getAudioEffectMode: ${effectMode}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## getAudioEffectMode

```TypeScript
getAudioEffectMode(): Promise<AudioEffectMode>
```

Obtains the audio effect mode in use. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-getAudioEffectMode(): Promise<AudioEffectMode>--><!--Device-AudioRenderer-getAudioEffectMode(): Promise<AudioEffectMode>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md)&gt; | Promise used to return the audio effect mode. |

**Examples**

See [getAudioEffectMode](#getaudioeffectmode)

## getAudioStreamId

```TypeScript
getAudioStreamId(callback: AsyncCallback<long>): void
```

Obtains the stream ID of this audio renderer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-getAudioStreamId(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getAudioStreamId(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Obtains the stream ID of this audio renderer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-getAudioStreamId(): Promise<long>--><!--Device-AudioRenderer-getAudioStreamId(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Obtains the stream ID of this audio renderer. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-getAudioStreamIdSync(): long--><!--Device-AudioRenderer-getAudioStreamIdSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Obtains the timestamp of the current playback position, measured in nanoseconds from the Unix epoch (January 1, 1 970). This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-getAudioTime(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getAudioTime(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Obtains the timestamp of the current playback position, measured in nanoseconds from the Unix epoch (January 1, 1 970). This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-getAudioTime(): Promise<long>--><!--Device-AudioRenderer-getAudioTime(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the timestamp. |

**Examples**

See [getAudioTime](#getaudiotime)

## getAudioTimestampInfo

```TypeScript
getAudioTimestampInfo(): Promise<AudioTimestampInfo>
```

Obtains the timestamp and position information of an output audio stream. It adapts to the speed adjustment interface. This API uses a promise to return the result.This information is commonly used for audio and video synchronization.Note that when the actual playback position (**framePosition**) is 0, the timestamp remains fixed until the stream begins to play. The playback position is also reset when **Flush** is called.Additionally, changes in the audio stream route, such as switching devices or output types, will reset the playback position, whereas the timestamp keeps increasing. You are advised to call this API to obtain the corresponding value only when the actual playback position and timestamp are stable. This API adapts to the speed adjustment interface. For example, if the playback speed is set to 2x, the rate at which the playback position increases is also twice the normal speed.

**Since:** 23

<!--Device-AudioRenderer-getAudioTimestampInfo(): Promise<AudioTimestampInfo>--><!--Device-AudioRenderer-getAudioTimestampInfo(): Promise<AudioTimestampInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md)&gt; | Promise used to return the audio stream timestamp and the current data frame position. |

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

Obtains the timestamp and position information of an output audio stream. It adapts to the speed adjustment interface. This API returns the result synchronously.This information is commonly used for audio and video synchronization.Note that when the actual playback position (**framePosition**) is 0, the timestamp remains fixed until the stream begins to play. The playback position is also reset when **Flush** is called.Additionally, changes in the audio stream route, such as switching devices or output types, will reset the playback position, whereas the timestamp keeps increasing. You are advised to call this API to obtain the corresponding value only when the actual playback position and timestamp are stable. This API adapts to the speed adjustment interface. For example, if the playback speed is set to 2x, the rate at which the playback position increases is also twice the normal speed.

**Since:** 23

<!--Device-AudioRenderer-getAudioTimestampInfoSync(): AudioTimestampInfo--><!--Device-AudioRenderer-getAudioTimestampInfoSync(): AudioTimestampInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md) | Information about the audio stream timestamp and the current data frame position. |

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

Obtains the timestamp of the current playback position, measured in nanoseconds from the Unix epoch (January 1, 1 970). This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-getAudioTimeSync(): long--><!--Device-AudioRenderer-getAudioTimeSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Obtains a reasonable minimum buffer size in bytes for rendering. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-getBufferSize(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getBufferSize(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Obtains a reasonable minimum buffer size in bytes for rendering. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-getBufferSize(): Promise<long>--><!--Device-AudioRenderer-getBufferSize(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Obtains a reasonable minimum buffer size in bytes for rendering. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-getBufferSizeSync(): long--><!--Device-AudioRenderer-getBufferSizeSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

## getCurrentOutputDevices

```TypeScript
getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void
```

Obtains the output device information of the audio stream. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the output device information obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getCurrentOutputDevices((err: BusinessError, deviceInfo: audio.AudioDeviceDescriptors) => {
  if (err) {
    console.error(`getCurrentOutputDevices Fail: ${err}`);
  } else {
    for (let i = 0; i < deviceInfo.length; i++) {
      console.info(`DeviceInfo id: ${deviceInfo[i].id}`);
      console.info(`DeviceInfo type: ${deviceInfo[i].deviceType}`);
      console.info(`DeviceInfo role: ${deviceInfo[i].deviceRole}`);
      console.info(`DeviceInfo name: ${deviceInfo[i].name}`);
      console.info(`DeviceInfo address: ${deviceInfo[i].address}`);
      console.info(`DeviceInfo samplerate: ${deviceInfo[i].sampleRates[0]}`);
      console.info(`DeviceInfo channelcount: ${deviceInfo[i].channelCounts[0]}`);
      console.info(`DeviceInfo channelmask: ${deviceInfo[i].channelMasks[0]}`);
    }
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getCurrentOutputDevices().then((deviceInfo: audio.AudioDeviceDescriptors) => {
  for (let i = 0; i < deviceInfo.length; i++) {
    console.info(`DeviceInfo id: ${deviceInfo[i].id}`);
    console.info(`DeviceInfo type: ${deviceInfo[i].deviceType}`);
    console.info(`DeviceInfo role: ${deviceInfo[i].deviceRole}`);
    console.info(`DeviceInfo name: ${deviceInfo[i].name}`);
    console.info(`DeviceInfo address: ${deviceInfo[i].address}`);
    console.info(`DeviceInfo samplerate: ${deviceInfo[i].sampleRates[0]}`);
    console.info(`DeviceInfo channelcount: ${deviceInfo[i].channelCounts[0]}`);
    console.info(`DeviceInfo channelmask: ${deviceInfo[i].channelMasks[0]}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Get current output devices Fail: ${err}`);
});
```

## getCurrentOutputDevices

```TypeScript
getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>
```

Obtains the output device information of the audio stream. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>--><!--Device-AudioRenderer-getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Promise used to return the output device information. |

**Examples**

See [getCurrentOutputDevices](#getcurrentoutputdevices)

## getCurrentOutputDevicesSync

```TypeScript
getCurrentOutputDevicesSync(): AudioDeviceDescriptors
```

Obtains the output device information of the audio stream. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-getCurrentOutputDevicesSync(): AudioDeviceDescriptors--><!--Device-AudioRenderer-getCurrentOutputDevicesSync(): AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) | Output device information. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let deviceInfo: audio.AudioDeviceDescriptors = audioRenderer.getCurrentOutputDevicesSync();
  for (let i = 0; i < deviceInfo.length; i++) {
    console.info(`DeviceInfo id: ${deviceInfo[i].id}`);
    console.info(`DeviceInfo type: ${deviceInfo[i].deviceType}`);
    console.info(`DeviceInfo role: ${deviceInfo[i].deviceRole}`);
    console.info(`DeviceInfo name: ${deviceInfo[i].name}`);
    console.info(`DeviceInfo address: ${deviceInfo[i].address}`);
    console.info(`DeviceInfo samplerate: ${deviceInfo[i].sampleRates[0]}`);
    console.info(`DeviceInfo channelcount: ${deviceInfo[i].channelCounts[0]}`);
    console.info(`DeviceInfo channelmask: ${deviceInfo[i].channelMasks[0]}`);
  }
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get current output devices Fail: ${error}`);
}
```

## getLatency

```TypeScript
getLatency(type: AudioLatencyType): int
```

Obtains the estimated latency of the current audio route.

> **NOTE：**&gt;
> - The estimated latency of a wireless audio device may be inaccurate. The result is for reference only.&gt;
> - Since the latency is not counted in the real-time buffer, you are advised to obtain the latency only when the
> audio playback starts to avoid frequent calls. Otherwise, the API call may be blocked due to route switching.&gt;
> - You are advised to use [getAudioTimestampInfo](#getaudiotimestampinfo) or
> [getAudioTimestampInfoSync](#getaudiotimestampinfosync) to implement audio and video
> synchronization after the audio is output to the hardware.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRenderer-getLatency(type: AudioLatencyType): int--><!--Device-AudioRenderer-getLatency(type: AudioLatencyType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [AudioLatencyType](arkts-audio-audio-audiolatencytype-e.md) | Yes | Obtains the latency type. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Audio latency, in milliseconds. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permitted in release state. |
| [6800301](../errorcode-audio.md#6800301-system-error) | System internal error, like audio service error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const latency: number = audioRenderer.getLatency(audio.AudioLatencyType.LATENCY_TYPE_ALL);
  console.info(`Current audio latency: ${latency}ms`);
} catch (err) {
  const error = err as BusinessError;
  console.error(`Failed to get latency. Code: ${error.code}, message: ${error.message}`);
}
```

## getLoudnessGain

```TypeScript
getLoudnessGain(): double
```

Gets loudness gain of this stream.

**Since:** 23

<!--Device-AudioRenderer-getLoudnessGain(): double--><!--Device-AudioRenderer-getLoudnessGain(): double-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| double | Returns one float value, unit is dB. |

**Examples**

```TypeScript
let loudnessGain = audioRenderer.getLoudnessGain();
```

## getMaxStreamVolume

```TypeScript
getMaxStreamVolume(callback: AsyncCallback<double>): void
```

Obtains the maximum volume of the audio stream. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-getMaxStreamVolume(callback: AsyncCallback<double>): void--><!--Device-AudioRenderer-getMaxStreamVolume(callback: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the maximum volume obtained; otherwise, **err** is an error object.<br>The volume range is [0.0, 1.0]. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMaxStreamVolume((err: BusinessError, maxVolume: number) => {
  if (err) {
    console.error(`getMaxStreamVolume Fail: ${err}`);
  } else {
    console.info(`getMaxStreamVolume Success! ${maxVolume}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMaxStreamVolume().then((value: number) => {
  console.info(`Get max stream volume Success! ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Get max stream volume Fail: ${err}`);
});
```

## getMaxStreamVolume

```TypeScript
getMaxStreamVolume(): Promise<double>
```

Obtains the maximum volume of the audio stream. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-getMaxStreamVolume(): Promise<double>--><!--Device-AudioRenderer-getMaxStreamVolume(): Promise<double>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;double&gt; | Promise used to return the maximum volume of the audio stream. <br>The volume range is [0.0, 1.0]. |

**Examples**

See [getMaxStreamVolume](#getmaxstreamvolume)

## getMaxStreamVolumeSync

```TypeScript
getMaxStreamVolumeSync(): double
```

Obtains the maximum volume of the audio stream. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-getMaxStreamVolumeSync(): double--><!--Device-AudioRenderer-getMaxStreamVolumeSync(): double-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| double | Maximum volume of the audio stream, which ranges from 0.0 to 1.0. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getMaxStreamVolumeSync();
  console.info(`Get max stream volume Success! ${value}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get max stream volume Fail: ${error}`);
}
```

## getMinStreamVolume

```TypeScript
getMinStreamVolume(callback: AsyncCallback<double>): void
```

Obtains the minimum volume of the audio stream. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-getMinStreamVolume(callback: AsyncCallback<double>): void--><!--Device-AudioRenderer-getMinStreamVolume(callback: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the minimum volume obtained; otherwise, **err** is an error object.<br>The volume range is [0.0, 1.0]. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMinStreamVolume((err: BusinessError, minVolume: number) => {
  if (err) {
    console.error(`getMinStreamVolume error: ${err}`);
  } else {
    console.info(`getMinStreamVolume Success! ${minVolume}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMinStreamVolume().then((value: number) => {
  console.info(`Get min stream volume Success! ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Get min stream volume Fail: ${err}`);
});
```

## getMinStreamVolume

```TypeScript
getMinStreamVolume(): Promise<double>
```

Obtains the minimum volume of the audio stream. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-getMinStreamVolume(): Promise<double>--><!--Device-AudioRenderer-getMinStreamVolume(): Promise<double>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;double&gt; | Promise used to return the minimum volume of the audio stream. <br>The volume range is [0.0, 1.0]. |

**Examples**

See [getMinStreamVolume](#getminstreamvolume)

## getMinStreamVolumeSync

```TypeScript
getMinStreamVolumeSync(): double
```

Obtains the minimum volume of the audio stream. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-getMinStreamVolumeSync(): double--><!--Device-AudioRenderer-getMinStreamVolumeSync(): double-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| double | Minimum volume of the audio stream, which ranges from 0.0 to 1.0. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getMinStreamVolumeSync();
  console.info(`Get min stream volume Success! ${value}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get min stream volume Fail: ${error}`);
}
```

## getRendererInfo

```TypeScript
getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void
```

Obtains the information about this audio renderer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void--><!--Device-AudioRenderer-getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio renderer information obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRendererInfo((err: BusinessError, audioRendererInfo: audio.AudioRendererInfo) => {
  if (err) {
    console.error(`Failed to get renderer info. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRendererInfo().then((audioRendererInfo: audio.AudioRendererInfo) => {
  console.info(`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get renderer info. Code: ${err.code}, message: ${err.message}`);
});
```

## getRendererInfo

```TypeScript
getRendererInfo(): Promise<AudioRendererInfo>
```

Obtains the information about this audio renderer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-getRendererInfo(): Promise<AudioRendererInfo>--><!--Device-AudioRenderer-getRendererInfo(): Promise<AudioRendererInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md)&gt; | Promise used to return the audio renderer information. |

**Examples**

See [getRendererInfo](#getrendererinfo)

## getRendererInfoSync

```TypeScript
getRendererInfoSync(): AudioRendererInfo
```

Obtains the information about this audio renderer. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-getRendererInfoSync(): AudioRendererInfo--><!--Device-AudioRenderer-getRendererInfoSync(): AudioRendererInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | Audio renderer information. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioRendererInfo = audioRenderer.getRendererInfoSync();
  console.info(`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get renderer info. Code: ${error.code}, message: ${error.message}`);
}
```

## getRenderRate

```TypeScript
getRenderRate(callback: AsyncCallback<AudioRendererRate>): void
```

Obtains the audio renderer rate. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [getSpeed](#getspeed)

<!--Device-AudioRenderer-getRenderRate(callback: AsyncCallback<AudioRendererRate>): void--><!--Device-AudioRenderer-getRenderRate(callback: AsyncCallback<AudioRendererRate>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the render rate obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRenderRate((err: BusinessError, renderRate: audio.AudioRendererRate) => {
  console.info(`getRenderRate: ${renderRate}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRenderRate().then((renderRate: audio.AudioRendererRate) => {
  console.info(`getRenderRate: ${renderRate}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## getRenderRate

```TypeScript
getRenderRate(): Promise<AudioRendererRate>
```

Obtains the audio renderer rate. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [getSpeed](#getspeed)

<!--Device-AudioRenderer-getRenderRate(): Promise<AudioRendererRate>--><!--Device-AudioRenderer-getRenderRate(): Promise<AudioRendererRate>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md)&gt; | Promise used to return the render rate. |

**Examples**

See [getRenderRate](#getrenderrate)

## getRenderRateSync

```TypeScript
getRenderRateSync(): AudioRendererRate
```

Obtains the audio renderer rate. This API returns the result synchronously.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [getSpeed](#getspeed)

<!--Device-AudioRenderer-getRenderRateSync(): AudioRendererRate--><!--Device-AudioRenderer-getRenderRateSync(): AudioRendererRate-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) | Audio render rate. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let renderRate: audio.AudioRendererRate = audioRenderer.getRenderRateSync();
  console.info(`getRenderRate: ${renderRate}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

## getSilentModeAndMixWithOthers

```TypeScript
getSilentModeAndMixWithOthers(): boolean
```

Obtains the silent mode in concurrent playback for the audio stream.

**Since:** 23

<!--Device-AudioRenderer-getSilentModeAndMixWithOthers(): boolean--><!--Device-AudioRenderer-getSilentModeAndMixWithOthers(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Enabled status of the silent mode in concurrent playback. **true** if enabled, **false** otherwise. |

**Examples**

```TypeScript
let on = audioRenderer.getSilentModeAndMixWithOthers();
```

## getSpeed

```TypeScript
getSpeed(): double
```

Obtains the playback speed.

**Since:** 23

<!--Device-AudioRenderer-getSpeed(): double--><!--Device-AudioRenderer-getSpeed(): double-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| double | Playback rate, which ranges from 0.25 to 4.0. |

**Examples**

```TypeScript
let speed = audioRenderer.getSpeed();
```

## getStreamInfo

```TypeScript
getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void
```

Obtains the stream information of this audio renderer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void--><!--Device-AudioRenderer-getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Obtains the stream information of this audio renderer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-getStreamInfo(): Promise<AudioStreamInfo>--><!--Device-AudioRenderer-getStreamInfo(): Promise<AudioStreamInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Obtains the stream information of this audio renderer. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-getStreamInfoSync(): AudioStreamInfo--><!--Device-AudioRenderer-getStreamInfoSync(): AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

## getUnderflowCount

```TypeScript
getUnderflowCount(callback: AsyncCallback<long>): void
```

Obtains the number of underflow audio frames in the audio stream that is being played. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-getUnderflowCount(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getUnderflowCount(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the number of underloaded audio frames obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getUnderflowCount((err: BusinessError, underflowCount: number) => {
  if (err) {
    console.error(`getUnderflowCount Fail: ${err}`);
  } else {
    console.info(`getUnderflowCount Success! ${underflowCount}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getUnderflowCount().then((value: number) => {
  console.info(`Get underflow count Success! ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Get underflow count Fail: ${err}`);
});
```

## getUnderflowCount

```TypeScript
getUnderflowCount(): Promise<long>
```

Obtains the number of underflow audio frames in the audio stream that is being played. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-getUnderflowCount(): Promise<long>--><!--Device-AudioRenderer-getUnderflowCount(): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the number of underflow audio frames. |

**Examples**

See [getUnderflowCount](#getunderflowcount)

## getUnderflowCountSync

```TypeScript
getUnderflowCountSync(): long
```

Obtains the number of underflow audio frames in the audio stream that is being played. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-getUnderflowCountSync(): long--><!--Device-AudioRenderer-getUnderflowCountSync(): long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| long | Number of underflow audio frames. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getUnderflowCountSync();
  console.info(`Get underflow count Success! ${value}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get underflow count Fail: ${error}`);
}
```

## getVolume

```TypeScript
getVolume(): double
```

Obtains the volume of the audio stream. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-getVolume(): double--><!--Device-AudioRenderer-getVolume(): double-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| double | Volume, in the range [0.0, 1.0]. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the volume. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the volume is obtained.');
});
```

```TypeScript
audioManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Promise returned to indicate that the volume is obtained ${value} .`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getVolume();
  console.info(`Indicate that the volume is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume, error ${error}.`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to get volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting volume. Volume: ${value}.`);
});
```

```TypeScript
audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in getting volume. Volume: ${value}.`);
});
```

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void
```

Unsubscribes from the audio interruption event. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-AudioRenderer-off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | Yes | Event type. The event **'audioInterrupt'** is triggered when the audio focus is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | No | Callback used to return the event information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('markReach')

```TypeScript
off(type: 'markReach', callback?: Callback<long>): void
```

Unsubscribes from the mark reached event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioRenderer-off(type: 'markReach', callback?: Callback<long>): void--><!--Device-AudioRenderer-off(type: 'markReach', callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'markReach' | Yes | Event type. The event **'markReach'** is triggered when the number of frames rendered reaches the value of the **frame** parameter. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | No | Callback used to return the value of the **frame** parameter.<br>**Since:** 18 |

## off('outputDeviceChange')

```TypeScript
off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void
```

Unsubscribes from the audio output device change event. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-AudioRenderer-off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'outputDeviceChange' | Yes | Event type. The event **'outputDeviceChange'** is triggered when an audio output device is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | No | Callback used to return the output device descriptor of the current audio stream. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('outputDeviceChangeWithInfo')

```TypeScript
off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void
```

Unsubscribes from the change event of audio output devices and reasons. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioRenderer-off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'outputDeviceChangeWithInfo' | Yes | Event type. The event **'outputDeviceChangeWithInfo'** is triggered when an audio output device is changed, and the change reason is reported. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | No | Callback used to return the output device descriptor of the current audio stream and the change reason. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('periodReach')

```TypeScript
off(type: 'periodReach', callback?: Callback<long>): void
```

Unsubscribes from the period reached event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioRenderer-off(type: 'periodReach', callback?: Callback<long>): void--><!--Device-AudioRenderer-off(type: 'periodReach', callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'periodReach' | Yes | Event type. The event **'periodReach'** is triggered each time the number of frames rendered reaches the value of the **frame** parameter. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | No | Callback used to return the value of the **frame** parameter.<br>**Since:** 18 |

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: Callback<AudioState>): void
```

Unsubscribes from the audio renderer state change event. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-AudioRenderer-off(type: 'stateChange', callback?: Callback<AudioState>): void--><!--Device-AudioRenderer-off(type: 'stateChange', callback?: Callback<AudioState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'stateChange' | Yes | Event type. The event **'stateChange'** is triggered when the listening for audio renderer state change event is canceled. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | No | Callback used to return the audio status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('writeData')

```TypeScript
off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void
```

Unsubscribes from the audio data write event. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioRenderer-off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'writeData' | Yes | Event type. The event **'writeData'** is triggered when audio data needs to be written. |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | No | Callback used to write the data to the buffer.<br>API version 11 does not support the return of the callback result. API version 12 and later support the return of the callback result [AudioDataCallbackResult](arkts-audio-audio-audiodatacallbackresult-e.md).<br>**Since:** 12 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offAudioInterrupt

```TypeScript
offAudioInterrupt(callback?: Callback<InterruptEvent>): void
```

Unsubscribes audio interrupt events.

**Since:** 23

<!--Device-AudioRenderer-offAudioInterrupt(callback?: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-offAudioInterrupt(callback?: Callback<InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | No | Callback used to listen for interrupt callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offMarkReach

```TypeScript
offMarkReach(callback?: Callback<long>): void
```

Unsubscribes from mark reached events.

**Since:** 23

<!--Device-AudioRenderer-offMarkReach(callback?: Callback<long>): void--><!--Device-AudioRenderer-offMarkReach(callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | No | Callback invoked when the event is triggered. |

## offOutputDeviceChange

```TypeScript
offOutputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void
```

Unsubscribes output device change event callback.

**Since:** 23

<!--Device-AudioRenderer-offOutputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-offOutputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | No | Callback used in subscribe. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offOutputDeviceChangeWithInfo

```TypeScript
offOutputDeviceChangeWithInfo(callback?: Callback<AudioStreamDeviceChangeInfo>): void
```

Unsubscribes output device change event callback.

**Since:** 23

<!--Device-AudioRenderer-offOutputDeviceChangeWithInfo(callback?: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-offOutputDeviceChangeWithInfo(callback?: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | No | Callback used in subscribe. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offPeriodReach

```TypeScript
offPeriodReach(callback?: Callback<long>): void
```

Unsubscribes from period reached events.

**Since:** 23

<!--Device-AudioRenderer-offPeriodReach(callback?: Callback<long>): void--><!--Device-AudioRenderer-offPeriodReach(callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | No | Callback invoked when the event is triggered. |

## offStateChange

```TypeScript
offStateChange(callback?: Callback<AudioState>): void
```

Unsubscribes audio state change event callback.

**Since:** 23

<!--Device-AudioRenderer-offStateChange(callback?: Callback<AudioState>): void--><!--Device-AudioRenderer-offStateChange(callback?: Callback<AudioState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | No | Callback invoked when state change. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offWriteData

```TypeScript
offWriteData(callback?: AudioRendererWriteDataCallback): void
```

Unsubscribes audio data callback.

**Since:** 23

<!--Device-AudioRenderer-offWriteData(callback?: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-offWriteData(callback?: AudioRendererWriteDataCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | No | Audio renderer write data callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void
```

Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an asynchronous callback to return the result.The AudioRenderer instance proactively gains the focus when the **start** event occurs and releases the focus when the **pause** or **stop** event occurs. Therefore, you do not need to request to gain or release the focus.After this API is called, an [InterruptEvent](arkts-audio-audio-interruptevent-i.md) is received when the AudioRenderer instance fails to obtain the focus or an audio interruption event occurs (for example, the audio stream is interrupted by others). It is recommended that the application perform further processing based on the **InterruptEvent** information. For details, see [Introduction to Audio Focus](../../../media/audio/audio-playback-concurrency.md).

**Since:** 9

<!--Device-AudioRenderer-on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void-End-->

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

## on('markReach')

```TypeScript
on(type: 'markReach', frame: long, callback: Callback<long>): void
```

Subscribes to the mark reached event, which is triggered (only once) when the number of frames rendered reaches the value of the **frame** parameter. This API uses an asynchronous callback to return the result.For example, if **frame** is set to **100**, the callback is invoked when the number of rendered frames reaches the 100th frame.

**Since:** 8

<!--Device-AudioRenderer-on(type: 'markReach', frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-on(type: 'markReach', frame: long, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'markReach' | Yes | Event type. The event **'markReach'** is triggered when the number of frames rendered reaches the value of the **frame** parameter. |
| frame | long | Yes | Number of frames to trigger the event. The value must be greater than **0**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | Callback used to return the value of the **frame** parameter. |

## on('outputDeviceChange')

```TypeScript
on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void
```

Subscribes to the audio output device change event, which is triggered when an audio output device is changed. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-AudioRenderer-on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'outputDeviceChange' | Yes | Event type. The event **'outputDeviceChange'** is triggered when an audio output device is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to return the output device descriptor of the current audio stream. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('outputDeviceChangeWithInfo')

```TypeScript
on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void
```

Subscribes to the change event of audio output devices and reasons, which is triggered when an audio output device is changed, and the change reason is reported. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-AudioRenderer-on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'outputDeviceChangeWithInfo' | Yes | Event type. The event **'outputDeviceChangeWithInfo'** is triggered when an audio output device is changed, and the change reason is reported. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | Yes | Callback used to return the output device descriptor of the current audio stream and the change reason. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('periodReach')

```TypeScript
on(type: 'periodReach', frame: long, callback: Callback<long>): void
```

Subscribes to the period reached event, which is triggered each time the number of frames rendered reaches the value of the **frame** parameter. In other words, the information is reported periodically. This API uses an asynchronous callback to return the result.For example, if **frame** is set to **10**, the callback is invoked each time 10 frames are rendered, for example, when the number of frames rendered reaches the 10th frame, 20th frame, and 30th frame.

**Since:** 8

<!--Device-AudioRenderer-on(type: 'periodReach', frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-on(type: 'periodReach', frame: long, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'periodReach' | Yes | Event type. The event **'periodReach'** is triggered each time the number of frames rendered reaches the value of the **frame** parameter. |
| frame | long | Yes | Number of frames to trigger the event. The value must be greater than **0**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | Callback used to return the value of the **frame** parameter. |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: Callback<AudioState>): void
```

Subscribes to the audio renderer state change event, which is triggered when the state of the audio renderer is changed. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioRenderer-on(type: 'stateChange', callback: Callback<AudioState>): void--><!--Device-AudioRenderer-on(type: 'stateChange', callback: Callback<AudioState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'stateChange' | Yes | Event type. The event **'stateChange'** is triggered when the state of the audio renderer is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | Yes | Callback used to return the audio status. |

## on('writeData')

```TypeScript
on(type: 'writeData', callback: AudioRendererWriteDataCallback): void
```

Subscribes to the audio data write event, which is triggered when audio data needs to be written. This API uses an asynchronous callback to return the result.The callback function is used only to write audio data. Do not call AudioRenderer APIs in it.

**Since:** 11

<!--Device-AudioRenderer-on(type: 'writeData', callback: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-on(type: 'writeData', callback: AudioRendererWriteDataCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'writeData' | Yes | Event type. The event **'writeData'** is triggered when audio data needs to be written. |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | Yes | Callback used to write the data to the buffer.<br>API version 11 does not support the return of the callback result. API version 12 and later support the return of the callback result [AudioDataCallbackResult](arkts-audio-audio-audiodatacallbackresult-e.md).<br>**Since:** 12 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onAudioInterrupt

```TypeScript
onAudioInterrupt(callback: Callback<InterruptEvent>): void
```

Listens for audio interrupt events. This method uses a callback to get interrupt events. The interrupt event is triggered when audio playback is interrupted.

**Since:** 23

<!--Device-AudioRenderer-onAudioInterrupt(callback: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-onAudioInterrupt(callback: Callback<InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | Yes | Callback used to listen for interrupt callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onMarkReach

```TypeScript
onMarkReach(frame: long, callback: Callback<long>): void
```

Subscribes to mark reached events. When the number of frames rendered reaches the value of the frame parameter, the callback is invoked.

**Since:** 23

<!--Device-AudioRenderer-onMarkReach(frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-onMarkReach(frame: long, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frame | long | Yes | Number of frames to trigger the event. The value must be greater than 0. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | Callback invoked when the event is triggered. |

## onOutputDeviceChange

```TypeScript
onOutputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void
```

Subscribes output device change event callback. The event is triggered when output device change for this stream.

**Since:** 23

<!--Device-AudioRenderer-onOutputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-onOutputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to listen device change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onOutputDeviceChangeWithInfo

```TypeScript
onOutputDeviceChangeWithInfo(callback: Callback<AudioStreamDeviceChangeInfo>): void
```

Subscribes output device change event callback. The event is triggered when output device change for this stream.

**Since:** 23

<!--Device-AudioRenderer-onOutputDeviceChangeWithInfo(callback: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-onOutputDeviceChangeWithInfo(callback: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | Yes | Callback used to listen device change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onPeriodReach

```TypeScript
onPeriodReach(frame: long, callback: Callback<long>): void
```

Subscribes to period reached events. When the period of frame rendering reaches the value of frame parameter, the callback is invoked.

**Since:** 23

<!--Device-AudioRenderer-onPeriodReach(frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-onPeriodReach(frame: long, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frame | long | Yes | Period during which frame rendering is listened. The value must be greater than 0. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | Callback invoked when the event is triggered. |

## onStateChange

```TypeScript
onStateChange(callback: Callback<AudioState>): void
```

Subscribes audio renderer state change event callback.

**Since:** 23

<!--Device-AudioRenderer-onStateChange(callback: Callback<AudioState>): void--><!--Device-AudioRenderer-onStateChange(callback: Callback<AudioState>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | Yes | Callback invoked when state change. |

## onWriteData

```TypeScript
onWriteData(callback: AudioRendererWriteDataCallback): void
```

Subscribes audio data callback. The event is triggered when audio buffer is available for writing more data.

**Since:** 23

<!--Device-AudioRenderer-onWriteData(callback: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-onWriteData(callback: AudioRendererWriteDataCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | Yes | Audio renderer write data callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses this audio renderer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-pause(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-pause(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.pause((err: BusinessError) => {
  if (err) {
    console.error('Renderer pause failed');
  } else {
    console.info('Renderer paused.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.pause().then(() => {
  console.info('Renderer paused');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## pause

```TypeScript
pause(): Promise<void>
```

Pauses this audio renderer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-pause(): Promise<void>--><!--Device-AudioRenderer-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [pause](#pause)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the renderer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-release(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Releases the renderer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-release(): Promise<void>--><!--Device-AudioRenderer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [release](#release)

## setAudioEffectMode

```TypeScript
setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void
```

Sets an audio effect mode. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md) | Yes | Audio effect mode to set. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by callback. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setAudioEffectMode(audio.AudioEffectMode.EFFECT_DEFAULT, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set params');
  } else {
    console.info('Callback invoked to indicate a successful audio effect mode setting.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setAudioEffectMode(audio.AudioEffectMode.EFFECT_DEFAULT).then(() => {
  console.info('setAudioEffectMode SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## setAudioEffectMode

```TypeScript
setAudioEffectMode(mode: AudioEffectMode): Promise<void>
```

Sets an audio effect mode. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode): Promise<void>--><!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md) | Yes | Audio effect mode to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by promise. |

**Examples**

See [setAudioEffectMode](#setaudioeffectmode)

## setChannelBlendMode

```TypeScript
setChannelBlendMode(mode: ChannelBlendMode): void
```

Sets the audio channel blending mode. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-setChannelBlendMode(mode: ChannelBlendMode): void--><!--Device-AudioRenderer-setChannelBlendMode(mode: ChannelBlendMode): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [ChannelBlendMode](arkts-audio-audio-channelblendmode-e.md) | Yes | Audio channel blending mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permit at current state. |

**Examples**

```TypeScript
let mode = audio.ChannelBlendMode.MODE_DEFAULT;

audioRenderer.setChannelBlendMode(mode);
console.info(`BlendMode: ${mode}`);
```

## setDefaultOutputDevice

```TypeScript
setDefaultOutputDevice(deviceType: DeviceType): Promise<void>
```

Temporarily changes the current audio device This function applies on audiorenderers whose StreamUsage are STREAM_USAGE_VOICE_COMMUNICATION/STREAM_USAGE_VIDEO_COMMUNICATION/STREAM_USAGE_VOICE_MESSAGE. Setting the device will only takes effect if no other accessory such as headphones are in use

**Since:** 23

<!--Device-AudioRenderer-setDefaultOutputDevice(deviceType: DeviceType): Promise<void>--><!--Device-AudioRenderer-setDefaultOutputDevice(deviceType: DeviceType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | DeviceType | Yes | the available deviceTypes are EARPIECE: Built-in earpiece SPEAKER: Built-in speaker DEFAULT: System default output device |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permit at current state. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// This API can be called at any time after an AudioRenderer instance is created.
// If the API is called when no audio is being played, the system records the default device set by the application. When the application starts playing, the sound is played from this default device.
// If the API is called when audio is being played and no external device, such as a Bluetooth or wired headset, is connected, the system immediately switches to the default device. If an external device is connected, the system records the default device and switches to it once the external device is disconnected.
audioRenderer.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('setDefaultOutputDevice Success!');
}).catch((err: BusinessError) => {
  console.error(`setDefaultOutputDevice Fail: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('setDefaultOutputDevice Success!');
}).catch((err: BusinessError) => {
  console.error(`setDefaultOutputDevice Fail: ${err}`);
});
```

## setIndependentAudioSessionStrategy

```TypeScript
setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void
```

Sets the independent audio session strategy and behavior parameters.

> **NOTE：**&gt;
> If this API is called while an audio renderer is running, you must call the
> [start](#start) API again for
> the settings to take effect.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRenderer-setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void--><!--Device-AudioRenderer-setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

## setInterruptMode

```TypeScript
setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void
```

Sets the audio interruption mode for the application. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [InterruptMode](arkts-audio-audio-interruptmode-e.md) | Yes | Audio interruption mode. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let mode = 0;

audioRenderer.setInterruptMode(mode).then(() => {
  console.info('setInterruptMode Success!');
}).catch((err: BusinessError) => {
  console.error(`setInterruptMode Fail: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let mode = 1;

audioRenderer.setInterruptMode(mode, (err: BusinessError) => {
  if(err){
    console.error(`setInterruptMode Fail: ${err}`);
  }
  console.info('setInterruptMode Success!');
});
```

## setInterruptMode

```TypeScript
setInterruptMode(mode: InterruptMode): Promise<void>
```

Sets the audio interruption mode for the application. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode): Promise<void>--><!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [InterruptMode](arkts-audio-audio-interruptmode-e.md) | Yes | Audio interruption mode. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [setInterruptMode](#setinterruptmode)

## setInterruptModeSync

```TypeScript
setInterruptModeSync(mode: InterruptMode): void
```

Sets the audio interruption mode for the application. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-setInterruptModeSync(mode: InterruptMode): void--><!--Device-AudioRenderer-setInterruptModeSync(mode: InterruptMode): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [InterruptMode](arkts-audio-audio-interruptmode-e.md) | Yes | Audio interruption mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  audioRenderer.setInterruptModeSync(0);
  console.info('setInterruptMode Success!');
} catch (err) {
  let error = err as BusinessError;
  console.error(`setInterruptMode Fail: ${error}`);
}
```

## setLoudnessGain

```TypeScript
setLoudnessGain(loudnessGain: double): Promise<void>
```

Sets the loudness gain of this stream. The default loudness gain is 0.0dB. The stream usage of the audio renderer must be [STREAM_USAGE_MUSIC](arkts-audio-audio-streamusage-e.md#stream_usage_music), [STREAM_USAGE_MOVIE](arkts-audio-audio-streamusage-e.md#stream_usage_movie) or [STREAM_USAGE_AUDIOBOOK](arkts-audio-audio-streamusage-e.md#stream_usage_audiobook). After calling this interface, the adjustment of loundness gain will take effect immediately.

**Since:** 23

<!--Device-AudioRenderer-setLoudnessGain(loudnessGain: double): Promise<void>--><!--Device-AudioRenderer-setLoudnessGain(loudnessGain: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loudnessGain | double | Yes | Loudness gain to set, expressed in dB. The value type is float. The loudness gain changes from -90.0dB to 24.0dB. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) | Operation is not supported on this renderer, e.g. the stream usage of this renderer is not one of [STREAM_USAGE_MUSIC](arkts-audio-audio-streamusage-e.md#stream_usage_music), [STREAM_USAGE_MOVIE](arkts-audio-audio-streamusage-e.md#stream_usage_movie) or [STREAM_USAGE_AUDIOBOOK](arkts-audio-audio-streamusage-e.md#stream_usage_audiobook), or this renderer is routed through the high-resolution playback path. |

**Examples**

```TypeScript
audioRenderer.setLoudnessGain(1.0);
```

## setRenderRate

```TypeScript
setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void
```

Sets the render rate. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** setSpeed

<!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) | Yes | Audio render rate. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setRenderRate(audio.AudioRendererRate.RENDER_RATE_NORMAL, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set params');
  } else {
    console.info('Callback invoked to indicate a successful render rate setting.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setRenderRate(audio.AudioRendererRate.RENDER_RATE_NORMAL).then(() => {
  console.info('setRenderRate SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## setRenderRate

```TypeScript
setRenderRate(rate: AudioRendererRate): Promise<void>
```

Sets the render rate. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** setSpeed

<!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate): Promise<void>--><!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) | Yes | Audio render rate. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [setRenderRate](#setrenderrate)

## setSilentModeAndMixWithOthers

```TypeScript
setSilentModeAndMixWithOthers(on: boolean): void
```

Sets the silent mode in concurrent playback for the audio stream.If the silent mode in concurrent playback is enabled, the system mutes the audio stream and does not interrupt other audio streams. If the silent mode in concurrent playback is disabled, the audio stream can gain focus based on the system focus strategy.

**Since:** 23

<!--Device-AudioRenderer-setSilentModeAndMixWithOthers(on: boolean): void--><!--Device-AudioRenderer-setSilentModeAndMixWithOthers(on: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | boolean | Yes | Whether to enable or disable the silent mode in concurrent playback for the audio stream. **true** to enable, **false** otherwise. |

**Examples**

```TypeScript
audioRenderer.setSilentModeAndMixWithOthers(true);
```

## setSpeed

```TypeScript
setSpeed(speed: double): void
```

Sets the playback speed.

**Since:** 23

<!--Device-AudioRenderer-setSpeed(speed: double): void--><!--Device-AudioRenderer-setSpeed(speed: double): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | double | Yes | Playback rate, which ranges from 0.25 to 4.0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

**Examples**

```TypeScript
audioRenderer.setSpeed(1.5);
```

## setVolume

```TypeScript
setVolume(volume: double, callback: AsyncCallback<void>): void
```

Sets the volume for the audio stream. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-setVolume(volume: double, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setVolume(volume: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volume | double | Yes | Volume to set, which is in the range [0.0, 1.0]. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.setVolume(audio.AudioVolumeType.MEDIA, 10, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the volume. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate a successful volume setting.');
});
```

```TypeScript
audioVolumeGroupManager.setVolume(audio.AudioVolumeType.MEDIA, 10).then(() => {
  console.info('Promise returned to indicate a successful volume setting.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the volume. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate a successful volume setting.');
});
```

```TypeScript
audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10).then(() => {
  console.info('Promise returned to indicate a successful volume setting.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setVolume(0.5).then(() => {
  console.info('setVolume Success!');
}).catch((err: BusinessError) => {
  console.error(`setVolume Fail: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setVolume(0.5, (err: BusinessError) => {
  if(err){
    console.error(`setVolume Fail: ${err}`);
    return;
  }
  console.info('setVolume Success!');
});
```

## setVolume

```TypeScript
setVolume(volume: double): Promise<void>
```

Sets the volume for the audio stream. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-setVolume(volume: double): Promise<void>--><!--Device-AudioRenderer-setVolume(volume: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volume | double | Yes | Volume to set, which is in the range [0.0, 1.0]. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [setVolume](#setvolume)

## setVolumeWithRamp

```TypeScript
setVolumeWithRamp(volume: double, duration: int): void
```

Sets a volume ramp. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRenderer-setVolumeWithRamp(volume: double, duration: int): void--><!--Device-AudioRenderer-setVolumeWithRamp(volume: double, duration: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volume | double | Yes | Target volume, within the range [0.0, 1.0]. |
| duration | int | Yes | Time range during which the ramp applies, in ms. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

**Examples**

```TypeScript
let volume = 0.5;
let duration = 1000;

audioRenderer.setVolumeWithRamp(volume, duration);
console.info(`setVolumeWithRamp: ${volume}`);
```

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts this audio renderer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-start(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. If the operation fails, an error object with one of the following error codes is returned:<br>Error code 6800301: indicates abnormal status, focus preemption failure, and abnormal system processing. For details, see system logs. |

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

Starts this audio renderer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-start(): Promise<void>--><!--Device-AudioRenderer-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise object, which indicates that the renderer is started successfully. If the operation fails, an error object with one of the following error codes is returned: <br>Error code 6800301: indicates abnormal status, focus preemption failure, and abnormal system processing. For details, see system logs. |

**Examples**

See [start](#start)

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops this audio renderer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRenderer-stop(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

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

Stops this audio renderer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRenderer-stop(): Promise<void>--><!--Device-AudioRenderer-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [stop](#stop)

## write

```TypeScript
write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void
```

Writes the buffer. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** writeData

<!--Device-AudioRenderer-write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void--><!--Device-AudioRenderer-write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Data to be written to the buffer. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the number of bytes written; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

let bufferSize: number;
class Options {
  offset?: number;
  length?: number;
}
audioRenderer.getBufferSize().then((data: number)=> {
  console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
  bufferSize = data;
  console.info(`Buffer size: ${bufferSize}`);
  // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let path = context.cacheDir;
  // This is just an example. Replace the file with the PCM file to be played by the application.
  let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
  let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
  fs.stat(filePath).then(async (stat: fs.Stat) => {
    let buf = new ArrayBuffer(bufferSize);
    let len = stat.size % bufferSize == 0 ? Math.floor(stat.size / bufferSize) : Math.floor(stat.size / bufferSize + 1);
    for (let i = 0;i < len; i++) {
      let options: Options = {
        offset: i * bufferSize,
        length: bufferSize
      };
      await fs.read(file.fd, buf, options);
      await new Promise((resolve,reject)=>{
        audioRenderer.write(buf,(err: BusinessError, writeSize: number)=>{
          if(err){
            reject(err)
          }else{
            resolve(writeSize)
          }
        })
      })
    }
  });
  }).catch((err: BusinessError) => {
    console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

let bufferSize: number;
class Options {
  offset?: number;
  length?: number;
}
audioRenderer.getBufferSize().then((data: number) => {
  console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
  bufferSize = data;
  console.info(`BufferSize: ${bufferSize}`);
  // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let path = context.cacheDir;
  // This is just an example. Replace the file with the PCM file to be played by the application.
  let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
  let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
  fs.stat(filePath).then(async (stat: fs.Stat) => {
    let buf = new ArrayBuffer(bufferSize);
    let len = stat.size % bufferSize == 0 ? Math.floor(stat.size / bufferSize) : Math.floor(stat.size / bufferSize + 1);
    for (let i = 0;i < len; i++) {
      let options: Options = {
        offset: i * bufferSize,
        length: bufferSize
      };
      await fs.read(file.fd, buf, options);
      try{
        await audioRenderer.write(buf);
      } catch(err) {
        let error = err as BusinessError;
        console.error(`audioRenderer.write err: ${error}`);
      }
    }
  });
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}`);
});
```

## write

```TypeScript
write(buffer: ArrayBuffer): Promise<number>
```

Writes the buffer. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** writeData

<!--Device-AudioRenderer-write(buffer: ArrayBuffer): Promise<number>--><!--Device-AudioRenderer-write(buffer: ArrayBuffer): Promise<number>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Data to be written to the buffer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the number of written bytes. |

**Examples**

See [write](#write)

## state

```TypeScript
readonly state: AudioState
```

Audio renderer state.

**Type:** AudioState

**Since:** 23

<!--Device-AudioRenderer-readonly state: AudioState--><!--Device-AudioRenderer-readonly state: AudioState-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

