# AudioSpatializationManager

空间音频管理。在使用AudioSpatializationManager的接口前，需要使用 [getSpatializationManager](arkts-audio-audio-audiomanager-i.md#getspatializationmanager)获取 AudioSpatializationManager实例。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## downloadPersonalizedHRTF

```TypeScript
downloadPersonalizedHRTF(hrtfDescriptor: AudioHRTFAnonymousDescriptor): Promise<void>
```

从匿名文件描述符下载个性化HRTF数据。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hrtfDescriptor | [AudioHRTFAnonymousDescriptor](arkts-audio-audio-audiohrtfanonymousdescriptor-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800105](../errorcode-audio.md#6800105-处理超时) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## getCurrentSpatialAudioSourceType

```TypeScript
getCurrentSpatialAudioSourceType(): SpatialAudioSourceType
```

获取当前空间音频源类型。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [SpatialAudioSourceType](arkts-audio-audio-spatialaudiosourcetype-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSpatializationSceneType

```TypeScript
getSpatializationSceneType(): AudioSpatializationSceneType
```

查询当前空间音频渲染场景类型，同步返回结果。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [AudioSpatializationSceneType](arkts-audio-audio-audiospatializationscenetype-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isAdaptiveSpatialRenderingEnabled

```TypeScript
isAdaptiveSpatialRenderingEnabled(deviceDescriptor: AudioDeviceDescriptor): boolean
```

检查指定设备是否启用了自适应空间渲染。

**起始版本：** 24

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## isHeadTrackingEnabled

```TypeScript
isHeadTrackingEnabled(): boolean
```

获取头动跟踪是否开启，同步返回结果。

> **说明：**
> 
> 从 API version 11 开始支持，从 API version 12 开始废弃，建议使用
> [isHeadTrackingEnabled(deviceDescriptor: AudioDeviceDescriptor): boolean](#isheadtrackingenabled)
> 替代。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [isHeadTrackingEnabled](#isheadtrackingenabled)

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isHeadTrackingEnabled

```TypeScript
isHeadTrackingEnabled(deviceDescriptor: AudioDeviceDescriptor): boolean
```

获取指定设备的头动跟踪是否开启，同步返回结果。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## isHeadTrackingSupported

```TypeScript
isHeadTrackingSupported(): boolean
```

获取系统是否支持头动跟踪，同步返回结果。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isHeadTrackingSupportedForDevice

```TypeScript
isHeadTrackingSupportedForDevice(deviceDescriptor: AudioDeviceDescriptor): boolean
```

获取指定设备是否支持头动跟踪，同步返回结果。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## isPersonalizedSpatializationEnabled

```TypeScript
isPersonalizedSpatializationEnabled(selectedAudioDevice: AudioDeviceDescriptor): boolean
```

检查指定设备是否启用了个性化空间化功能。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| selectedAudioDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## isPersonalizedSpatializationSupported

```TypeScript
isPersonalizedSpatializationSupported(): boolean
```

检查系统是否支持个性化空间化。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isSpatializationEnabled

```TypeScript
isSpatializationEnabled(): boolean
```

获取空间音频渲染是否开启，同步返回结果。

> **说明：**
> 
> 从 API version 11 开始支持，从 API version 12 开始废弃，建议使用
> [isSpatializationEnabled(deviceDescriptor: AudioDeviceDescriptor): boolean](#isspatializationenabled)
> 替代。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [isSpatializationEnabled](#isspatializationenabled)

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isSpatializationEnabled

```TypeScript
isSpatializationEnabled(deviceDescriptor: AudioDeviceDescriptor): boolean
```

获取指定设备的空间音频渲染是否开启，同步返回结果。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## isSpatializationSupported

```TypeScript
isSpatializationSupported(): boolean
```

获取系统是否支持空间音频，同步返回结果。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isSpatializationSupportedForDevice

```TypeScript
isSpatializationSupportedForDevice(deviceDescriptor: AudioDeviceDescriptor): boolean
```

获取指定设备是否支持空间音频，同步返回结果。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('spatializationEnabledChange')

```TypeScript
off(type: 'spatializationEnabledChange', callback?: Callback<boolean>): void
```

取消监听空间音频渲染开关状态变化事件。使用callback异步回调。

> **说明：**
> 
> 从 API version 11 开始支持，从 API version 12 开始废弃，建议使用
> [off('spatializationEnabledChangeForAnyDevice')](#offspatializationenabledchangeforanydevice)
> 替代。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** off

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'spatializationEnabledChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('spatializationEnabledChangeForAnyDevice')

```TypeScript
off(type: 'spatializationEnabledChangeForAnyDevice', callback?: Callback<AudioSpatialEnabledStateForDevice>): void
```

取消监听空间音频渲染开关状态变化事件。使用callback异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'spatializationEnabledChangeForAnyDevice' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSpatialEnabledStateForDevice](arkts-audio-audio-audiospatialenabledstatefordevice-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('headTrackingEnabledChange')

```TypeScript
off(type: 'headTrackingEnabledChange', callback?: Callback<boolean>): void
```

取消监听头动跟踪开关状态变化事件。使用callback异步回调。

> **说明：**
> 
> 从 API version 11 开始支持，从 API version 12 开始废弃，建议使用
> [off('headTrackingEnabledChangeForAnyDevice')](#offheadtrackingenabledchangeforanydevice)
> 替代。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** off

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'headTrackingEnabledChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('headTrackingEnabledChangeForAnyDevice')

```TypeScript
off(type: 'headTrackingEnabledChangeForAnyDevice', callback?: Callback<AudioSpatialEnabledStateForDevice>): void
```

取消监听头动跟踪开关状态变化事件。使用callback异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'headTrackingEnabledChangeForAnyDevice' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSpatialEnabledStateForDevice](arkts-audio-audio-audiospatialenabledstatefordevice-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## offAdaptiveSpatialRenderingEnabledChangeForAnyDevice

```TypeScript
offAdaptiveSpatialRenderingEnabledChangeForAnyDevice(callback?: Callback<AudioSpatialEnabledStateForDevice>): void
```

取消订阅指定设备的自适应空间渲染启用状态变更事件。

**起始版本：** 24

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSpatialEnabledStateForDevice](arkts-audio-audio-audiospatialenabledstatefordevice-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## offPersonalizedSpatializationEnabledChangeForAnyDevice

```TypeScript
offPersonalizedSpatializationEnabledChangeForAnyDevice(
      callback?: Callback<AudioPersonalizedSpatialEnabledChangeForAnyDevice>): void
```

取消订阅由指定设备触发的个性化空间化状态变更事件。当状态发生变化时，已注册的客户端将收到回调通知。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioPersonalizedSpatialEnabledChangeForAnyDevice](arkts-audio-audio-audiopersonalizedspatialenabledchangeforanydevice-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## offSpatialAudioSourceTypeChange

```TypeScript
offSpatialAudioSourceTypeChange(callback?: Callback<SpatialAudioSourceType>): void
```

取消订阅空间音频源类型更改事件。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SpatialAudioSourceType](arkts-audio-audio-spatialaudiosourcetype-e-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('spatializationEnabledChange')

```TypeScript
on(type: 'spatializationEnabledChange', callback: Callback<boolean>): void
```

监听空间音频渲染开关状态变化事件（当空间音频渲染开关状态发生变化时触发）。使用callback异步回调。

> **说明：**
> 
> 从 API version 11 开始支持，从 API version 12 开始废弃，建议使用
> [on(type: 'spatializationEnabledChangeForAnyDevice', callback: Callback&lt;AudioSpatialEnabledStateForDevice\&gt;): void](#onspatializationenabledchangeforanydevice)
> 替代。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** on

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'spatializationEnabledChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('spatializationEnabledChangeForAnyDevice')

```TypeScript
on(type: 'spatializationEnabledChangeForAnyDevice', callback: Callback<AudioSpatialEnabledStateForDevice>): void
```

监听空间音频渲染开关状态变化事件（当空间音频渲染开关状态发生变化时触发）。使用callback异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'spatializationEnabledChangeForAnyDevice' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSpatialEnabledStateForDevice](arkts-audio-audio-audiospatialenabledstatefordevice-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('headTrackingEnabledChange')

```TypeScript
on(type: 'headTrackingEnabledChange', callback: Callback<boolean>): void
```

监听头动跟踪开关状态变化事件（当动跟踪开关状态发生变化时触发）。使用callback异步回调。

> **说明：**
> 
> 从 API version 11 开始支持，从 API version 12 开始废弃，建议使用
> [on(type: 'headTrackingEnabledChangeForAnyDevice', callback: Callback&lt;AudioSpatialEnabledStateForDevice\&gt;): void](#onheadtrackingenabledchangeforanydevice)
> 替代。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** on

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'headTrackingEnabledChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('headTrackingEnabledChangeForAnyDevice')

```TypeScript
on(type: 'headTrackingEnabledChangeForAnyDevice', callback: Callback<AudioSpatialEnabledStateForDevice>): void
```

监听头动跟踪开关状态变化事件（当动跟踪开关状态发生变化时触发）。使用callback异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'headTrackingEnabledChangeForAnyDevice' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSpatialEnabledStateForDevice](arkts-audio-audio-audiospatialenabledstatefordevice-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## onAdaptiveSpatialRenderingEnabledChangeForAnyDevice

```TypeScript
onAdaptiveSpatialRenderingEnabledChangeForAnyDevice(callback: Callback<AudioSpatialEnabledStateForDevice>): void
```

订阅指定设备的自适应空间渲染启用状态变更事件。当自适应空间渲染启用状态发生变化时，已注册的客户端将收到回调。

**起始版本：** 24

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSpatialEnabledStateForDevice](arkts-audio-audio-audiospatialenabledstatefordevice-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## onPersonalizedSpatializationEnabledChangeForAnyDevice

```TypeScript
onPersonalizedSpatializationEnabledChangeForAnyDevice(
      callback: Callback<AudioPersonalizedSpatialEnabledChangeForAnyDevice>): void
```

订阅由指定设备触发的个性化空间化状态变更事件。当状态发生变化时，已注册的客户端将收到回调通知。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioPersonalizedSpatialEnabledChangeForAnyDevice](arkts-audio-audio-audiopersonalizedspatialenabledchangeforanydevice-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onSpatialAudioSourceTypeChange

```TypeScript
onSpatialAudioSourceTypeChange(callback: Callback<SpatialAudioSourceType>): void
```

订阅空间音频源类型更改事件。当当前空间音频源类型发生变化时，注册的客户端将收到回调通知。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SpatialAudioSourceType](arkts-audio-audio-spatialaudiosourcetype-e-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setAdaptiveSpatialRenderingEnabled

```TypeScript
setAdaptiveSpatialRenderingEnabled(deviceDescriptor: AudioDeviceDescriptor, enabled: boolean): Promise<void>
```

设置指定设备是否启用自适应空间渲染。 该方法使用 Promise 返回结果。 当启用自适应空间渲染时，空间音频渲染将不会对立体声音频生效。

**起始版本：** 24

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setHeadTrackingEnabled

```TypeScript
setHeadTrackingEnabled(enable: boolean, callback: AsyncCallback<void>): void
```

根据输入指令，开启/关闭头动跟踪效果。使用callback异步回调。

> **说明：**
> 
> 从 API version 11 开始支持，从 API version 12 开始废弃，建议使用
> [setHeadTrackingEnabled(deviceDescriptor: AudioDeviceDescriptor, enabled: boolean): Promise\&lt;void&gt;](#setheadtrackingenabled)
> 替代。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [setHeadTrackingEnabled](#setheadtrackingenabled)

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setHeadTrackingEnabled

```TypeScript
setHeadTrackingEnabled(enable: boolean): Promise<void>
```

根据输入指令，开启/关闭头动跟踪效果。使用Promise异步回调。

> **说明：**
> 
> 从 API version 11 开始支持，从 API version 12 开始废弃，建议使用
> [setHeadTrackingEnabled(deviceDescriptor: AudioDeviceDescriptor, enabled: boolean): Promise\&lt;void&gt;](#setheadtrackingenabled)
> 替代。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [setHeadTrackingEnabled](#setheadtrackingenabled)

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setHeadTrackingEnabled

```TypeScript
setHeadTrackingEnabled(deviceDescriptor: AudioDeviceDescriptor, enabled: boolean): Promise<void>
```

根据输入指令，开启/关闭指定设备的头动跟踪效果。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setPersonalizedSpatializationEnabled

```TypeScript
setPersonalizedSpatializationEnabled(selectedAudioDevice: AudioDeviceDescriptor,
      enable: boolean): Promise<void>
```

设置指定设备是否启用个性化空间化。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| selectedAudioDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## setSpatializationEnabled

```TypeScript
setSpatializationEnabled(enable: boolean, callback: AsyncCallback<void>): void
```

根据输入指令，开启/关闭空间音频渲染效果。使用callback异步回调。

> **说明：**
> 
> 从 API version 11 开始支持，从 API version 12 开始废弃，建议使用
> [setSpatializationEnabled(deviceDescriptor: AudioDeviceDescriptor, enabled: boolean): Promise\&lt;void&gt;](#setspatializationenabled)
> 替代。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [setSpatializationEnabled](#setspatializationenabled)

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setSpatializationEnabled

```TypeScript
setSpatializationEnabled(enable: boolean): Promise<void>
```

根据输入指令，开启/关闭空间音频渲染效果。使用Promise异步回调。

> **说明：**
> 
> 从 API version 11 开始支持，从 API version 12 开始废弃，建议使用
> [setSpatializationEnabled(deviceDescriptor: AudioDeviceDescriptor, enabled: boolean): Promise\&lt;void&gt;](#setspatializationenabled)
> 替代。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [setSpatializationEnabled](#setspatializationenabled)

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setSpatializationEnabled

```TypeScript
setSpatializationEnabled(deviceDescriptor: AudioDeviceDescriptor, enabled: boolean): Promise<void>
```

根据输入指令，开启/关闭指定设备的空间音频渲染效果。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setSpatializationSceneType

```TypeScript
setSpatializationSceneType(spatializationSceneType: AudioSpatializationSceneType): void
```

设置空间音频渲染场景类型，同步返回结果。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| spatializationSceneType | [AudioSpatializationSceneType](arkts-audio-audio-audiospatializationscenetype-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## updateSpatialDeviceState

```TypeScript
updateSpatialDeviceState(spatialDeviceState: AudioSpatialDeviceState): void
```

更新空间化设备状态，同步返回结果。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| spatialDeviceState | [AudioSpatialDeviceState](arkts-audio-audio-audiospatialdevicestate-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
