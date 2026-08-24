# AudioRenderer

音频渲染。在使用AudioRenderer的接口之前，需先通过 [audio.createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md) 获取AudioRenderer实例。

**起始版本：** 23

<!--Device-audio-interface AudioRenderer--><!--Device-audio-interface AudioRenderer-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
```

## drain

```TypeScript
drain(callback: AsyncCallback<void>): void
```

检查缓冲区是否已被耗尽。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-drain(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-drain(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当检查缓冲区是否已被耗尽成功，err为undefined，否则为错误对象。 |

**示例**

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

检查缓冲区是否已被耗尽。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-drain(): Promise<void>--><!--Device-AudioRenderer-drain(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**示例**

参见 [drain](#drain)

## flush

```TypeScript
flush(): Promise<void>
```

清空缓冲区（[AudioState](arkts-audio-audio-audiostate-e.md)为STATE_RUNNING、STATE_PAUSED、STATE_STOPPED状态下可用）。 使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-flush(): Promise<void>--><!--Device-AudioRenderer-flush(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Operation not permit at current state. Return by promise. |

**示例**

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

获取当前音效模式。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void--><!--Device-AudioRenderer-getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md)&gt; | 是 | 回调函数。当获取当前音效模式成功，err为undefined，data为获取到的当前音效模式；否则为错误对象。 |

**示例**

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

获取当前音效模式。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getAudioEffectMode(): Promise<AudioEffectMode>--><!--Device-AudioRenderer-getAudioEffectMode(): Promise<AudioEffectMode>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md)&gt; | Promise对象，返回当前音效模式。 |

**示例**

参见 [getAudioEffectMode](#getaudioeffectmode)

## getAudioStreamId

```TypeScript
getAudioStreamId(callback: AsyncCallback<long>): void
```

获取音频流id。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getAudioStreamId(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getAudioStreamId(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | 是 | 回调函数。当获取音频流id成功，err为undefined，data为获取到的音频流id；否则为错误对象。 |

**示例**

```TypeScript
audioCapturer.getAudioStreamId((err, streamId) => {
  if (err) {
    console.error(`Failed to get audio stream id. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting audio stream id. AudioStreamId: ${streamId}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioStreamId().then((streamId) => {
  console.info(`Succeeded in getting audio stream id. AudioStreamId: ${streamId}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get audio stream id. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
audioRenderer.getAudioStreamId((err, streamId) => {
  console.info(`Renderer GetStreamId: ${streamId}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioStreamId().then((streamId) => {
  console.info(`Renderer getAudioStreamId: ${streamId}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## getAudioStreamId

```TypeScript
getAudioStreamId(): Promise<long>
```

获取音频流id。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getAudioStreamId(): Promise<long>--><!--Device-AudioRenderer-getAudioStreamId(): Promise<long>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;long&gt; | Promise对象，返回音频流id。 |

**示例**

参见 [getAudioStreamId](#getaudiostreamid)

## getAudioStreamIdSync

```TypeScript
getAudioStreamIdSync(): long
```

获取音频流id。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-getAudioStreamIdSync(): long--><!--Device-AudioRenderer-getAudioStreamIdSync(): long-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 返回音频流id。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let streamId = audioCapturer.getAudioStreamIdSync();
  console.info(`Succeeded in getting audio stream id. AudioStreamId: ${streamId}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get audio stream id. Code: ${error.code}, message: ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let streamId = audioRenderer.getAudioStreamIdSync();
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

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getAudioTime(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getAudioTime(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | 是 | 回调函数。当获取时间戳成功，err为undefined，data为获取到的时间戳；否则为错误对象。 |

**示例**

```TypeScript
audioCapturer.getAudioTime((err, timestamp) => {
  if (err) {
    console.error(`Failed to get audio time. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting audio time. Timestamp: ${timestamp}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioTime().then((timestamp) => {
  console.info(`Succeeded in getting audio time. Timestamp: ${timestamp}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get audio time. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
audioRenderer.getAudioTime((err, timestamp) => {
  console.info(`Current timestamp: ${timestamp}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioTime().then((timestamp) => {
  console.info(`Current timestamp: ${timestamp}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## getAudioTime

```TypeScript
getAudioTime(): Promise<long>
```

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getAudioTime(): Promise<long>--><!--Device-AudioRenderer-getAudioTime(): Promise<long>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;long&gt; | Promise对象，返回时间戳。 |

**示例**

参见 [getAudioTime](#getaudiotime)

## getAudioTimestampInfo

```TypeScript
getAudioTimestampInfo(): Promise<AudioTimestampInfo>
```

获取输出音频流时间戳和位置信息，适配倍速接口。使用Promise异步回调。 获取输出音频流时间戳和位置信息，通常用于进行音画同步对齐。 注意，当实际播放位置（framePosition）为0时，时间戳（timestamp）是固定值，直到流真正开始播放时才会更新。当调用Flush接口时实际播放位置也会被重置。 当音频流路由（route）变化时，例如设备变化或者输出类型变化时，播放位置也会被重置，但此时时间戳仍会持续增长。推荐当实际播放位置和时间戳的变化稳定后再使用该接口获取的值。该接口适配倍速接口，例如当播放速度设置为2倍时，播放位 置的增长速度也会返回为正常的2倍。

**起始版本：** 23

<!--Device-AudioRenderer-getAudioTimestampInfo(): Promise<AudioTimestampInfo>--><!--Device-AudioRenderer-getAudioTimestampInfo(): Promise<AudioTimestampInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md)&gt; | Promise对象，返回音频流时间戳和当前数据帧位置信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Operation not permit at current state. |

**示例**

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

获取音频流时间戳和当前数据帧位置信息。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-getAudioTimestampInfoSync(): AudioTimestampInfo--><!--Device-AudioRenderer-getAudioTimestampInfoSync(): AudioTimestampInfo-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md) | 返回音频流时间戳和当前数据帧位置信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Operation not permit at current state. |

**示例**

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

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-getAudioTimeSync(): long--><!--Device-AudioRenderer-getAudioTimeSync(): long-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 返回时间戳。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let timestamp = audioCapturer.getAudioTimeSync();
  console.info(`Succeeded in getting audio time. Timestamp: ${timestamp}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get audio time. Code: ${error.code}, message: ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let timestamp = audioRenderer.getAudioTimeSync();
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

获取音频渲染器的最小缓冲区大小。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getBufferSize(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getBufferSize(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | 是 | 回调函数。当获取音频渲染器的最小缓冲区大小成功，err为undefined，data为获取到的最小缓冲区大小；否则为错误对象。<br>单位为字节。 |

**示例**

```TypeScript
audioCapturer.getBufferSize((err, bufferSize) => {
  if (err) {
    console.error(`Failed to get buffer size. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting buffer size, BufferSize: ${bufferSize}.`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getBufferSize().then((bufferSize) => {
  console.info(`Succeeded in getting buffer size, BufferSize: ${bufferSize}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get buffer size. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
let bufferSize;

audioRenderer.getBufferSize((err, data) => {
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

let bufferSize;

audioRenderer.getBufferSize().then((data) => {
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

获取音频渲染器的最小缓冲区大小。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getBufferSize(): Promise<long>--><!--Device-AudioRenderer-getBufferSize(): Promise<long>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;long&gt; | Promise对象，返回缓冲区大小。 |

**示例**

参见 [getBufferSize](#getbuffersize)

## getBufferSizeSync

```TypeScript
getBufferSizeSync(): long
```

获取音频渲染器的最小缓冲区大小。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-getBufferSizeSync(): long--><!--Device-AudioRenderer-getBufferSizeSync(): long-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 返回缓冲区大小，单位为字节。 |

**示例**

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

let bufferSize = 0;

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

获取音频流输出设备信息。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 是 | 回调函数。当获取音频流输出设备信息成功，err为undefined，data为获取到的音频流输出设备信息；否则为错误对象 。 |

**示例**

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

获取音频流输出设备信息。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>--><!--Device-AudioRenderer-getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Promise对象，返回音频流的输出设备信息。 |

**示例**

参见 [getCurrentOutputDevices](#getcurrentoutputdevices)

## getCurrentOutputDevicesSync

```TypeScript
getCurrentOutputDevicesSync(): AudioDeviceDescriptors
```

获取音频流输出设备信息。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-getCurrentOutputDevicesSync(): AudioDeviceDescriptors--><!--Device-AudioRenderer-getCurrentOutputDevicesSync(): AudioDeviceDescriptors-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) | 返回音频流的输出设备信息。 |

**示例**

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

获取当前音频路由的预估时延。

> **说明：**&gt;
> - 无线连接的音频设备，时延估算会存在误差，结果仅供参考。&gt;
> - 由于时延未计入实时缓冲区，建议仅在音频播放开始时获取，避免频繁调用，否则可能因路由切换而阻塞该接口调用。&gt;
> - 音频输出到硬件后的音画同步建议使用[getAudioTimestampInfo](#getaudiotimestampinfo)或
> [getAudioTimestampInfoSync](#getaudiotimestampinfosync)完成。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRenderer-getLatency(type: AudioLatencyType): int--><!--Device-AudioRenderer-getLatency(type: AudioLatencyType): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AudioLatencyType](arkts-audio-audio-audiolatencytype-e.md) | 是 | 获取的时延类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 返回音频时延，单位为毫秒。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Operation not permitted in release state. |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | System internal error, like audio service error. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let latency = audioRenderer.getLatency(audio.AudioLatencyType.LATENCY_TYPE_ALL);
  console.info(`Current audio latency: ${latency}ms`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get latency. Code: ${error.code}, message: ${error.message}`);
}
```

## getLoudnessGain

```TypeScript
getLoudnessGain(): double
```

获取播放响度。

**起始版本：** 23

<!--Device-AudioRenderer-getLoudnessGain(): double--><!--Device-AudioRenderer-getLoudnessGain(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 返回播放的响度值，单位为分贝。 |

**示例**

```TypeScript
let loudnessGain = audioRenderer.getLoudnessGain();
```

## getMaxStreamVolume

```TypeScript
getMaxStreamVolume(callback: AsyncCallback<double>): void
```

获取音频流的最大音量。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getMaxStreamVolume(callback: AsyncCallback<double>): void--><!--Device-AudioRenderer-getMaxStreamVolume(callback: AsyncCallback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | 是 | 回调函数。当获取音频流的最大音量成功，err为undefined，data为获取到的应用基于音频流的最大音量；否则为错误对象。<br>音量范围为 [0.0, 1.0]。 |

**示例**

```TypeScript
audioRenderer.getMaxStreamVolume((err, maxVolume) => {
  if (err) {
    console.error(`getMaxStreamVolume Fail: ${err}`);
  } else {
    console.info(`getMaxStreamVolume Success! ${maxVolume}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMaxStreamVolume().then((value) => {
  console.info(`Get max stream volume Success! ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Get max stream volume Fail: ${err}`);
});
```

## getMaxStreamVolume

```TypeScript
getMaxStreamVolume(): Promise<double>
```

获取音频流的最大音量。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getMaxStreamVolume(): Promise<double>--><!--Device-AudioRenderer-getMaxStreamVolume(): Promise<double>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;double&gt; | Promise对象，返回音频流最大音量。 |

**示例**

参见 [getMaxStreamVolume](#getmaxstreamvolume)

## getMaxStreamVolumeSync

```TypeScript
getMaxStreamVolumeSync(): double
```

获取音频流的最大音量。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-getMaxStreamVolumeSync(): double--><!--Device-AudioRenderer-getMaxStreamVolumeSync(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 返回音频流最大音量，音量范围为[0.0, 1.0]。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value = audioRenderer.getMaxStreamVolumeSync();
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

获取音频流的最小音量。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getMinStreamVolume(callback: AsyncCallback<double>): void--><!--Device-AudioRenderer-getMinStreamVolume(callback: AsyncCallback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | 是 | 回调函数。当获取音频流的最小音量成功，err为undefined，data为获取到的应用基于音频流的最小音量；否则为错误对象。<br>音量范围为 [0.0, 1.0]。 |

**示例**

```TypeScript
audioRenderer.getMinStreamVolume((err, minVolume) => {
  if (err) {
    console.error(`getMinStreamVolume error: ${err}`);
  } else {
    console.info(`getMinStreamVolume Success! ${minVolume}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMinStreamVolume().then((value) => {
  console.info(`Get min stream volume Success! ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Get min stream volume Fail: ${err}`);
});
```

## getMinStreamVolume

```TypeScript
getMinStreamVolume(): Promise<double>
```

获取音频流的最小音量。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getMinStreamVolume(): Promise<double>--><!--Device-AudioRenderer-getMinStreamVolume(): Promise<double>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;double&gt; | Promise对象，返回音频流最小音量。 |

**示例**

参见 [getMinStreamVolume](#getminstreamvolume)

## getMinStreamVolumeSync

```TypeScript
getMinStreamVolumeSync(): double
```

获取音频流的最小音量。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-getMinStreamVolumeSync(): double--><!--Device-AudioRenderer-getMinStreamVolumeSync(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 返回音频流最小音量，音量范围为[0.0, 1.0]。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value = audioRenderer.getMinStreamVolumeSync();
  console.info(`Get min stream volume Success! ${value}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get min stream volume Fail: ${error}`);
}
```

## getNoiseReductionMode

```TypeScript
getNoiseReductionMode(): NoiseReductionMode
```

Gets the noise reduction mode for current audio renderer. The mode will only consider the default and setted status, audio output device and stream concurrency will not be considered.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRenderer-getNoiseReductionMode(): NoiseReductionMode--><!--Device-AudioRenderer-getNoiseReductionMode(): NoiseReductionMode-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md) | The noise reduction mode for current audio renderer, the default value is { |

**示例**

```TypeScript
let noiseReductionMode: audio.NoiseReductionMode = audioCapturer.getNoiseReductionMode();
console.info(`getNoiseReductionMode success: ${noiseReductionMode}`);
```

## getRendererInfo

```TypeScript
getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void
```

获取当前创建的音频渲染器信息。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void--><!--Device-AudioRenderer-getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md)&gt; | 是 | 回调函数。当获取音频渲染器的信息成功，err为undefined，data为获取到的音频渲染器的信息；否则为错误对象。 |

**示例**

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

获取当前创建的音频渲染器信息。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getRendererInfo(): Promise<AudioRendererInfo>--><!--Device-AudioRenderer-getRendererInfo(): Promise<AudioRendererInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md)&gt; | Promise对象，返回音频渲染器信息。 |

**示例**

参见 [getRendererInfo](#getrendererinfo)

## getRendererInfoSync

```TypeScript
getRendererInfoSync(): AudioRendererInfo
```

获取当前创建的音频渲染器信息。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-getRendererInfoSync(): AudioRendererInfo--><!--Device-AudioRenderer-getRendererInfoSync(): AudioRendererInfo-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | 返回音频渲染器信息。 |

**示例**

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

获取音频渲染速率。使用callback异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 11开始废弃，建议使用[getSpeed](#getspeed)替代。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [getSpeed](#getspeed)

<!--Device-AudioRenderer-getRenderRate(callback: AsyncCallback<AudioRendererRate>): void--><!--Device-AudioRenderer-getRenderRate(callback: AsyncCallback<AudioRendererRate>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md)&gt; | 是 | 回调函数。当获取当前渲染速率成功，err为undefined，data为获取到的当前渲染速率；否则为错误对象。 |

**示例**

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

获取音频渲染速率。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 11开始废弃，建议使用[getSpeed](#getspeed)替代。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [getSpeed](#getspeed)

<!--Device-AudioRenderer-getRenderRate(): Promise<AudioRendererRate>--><!--Device-AudioRenderer-getRenderRate(): Promise<AudioRendererRate>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md)&gt; | Promise对象，返回渲染速率。 |

**示例**

参见 [getRenderRate](#getrenderrate)

## getRenderRateSync

```TypeScript
getRenderRateSync(): AudioRendererRate
```

获取音频渲染速率。同步返回结果。

> **说明：**
> 
> 从API version 10开始支持，从API version 11开始废弃，建议使用[getSpeed](#getspeed)替代。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getSpeed](#getspeed)

<!--Device-AudioRenderer-getRenderRateSync(): AudioRendererRate--><!--Device-AudioRenderer-getRenderRateSync(): AudioRendererRate-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) | 返回渲染速率。 |

**示例**

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

获取静音并发播放模式。

**起始版本：** 23

<!--Device-AudioRenderer-getSilentModeAndMixWithOthers(): boolean--><!--Device-AudioRenderer-getSilentModeAndMixWithOthers(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 静音并发播放模式状态。返回true表示打开，返回false表示关闭。 |

**示例**

```TypeScript
let on = audioRenderer.getSilentModeAndMixWithOthers();
```

## getSpeed

```TypeScript
getSpeed(): double
```

获取播放倍速。

**起始版本：** 23

<!--Device-AudioRenderer-getSpeed(): double--><!--Device-AudioRenderer-getSpeed(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 返回播放的倍速值，倍速范围为[0.25, 4.0]。 |

**示例**

```TypeScript
let speed = audioRenderer.getSpeed();
```

## getStreamInfo

```TypeScript
getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void
```

获取音频流信息。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void--><!--Device-AudioRenderer-getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)&gt; | 是 | 回调函数。当获取音频流信息成功，err为undefined，data为获取到的音频流信息；否则为错误对象。 |

**示例**

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

获取音频流信息。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getStreamInfo(): Promise<AudioStreamInfo>--><!--Device-AudioRenderer-getStreamInfo(): Promise<AudioStreamInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)&gt; | Promise对象，返回音频流信息。 |

**示例**

参见 [getStreamInfo](#getstreaminfo)

## getStreamInfoSync

```TypeScript
getStreamInfoSync(): AudioStreamInfo
```

获取音频流信息。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-getStreamInfoSync(): AudioStreamInfo--><!--Device-AudioRenderer-getStreamInfoSync(): AudioStreamInfo-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | 返回音频流信息。 |

**示例**

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

Gets all the supported noise reduction modes for current device platform. Currently the noise reduction effect is only supported when using [STREAM_USAGE_VOICE_MESSAGE](arkts-audio-audio-streamusage-e.md#stream_usage_voice_message), other supported usage may be extened later. The supported modes will only consider the audio format and device platform, audio output device and stream concurrency will not be considered.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRenderer-getSupportedNoiseReductionModes(): Array<NoiseReductionMode>--><!--Device-AudioRenderer-getSupportedNoiseReductionModes(): Array<NoiseReductionMode>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md)&gt; | The supported noise reduction mode array, at least { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | Audio server process died. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let supportedModes: Array<audio.NoiseReductionMode> = audioCapturer.getSupportedNoiseReductionModes();
  console.info(`getSupportedNoiseReductionModes success: ${supportedModes}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`getSupportedNoiseReductionModes failed. Code: ${error.code}, message: ${error.message}`);
}
```

## getUnderflowCount

```TypeScript
getUnderflowCount(callback: AsyncCallback<long>): void
```

获取当前播放音频流的欠载音频帧数量。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getUnderflowCount(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getUnderflowCount(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | 是 | 回调函数。当获取当前播放音频流的欠载音频帧数量成功，err为undefined，data为获取到的当前播放音频流的欠载音频帧数量；否则为错误对象。 |

**示例**

```TypeScript
audioRenderer.getUnderflowCount((err, underflowCount) => {
  if (err) {
    console.error(`getUnderflowCount Fail: ${err}`);
  } else {
    console.info(`getUnderflowCount Success! ${underflowCount}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getUnderflowCount().then((value) => {
  console.info(`Get underflow count Success! ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Get underflow count Fail: ${err}`);
});
```

## getUnderflowCount

```TypeScript
getUnderflowCount(): Promise<long>
```

获取当前播放音频流的欠载音频帧数量。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-getUnderflowCount(): Promise<long>--><!--Device-AudioRenderer-getUnderflowCount(): Promise<long>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;long&gt; | Promise对象，返回音频流的欠载音频帧数量。 |

**示例**

参见 [getUnderflowCount](#getunderflowcount)

## getUnderflowCountSync

```TypeScript
getUnderflowCountSync(): long
```

获取当前播放音频流的欠载音频帧数量，同步返回数据。

**起始版本：** 23

<!--Device-AudioRenderer-getUnderflowCountSync(): long--><!--Device-AudioRenderer-getUnderflowCountSync(): long-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 返回音频流的欠载音频帧数量。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value = audioRenderer.getUnderflowCountSync();
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

获取音频流的音量。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-getVolume(): double--><!--Device-AudioRenderer-getVolume(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 返回音量大小，音量值范围为[0.0, 1.0]。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the volume, volume: ${value}.`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in obtaining the volume, volume: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the volume. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value = audioRenderer.getVolume();
  console.info(`Indicate that the volume is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume, error ${error}.`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, volume) => {
  if (err) {
    console.error(`Failed to obtain the volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the volume, volume: ${volume}.`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA).then((volume) => {
  console.info(`Succeeded in obtaining the volume, volume: ${volume}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the volume. Code: ${err.code}, message: ${err.message}`);
});
```

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void
```

取消监听音频中断事件。使用callback异步回调。

**起始版本：** 18

<!--Device-AudioRenderer-off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | 是 | 事件回调类型，支持的事件为'audioInterrupt'，当取消监听音频中断事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | 否 | 回调函数，返回中断事件信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## off('markReach')

```TypeScript
off(type: 'markReach', callback?: Callback<long>): void
```

取消监听标记到达事件。使用callback异步回调。

**起始版本：** 8

<!--Device-AudioRenderer-off(type: 'markReach', callback?: Callback<long>): void--><!--Device-AudioRenderer-off(type: 'markReach', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'markReach' | 是 | 事件回调类型，支持的事件为'markReach'，当取消监听标记到达事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 | 回调函数，返回frame参数的值。 |

## off('outputDeviceChange')

```TypeScript
off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void
```

取消监听音频输出设备变化事件。使用callback异步回调。

**起始版本：** 10

<!--Device-AudioRenderer-off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'outputDeviceChange' | 是 | 事件回调类型，支持的事件为'outputDeviceChange'，当取消监听音频输出设备变化事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 否 | 回调函数，返回当前音频流的输出设备描述信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## off('outputDeviceChangeWithInfo')

```TypeScript
off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void
```

取消监听音频流输出设备变化及原因事件。使用callback异步回调。

**起始版本：** 11

<!--Device-AudioRenderer-off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'outputDeviceChangeWithInfo' | 是 | 事件回调类型，支持的事件为'outputDeviceChangeWithInfo'，当取消监听音频流输出设备变化及原因事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | 否 | 回调函数，返回当前音频流的输出设备描述信息及变化原因。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## off('periodReach')

```TypeScript
off(type: 'periodReach', callback?: Callback<long>): void
```

取消监听标记到达事件。使用callback异步回调。

**起始版本：** 8

<!--Device-AudioRenderer-off(type: 'periodReach', callback?: Callback<long>): void--><!--Device-AudioRenderer-off(type: 'periodReach', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'periodReach' | 是 | 事件回调类型，支持的事件为'periodReach'，当取消监听标记到达事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 | 回调函数，返回frame参数的值。 |

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: Callback<AudioState>): void
```

取消监听状态变化事件。使用callback异步回调。

**起始版本：** 18

<!--Device-AudioRenderer-off(type: 'stateChange', callback?: Callback<AudioState>): void--><!--Device-AudioRenderer-off(type: 'stateChange', callback?: Callback<AudioState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'stateChange' | 是 | 事件回调类型，支持的事件为'stateChange'，当取消监听状态变化事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | 否 | 回调函数，返回当前音频的状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## off('writeData')

```TypeScript
off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void
```

取消监听音频数据写入回调事件。使用callback异步回调。

**起始版本：** 11

<!--Device-AudioRenderer-off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'writeData' | 是 | 事件回调类型，支持的事件为'writeData'，当取消监听音频数据写入回调事件时，触发该事件。 |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | 否 | 回调函数，入参代表应用接收待写入的数据缓冲区。<br>API version 11 不支持返回回调结果，从 API version 1 2 开始支持返回回调结果[AudioDataCallbackResult](arkts-audio-audio-audiodatacallbackresult-e.md)。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## offAudioInterrupt

```TypeScript
offAudioInterrupt(callback?: Callback<InterruptEvent>): void
```

Unsubscribes audio interrupt events.

**起始版本：** 23

<!--Device-AudioRenderer-offAudioInterrupt(callback?: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-offAudioInterrupt(callback?: Callback<InterruptEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | 否 | 回调函数，用于监听中断回调。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
audioCapturer.offAudioInterrupt();
```

```TypeScript
// 取消该事件的所有监听。
audioRenderer.offAudioInterrupt();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let isPlaying: boolean; // 标识符，表示是否正在渲染。
let isDucked: boolean; // 标识符，表示是否被降低音量。

let audioInterruptCallback = (interruptEvent: audio.InterruptEvent) => {
  // 在发生音频打断事件时，audioRenderer收到interruptEvent回调，此处根据其内容做相应处理。
  // 1. 可选：读取interruptEvent.forceType的类型，判断系统是否已强制执行相应操作。
  // 注：默认焦点策略下，INTERRUPT_HINT_RESUME为INTERRUPT_SHARE类型，其余hintType均为INTERRUPT_FORCE类型。因此对forceType可不做判断。
  // 2. 必选：读取interruptEvent.hintType的类型，做出相应的处理。
  if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
    // 音频焦点事件已由系统强制执行，应用需更新自身状态及显示内容等。
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
        // 音频流已被暂停，临时失去焦点，待可重获焦点时会收到resume对应的interruptEvent。
        console.info('Force paused. Update playing status and stop writing');
        isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_STOP:
        // 音频流已被停止，永久失去焦点，若想恢复渲染，需用户主动触发。
        console.info('Force stopped. Update playing status and stop writing');
        isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_DUCK:
        // 音频流已被降低音量渲染。
        console.info('Force ducked. Update volume status');
        isDucked = true; // 简化处理，代表应用更新音量状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
        // 音频流已被恢复正常音量渲染。
        console.info('Force ducked. Update volume status');
        isDucked = false; // 简化处理，代表应用更新音量状态的若干操作。
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }  
  } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
    // 音频焦点事件需由应用进行操作，应用可以自主选择如何处理该事件，建议应用遵从InterruptHint提示处理。
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_RESUME:
        // 建议应用继续渲染（说明音频流此前被强制暂停，临时失去焦点，现在可以恢复渲染）。
        // 由于INTERRUPT_HINT_RESUME操作需要应用主动执行，系统无法强制，故INTERRUPT_HINT_RESUME事件一定为INTERRUPT_SHARE类型。
        console.info('Resume force paused renderer or ignore');
        // 若选择继续渲染，需在此处主动执行开始渲染的若干操作。
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  }
};

audioRenderer.onAudioInterrupt(audioInterruptCallback);

audioRenderer.offAudioInterrupt(audioInterruptCallback);
```

## offMarkReach

```TypeScript
offMarkReach(callback?: Callback<long>): void
```

取消监听标记到达事件。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-offMarkReach(callback?: Callback<long>): void--><!--Device-AudioRenderer-offMarkReach(callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 | 回调函数，返回frame参数的值。 |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioCapturer.offMarkReach();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let markReachCallback = (position: long) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
};

audioCapturer.onMarkReach(1000, markReachCallback);

audioCapturer.offMarkReach(markReachCallback);
```

```TypeScript
// 取消该事件的所有监听。
audioRenderer.offMarkReach();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let markReachCallback = (position: long) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
};

audioRenderer.onMarkReach(1000, markReachCallback);

audioRenderer.offMarkReach(markReachCallback);
```

## offOutputDeviceChange

```TypeScript
offOutputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void
```

取消监听音频输出设备变化事件。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-offOutputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-offOutputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 否 | 回调函数，返回当前音频流的输出设备描述信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioRenderer.offOutputDeviceChange();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let outputDeviceChangeCallback = (deviceInfo: audio.AudioDeviceDescriptors) => {
  console.info(`DeviceInfo id: ${deviceInfo[0].id}`);
  console.info(`DeviceInfo name: ${deviceInfo[0].name}`);
  console.info(`DeviceInfo address: ${deviceInfo[0].address}`);
};

audioRenderer.onOutputDeviceChange(outputDeviceChangeCallback);

audioRenderer.offOutputDeviceChange(outputDeviceChangeCallback);
```

## offOutputDeviceChangeWithInfo

```TypeScript
offOutputDeviceChangeWithInfo(callback?: Callback<AudioStreamDeviceChangeInfo>): void
```

取消监听音频流输出设备变化及原因事件。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-offOutputDeviceChangeWithInfo(callback?: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-offOutputDeviceChangeWithInfo(callback?: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | 否 | 回调函数，返回当前音频流的输出设备描述信息及变化原因。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioRenderer.offOutputDeviceChangeWithInfo();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let outputDeviceChangeWithInfoCallback = (deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
  console.info(`DeviceInfo id: ${deviceChangeInfo.devices[0].id}`);
  console.info(`DeviceInfo name: ${deviceChangeInfo.devices[0].name}`);
  console.info(`DeviceInfo address: ${deviceChangeInfo.devices[0].address}`);
  console.info(`Device change reason: ${deviceChangeInfo.changeReason}`);
};

audioRenderer.onOutputDeviceChangeWithInfo(outputDeviceChangeWithInfoCallback);

audioRenderer.offOutputDeviceChangeWithInfo(outputDeviceChangeWithInfoCallback);
```

## offPeriodReach

```TypeScript
offPeriodReach(callback?: Callback<long>): void
```

取消监听标记到达事件。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-offPeriodReach(callback?: Callback<long>): void--><!--Device-AudioRenderer-offPeriodReach(callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 | 事件触发时调用的回调函数。 |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioCapturer.offPeriodReach();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let periodReachCallback = (position: long) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
};

audioCapturer.onPeriodReach(1000, periodReachCallback);

audioCapturer.offPeriodReach(periodReachCallback);
```

```TypeScript
// 取消该事件的所有监听。
audioRenderer.offPeriodReach();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let periodReachCallback = (position: long) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
};

audioRenderer.onPeriodReach(1000, periodReachCallback);

audioRenderer.offPeriodReach(periodReachCallback);
```

## offStateChange

```TypeScript
offStateChange(callback?: Callback<AudioState>): void
```

取消订阅音频状态变更事件回调。

**起始版本：** 23

<!--Device-AudioRenderer-offStateChange(callback?: Callback<AudioState>): void--><!--Device-AudioRenderer-offStateChange(callback?: Callback<AudioState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | 否 | 回调函数，返回当前音频的状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioCapturer.offStateChange();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let stateChangeCallback = (state: audio.AudioState) => {
  if (state == 1) {
    console.info('audio capturer state is: STATE_PREPARED');
  }
  if (state == 2) {
    console.info('audio capturer state is: STATE_RUNNING');
  }
};

audioCapturer.onStateChange(stateChangeCallback);

audioCapturer.offStateChange(stateChangeCallback);
```

```TypeScript
// 取消该事件的所有监听。
audioRenderer.offStateChange();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let stateChangeCallback = (state: audio.AudioState) => {
  if (state == 1) {
    console.info('audio renderer state is: STATE_PREPARED');
  }
  if (state == 2) {
    console.info('audio renderer state is: STATE_RUNNING');
  }
};

audioRenderer.onStateChange(stateChangeCallback);

audioRenderer.offStateChange(stateChangeCallback);
```

## offWriteData

```TypeScript
offWriteData(callback?: AudioRendererWriteDataCallback): void
```

取消监听音频数据写入回调事件。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-offWriteData(callback?: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-offWriteData(callback?: AudioRendererWriteDataCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | 否 | 回调函数，入参代表应用接收待写入的数据缓冲区。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioRenderer.offWriteData();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let writeDataCallback = (data: ArrayBuffer) => {
    console.info(`write data: ${data}`);
};

audioRenderer.onWriteData(writeDataCallback);

audioRenderer.offWriteData(writeDataCallback);
```

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void
```

监听音频中断事件（当音频焦点发生变化时触发）。使用callback异步回调。 AudioRenderer对象在start事件时获取焦点，在pause、stop等事件时释放焦点，无需开发者主动申请。 调用此方法后，如果AudioRenderer对象获取焦点失败或发生中断事件（如被其他音频打断等），会收到 [InterruptEvent](arkts-audio-audio-interruptevent-i.md)。建议应用根据 InterruptEvent的信息进行进一步处理。更多信息请参阅音频焦点介绍文档。

**起始版本：** 9

<!--Device-AudioRenderer-on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | 是 | 事件回调类型，支持的事件为'audioInterrupt'，当音频焦点状态发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | 是 | 回调函数，返回中断事件信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## on('markReach')

```TypeScript
on(type: 'markReach', frame: long, callback: Callback<long>): void
```

监听标记到达事件（当渲染的帧数到达frame参数的值时触发，仅调用一次）。使用callback异步回调。 如果将frame设置为100，当渲染帧数到达第100帧时，系统将上报信息。

**起始版本：** 8

<!--Device-AudioRenderer-on(type: 'markReach', frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-on(type: 'markReach', frame: long, callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'markReach' | 是 | 事件回调类型，支持的事件为'markReach'，当渲染的帧数到达frame参数的值时，触发该事件。 |
| frame | long | 是 | 触发事件的帧数。该值必须大于0。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 是 | 回调函数，返回frame参数的值。 |

## on('outputDeviceChange')

```TypeScript
on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void
```

监听音频输出设备变化事件（当音频输出设备发生变化时触发）。使用callback异步回调。

**起始版本：** 10

<!--Device-AudioRenderer-on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'outputDeviceChange' | 是 | 事件回调类型，支持的事件为'outputDeviceChange'，当音频输出设备发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 是 | 回调函数，返回当前音频流的输出设备描述信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## on('outputDeviceChangeWithInfo')

```TypeScript
on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void
```

监听音频流输出设备变化及原因事件（当音频输出设备发生变化时触发）。使用callback异步回调。

**起始版本：** 11

<!--Device-AudioRenderer-on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'outputDeviceChangeWithInfo' | 是 | 事件回调类型，支持的事件为'outputDeviceChangeWithInfo'，当音频输出设备发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | 是 | 回调函数，返回当前音频流的输出设备描述信息及变化原因。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## on('periodReach')

```TypeScript
on(type: 'periodReach', frame: long, callback: Callback<long>): void
```

监听标记到达事件（每当渲染的帧数达到frame参数的值时触发，即按周期上报信息）。使用callback异步回调。 如果将frame设置为10，每渲染10帧数据均会上报信息（例如：第10帧、第20帧、第30帧......）。

**起始版本：** 8

<!--Device-AudioRenderer-on(type: 'periodReach', frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-on(type: 'periodReach', frame: long, callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'periodReach' | 是 | 事件回调类型，支持的事件为'periodReach'，当渲染的帧数达到frame参数的值时，触发该事件。 |
| frame | long | 是 | 触发事件的帧数。该值必须大于 0。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 是 | 回调函数，返回frame参数的值。 |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: Callback<AudioState>): void
```

监听状态变化事件（当AudioRenderer的状态发生变化时触发）。使用callback异步回调。

**起始版本：** 8

<!--Device-AudioRenderer-on(type: 'stateChange', callback: Callback<AudioState>): void--><!--Device-AudioRenderer-on(type: 'stateChange', callback: Callback<AudioState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'stateChange' | 是 | 事件回调类型，支持的事件为'stateChange'，当AudioRenderer的状态发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | 是 | 回调函数，返回当前音频的状态。 |

## on('writeData')

```TypeScript
on(type: 'writeData', callback: AudioRendererWriteDataCallback): void
```

监听音频数据写入回调事件（当需要写入音频数据时触发）。使用callback异步回调。

> **说明：**&gt;
> - 回调函数仅用来写入音频数据，请勿在回调函数中调用AudioRenderer相关接口。&gt;
> - 为避免音频播放启动和停止时数据不连续可能出现的杂音，系统通常会在启动和停止时对音频数据做20ms以内的淡入淡出处理。

**起始版本：** 11

<!--Device-AudioRenderer-on(type: 'writeData', callback: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-on(type: 'writeData', callback: AudioRendererWriteDataCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'writeData' | 是 | 事件回调类型，支持的事件为'writeData'，当需要写入音频数据时，触发该事件。 |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | 是 | 回调函数，入参代表应用接收待写入的数据缓冲区。<br>API version 11 不支持返回回调结果，从 API version 1 2 开始支持返回回调结果[AudioDataCallbackResult](arkts-audio-audio-audiodatacallbackresult-e.md)。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## onAudioInterrupt

```TypeScript
onAudioInterrupt(callback: Callback<InterruptEvent>): void
```

监听音频中断事件。此方法通过回调获取中断事件。当音频播放被中断时，会触发中断事件。

**起始版本：** 23

<!--Device-AudioRenderer-onAudioInterrupt(callback: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-onAudioInterrupt(callback: Callback<InterruptEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | 是 | 回调函数，用于监听中断回调。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
let isCapturing: boolean = false;

audioCapturer.onAudioInterrupt((interruptEvent: audio.InterruptEvent) => {
  if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
        isCapturing = false;
        break;
      case audio.InterruptHint.INTERRUPT_HINT_STOP:
        isCapturing = false;
        break;
      default:
        break;
    }
  } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_RESUME:
        isCapturing = true;
        break;
      default:
        break;
    }
  }
});
```

```TypeScript
import { audio } from '@kit.AudioKit';

let isPlaying: boolean = false; // 标识符，表示是否正在渲染。
let isDucked: boolean = false; // 标识符，表示是否被降低音量。

audioRenderer.onAudioInterrupt((interruptEvent: audio.InterruptEvent) => {
  // 在发生音频打断事件时，audioRenderer收到interruptEvent回调，此处根据其内容做相应处理。
  // 1. 可选：读取interruptEvent.forceType的类型，判断系统是否已强制执行相应操作。
  // 注意：默认焦点策略下，INTERRUPT_HINT_RESUME为INTERRUPT_SHARE类型，其余hintType均为INTERRUPT_FORCE类型。因此对forceType可不做判断。
  // 2. 必选：读取interruptEvent.hintType的类型，做出相应的处理。
  if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
    // 音频焦点事件已由系统强制执行，应用需更新自身状态及显示内容等。
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
        // 音频流已被暂停，临时失去焦点，待可重获焦点时会收到resume对应的interruptEvent。
        console.info('Force paused. Update playing status and stop writing');
        isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_STOP:
        // 音频流已被停止，永久失去焦点，若想恢复渲染，需用户主动触发。
        console.info('Force stopped. Update playing status and stop writing');
        isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_DUCK:
        // 音频流已被降低音量渲染。
        console.info('Force ducked. Update volume status');
        isDucked = true; // 简化处理，代表应用更新音量状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
        // 音频流已被恢复正常音量渲染。
        console.info('Force unducked. Update volume status');
        isDucked = false; // 简化处理，代表应用更新音量状态的若干操作。
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
    // 音频焦点事件需由应用进行操作，应用可以自主选择如何处理该事件，建议应用遵从InterruptHint提示处理。
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_RESUME:
        // 建议应用继续渲染（说明音频流此前被强制暂停，临时失去焦点，现在可以恢复渲染）。
        // 由于INTERRUPT_HINT_RESUME操作需要应用主动执行，系统无法强制，故INTERRUPT_HINT_RESUME事件一定为INTERRUPT_SHARE类型。
        console.info('Resume force paused renderer or ignore');
        // 若选择继续渲染，需在此处主动执行开始渲染的若干操作。
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  }
});
```

## onMarkReach

```TypeScript
onMarkReach(frame: long, callback: Callback<long>): void
```

订阅达到标记的事件。当渲染的帧数达到 frame 参数的值时， 会调用回调函数。

**起始版本：** 23

<!--Device-AudioRenderer-onMarkReach(frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-onMarkReach(frame: long, callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| frame | long | 是 | 触发事件帧数，必须大于0。 <br>取值应&gt;0。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 是 | 事件触发时调用的回调函数。 |

**示例**

```TypeScript
audioCapturer.onMarkReach(1000, (position: long) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
});
```

```TypeScript
audioRenderer.onMarkReach(1000, (position: long) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
});
```

## onOutputDeviceChange

```TypeScript
onOutputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void
```

监听音频输出设备变化事件（当音频输出设备发生变化时触发）。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-onOutputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-onOutputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 是 | 回调函数，返回当前音频流的输出设备描述信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
audioRenderer.onOutputDeviceChange((deviceInfo: audio.AudioDeviceDescriptors) => {
  console.info(`DeviceInfo id: ${deviceInfo[0].id}`);
  console.info(`DeviceInfo name: ${deviceInfo[0].name}`);
  console.info(`DeviceInfo address: ${deviceInfo[0].address}`);
});
```

## onOutputDeviceChangeWithInfo

```TypeScript
onOutputDeviceChangeWithInfo(callback: Callback<AudioStreamDeviceChangeInfo>): void
```

监听音频流输出设备变化及原因事件（当音频输出设备发生变化时触发）。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-onOutputDeviceChangeWithInfo(callback: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-onOutputDeviceChangeWithInfo(callback: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | 是 | 回调函数，返回当前音频流的输出设备描述信息及变化原因。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
audioRenderer.onOutputDeviceChangeWithInfo((deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
  console.info(`DeviceInfo id: ${deviceChangeInfo.devices[0].id}`);
  console.info(`DeviceInfo name: ${deviceChangeInfo.devices[0].name}`);
  console.info(`DeviceInfo address: ${deviceChangeInfo.devices[0].address}`);
  console.info(`Device change reason: ${deviceChangeInfo.changeReason}`);
});
```

## onPeriodReach

```TypeScript
onPeriodReach(frame: long, callback: Callback<long>): void
```

监听标记到达事件（每当渲染的帧数达到frame参数的值时触发，即按周期上报信息）。使用callback异步回调。 如果将frame设置为10，每渲染10帧数据均会上报信息（例如：第10帧、第20帧、第30帧......）。

**起始版本：** 23

<!--Device-AudioRenderer-onPeriodReach(frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-onPeriodReach(frame: long, callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| frame | long | 是 | 触发事件的帧数。该值必须大于 0。 <br>取值应&gt;0。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 是 | 回调函数，返回frame参数的值。 |

**示例**

```TypeScript
audioCapturer.onPeriodReach(1000, (position: long) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
});
```

```TypeScript
audioRenderer.onPeriodReach(1000, (position: long) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
});
```

## onStateChange

```TypeScript
onStateChange(callback: Callback<AudioState>): void
```

监听状态变化事件（当AudioRenderer的状态发生变化时触发）。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-onStateChange(callback: Callback<AudioState>): void--><!--Device-AudioRenderer-onStateChange(callback: Callback<AudioState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | 是 | 回调函数，返回当前音频的状态。 |

**示例**

```TypeScript
audioCapturer.onStateChange((state: audio.AudioState) => {
  if (state == 1) {
    console.info('audio capturer state is: STATE_PREPARED');
  }
  if (state == 2) {
    console.info('audio capturer state is: STATE_RUNNING');
  }
});
```

```TypeScript
audioRenderer.onStateChange((state: audio.AudioState) => {
  if (state == 1) {
    console.info('audio renderer state is: STATE_PREPARED');
  }
  if (state == 2) {
    console.info('audio renderer state is: STATE_RUNNING');
  }
});
```

## onWriteData

```TypeScript
onWriteData(callback: AudioRendererWriteDataCallback): void
```

订阅音频数据回调。当音频缓冲区可用以写入更多数据时，将触发该事件。

**起始版本：** 23

<!--Device-AudioRenderer-onWriteData(callback: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-onWriteData(callback: AudioRendererWriteDataCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | 是 | Audio renderer write data callback. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

let bufferSize: long = 0;
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.cacheDir;
// 确保该沙箱路径下存在该资源。
let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
let file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
let writeDataCallback = (buffer: ArrayBuffer) => {
  let options: ReadOptions = {
    offset: bufferSize,
    length: buffer.byteLength
  };

  try {
    fileIo.readSync(file.fd, buffer, options);
    bufferSize += buffer.byteLength;
    // API version 11不支持返回回调结果，从 API version 12开始支持返回回调结果。
    return audio.AudioDataCallbackResult.VALID;
  } catch (error) {
    console.error('Error reading file:', error);
    // API version 11不支持返回回调结果，从 API version 12开始支持返回回调结果。
    return audio.AudioDataCallbackResult.INVALID;
  }
};

audioRenderer.onWriteData(writeDataCallback);
audioRenderer.start().then(() => {
  console.info('Renderer started');
}).catch(async (err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

暂停音频渲染。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-pause(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-pause(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当暂停渲染成功，err为undefined，否则为错误对象。 |

**示例**

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

暂停音频渲染。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-pause(): Promise<void>--><!--Device-AudioRenderer-pause(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**示例**

参见 [pause](#pause)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放音频渲染器。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-release(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当释放音频渲染器成功，err为undefined，否则为错误对象。 |

**示例**

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

释放音频渲染器。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-release(): Promise<void>--><!--Device-AudioRenderer-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**示例**

参见 [release](#release)

## setAudioEffectMode

```TypeScript
setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void
```

设置当前音效模式。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md) | 是 | 音效模式。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当设置当前音效模式成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. Return by callback. |

**示例**

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

设置当前音效模式。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode): Promise<void>--><!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md) | 是 | 音效模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. Return by promise. |

**示例**

参见 [setAudioEffectMode](#setaudioeffectmode)

## setChannelBlendMode

```TypeScript
setChannelBlendMode(mode: ChannelBlendMode): void
```

设置单双声道混合模式。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-setChannelBlendMode(mode: ChannelBlendMode): void--><!--Device-AudioRenderer-setChannelBlendMode(mode: ChannelBlendMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [ChannelBlendMode](arkts-audio-audio-channelblendmode-e.md) | 是 | 声道混合模式类型。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Operation not permit at current state. |

**示例**

```TypeScript
let mode = audio.ChannelBlendMode.MODE_DEFAULT;

audioRenderer.setChannelBlendMode(mode);
console.info(`BlendMode: ${mode}`);
```

## setDefaultOutputDevice

```TypeScript
setDefaultOutputDevice(deviceType: DeviceType): Promise<void>
```

设置默认发声设备。使用Promise异步回调。

> **说明：**&gt;
> - 本接口仅适用于[StreamUsage](arkts-audio-audio-streamusage-e.md)为语音消息、VoIP语音通话或者VoIP视频通话的场景，支持听筒、扬声器和系统默认
> 设备。&gt;
> - 本接口允许在AudioRenderer创建后随时调用，系统会记录应用设置的默认本机内置发声设备。应用启动播放时，若外接设备如蓝牙耳机或有线耳机已接入，系统优先从外接设备发声；否则，系统遵循应用设置的默认本机内置发声设备
> 。

**起始版本：** 23

<!--Device-AudioRenderer-setDefaultOutputDevice(deviceType: DeviceType): Promise<void>--><!--Device-AudioRenderer-setDefaultOutputDevice(deviceType: DeviceType): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | DeviceType | 是 | 设备类型。<br>仅支持以下设备：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Operation not permit at current state. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 本接口允许在AudioRenderer创建以后的任何时间被调用。
// 未播放时调用，系统会记录应用设置的默认本机内置发声设备，当应用启动播放时从设置的默认本机内置发声设备发声。
// 正在播放时调用，在没有外接设备如蓝牙耳机/有线耳机，系统会立即切换到设置的默认本机内置发声设备发声；否则系统会先记录应用设置的默认本机内置发声设备，等外接设备移除后再切换到设置的默认本机内置发声设备发声。
audioRenderer.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('setDefaultOutputDevice Success!');
}).catch((err: BusinessError) => {
  console.error(`setDefaultOutputDevice Fail: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('Succeeded in setting the default output device.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the default output device. Code: ${err.code}, message: ${err.message}`);
});
```

## setIndependentAudioSessionStrategy

```TypeScript
setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void
```

设置独立的音频会话策略和行为参数。

> **说明：**&gt;
> 当音频渲染器在运行状态时调用此接口后，必须重新调用接口
> [start](#start)使其生效。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRenderer-setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void--><!--Device-AudioRenderer-setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | [AudioSessionStrategy](arkts-audio-audio-audiosessionstrategy-i.md) | 是 | 音频会话策略。 |
| behavior | int | 是 | 用于设置音频会话行为。<br>该参数可以是单个标志，也可以是多个标志的按位OR组合。<br>当前支持的音频会话行为详见 [AudioSessionBehaviorFlags](arkts-audio-audio-audiosessionbehaviorflags-e.md)中定义的标志。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Operation not permit at current state. |

**示例**

```TypeScript
let strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS
};
let behavior = audio.AudioSessionBehaviorFlags.MUTE_WHEN_INTERRUPTED;
audioCapturer.setIndependentAudioSessionStrategy(strategy, behavior);
```

```TypeScript
let strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS
};
let behavior = audio.AudioSessionBehaviorFlags.MUTE_WHEN_INTERRUPTED;
audioRenderer.setIndependentAudioSessionStrategy(strategy, behavior);
```

## setInterruptMode

```TypeScript
setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void
```

设置应用的焦点模型。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [InterruptMode](arkts-audio-audio-interruptmode-e.md) | 是 | 焦点模型。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当设置应用的焦点模型成功，err为undefined，否则为错误对象。 |

**示例**

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

设置应用的焦点模型。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode): Promise<void>--><!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [InterruptMode](arkts-audio-audio-interruptmode-e.md) | 是 | 焦点模型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**示例**

参见 [setInterruptMode](#setinterruptmode)

## setInterruptModeSync

```TypeScript
setInterruptModeSync(mode: InterruptMode): void
```

设置应用的焦点模型。同步设置。

**起始版本：** 23

<!--Device-AudioRenderer-setInterruptModeSync(mode: InterruptMode): void--><!--Device-AudioRenderer-setInterruptModeSync(mode: InterruptMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [InterruptMode](arkts-audio-audio-interruptmode-e.md) | 是 | 焦点模型。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

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

设置播放响度。使用Promise异步回调。

> **说明：**&gt;
> - 该接口仅支持类型为[STREAM_USAGE_MUSIC](arkts-audio-audio-streamusage-e.md)、
> [STREAM_USAGE_MOVIE](arkts-audio-audio-streamusage-e.md)或
> [STREAM_USAGE_AUDIOBOOK](arkts-audio-audio-streamusage-e.md)的音频流。&gt;
> - 该接口不支持高清通路的响度设置。&gt;
> - 由于音频框架与硬件之间存在缓冲区，响度调节实际生效存在延迟，时长取决于缓冲区长度。&gt;
> - 建议在不同音频开始播放前预先设置响度，以实现最佳均衡效果。

**起始版本：** 23

<!--Device-AudioRenderer-setLoudnessGain(loudnessGain: double): Promise<void>--><!--Device-AudioRenderer-setLoudnessGain(loudnessGain: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loudnessGain | double | 是 | 设置播放的响度值，单位为dB，响度范围为[-90.0, 24.0]。默认值为0.0dB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) | Operation is not supported on this renderer, e.g. the stream usage of this renderer is not one of [STREAM_USAGE_MUSIC](arkts-audio-audio-streamusage-e.md#stream_usage_music), [STREAM_USAGE_MOVIE](arkts-audio-audio-streamusage-e.md#stream_usage_movie) or [STREAM_USAGE_AUDIOBOOK](arkts-audio-audio-streamusage-e.md#stream_usage_audiobook). |

**示例**

```TypeScript
audioRenderer.setLoudnessGain(1.0);
```

## setNoiseReductionMode

```TypeScript
setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void
```

Sets noise reduction mode for current audio renderer. The supported mode should be obtained by getSupportedNoiseReductionModes. The actual effect may vary from different audio devices, and will be invalid when there are multiple direct streams running simultaneously. The mode can only be changed in created and stopped state.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRenderer-setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void--><!--Device-AudioRenderer-setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| noiseReductionMode | [NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md) | 是 | The noise reduction mode to set. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Illegal state, audio renderer is in running or released state. |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) | The setted mode is not supported. |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | Audio server process died. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let supportedModes: Array<audio.NoiseReductionMode> = audioCapturer.getSupportedNoiseReductionModes();
  if (supportedModes.includes(audio.NoiseReductionMode.PURE_VOCALS)) {
    audioCapturer.setNoiseReductionMode(audio.NoiseReductionMode.PURE_VOCALS);
  } else {
    audioCapturer.setNoiseReductionMode(audio.NoiseReductionMode.FIDELITY);
  }
  console.info(`setNoiseReductionMode success: ${audioCapturer.getNoiseReductionMode()}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`setNoiseReductionMode failed. Code: ${error.code}, message: ${error.message}`);
}
```

## setRenderRate

```TypeScript
setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void
```

设置音频渲染速率。使用callback异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 11开始废弃，建议使用[setSpeed](#setspeed)替代。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** setSpeed

<!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rate | [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) | 是 | 渲染的速率。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当设置音频渲染速率成功，err为undefined，否则为错误对象。 |

**示例**

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

设置音频渲染速率。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 11开始废弃，建议使用[setSpeed](#setspeed)替代。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** setSpeed

<!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate): Promise<void>--><!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rate | [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) | 是 | 渲染的速率。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**示例**

参见 [setRenderRate](#setrenderrate)

## setSilentModeAndMixWithOthers

```TypeScript
setSilentModeAndMixWithOthers(on: boolean): void
```

设置静音并发播放模式。 当设置为true，打开静音并发播放模式，系统将让此音频流静音播放，并且不会打断其他音频流。设置为false，将关闭静音并发播放，音频流可根据系统焦点策略抢占焦点。

**起始版本：** 23

<!--Device-AudioRenderer-setSilentModeAndMixWithOthers(on: boolean): void--><!--Device-AudioRenderer-setSilentModeAndMixWithOthers(on: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | boolean | 是 | 打开/关闭静音并发播放模式。true表示设置当前播放的音频流静音播放，并且不会打断其它音频流播放。false表示取消当前播放的音频流静音播放，音频流可根据系统焦点策略抢占焦点。 |

**示例**

```TypeScript
audioRenderer.setSilentModeAndMixWithOthers(true);
```

## setSpeed

```TypeScript
setSpeed(speed: double): void
```

设置播放倍速。

**起始版本：** 23

<!--Device-AudioRenderer-setSpeed(speed: double): void--><!--Device-AudioRenderer-setSpeed(speed: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | double | 是 | 设置播放的倍速值，倍速范围为[0.25, 4.0]。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
audioRenderer.setSpeed(1.5);
```

## setVolume

```TypeScript
setVolume(volume: double, callback: AsyncCallback<void>): void
```

设置音频流的音量。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-setVolume(volume: double, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setVolume(volume: double, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | double | 是 | 音量值范围为[0.0, 1.0]。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当设置应用的音量成功，err为undefined，否则为错误对象。 |

**示例**

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
    console.error(`Failed to set the volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the volume.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10).then(() => {
  console.info('Succeeded in setting the volume.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the volume. Code: ${err.code}, message: ${err.message}`);
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

设置音频流的音量。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-setVolume(volume: double): Promise<void>--><!--Device-AudioRenderer-setVolume(volume: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | double | 是 | 音量值范围为[0.0, 1.0]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**示例**

参见 [setVolume](#setvolume)

## setVolumeWithRamp

```TypeScript
setVolumeWithRamp(volume: double, duration: int): void
```

在指定时间范围内设置音量渐变模式。同步返回结果。

**起始版本：** 23

<!--Device-AudioRenderer-setVolumeWithRamp(volume: double, duration: int): void--><!--Device-AudioRenderer-setVolumeWithRamp(volume: double, duration: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | double | 是 | 渐变目标音量值，音量范围为[0.0, 1.0]。 |
| duration | int | 是 | 渐变持续时间，单位为ms。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

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

启动音频渲染器。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-start(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当启动音频渲染器成功，err为undefined，否则为错误对象。异常将返回error对象：<br>错误码6800301：表示包含状态检查异常、焦 点抢占失败、系统处理异常（具体错误查看系统日志）。 |

**示例**

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

启动音频渲染器。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-start(): Promise<void>--><!--Device-AudioRenderer-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，成功表示启动音频渲染器成功。异常将返回error对象： |

**示例**

参见 [start](#start)

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止音频渲染。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-stop(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当停止渲染成功，err为undefined，否则为错误对象。 |

**示例**

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

停止音频渲染。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioRenderer-stop(): Promise<void>--><!--Device-AudioRenderer-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**示例**

参见 [stop](#stop)

## write

```TypeScript
write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void
```

写入缓冲区。使用callback异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 11开始废弃，建议使用[on('writeData')](#onwritedata)替代。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** writeData

<!--Device-AudioRenderer-write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void--><!--Device-AudioRenderer-write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 要写入缓冲区的数据。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 | 回调函数。当写入缓冲区成功，err为undefined，data为获取到的写入的字节数；否则为错误对象。 |

**示例**

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
  // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let path = context.cacheDir;
  // 此处仅作示例，实际使用时需要将文件替换为应用要播放的PCM文件。
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
  // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let path = context.cacheDir;
  // 此处仅作示例，实际使用时需要将文件替换为应用要播放的PCM文件。
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

写入缓冲区。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 11开始废弃，建议使用[on('writeData')](#onwritedata)替代。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** writeData

<!--Device-AudioRenderer-write(buffer: ArrayBuffer): Promise<number>--><!--Device-AudioRenderer-write(buffer: ArrayBuffer): Promise<number>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 要写入缓冲区的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回写入的字节数。 |

**示例**

参见 [write](#write)

## state

```TypeScript
readonly state: AudioState
```

音频渲染器的状态。

**类型：** AudioState

**起始版本：** 23

<!--Device-AudioRenderer-readonly state: AudioState--><!--Device-AudioRenderer-readonly state: AudioState-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

