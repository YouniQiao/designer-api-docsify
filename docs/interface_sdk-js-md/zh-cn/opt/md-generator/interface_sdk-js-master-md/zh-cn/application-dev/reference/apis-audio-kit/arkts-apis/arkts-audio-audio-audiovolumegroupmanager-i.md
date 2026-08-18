# AudioVolumeGroupManager

管理音频组音量。 在使用AudioVolumeGroupManager的接口之前，需先通过 [getVolumeGroupManager](arkts-audio-audio-audiovolumemanager-i.md#getvolumegroupmanager) 获取AudioVolumeGroupManager实例。 > **说明：** > > - 本Interface首批接口从API version 9开始支持。

**起始版本：** 23

<!--Device-audio-interface AudioVolumeGroupManager--><!--Device-audio-interface AudioVolumeGroupManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

## 导入模块

```TypeScript
```

## getMaxAmplitudeForInputDevice

```TypeScript
getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>
```

获取输入设备音频流的最大电平值，取值范围为[0, 1]。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<double>--><!--Device-AudioVolumeGroupManager-getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<double>-End-->

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

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<double>--><!--Device-AudioVolumeGroupManager-getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<double>-End-->

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)

<!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void--><!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType): Promise<number>
```

获取指定流的最大音量等级。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)

<!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType): Promise<int>--><!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType): Promise<int>-End-->

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)

<!--Device-AudioVolumeGroupManager-getMaxVolumeSync(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeGroupManager-getMaxVolumeSync(volumeType: AudioVolumeType): int-End-->

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)

<!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void--><!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType): Promise<number>
```

获取指定流的最小音量等级。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)

<!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType): Promise<int>--><!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType): Promise<int>-End-->

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)

<!--Device-AudioVolumeGroupManager-getMinVolumeSync(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeGroupManager-getMinVolumeSync(volumeType: AudioVolumeType): int-End-->

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

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | 是 |

## getRingerMode

```TypeScript
getRingerMode(): Promise<AudioRingMode>
```

获取铃声模式。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-getRingerMode(): Promise<AudioRingMode>--><!--Device-AudioVolumeGroupManager-getRingerMode(): Promise<AudioRingMode>-End-->

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

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-getRingerModeSync(): AudioRingMode--><!--Device-AudioVolumeGroupManager-getRingerModeSync(): AudioRingMode-End-->

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)

<!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType, callback: AsyncCallback<double>): void--><!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType, callback: AsyncCallback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| [volumeLevel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md) | number | 是 |
| device | [DeviceType](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-devicetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)

<!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): Promise<double>--><!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): Promise<double>-End-->

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)

<!--Device-AudioVolumeGroupManager-getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double--><!--Device-AudioVolumeGroupManager-getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double-End-->

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)

<!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void--><!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType): Promise<number>
```

获取指定流的音量等级。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)

<!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType): Promise<int>--><!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType): Promise<int>-End-->

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)

<!--Device-AudioVolumeGroupManager-getVolumeSync(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeGroupManager-getVolumeSync(volumeType: AudioVolumeType): int-End-->

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

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void--><!--Device-AudioVolumeGroupManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(): Promise<boolean>
```

获取麦克风静音状态。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-isMicrophoneMute(): Promise<boolean>--><!--Device-AudioVolumeGroupManager-isMicrophoneMute(): Promise<boolean>-End-->

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

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-isMicrophoneMuteSync(): boolean--><!--Device-AudioVolumeGroupManager-isMicrophoneMuteSync(): boolean-End-->

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)

<!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType): Promise<boolean>
```

获取指定音量流是否被静音。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)

<!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType): Promise<boolean>-End-->

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

**起始版本：** 23

**废弃版本：** 20

**替代接口：** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)

<!--Device-AudioVolumeGroupManager-isMuteSync(volumeType: AudioVolumeType): boolean--><!--Device-AudioVolumeGroupManager-isMuteSync(volumeType: AudioVolumeType): boolean-End-->

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

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-isVolumeUnadjustable(): boolean--><!--Device-AudioVolumeGroupManager-isVolumeUnadjustable(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 |
| --- |
| boolean |

## offMicStateChange

```TypeScript
offMicStateChange(callback?: Callback<MicStateChangeEvent>): void
```

Unsubscribes to the microphone state change events.

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-offMicStateChange(callback?: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-offMicStateChange(callback?: Callback<MicStateChangeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## offRingerModeChange

```TypeScript
offRingerModeChange(callback?: Callback<AudioRingMode>): void
```

Unsubscribes to the ringer mode state change events.

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-offRingerModeChange(callback?: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-offRingerModeChange(callback?: Callback<AudioRingMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off_micStateChange

```TypeScript
off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void
```

取消监听系统麦克风状态更改事件。使用callback异步回调。

**起始版本：** 12

<!--Device-AudioVolumeGroupManager-off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'micStateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off_ringerModeChange

```TypeScript
off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void
```

取消监听铃声模式变化事件。使用callback异步回调。

**起始版本：** 18

<!--Device-AudioVolumeGroupManager-off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'ringerModeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## onMicStateChange

```TypeScript
onMicStateChange(callback: Callback<MicStateChangeEvent>): void
```

Listens for system microphone state change events. This method uses a callback to get microphone change events.

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-onMicStateChange(callback: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-onMicStateChange(callback: Callback<MicStateChangeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## onRingerModeChange

```TypeScript
onRingerModeChange(callback: Callback<AudioRingMode>): void
```

Listens for ringer mode change events. This method uses a callback to get ringer mode changes.

**起始版本：** 23

<!--Device-AudioVolumeGroupManager-onRingerModeChange(callback: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-onRingerModeChange(callback: Callback<AudioRingMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on_micStateChange

```TypeScript
on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void
```

监听系统麦克风状态更改事件（当检测到系统麦克风状态发生改变时触发）。使用callback异步回调。 目前此订阅接口在单进程多AudioManager实例的使用场景下，仅最后一个实例的订阅生效，其他实例的订阅会被覆盖（即使最后一个实例没有进行订阅）。因此，推荐使用单一AudioManager实例进行开发。

**起始版本：** 9

<!--Device-AudioVolumeGroupManager-on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'micStateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on_ringerModeChange

```TypeScript
on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void
```

监听铃声模式变化事件（当[AudioRingMode](arkts-audio-audio-audioringmode-e.md#audioringmode)发生变化时触发）。使用callback异步回调。

**起始版本：** 9

<!--Device-AudioVolumeGroupManager-on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'ringerModeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void
```

设置麦克风静音状态。使用callback异步回调。 > **说明：** > > 从API version 9开始支持，从API version 11开始废弃。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeGroupManager-setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioVolumeGroupManager-setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mute | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean): Promise<void>
```

设置麦克风静音状态。使用Promise异步回调。 > **说明：** > > 从API version 9开始支持，从API version 11开始废弃。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeGroupManager-setMicrophoneMute(mute: boolean): Promise<void>--><!--Device-AudioVolumeGroupManager-setMicrophoneMute(mute: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mute | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
