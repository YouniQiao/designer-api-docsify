# AudioRenderer

提供音频渲染的相关接口。 在使用AudioRenderer的接口之前，需先通过[createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md#createAudioRenderer)获取AudioRenderer实例。 > **说明：** > > - 本Interface首批接口从API version 8开始支持。

**起始版本：** 23

**废弃版本：** -1

<!--Device-audio-interface AudioRenderer--><!--Device-audio-interface AudioRenderer-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

## drain

```TypeScript
drain(callback: AsyncCallback<void>): void
```

检查缓冲区是否已被耗尽。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-drain(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-drain(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## drain

```TypeScript
drain(): Promise<void>
```

检查缓冲区是否已被耗尽。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-drain(): Promise<void>--><!--Device-AudioRenderer-drain(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## flush

```TypeScript
flush(): Promise<void>
```

清空缓冲区（[AudioState](arkts-audio-audio-audiostate-e.md#AudioState)为STATE_RUNNING、STATE_PAUSED、STATE_STOPPED状态下可用）。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-flush(): Promise<void>--><!--Device-AudioRenderer-flush(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |

## getAudioEffectMode

```TypeScript
getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void
```

获取当前音效模式。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void--><!--Device-AudioRenderer-getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md)&gt; | 是 |

## getAudioEffectMode

```TypeScript
getAudioEffectMode(): Promise<AudioEffectMode>
```

获取当前音效模式。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getAudioEffectMode(): Promise<AudioEffectMode>--><!--Device-AudioRenderer-getAudioEffectMode(): Promise<AudioEffectMode>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md)&gt; |

## getAudioStreamId

```TypeScript
getAudioStreamId(callback: AsyncCallback<number>): void
```

获取音频流id。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getAudioStreamId(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getAudioStreamId(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getAudioStreamId

```TypeScript
getAudioStreamId(): Promise<number>
```

获取音频流id。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getAudioStreamId(): Promise<long>--><!--Device-AudioRenderer-getAudioStreamId(): Promise<long>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getAudioStreamIdSync

```TypeScript
getAudioStreamIdSync(): number
```

获取音频流id。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getAudioStreamIdSync(): long--><!--Device-AudioRenderer-getAudioStreamIdSync(): long-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| number |

## getAudioTime

```TypeScript
getAudioTime(callback: AsyncCallback<number>): void
```

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getAudioTime(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getAudioTime(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getAudioTime

```TypeScript
getAudioTime(): Promise<number>
```

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getAudioTime(): Promise<long>--><!--Device-AudioRenderer-getAudioTime(): Promise<long>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getAudioTimeSync

```TypeScript
getAudioTimeSync(): number
```

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getAudioTimeSync(): long--><!--Device-AudioRenderer-getAudioTimeSync(): long-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| number |

## getAudioTimestampInfo

```TypeScript
getAudioTimestampInfo(): Promise<AudioTimestampInfo>
```

获取输出音频流时间戳和位置信息，适配倍速接口。使用Promise异步回调。 获取输出音频流时间戳和位置信息，通常用于进行音画同步对齐。 注意，当实际播放位置（framePosition）为0时，时间戳（timestamp）是固定值，直到流真正开始播放时才会更新。当调用Flush接口时实际播放位置也会被重置。 当音频流路由（route）变化时，例如设备变化或者输出类型变化时，播放位置也会被重置，但此时时间戳仍会持续增长。推荐当实际播放位置和时间戳的变化稳定后再使用该接口获取的值。该接口适配倍速接口，例如当播放速度设置为2倍时，播放位 置的增长速度也会返回为正常的2倍。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getAudioTimestampInfo(): Promise<AudioTimestampInfo>--><!--Device-AudioRenderer-getAudioTimestampInfo(): Promise<AudioTimestampInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

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

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getAudioTimestampInfoSync(): AudioTimestampInfo--><!--Device-AudioRenderer-getAudioTimestampInfoSync(): AudioTimestampInfo-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| [AudioTimestampInfo](arkts-audio-audio-audiotimestampinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |

## getBufferSize

```TypeScript
getBufferSize(callback: AsyncCallback<number>): void
```

获取音频渲染器的最小缓冲区大小。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getBufferSize(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getBufferSize(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getBufferSize

```TypeScript
getBufferSize(): Promise<number>
```

获取音频渲染器的最小缓冲区大小。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getBufferSize(): Promise<long>--><!--Device-AudioRenderer-getBufferSize(): Promise<long>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getBufferSizeSync

```TypeScript
getBufferSizeSync(): number
```

获取音频渲染器的最小缓冲区大小。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getBufferSizeSync(): long--><!--Device-AudioRenderer-getBufferSizeSync(): long-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| number |

## getCurrentOutputDevices

```TypeScript
getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void
```

获取音频流输出设备信息。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 是 |

## getCurrentOutputDevices

```TypeScript
getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>
```

获取音频流输出设备信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>--><!--Device-AudioRenderer-getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; |

## getCurrentOutputDevicesSync

```TypeScript
getCurrentOutputDevicesSync(): AudioDeviceDescriptors
```

获取音频流输出设备信息。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getCurrentOutputDevicesSync(): AudioDeviceDescriptors--><!--Device-AudioRenderer-getCurrentOutputDevicesSync(): AudioDeviceDescriptors-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 |
| --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) |

## getLatency

```TypeScript
getLatency(type: AudioLatencyType): number
```

获取当前音频路由的预估时延。 > **说明：** > > - 无线连接的音频设备，时延估算会存在误差，结果仅供参考。 > > - 由于时延未计入实时缓冲区，建议仅在音频播放开始时获取，避免频繁调用，否则可能因路由切换而阻塞该接口调用。 > > - 音频输出到硬件后的音画同步建议使用[getAudioTimestampInfo](#getAudioTimestampInfo)或 > [getAudioTimestampInfoSync](#getAudioTimestampInfoSync)完成。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRenderer-getLatency(type: AudioLatencyType): int--><!--Device-AudioRenderer-getLatency(type: AudioLatencyType): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AudioLatencyType](arkts-audio-audio-audiolatencytype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## getLoudnessGain

```TypeScript
getLoudnessGain(): number
```

获取播放响度。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getLoudnessGain(): double--><!--Device-AudioRenderer-getLoudnessGain(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| number |

## getMaxStreamVolume

```TypeScript
getMaxStreamVolume(callback: AsyncCallback<number>): void
```

获取音频流的最大音量。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getMaxStreamVolume(callback: AsyncCallback<double>): void--><!--Device-AudioRenderer-getMaxStreamVolume(callback: AsyncCallback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getMaxStreamVolume

```TypeScript
getMaxStreamVolume(): Promise<number>
```

获取音频流的最大音量。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getMaxStreamVolume(): Promise<double>--><!--Device-AudioRenderer-getMaxStreamVolume(): Promise<double>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getMaxStreamVolumeSync

```TypeScript
getMaxStreamVolumeSync(): number
```

获取音频流的最大音量。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getMaxStreamVolumeSync(): double--><!--Device-AudioRenderer-getMaxStreamVolumeSync(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| number |

## getMinStreamVolume

```TypeScript
getMinStreamVolume(callback: AsyncCallback<number>): void
```

获取音频流的最小音量。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getMinStreamVolume(callback: AsyncCallback<double>): void--><!--Device-AudioRenderer-getMinStreamVolume(callback: AsyncCallback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getMinStreamVolume

```TypeScript
getMinStreamVolume(): Promise<number>
```

获取音频流的最小音量。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getMinStreamVolume(): Promise<double>--><!--Device-AudioRenderer-getMinStreamVolume(): Promise<double>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getMinStreamVolumeSync

```TypeScript
getMinStreamVolumeSync(): number
```

获取音频流的最小音量。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getMinStreamVolumeSync(): double--><!--Device-AudioRenderer-getMinStreamVolumeSync(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| number |

## getRenderRate

```TypeScript
getRenderRate(callback: AsyncCallback<AudioRendererRate>): void
```

获取音频渲染速率。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [getSpeed](#getSpeed)

<!--Device-AudioRenderer-getRenderRate(callback: AsyncCallback<AudioRendererRate>): void--><!--Device-AudioRenderer-getRenderRate(callback: AsyncCallback<AudioRendererRate>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md)&gt; | 是 |

## getRenderRate

```TypeScript
getRenderRate(): Promise<AudioRendererRate>
```

获取音频渲染速率。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [getSpeed](#getSpeed)

<!--Device-AudioRenderer-getRenderRate(): Promise<AudioRendererRate>--><!--Device-AudioRenderer-getRenderRate(): Promise<AudioRendererRate>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md)&gt; |

## getRenderRateSync

```TypeScript
getRenderRateSync(): AudioRendererRate
```

获取音频渲染速率。同步返回结果。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getSpeed](#getSpeed)

<!--Device-AudioRenderer-getRenderRateSync(): AudioRendererRate--><!--Device-AudioRenderer-getRenderRateSync(): AudioRendererRate-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) |

## getRendererInfo

```TypeScript
getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void
```

获取当前创建的音频渲染器信息。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void--><!--Device-AudioRenderer-getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md)&gt; | 是 |

## getRendererInfo

```TypeScript
getRendererInfo(): Promise<AudioRendererInfo>
```

获取当前创建的音频渲染器信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getRendererInfo(): Promise<AudioRendererInfo>--><!--Device-AudioRenderer-getRendererInfo(): Promise<AudioRendererInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md)&gt; |

## getRendererInfoSync

```TypeScript
getRendererInfoSync(): AudioRendererInfo
```

获取当前创建的音频渲染器信息。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getRendererInfoSync(): AudioRendererInfo--><!--Device-AudioRenderer-getRendererInfoSync(): AudioRendererInfo-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) |

## getSilentModeAndMixWithOthers

```TypeScript
getSilentModeAndMixWithOthers(): boolean
```

获取静音并发播放模式。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getSilentModeAndMixWithOthers(): boolean--><!--Device-AudioRenderer-getSilentModeAndMixWithOthers(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| boolean |

## getSpeed

```TypeScript
getSpeed(): number
```

获取播放倍速。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getSpeed(): double--><!--Device-AudioRenderer-getSpeed(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| number |

## getStreamInfo

```TypeScript
getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void
```

获取音频流信息。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void--><!--Device-AudioRenderer-getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)&gt; | 是 |

## getStreamInfo

```TypeScript
getStreamInfo(): Promise<AudioStreamInfo>
```

获取音频流信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getStreamInfo(): Promise<AudioStreamInfo>--><!--Device-AudioRenderer-getStreamInfo(): Promise<AudioStreamInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)&gt; |

## getStreamInfoSync

```TypeScript
getStreamInfoSync(): AudioStreamInfo
```

获取音频流信息。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getStreamInfoSync(): AudioStreamInfo--><!--Device-AudioRenderer-getStreamInfoSync(): AudioStreamInfo-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) |

## getUnderflowCount

```TypeScript
getUnderflowCount(callback: AsyncCallback<number>): void
```

获取当前播放音频流的欠载音频帧数量。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getUnderflowCount(callback: AsyncCallback<long>): void--><!--Device-AudioRenderer-getUnderflowCount(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getUnderflowCount

```TypeScript
getUnderflowCount(): Promise<number>
```

获取当前播放音频流的欠载音频帧数量。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getUnderflowCount(): Promise<long>--><!--Device-AudioRenderer-getUnderflowCount(): Promise<long>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getUnderflowCountSync

```TypeScript
getUnderflowCountSync(): number
```

获取当前播放音频流的欠载音频帧数量，同步返回数据。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getUnderflowCountSync(): long--><!--Device-AudioRenderer-getUnderflowCountSync(): long-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| number |

## getVolume

```TypeScript
getVolume(): number
```

获取音频流的音量。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-getVolume(): double--><!--Device-AudioRenderer-getVolume(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| number |

## offAudioInterrupt

```TypeScript
offAudioInterrupt(callback?: Callback<InterruptEvent>): void
```

Unsubscribes audio interrupt events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-offAudioInterrupt(callback?: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-offAudioInterrupt(callback?: Callback<InterruptEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## offMarkReach

```TypeScript
offMarkReach(callback?: Callback<number>): void
```

Unsubscribes from mark reached events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-offMarkReach(callback?: Callback<long>): void--><!--Device-AudioRenderer-offMarkReach(callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

## offOutputDeviceChange

```TypeScript
offOutputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void
```

Unsubscribes output device change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-offOutputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-offOutputDeviceChange(callback?: Callback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## offOutputDeviceChangeWithInfo

```TypeScript
offOutputDeviceChangeWithInfo(callback?: Callback<AudioStreamDeviceChangeInfo>): void
```

Unsubscribes output device change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-offOutputDeviceChangeWithInfo(callback?: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-offOutputDeviceChangeWithInfo(callback?: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## offPeriodReach

```TypeScript
offPeriodReach(callback?: Callback<number>): void
```

Unsubscribes from period reached events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-offPeriodReach(callback?: Callback<long>): void--><!--Device-AudioRenderer-offPeriodReach(callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

## offStateChange

```TypeScript
offStateChange(callback?: Callback<AudioState>): void
```

Unsubscribes audio state change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-offStateChange(callback?: Callback<AudioState>): void--><!--Device-AudioRenderer-offStateChange(callback?: Callback<AudioState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## offWriteData

```TypeScript
offWriteData(callback?: AudioRendererWriteDataCallback): void
```

Unsubscribes audio data callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-offWriteData(callback?: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-offWriteData(callback?: AudioRendererWriteDataCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off_audioInterrupt

```TypeScript
off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void
```

取消监听音频中断事件。使用callback异步回调。

**起始版本：** 18

**废弃版本：** -1

<!--Device-AudioRenderer-off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioInterrupt' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off_markReach

```TypeScript
off(type: 'markReach', callback?: Callback<number>): void
```

取消监听标记到达事件。使用callback异步回调。

**起始版本：** 8

**废弃版本：** -1

<!--Device-AudioRenderer-off(type: 'markReach', callback?: Callback<long>): void--><!--Device-AudioRenderer-off(type: 'markReach', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'markReach' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

## off_outputDeviceChange

```TypeScript
off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void
```

取消监听音频输出设备变化事件。使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

<!--Device-AudioRenderer-off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'outputDeviceChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off_outputDeviceChangeWithInfo

```TypeScript
off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void
```

取消监听音频流输出设备变化及原因事件。使用callback异步回调。

**起始版本：** 11

**废弃版本：** -1

<!--Device-AudioRenderer-off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'outputDeviceChangeWithInfo' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off_periodReach

```TypeScript
off(type: 'periodReach', callback?: Callback<number>): void
```

取消监听标记到达事件。使用callback异步回调。

**起始版本：** 8

**废弃版本：** -1

<!--Device-AudioRenderer-off(type: 'periodReach', callback?: Callback<long>): void--><!--Device-AudioRenderer-off(type: 'periodReach', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'periodReach' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

## off_stateChange

```TypeScript
off(type: 'stateChange', callback?: Callback<AudioState>): void
```

取消监听状态变化事件。使用callback异步回调。

**起始版本：** 18

**废弃版本：** -1

<!--Device-AudioRenderer-off(type: 'stateChange', callback?: Callback<AudioState>): void--><!--Device-AudioRenderer-off(type: 'stateChange', callback?: Callback<AudioState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off_writeData

```TypeScript
off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void
```

取消监听音频数据写入回调事件。使用callback异步回调。

**起始版本：** 11

**废弃版本：** -1

<!--Device-AudioRenderer-off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'writeData' | 是 |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## onAudioInterrupt

```TypeScript
onAudioInterrupt(callback: Callback<InterruptEvent>): void
```

Listens for audio interrupt events. This method uses a callback to get interrupt events. The interrupt event is triggered when audio playback is interrupted.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-onAudioInterrupt(callback: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-onAudioInterrupt(callback: Callback<InterruptEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## onMarkReach

```TypeScript
onMarkReach(frame: number, callback: Callback<number>): void
```

Subscribes to mark reached events. When the number of frames rendered reaches the value of the frame parameter, the callback is invoked.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-onMarkReach(frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-onMarkReach(frame: long, callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| frame | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## onOutputDeviceChange

```TypeScript
onOutputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void
```

Subscribes output device change event callback. The event is triggered when output device change for this stream.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-onOutputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-onOutputDeviceChange(callback: Callback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## onOutputDeviceChangeWithInfo

```TypeScript
onOutputDeviceChangeWithInfo(callback: Callback<AudioStreamDeviceChangeInfo>): void
```

Subscribes output device change event callback. The event is triggered when output device change for this stream.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-onOutputDeviceChangeWithInfo(callback: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-onOutputDeviceChangeWithInfo(callback: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## onPeriodReach

```TypeScript
onPeriodReach(frame: number, callback: Callback<number>): void
```

Subscribes to period reached events. When the period of frame rendering reaches the value of frame parameter, the callback is invoked.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-onPeriodReach(frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-onPeriodReach(frame: long, callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| frame | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## onStateChange

```TypeScript
onStateChange(callback: Callback<AudioState>): void
```

Subscribes audio state change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-onStateChange(callback: Callback<AudioState>): void--><!--Device-AudioRenderer-onStateChange(callback: Callback<AudioState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | 是 |

## onWriteData

```TypeScript
onWriteData(callback: AudioRendererWriteDataCallback): void
```

Subscribes audio data callback. The event is triggered when audio buffer is available for writing more data.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-onWriteData(callback: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-onWriteData(callback: AudioRendererWriteDataCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on_audioInterrupt

```TypeScript
on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void
```

监听音频中断事件（当音频焦点发生变化时触发）。使用callback异步回调。 AudioRenderer对象在start事件时获取焦点，在pause、stop等事件时释放焦点，无需开发者主动申请。 调用此方法后，如果AudioRenderer对象获取焦点失败或发生中断事件（如被其他音频打断等），会收到[InterruptEvent](arkts-audio-audio-interruptevent-i.md#InterruptEvent)。建议应用根据 InterruptEvent的信息进行进一步处理。更多信息请参阅文档[音频焦点介绍](../../../media/audio/audio-playback-concurrency.md)。

**起始版本：** 9

**废弃版本：** -1

<!--Device-AudioRenderer-on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void--><!--Device-AudioRenderer-on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioInterrupt' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptEvent](arkts-audio-audio-interruptevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on_markReach

```TypeScript
on(type: 'markReach', frame: number, callback: Callback<number>): void
```

监听标记到达事件（当渲染的帧数到达frame参数的值时触发，仅调用一次）。使用callback异步回调。 如果将frame设置为100，当渲染帧数到达第100帧时，系统将上报信息。

**起始版本：** 8

**废弃版本：** -1

<!--Device-AudioRenderer-on(type: 'markReach', frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-on(type: 'markReach', frame: long, callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'markReach' | 是 |
| frame | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## on_outputDeviceChange

```TypeScript
on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void
```

监听音频输出设备变化事件（当音频输出设备发生变化时触发）。使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

<!--Device-AudioRenderer-on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRenderer-on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'outputDeviceChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on_outputDeviceChangeWithInfo

```TypeScript
on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void
```

监听音频流输出设备变化及原因事件（当音频输出设备发生变化时触发）。使用callback异步回调。

**起始版本：** 11

**废弃版本：** -1

<!--Device-AudioRenderer-on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void--><!--Device-AudioRenderer-on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'outputDeviceChangeWithInfo' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioStreamDeviceChangeInfo](arkts-audio-audio-audiostreamdevicechangeinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on_periodReach

```TypeScript
on(type: 'periodReach', frame: number, callback: Callback<number>): void
```

监听标记到达事件（每当渲染的帧数达到frame参数的值时触发，即按周期上报信息）。使用callback异步回调。 如果将frame设置为10，每渲染10帧数据均会上报信息（例如：第10帧、第20帧、第30帧......）。

**起始版本：** 8

**废弃版本：** -1

<!--Device-AudioRenderer-on(type: 'periodReach', frame: long, callback: Callback<long>): void--><!--Device-AudioRenderer-on(type: 'periodReach', frame: long, callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'periodReach' | 是 |
| frame | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## on_stateChange

```TypeScript
on(type: 'stateChange', callback: Callback<AudioState>): void
```

监听状态变化事件（当AudioRenderer的状态发生变化时触发）。使用callback异步回调。

**起始版本：** 8

**废弃版本：** -1

<!--Device-AudioRenderer-on(type: 'stateChange', callback: Callback<AudioState>): void--><!--Device-AudioRenderer-on(type: 'stateChange', callback: Callback<AudioState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioState&gt; | 是 |

## on_writeData

```TypeScript
on(type: 'writeData', callback: AudioRendererWriteDataCallback): void
```

监听音频数据写入回调事件（当需要写入音频数据时触发）。使用callback异步回调。 > **说明：** > > - 回调函数仅用来写入音频数据，请勿在回调函数中调用AudioRenderer相关接口。 > > - 为避免音频播放启动和停止时数据不连续可能出现的杂音，系统通常会在启动和停止时对音频数据做20ms以内的淡入淡出处理。

**起始版本：** 11

**废弃版本：** -1

<!--Device-AudioRenderer-on(type: 'writeData', callback: AudioRendererWriteDataCallback): void--><!--Device-AudioRenderer-on(type: 'writeData', callback: AudioRendererWriteDataCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'writeData' | 是 |
| callback | [AudioRendererWriteDataCallback](arkts-audio-audio-audiorendererwritedatacallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

暂停音频渲染。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-pause(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-pause(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## pause

```TypeScript
pause(): Promise<void>
```

暂停音频渲染。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-pause(): Promise<void>--><!--Device-AudioRenderer-pause(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放音频渲染器。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-release(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## release

```TypeScript
release(): Promise<void>
```

释放音频渲染器。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-release(): Promise<void>--><!--Device-AudioRenderer-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setAudioEffectMode

```TypeScript
setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void
```

设置当前音效模式。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setAudioEffectMode

```TypeScript
setAudioEffectMode(mode: AudioEffectMode): Promise<void>
```

设置当前音效模式。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode): Promise<void>--><!--Device-AudioRenderer-setAudioEffectMode(mode: AudioEffectMode): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AudioEffectMode](arkts-audio-audio-audioeffectmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setChannelBlendMode

```TypeScript
setChannelBlendMode(mode: ChannelBlendMode): void
```

设置单双声道混合模式。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setChannelBlendMode(mode: ChannelBlendMode): void--><!--Device-AudioRenderer-setChannelBlendMode(mode: ChannelBlendMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [ChannelBlendMode](arkts-audio-audio-channelblendmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setDefaultOutputDevice

```TypeScript
setDefaultOutputDevice(deviceType: DeviceType): Promise<void>
```

设置默认发声设备。使用Promise异步回调。 > **说明：** > > - 本接口仅适用于[StreamUsage](arkts-audio-audio-streamusage-e.md#StreamUsage)为语音消息、VoIP语音通话或者VoIP视频通话的场景，支持听筒、扬声器和系统默认设备。 > > - 本接口允许在AudioRenderer创建后随时调用，系统会记录应用设置的默认本机内置发声设备。应用启动播放时，若外接设备如蓝牙耳机或有线耳机已接入，系统优先从外接设备发声；否则，系统遵循应用设置的默认本机内置发声设 > 备。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setDefaultOutputDevice(deviceType: DeviceType): Promise<void>--><!--Device-AudioRenderer-setDefaultOutputDevice(deviceType: DeviceType): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceType | [DeviceType](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-devicetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setIndependentAudioSessionStrategy

```TypeScript
setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: number): void
```

设置独立的音频会话策略和行为参数。 > **说明：** > > 当音频渲染器在运行状态时调用此接口后，必须重新调用接口[start](#start)使其生效。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRenderer-setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void--><!--Device-AudioRenderer-setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strategy | [AudioSessionStrategy](arkts-audio-audio-audiosessionstrategy-i.md) | 是 |
| behavior | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setInterruptMode

```TypeScript
setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void
```

设置应用的焦点模型。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [InterruptMode](arkts-audio-audio-interruptmode-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setInterruptMode

```TypeScript
setInterruptMode(mode: InterruptMode): Promise<void>
```

设置应用的焦点模型。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode): Promise<void>--><!--Device-AudioRenderer-setInterruptMode(mode: InterruptMode): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [InterruptMode](arkts-audio-audio-interruptmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setInterruptModeSync

```TypeScript
setInterruptModeSync(mode: InterruptMode): void
```

设置应用的焦点模型。同步设置。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setInterruptModeSync(mode: InterruptMode): void--><!--Device-AudioRenderer-setInterruptModeSync(mode: InterruptMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [InterruptMode](arkts-audio-audio-interruptmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setLoudnessGain

```TypeScript
setLoudnessGain(loudnessGain: number): Promise<void>
```

设置播放响度。使用Promise异步回调。 > **说明：** > > - 该接口仅支持类型为[STREAM_USAGE_MUSIC](arkts-audio-audio-streamusage-e.md#StreamUsage)、[STREAM_USAGE_MOVIE](arkts-audio-audio-streamusage-e.md#StreamUsage)或 > [STREAM_USAGE_AUDIOBOOK](arkts-audio-audio-streamusage-e.md#StreamUsage)的音频流。 > > - 该接口不支持高清通路的响度设置。 > > - 由于音频框架与硬件之间存在缓冲区，响度调节实际生效存在延迟，时长取决于缓冲区长度。 > > - 建议在不同音频开始播放前预先设置响度，以实现最佳均衡效果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setLoudnessGain(loudnessGain: double): Promise<void>--><!--Device-AudioRenderer-setLoudnessGain(loudnessGain: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loudnessGain | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## setRenderRate

```TypeScript
setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void
```

设置音频渲染速率。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** setSpeed

<!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rate | [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setRenderRate

```TypeScript
setRenderRate(rate: AudioRendererRate): Promise<void>
```

设置音频渲染速率。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** setSpeed

<!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate): Promise<void>--><!--Device-AudioRenderer-setRenderRate(rate: AudioRendererRate): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rate | [AudioRendererRate](arkts-audio-audio-audiorendererrate-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setSilentModeAndMixWithOthers

```TypeScript
setSilentModeAndMixWithOthers(on: boolean): void
```

设置静音并发播放模式。 当设置为true，打开静音并发播放模式，系统将让此音频流静音播放，并且不会打断其他音频流。设置为false，将关闭静音并发播放，音频流可根据系统焦点策略抢占焦点。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setSilentModeAndMixWithOthers(on: boolean): void--><!--Device-AudioRenderer-setSilentModeAndMixWithOthers(on: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| on | boolean | 是 |

## setSpeed

```TypeScript
setSpeed(speed: number): void
```

设置播放倍速。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setSpeed(speed: double): void--><!--Device-AudioRenderer-setSpeed(speed: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speed | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setVolume

```TypeScript
setVolume(volume: number, callback: AsyncCallback<void>): void
```

设置音频流的音量。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setVolume(volume: double, callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-setVolume(volume: double, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volume | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setVolume

```TypeScript
setVolume(volume: number): Promise<void>
```

设置音频流的音量。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setVolume(volume: double): Promise<void>--><!--Device-AudioRenderer-setVolume(volume: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volume | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setVolumeWithRamp

```TypeScript
setVolumeWithRamp(volume: number, duration: number): void
```

在指定时间范围内设置音量渐变模式。同步返回结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-setVolumeWithRamp(volume: double, duration: int): void--><!--Device-AudioRenderer-setVolumeWithRamp(volume: double, duration: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volume | number | 是 |
| duration | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

启动音频渲染器。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-start(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## start

```TypeScript
start(): Promise<void>
```

启动音频渲染器。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-start(): Promise<void>--><!--Device-AudioRenderer-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止音频渲染。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-stop(callback: AsyncCallback<void>): void--><!--Device-AudioRenderer-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## stop

```TypeScript
stop(): Promise<void>
```

停止音频渲染。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-stop(): Promise<void>--><!--Device-AudioRenderer-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## write

```TypeScript
write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void
```

写入缓冲区。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** writeData

<!--Device-AudioRenderer-write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void--><!--Device-AudioRenderer-write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## write

```TypeScript
write(buffer: ArrayBuffer): Promise<number>
```

写入缓冲区。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** writeData

<!--Device-AudioRenderer-write(buffer: ArrayBuffer): Promise<number>--><!--Device-AudioRenderer-write(buffer: ArrayBuffer): Promise<number>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## state

```TypeScript
readonly state: AudioState
```

音频渲染器的状态。

**类型：** AudioState

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioRenderer-readonly state: AudioState--><!--Device-AudioRenderer-readonly state: AudioState-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer
