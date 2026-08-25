# AudioVolumeGroupManager

管理音频组音量。在调用AudioVolumeGroupManager的接口前，需要先通过 [getVolumeGroupManager](arkts-audio-audio-audiovolumemanager-i.md#getvolumegroupmanager) 创建实例。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Audio.Volume

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## getMaxAmplitudeForInputDevice

```TypeScript
getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>
```

获取输入设备音频流的最大电平值，取值范围为[0, 1]。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inputDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## getMaxAmplitudeForOutputDevice

```TypeScript
getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<number>
```

获取输出设备音频流的最大电平值，取值范围为[0, 1]。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| outputDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

获取指定流的最大音量等级。使用callback异步回调。

> **说明：**
> 
> 从API version 9开始支持，从API version 20开始废弃，建议使用
> [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)替代。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType): Promise<number>
```

获取指定流的最大音量等级。使用Promise异步回调。

> **说明：**
> 
> 从API version 9开始支持，从API version 20开始废弃，建议使用
> [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)替代。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getMaxVolumeSync

```TypeScript
getMaxVolumeSync(volumeType: AudioVolumeType): number
```

获取指定流的最大音量等级。同步返回结果。

> **说明：**
> 
> 从API version 10开始支持，从API version 20开始废弃，建议使用
> [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)替代。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

获取指定流的最小音量等级。使用callback异步回调。

> **说明：**
> 
> 从API version 9开始支持，从API version 20开始废弃，建议使用
> [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)替代。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType): Promise<number>
```

获取指定流的最小音量等级。使用Promise异步回调。

> **说明：**
> 
> 从API version 9开始支持，从API version 20开始废弃，建议使用
> [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)替代。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getMinVolumeSync

```TypeScript
getMinVolumeSync(volumeType: AudioVolumeType): number
```

获取指定流的最小音量等级。同步返回结果。

> **说明：**
> 
> 从API version 10开始支持，从API version 20开始废弃，建议使用
> [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)替代。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## getRingerMode

```TypeScript
getRingerMode(callback: AsyncCallback<AudioRingMode>): void
```

获取铃声模式。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | 是 |

## getRingerMode

```TypeScript
getRingerMode(): Promise<AudioRingMode>
```

获取铃声模式。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; |

## getRingerModeSync

```TypeScript
getRingerModeSync(): AudioRingMode
```

获取铃声模式。同步返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 |
| --- |
| [AudioRingMode](arkts-audio-audio-audioringmode-e.md) |

## getSystemVolumeInDb

```TypeScript
getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void
```

获取音量增益dB值。使用callback异步回调。

> **说明：**
> 
> 从API version 10开始支持，从API version 20开始废弃，建议使用
> [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)
> 替代。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| [volumeLevel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md) | number | 是 |
| device | [DeviceType](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-devicetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## getSystemVolumeInDb

```TypeScript
getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>
```

获取音量增益dB值。使用Promise异步回调。

> **说明：**
> 
> 从API version 10开始支持，从API version 20开始废弃，建议使用
> [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)
> 替代。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| [volumeLevel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md) | number | 是 |
| device | [DeviceType](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-devicetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## getSystemVolumeInDbSync

```TypeScript
getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number
```

获取音量增益dB值。同步返回结果。

> **说明：**
> 
> 从API version 10开始支持，从API version 20开始废弃，建议使用
> [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)
> 替代。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| [volumeLevel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md) | number | 是 |
| device | [DeviceType](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-devicetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

获取指定流的音量等级。使用callback异步回调。

> **说明：**
> 
> 从API version 9开始支持，从API version 20开始废弃，建议使用
> [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)替代。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType): Promise<number>
```

获取指定流的音量等级。使用Promise异步回调。

> **说明：**
> 
> 从API version 9开始支持，从API version 20开始废弃，建议使用
> [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)替代。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getVolumeSync

```TypeScript
getVolumeSync(volumeType: AudioVolumeType): number
```

获取指定流的音量等级。同步返回结果。

> **说明：**
> 
> 从API version 10开始支持，从API version 20开始废弃，建议使用
> [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)替代。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(callback: AsyncCallback<boolean>): void
```

获取麦克风静音状态。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(): Promise<boolean>
```

获取麦克风静音状态。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isMicrophoneMuteSync

```TypeScript
isMicrophoneMuteSync(): boolean
```

获取麦克风静音状态。同步返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 |
| --- |
| boolean |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

获取指定音量流静音状态。使用callback异步回调。

> **说明：**
> 
> 从API version 9开始支持，从API version 20开始废弃，建议使用
> [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)替代。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType): Promise<boolean>
```

获取指定音量流是否被静音。使用Promise异步回调。

> **说明：**
> 
> 从API version 9开始支持，从API version 20开始废弃，建议使用
> [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)替代。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isMuteSync

```TypeScript
isMuteSync(volumeType: AudioVolumeType): boolean
```

获取指定音量流是否被静音。同步返回结果。

> **说明：**
> 
> 从API version 10开始支持，从API version 20开始废弃，建议使用
> [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)替代。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## isVolumeUnadjustable

```TypeScript
isVolumeUnadjustable(): boolean
```

获取固定音量模式开关状态，打开时进入固定音量模式，此时音量固定无法被调节。同步返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 |
| --- |
| boolean |

## off('ringerModeChange')

```TypeScript
off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void
```

取消监听铃声模式变化事件。使用callback异步回调。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'ringerModeChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('micStateChange')

```TypeScript
off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void
```

取消监听系统麦克风状态更改事件。使用callback异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'micStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('ringerModeChange')

```TypeScript
on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void
```

监听铃声模式变化事件（当[AudioRingMode](arkts-audio-audio-audioringmode-e.md)发生变化时触发）。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'ringerModeChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('micStateChange')

```TypeScript
on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void
```

监听系统麦克风状态更改事件（当检测到系统麦克风状态发生改变时触发）。使用callback异步回调。 目前此订阅接口在单进程多AudioManager实例的使用场景下，仅最后一个实例的订阅生效，其他实例的订阅会被覆盖（即使最后一个实例没有进行订阅）。因此，推荐使用单一AudioManager实例进行开发。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'micStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void
```

设置麦克风静音状态。使用callback异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mute | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean): Promise<void>
```

设置麦克风静音状态。使用Promise异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mute | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
