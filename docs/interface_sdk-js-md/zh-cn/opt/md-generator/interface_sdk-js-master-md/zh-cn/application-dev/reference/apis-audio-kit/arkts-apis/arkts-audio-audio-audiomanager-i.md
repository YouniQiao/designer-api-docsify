# AudioManager

音频音量和设备管理。 在使用AudioManager的接口之前，需先通过[getAudioManager](arkts-audio-audio-getaudiomanager-f.md#getaudiomanager)获取AudioManager实例。

**起始版本：** 23

<!--Device-audio-interface AudioManager--><!--Device-audio-interface AudioManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

## 导入模块

```TypeScript
```

## getAudioParameter

```TypeScript
getAudioParameter(key: string, callback: AsyncCallback<string>): void
```

获取指定音频参数值。使用callback异步回调。 本接口的使用场景为：根据硬件设备的支持能力扩展音频配置。在不同的设备平台上，所支持的音频参数会存在差异。示例代码内使用样例参数，实际支持的音频配置参数见具体设备平台的资料描述。 > **说明：** > > 从API version 7开始支持，从API version 11开始废弃。

**起始版本：** 7

**废弃版本：** 11

<!--Device-AudioManager-getAudioParameter(key: string, callback: AsyncCallback<string>): void--><!--Device-AudioManager-getAudioParameter(key: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getAudioParameter

```TypeScript
getAudioParameter(key: string): Promise<string>
```

获取指定音频参数值。使用Promise异步回调。 本接口的使用场景为：根据硬件设备的支持能力扩展音频配置。在不同的设备平台上，所支持的音频参数会存在差异。示例代码内使用样例参数，实际支持的音频配置参数见具体设备平台的资料描述。 > **说明：** > > 从API version 7开始支持，从API version 11开始废弃。

**起始版本：** 7

**废弃版本：** 11

<!--Device-AudioManager-getAudioParameter(key: string): Promise<string>--><!--Device-AudioManager-getAudioParameter(key: string): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getAudioScene

```TypeScript
getAudioScene(callback: AsyncCallback<AudioScene>): void
```

获取音频场景模式。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioManager-getAudioScene(callback: AsyncCallback<AudioScene>): void--><!--Device-AudioManager-getAudioScene(callback: AsyncCallback<AudioScene>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioScene](arkts-audio-audio-audioscene-e.md)&gt; | 是 |

## getAudioScene

```TypeScript
getAudioScene(): Promise<AudioScene>
```

获取音频场景模式。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioManager-getAudioScene(): Promise<AudioScene>--><!--Device-AudioManager-getAudioScene(): Promise<AudioScene>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioScene](arkts-audio-audio-audioscene-e.md)&gt; |

## getAudioSceneSync

```TypeScript
getAudioSceneSync(): AudioScene
```

获取音频场景模式。同步返回结果。

**起始版本：** 23

<!--Device-AudioManager-getAudioSceneSync(): AudioScene--><!--Device-AudioManager-getAudioSceneSync(): AudioScene-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**返回值：**

| 类型 |
| --- |
| [AudioScene](arkts-audio-audio-audioscene-e.md) |

## getDebuggingManager

```TypeScript
getDebuggingManager(): AudioDebuggingManager
```

获取音频调试管理器实例。该实例为单例，获取后可重复使用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioManager-getDebuggingManager(): AudioDebuggingManager--><!--Device-AudioManager-getDebuggingManager(): AudioDebuggingManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 |
| --- |
| [AudioDebuggingManager](arkts-audio-audio-audiodebuggingmanager-i.md) |

## getDeviceEnhanceManager

```TypeScript
getDeviceEnhanceManager(): AudioDeviceEnhanceManager
```

获取音频设备增强管理器实例。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioManager-getDeviceEnhanceManager(): AudioDeviceEnhanceManager--><!--Device-AudioManager-getDeviceEnhanceManager(): AudioDeviceEnhanceManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.DeviceEnhance

**返回值：**

| 类型 |
| --- |
| [AudioDeviceEnhanceManager](arkts-audio-audio-audiodeviceenhancemanager-i.md) |

## getDevices

```TypeScript
getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void
```

获取音频设备列表。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getDevices

<!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void--><!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-audio-audio-deviceflag-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | 是 |

## getDevices

```TypeScript
getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>
```

获取音频设备列表。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getDevices

<!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>--><!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-audio-audio-deviceflag-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

获取指定流的最大音量等级。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getMaxVolume

<!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void--><!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void-End-->

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

获取指定流的最大音量等级。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getMaxVolume

<!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType): Promise<number>--><!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType): Promise<number>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

获取指定流的最小音量等级。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getMinVolume

<!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void--><!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void-End-->

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

获取指定流的最小音量等级。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getMinVolume

<!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType): Promise<number>--><!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType): Promise<number>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getRingerMode

```TypeScript
getRingerMode(callback: AsyncCallback<AudioRingMode>): void
```

获取铃声模式。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getRingerMode

<!--Device-AudioManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void--><!--Device-AudioManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | 是 |

## getRingerMode

```TypeScript
getRingerMode(): Promise<AudioRingMode>
```

获取铃声模式。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getRingerMode

<!--Device-AudioManager-getRingerMode(): Promise<AudioRingMode>--><!--Device-AudioManager-getRingerMode(): Promise<AudioRingMode>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; |

## getRoutingManager

```TypeScript
getRoutingManager(): AudioRoutingManager
```

获取音频路由管理器。

**起始版本：** 23

<!--Device-AudioManager-getRoutingManager(): AudioRoutingManager--><!--Device-AudioManager-getRoutingManager(): AudioRoutingManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 |
| --- |
| [AudioRoutingManager](arkts-audio-audio-audioroutingmanager-i.md) |

## getSessionManager

```TypeScript
getSessionManager(): AudioSessionManager
```

获取音频会话管理器。

**起始版本：** 23

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AudioManager-getSessionManager(): AudioSessionManager--><!--Device-AudioManager-getSessionManager(): AudioSessionManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 |
| --- |
| [AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md) |

## getSpatializationManager

```TypeScript
getSpatializationManager(): AudioSpatializationManager
```

获取空间音频管理器。

**起始版本：** 23

<!--Device-AudioManager-getSpatializationManager(): AudioSpatializationManager--><!--Device-AudioManager-getSpatializationManager(): AudioSpatializationManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**返回值：**

| 类型 |
| --- |
| [AudioSpatializationManager](arkts-audio-audio-audiospatializationmanager-i.md) |

## getStreamManager

```TypeScript
getStreamManager(): AudioStreamManager
```

获取音频流管理器。

**起始版本：** 23

<!--Device-AudioManager-getStreamManager(): AudioStreamManager--><!--Device-AudioManager-getStreamManager(): AudioStreamManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 |
| --- |
| [AudioStreamManager](arkts-audio-audio-audiostreammanager-i.md) |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

获取指定流的音量等级。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getVolume

<!--Device-AudioManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void--><!--Device-AudioManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void-End-->

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

获取指定流的音量等级。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getVolume

<!--Device-AudioManager-getVolume(volumeType: AudioVolumeType): Promise<number>--><!--Device-AudioManager-getVolume(volumeType: AudioVolumeType): Promise<number>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getVolumeManager

```TypeScript
getVolumeManager(): AudioVolumeManager
```

获取音频音量管理器。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AudioManager-getVolumeManager(): AudioVolumeManager--><!--Device-AudioManager-getVolumeManager(): AudioVolumeManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 |
| --- |
| [AudioVolumeManager](arkts-audio-audio-audiovolumemanager-i.md) |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

获取指定音量流的活跃状态。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**起始版本：** 7

**废弃版本：** 9

**替代接口：** isActive

<!--Device-AudioManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType): Promise<boolean>
```

获取指定音量流的活跃状态。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**起始版本：** 7

**废弃版本：** 9

**替代接口：** isActive

<!--Device-AudioManager-isActive(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioManager-isActive(volumeType: AudioVolumeType): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isDeviceActive

```TypeScript
isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void
```

获取指定设备的激活状态。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isCommunicationDeviceActive](arkts-audio-audio-audioroutingmanager-i.md#iscommunicationdeviceactive)

<!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isDeviceActive

```TypeScript
isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>
```

获取指定设备的激活状态。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isCommunicationDeviceActive](arkts-audio-audio-audioroutingmanager-i.md#iscommunicationdeviceactive)

<!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>--><!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(callback: AsyncCallback<boolean>): void
```

获取麦克风静音状态。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** isMicrophoneMute

**需要权限：** ohos.permission.MICROPHONE

<!--Device-AudioManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(): Promise<boolean>
```

获取麦克风静音状态。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** isMicrophoneMute

**需要权限：** ohos.permission.MICROPHONE

<!--Device-AudioManager-isMicrophoneMute(): Promise<boolean>--><!--Device-AudioManager-isMicrophoneMute(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

获取指定音量流的静音状态。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**起始版本：** 7

**废弃版本：** 9

**替代接口：** isMute

<!--Device-AudioManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

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

获取指定音量流的静音状态。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**起始版本：** 7

**废弃版本：** 9

**替代接口：** isMute

<!--Device-AudioManager-isMute(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioManager-isMute(volumeType: AudioVolumeType): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## mute

```TypeScript
mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void
```

设置指定音量流静音。使用callback异步回调。 当该音量流可设置的最小音量不能为0时，不支持静音操作。例如：闹钟和通话。 > **说明：** > > - 从API version 7开始支持，从API version 9开始废弃。 > > - 应用无法直接静音流音量，建议通过系统音量面板组件进行静音。具体样例和介绍请参考API文档 > @ohos.multimedia.avVolumePanel (音量面板)。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [AVVolumePanel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md#avvolumepanel)

<!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| [mute](#mute) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## mute

```TypeScript
mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>
```

设置指定音量流静音。使用Promise异步回调。 当该音量流可设置的最小音量不能为0时，不支持静音操作。例如：闹钟和通话。 > **说明：** > > - 从API version 7开始支持，从API version 9开始废弃。 > > - 应用无法直接静音流音量，建议通过系统音量面板组件进行静音。具体样例和介绍请参考API文档 > @ohos.multimedia.avVolumePanel (音量面板)。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [AVVolumePanel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md#avvolumepanel)

<!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>--><!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| [mute](#mute) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## offAudioSceneChange

```TypeScript
offAudioSceneChange(callback?: Callback<AudioScene>): void
```

Unsubscribes to audio scene change events.

**起始版本：** 23

<!--Device-AudioManager-offAudioSceneChange(callback?: Callback<AudioScene>): void--><!--Device-AudioManager-offAudioSceneChange(callback?: Callback<AudioScene>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioScene](arkts-audio-audio-audioscene-e.md)&gt; | 否 |

## off_audioSceneChange

```TypeScript
off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void
```

取消监听音频场景变化事件。使用callback异步回调。

**起始版本：** 20

<!--Device-AudioManager-off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void--><!--Device-AudioManager-off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioSceneChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioScene](arkts-audio-audio-audioscene-e.md)&gt; | 否 |

## off_deviceChange

```TypeScript
off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void
```

取消监听音频设备连接变化事件。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** deviceChange

<!--Device-AudioManager-off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void--><!--Device-AudioManager-off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | 否 |

## off_interrupt

```TypeScript
off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void
```

取消监听音频打断事件。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** audioInterrupt

<!--Device-AudioManager-off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void--><!--Device-AudioManager-off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'interrupt' | 是 |
| interrupt | [AudioInterrupt](arkts-audio-audio-audiointerrupt-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptAction](arkts-audio-audio-interruptaction-i.md)&gt; | 否 |

## onAudioSceneChange

```TypeScript
onAudioSceneChange(callback: Callback<AudioScene>): void
```

Subscribes to audio scene change events. When system changes communication scene status, registered clients will receive the callback.

**起始版本：** 23

<!--Device-AudioManager-onAudioSceneChange(callback: Callback<AudioScene>): void--><!--Device-AudioManager-onAudioSceneChange(callback: Callback<AudioScene>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioScene](arkts-audio-audio-audioscene-e.md)&gt; | 是 |

## on_audioSceneChange

```TypeScript
on(type: 'audioSceneChange', callback: Callback<AudioScene>): void
```

监听音频场景变化事件。使用callback异步回调。

**起始版本：** 20

<!--Device-AudioManager-on(type: 'audioSceneChange', callback: Callback<AudioScene>): void--><!--Device-AudioManager-on(type: 'audioSceneChange', callback: Callback<AudioScene>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioSceneChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioScene](arkts-audio-audio-audioscene-e.md)&gt; | 是 |

## on_deviceChange

```TypeScript
on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void
```

监听音频设备连接变化事件（当音频设备连接状态发生变化时触发）。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** deviceChange

<!--Device-AudioManager-on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void--><!--Device-AudioManager-on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | 是 |

## on_interrupt

```TypeScript
on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void
```

监听音频打断事件（当音频焦点发生变化时触发）。使用callback异步回调。 与[on('audioInterrupt')](arkts-audio-audio-audiorenderer-i.md#onaudiointerrupt) 作用一致，均用于监听焦点变化。为无音频流的场景（未曾创建AudioRenderer对象），比如FM、语音唤醒等提供焦点变化监听功能。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** audioInterrupt

<!--Device-AudioManager-on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void--><!--Device-AudioManager-on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'interrupt' | 是 |
| interrupt | [AudioInterrupt](arkts-audio-audio-audiointerrupt-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterruptAction](arkts-audio-audio-interruptaction-i.md)&gt; | 是 |

## setAudioParameter

```TypeScript
setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void
```

音频参数设置。使用callback异步回调。 接口根据硬件设备的支持能力扩展音频配置。支持的参数与产品和设备强相关，非通用参数，示例代码内使用样例参数。 > **说明：** > > 从API version 7开始支持，从API version 11开始废弃。

**起始版本：** 7

**废弃版本：** 11

**需要权限：** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioManager-setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setAudioParameter

```TypeScript
setAudioParameter(key: string, value: string): Promise<void>
```

音频参数设置。使用Promise异步回调。 接口根据硬件设备的支持能力扩展音频配置。支持的参数与产品和设备强相关，非通用参数，示例代码内使用样例参数。 > **说明：** > > 从API version 7开始支持，从API version 11开始废弃。

**起始版本：** 7

**废弃版本：** 11

**需要权限：** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioManager-setAudioParameter(key: string, value: string): Promise<void>--><!--Device-AudioManager-setAudioParameter(key: string, value: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setDeviceActive

```TypeScript
setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void
```

设置设备激活状态。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCommunicationDevice](arkts-audio-audio-audioroutingmanager-i.md#setcommunicationdevice)

<!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | 是 |
| active | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setDeviceActive

```TypeScript
setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>
```

设置设备激活状态。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCommunicationDevice](arkts-audio-audio-audioroutingmanager-i.md#setcommunicationdevice)

<!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>--><!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | 是 |
| active | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void
```

设置麦克风静音状态。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MICROPHONE

<!--Device-AudioManager-setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [mute](#mute) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean): Promise<void>
```

设置麦克风静音状态。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MICROPHONE

<!--Device-AudioManager-setMicrophoneMute(mute: boolean): Promise<void>--><!--Device-AudioManager-setMicrophoneMute(mute: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [mute](#mute) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setRingerMode

```TypeScript
setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void
```

设置铃声模式。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AudioRingMode](arkts-audio-audio-audioringmode-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setRingerMode

```TypeScript
setRingerMode(mode: AudioRingMode): Promise<void>
```

设置铃声模式。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setRingerMode(mode: AudioRingMode): Promise<void>--><!--Device-AudioManager-setRingerMode(mode: AudioRingMode): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AudioRingMode](arkts-audio-audio-audioringmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setVolume

```TypeScript
setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void
```

设置指定流的音量等级。使用callback异步回调。 > **说明：** > > - 从API version 7开始支持，从API version 9开始废弃。 > > - 应用无法直接调节系统音量，建议通过系统音量面板组件调节音量。具体样例和介绍请参考API文档 > @ohos.multimedia.avVolumePanel (音量面板)。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [AVVolumePanel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md#avvolumepanel)

**需要权限：** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| volume | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setVolume

```TypeScript
setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>
```

设置指定流的音量等级。使用Promise异步回调。 > **说明：** > > - 从API version 7开始支持，从API version 9开始废弃。 > > - 应用无法直接调节系统音量，建议通过系统音量面板组件调节音量。具体样例和介绍请参考API文档 > @ohos.multimedia.avVolumePanel (音量面板)。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [AVVolumePanel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md#avvolumepanel)

**需要权限：** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>--><!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| volume | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
