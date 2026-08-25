# AudioCapturer

提供音频采集的相关接口。在使用AudioCapturer的接口之前，需先通过 [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md) 获取AudioCapturer实例。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## getAudioStreamId

```TypeScript
getAudioStreamId(callback: AsyncCallback<number>): void
```

获取音频流id。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getAudioStreamId

```TypeScript
getAudioStreamId(): Promise<number>
```

获取音频流id。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getAudioStreamIdSync

```TypeScript
getAudioStreamIdSync(): number
```

获取音频流id。同步返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| number |

## getAudioTime

```TypeScript
getAudioTime(callback: AsyncCallback<number>): void
```

获取当前录制位置的时间戳（从1970年1月1日开始），单位为纳秒。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getAudioTime

```TypeScript
getAudioTime(): Promise<number>
```

获取当前录制位置的时间戳（从1970年1月1日开始），单位为纳秒。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getAudioTimestampInfo

```TypeScript
getAudioTimestampInfo(): Promise<AudioTimestampInfo>
```

获取输入音频流时间戳和当前数据帧位置信息。 该接口可以获取到音频通道实际录制位置（framePos）以及录制到该位置时候的时间戳（timestamp），时间戳单位为纳秒。

**起始版本：** 19

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |

## getAudioTimestampInfoSync

```TypeScript
getAudioTimestampInfoSync(): AudioTimestampInfo
```

获取音频流时间戳和当前数据帧位置信息。同步返回结果。

**起始版本：** 19

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| [AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |

## getAudioTimeSync

```TypeScript
getAudioTimeSync(): number
```

获取当前录制位置的时间戳（从1970年1月1日开始），单位为纳秒。同步返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| number |

## getBufferSize

```TypeScript
getBufferSize(callback: AsyncCallback<number>): void
```

获取采集器合理的最小缓冲区大小。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getBufferSize

```TypeScript
getBufferSize(): Promise<number>
```

获取采集器合理的最小缓冲区大小。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getBufferSizeSync

```TypeScript
getBufferSizeSync(): number
```

获取采集器合理的最小缓冲区大小。同步返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| number |

## getCapturerInfo

```TypeScript
getCapturerInfo(callback: AsyncCallback<AudioCapturerInfo>): void
```

获取音频采集器信息。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)&gt; | 是 |

## getCapturerInfo

```TypeScript
getCapturerInfo(): Promise<AudioCapturerInfo>
```

获取音频采集器信息。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)&gt; |

## getCapturerInfoSync

```TypeScript
getCapturerInfoSync(): AudioCapturerInfo
```

获取音频采集器信息。同步返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) |

## getCurrentAudioCapturerChangeInfo

```TypeScript
getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo
```

获取录音流配置。同步返回结果。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 |
| --- |
| [AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md) |

## getCurrentInputDevices

```TypeScript
getCurrentInputDevices(): AudioDeviceDescriptors
```

获取录音流输入设备信息。同步返回结果。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 |
| --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) |

## getNoiseReductionMode

```TypeScript
getNoiseReductionMode(): NoiseReductionMode
```

获取当前录音流的降噪模式。返回结果仅反映当前录音流的降噪模式。默认值为 [NoiseReductionMode.FIDELITY](arkts-audio-audio-noisereductionmode-e.md)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| [NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md) |

## getOverflowCount

```TypeScript
getOverflowCount(): Promise<number>
```

获取当前录制音频流的过载音频帧数量。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getOverflowCountSync

```TypeScript
getOverflowCountSync(): number
```

获取当前录制音频流的过载音频帧数量。同步返回数据。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| number |

## getStreamInfo

```TypeScript
getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void
```

获取音频采集器流信息。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)&gt; | 是 |

## getStreamInfo

```TypeScript
getStreamInfo(): Promise<AudioStreamInfo>
```

获取音频采集器流信息。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)&gt; |

## getStreamInfoSync

```TypeScript
getStreamInfoSync(): AudioStreamInfo
```

获取音频采集器流信息。同步返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) |

## getSupportedNoiseReductionModes

```TypeScript
getSupportedNoiseReductionModes(): Array<NoiseReductionMode>
```

获取当前设备支持的录音降噪模式。

> **说明：**&gt;
> - 当前仅使用[SourceType.SOURCE_TYPE_VOICE_MESSAGE](arkts-audio-audio-sourcetype-e.md)创建的录音流会根据设备平台查询支持的降
> 噪模式，其他录音流默认仅返回[NoiseReductionMode.FIDELITY](arkts-audio-audio-noisereductionmode-e.md)。&gt;
> - 返回结果仅考虑音频格式和设备平台，不考虑当前输入设备和录音并发情况。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Array&lt;[NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## off('markReach')

```TypeScript
off(type: 'markReach', callback?: Callback<number>): void
```

取消监听标记到达事件。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'markReach' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

## off('periodReach')

```TypeScript
off(type: 'periodReach', callback?: Callback<number>): void
```

取消监听标记到达事件。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'periodReach' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: Callback<AudioState>): void
```

取消监听状态变化事件。使用callback异步回调。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt'): void
```

取消监听音频中断事件。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioInterrupt' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('inputDeviceChange')

```TypeScript
off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void
```

取消监听音频输入设备更改事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'inputDeviceChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('audioCapturerChange')

```TypeScript
off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void
```

取消监听录音流配置变化事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioCapturerChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('readData')

```TypeScript
off(type: 'readData', callback?: Callback<ArrayBuffer>): void
```

取消监听音频数据读取回调事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'readData' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('markReach')

```TypeScript
on(type: 'markReach', frame: number, callback: Callback<number>): void
```

监听标记到达事件（当采集的帧数达到frame参数的值时触发，仅调用一次）。使用callback异步回调。 如果将frame设置为100，当采集帧数到达第100帧时，系统将上报信息。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'markReach' | 是 |
| [frame](../../apis-arkui/arkts-apis/arkts-arkui-rendernode-c.md) | number | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## on('periodReach')

```TypeScript
on(type: 'periodReach', frame: number, callback: Callback<number>): void
```

监听标记到达事件（当采集的帧数达到frame参数的值时触发，即按周期上报信息）。使用callback异步回调。 如果将frame设置为10，每采集10帧数据均会上报信息（例如：第10帧、第20帧、第30帧......）。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'periodReach' | 是 |
| [frame](../../apis-arkui/arkts-apis/arkts-arkui-rendernode-c.md) | number | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: Callback<AudioState>): void
```

监听状态变化事件（当AudioCapturer状态发生变化时触发）。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | 是 |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void
```

监听音频中断事件（当音频焦点发生变化时触发）。使用callback异步回调。 AudioCapturer对象在start事件时获取焦点，在pause、stop等事件时释放焦点，无需开发者主动申请。 调用此方法后，如果AudioCapturer对象获取焦点失败或发生中断事件（如被其他音频打断等），会收到 [InterruptEvent](arkts-audio-audio-interruptevent-i.md)。建议应用根据InterruptEvent的信息进行进一步处理。更多信息请参阅音频焦点介绍文档。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioInterrupt' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('inputDeviceChange')

```TypeScript
on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void
```

监听音频输入设备变化事件（当音频输入设备发生变化时触发）。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'inputDeviceChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('audioCapturerChange')

```TypeScript
on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void
```

监听录音流配置变化事件（当音频录制流状态变化、设备变化时触发）。使用callback异步回调。订阅内部是异步实现，是非精确回调，在录音流配置变化的同时注册回调，收到的返回结果存在变化可能性。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioCapturerChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfo](arkts-audio-audio-audiocapturerchangeinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('readData')

```TypeScript
on(type: 'readData', callback: Callback<ArrayBuffer>): void
```

监听音频数据读取回调事件（当需要读取音频流数据时触发）。使用callback异步回调。 回调函数仅用来读取音频数据，请勿在回调函数中调用AudioCapturer相关接口。 为了消除麦克风硬件设计带来的上电杂音，通常会对录音启动后的前100ms数据进行静音。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'readData' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## read

```TypeScript
read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void
```

读入缓冲区。使用callback异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 11开始废弃，建议使用[on('readData')](#onreaddata)替代。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** readData

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |
| isBlockingRead | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | 是 |

## read

```TypeScript
read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>
```

读入缓冲区。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 11开始废弃，建议使用[on('readData')](#onreaddata)替代。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** readData

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |
| isBlockingRead | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放音频采集器。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## release

```TypeScript
release(): Promise<void>
```

释放音频采集器。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## requestPlaybackCaptureStart

```TypeScript
requestPlaybackCaptureStart(callback: Callback<PlaybackCaptureStartState>): void
```

请求启动内录流接口，内录流只能通过该接口触发启动。使用callback异步回调。 内录是指以系统内部音频数据作为音频源的输入类型，简称为内录，对应的流称为内录流。常用于录制目标设备应用发送到系统以供播放的音频。 该接口为非阻塞接口，系统接收到内录启动请求后，会继续处理用户授权检查和内录流启动，最终结果通过回调函数返回。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PlaybackCaptureStartState](arkts-audio-audio-playbackcapturestartstate-e.md)&gt; | 是 |

## setIndependentAudioSessionStrategy

```TypeScript
setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: number): void
```

设置独立的音频会话策略和行为参数。

> **说明：**&gt;
> 当音频采集器在运行状态时调用此接口后，必须重新调用接口
> [start](#start)使其生效。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strategy | [AudioSessionStrategy](arkts-audio-audio-audiosessionstrategy-i.md) | 是 |
| behavior | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |

## setMuteHint

```TypeScript
setMuteHint(mute: boolean): Promise<void>
```

应用将当前录音流的自身静音状态传递给系统音频模块。<!--RP1-->该接口不会触发录音流静音，当前仅在部分PC/2in1设备上用于优化设备功耗。<!--RP1End-->使用Promise异步回调。

> **说明：**&gt;
> - 该接口用于向系统音频模块上报应用自身的静音状态，不会改变录音流的实际静音状态。&gt;
> - 该接口仅在录音流处于运行态时允许调用，否则返回错误码6800103。&gt;
> - 同一录音流同时设置流级静音提示接口（本接口）和会话级静音提示接口
> [AudioSessionManager.setCapturerMuteHint](arkts-audio-audio-audiosessionmanager-i.md#setcapturermutehint)
> 时，流级[setMuteHint](#setmutehint)优先级更高，数值以流级设置值为准。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mute | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |

## setNoiseReductionMode

```TypeScript
setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void
```

设置当前录音流的降噪模式。建议先调用[getSupportedNoiseReductionModes](#getsupportednoisereductionmodes)获取当 前录音流支持的降噪模式后，再通过本接口进行设置。

> **说明：**&gt;
> - 当前仅支持使用[SourceType.SOURCE_TYPE_VOICE_MESSAGE](arkts-audio-audio-sourcetype-e.md)创建的录音流进行降噪模式设置，其他
> 录音流默认仅支持[NoiseReductionMode.FIDELITY](arkts-audio-audio-noisereductionmode-e.md)。&gt;
> - 降噪效果受设备平台、音频设备和录音并发情况影响。存在多个录音流同时运行时，设置的降噪模式可能不生效。&gt;
> - 该接口仅可在录音流创建后未开始录音，或停止录音后调用；录音流处于运行态或已释放时调用将抛出异常。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [noiseReductionMode](arkts-audio-audio-noisereductionconfigaction-i-sys.md) | [NoiseReductionMode](arkts-audio-audio-noisereductionmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## setWillMuteWhenInterrupted

```TypeScript
setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>
```

设置当前录制音频流是否启用静音打断模式。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| muteWhenInterrupted | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

启动音频采集器，开始获取音频数据。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## start

```TypeScript
start(): Promise<void>
```

启动音频采集器，开始获取音频数据。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止音频采集器，停止输入音频流。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## stop

```TypeScript
stop(): Promise<void>
```

停止音频采集器，停止输入音频流。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## state

```TypeScript
readonly state: AudioState
```

音频采集器状态。

**类型：** AudioState

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer
