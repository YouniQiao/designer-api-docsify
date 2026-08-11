# AudioVolumeManager

音量管理。

在使用AudioVolumeManager的接口之前，需先通过[getVolumeManager](arkts-audio-audio-audiomanager-i.md#getvolumemanager)获取AudioVolumeManager实例。

> **说明：**
> 
> - 本Interface首批接口从API version 9开始支持。

**起始版本：** 9

<!--Device-audio-interface AudioVolumeManager--><!--Device-audio-interface AudioVolumeManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

## getAppVolumePercentage

```TypeScript
getAppVolumePercentage(): Promise<number>
```

获取应用的音量（范围为[0, 100]）。使用Promise异步回调。

**起始版本：** 19

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AudioVolumeManager-getAppVolumePercentage(): Promise<int>--><!--Device-AudioVolumeManager-getAppVolumePercentage(): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

## getMaxVolumeByStream

```TypeScript
getMaxVolumeByStream(streamUsage: StreamUsage): number
```

获取指定音频流的最大音量。

**起始版本：** 20

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AudioVolumeManager-getMaxVolumeByStream(streamUsage: StreamUsage): int--><!--Device-AudioVolumeManager-getMaxVolumeByStream(streamUsage: StreamUsage): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## getMinVolumeByStream

```TypeScript
getMinVolumeByStream(streamUsage: StreamUsage): number
```

获取指定音频流的最小音量。

**起始版本：** 20

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AudioVolumeManager-getMinVolumeByStream(streamUsage: StreamUsage): int--><!--Device-AudioVolumeManager-getMinVolumeByStream(streamUsage: StreamUsage): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## getVolumeByStream

```TypeScript
getVolumeByStream(streamUsage: StreamUsage): number
```

获取指定音频流的音量。

**起始版本：** 20

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AudioVolumeManager-getVolumeByStream(streamUsage: StreamUsage): int--><!--Device-AudioVolumeManager-getVolumeByStream(streamUsage: StreamUsage): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## getVolumeGroupManager

```TypeScript
getVolumeGroupManager(groupId: number, callback: AsyncCallback<AudioVolumeGroupManager>): void
```

获取音频组音量管理器实例。使用callback异步回调。

**起始版本：** 9

<!--Device-AudioVolumeManager-getVolumeGroupManager(groupId: int, callback: AsyncCallback<AudioVolumeGroupManager>): void--><!--Device-AudioVolumeManager-getVolumeGroupManager(groupId: int, callback: AsyncCallback<AudioVolumeGroupManager>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| groupId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioVolumeGroupManager&gt; | 是 |

## getVolumeGroupManager

```TypeScript
getVolumeGroupManager(groupId: number): Promise<AudioVolumeGroupManager>
```

获取音频组音量管理器实例。使用Promise异步回调。

**起始版本：** 9

<!--Device-AudioVolumeManager-getVolumeGroupManager(groupId: int): Promise<AudioVolumeGroupManager>--><!--Device-AudioVolumeManager-getVolumeGroupManager(groupId: int): Promise<AudioVolumeGroupManager>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| groupId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;AudioVolumeGroupManager&gt; |

## getVolumeGroupManagerSync

```TypeScript
getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager
```

获取音频组音量管理器实例。同步返回结果。

**起始版本：** 10

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AudioVolumeManager-getVolumeGroupManagerSync(groupId: int): AudioVolumeGroupManager--><!--Device-AudioVolumeManager-getVolumeGroupManagerSync(groupId: int): AudioVolumeGroupManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| groupId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [AudioVolumeGroupManager](arkts-audio-audio-audiovolumegroupmanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## getVolumeInUnitOfDbByStream

```TypeScript
getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: number, device: DeviceType): number
```

获取系统通过音频流、音量等级和设备类型计算出的音量dB值。

**起始版本：** 20

<!--Device-AudioVolumeManager-getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: int, device: DeviceType): double--><!--Device-AudioVolumeManager-getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: int, device: DeviceType): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |
| volumeLevel | number | 是 |
| device | [DeviceType](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-devicetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## isSystemMutedForStream

```TypeScript
isSystemMutedForStream(streamUsage: StreamUsage): boolean
```

检查指定音频流是否静音。

**起始版本：** 20

<!--Device-AudioVolumeManager-isSystemMutedForStream(streamUsage: StreamUsage): boolean--><!--Device-AudioVolumeManager-isSystemMutedForStream(streamUsage: StreamUsage): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('volumeChange')

```TypeScript
off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void
```

取消监听系统音量变化事件。使用callback异步回调。

**起始版本：** 12

**废弃版本：** 20

**替代接口：** ohos.multimedia.audio.AudioVolumeManager#event:streamVolumeChange

<!--Device-AudioVolumeManager-off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'volumeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VolumeEvent&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('appVolumeChange')

```TypeScript
off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void
```

取消监听当前应用的应用级音量变化事件。使用callback异步回调。

**起始版本：** 19

<!--Device-AudioVolumeManager-off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'appVolumeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VolumeEvent&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('streamVolumeChange')

```TypeScript
off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void
```

取消监听系统音频流音量变化事件（当系统音频流音量发生变化时触发）。使用callback异步回调。

**起始版本：** 20

<!--Device-AudioVolumeManager-off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void--><!--Device-AudioVolumeManager-off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'streamVolumeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StreamVolumeEvent&gt; | 否 |

## on('volumeChange')

```TypeScript
on(type: 'volumeChange', callback: Callback<VolumeEvent>): void
```

监听系统音量变化事件（当系统音量发生变化时触发）。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** ohos.multimedia.audio.AudioVolumeManager#event:streamVolumeChange

<!--Device-AudioVolumeManager-on(type: 'volumeChange', callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-on(type: 'volumeChange', callback: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'volumeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VolumeEvent&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('appVolumeChange')

```TypeScript
on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void
```

监听当前应用的应用级音量变化事件（当应用级音量发生变化时触发）。使用callback异步回调。

**起始版本：** 19

<!--Device-AudioVolumeManager-on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'appVolumeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VolumeEvent&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('streamVolumeChange')

```TypeScript
on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void
```

监听系统音频流音量变化事件（当系统音频流音量发生变化时触发）。使用callback异步回调。

**起始版本：** 20

<!--Device-AudioVolumeManager-on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void--><!--Device-AudioVolumeManager-on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'streamVolumeChange' | 是 |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StreamVolumeEvent&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setAppVolumePercentage

```TypeScript
setAppVolumePercentage(volume: number): Promise<void>
```

设置应用的音量（范围为[0, 100]）。使用Promise异步回调。

**起始版本：** 19

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AudioVolumeManager-setAppVolumePercentage(volume: int): Promise<void>--><!--Device-AudioVolumeManager-setAppVolumePercentage(volume: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volume | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |
