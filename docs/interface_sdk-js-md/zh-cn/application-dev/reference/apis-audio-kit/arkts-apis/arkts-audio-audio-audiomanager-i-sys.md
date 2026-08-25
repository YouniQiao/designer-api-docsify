# AudioManager

管理音频音量和音频设备。在调用AudioManager的接口前，需要先通过[getAudioManager](arkts-audio-audio-getaudiomanager-f.md)创建实例。

**起始版本：** 7

**系统能力：** SystemCapability.Multimedia.Audio.Core

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## disableSafeMediaVolume

```TypeScript
disableSafeMediaVolume(): Promise<void>
```

设置安全音量为非激活状态。使用Promise异步回调。 设置为非激活状态后，当设备长时间高音量播放时，不再自动提醒用户降低到安全音量。

**起始版本：** 12

**需要权限：** ohos.permission.MODIFY_AUDIO_SETTINGS

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getCollaborativeManager

```TypeScript
getCollaborativeManager(): AudioCollaborativeManager
```

获取移动全景声管理器。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [AudioCollaborativeManager](arkts-audio-audio-audiocollaborativemanager-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getEffectManager

```TypeScript
getEffectManager(): AudioEffectManager
```

获取音效会话管理器。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [AudioEffectManager](arkts-audio-audio-audioeffectmanager-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getExtraParameters

```TypeScript
getExtraParameters(mainKey: string, subKeys?: Array<string>): Promise<Record<string, string>>
```

获取指定音频参数值。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mainKey | string | 是 |
| subKeys | Array & lt;string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Record & lt;string, string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## getRecordingManager

```TypeScript
getRecordingManager(): AudioRecordingManager
```

获取录音策略管理器。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [AudioRecordingManager](arkts-audio-audio-audiorecordingmanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('volumeChange')

```TypeScript
on(type: 'volumeChange', callback: Callback<VolumeEvent>): void
```


> **说明：**
> 
> 从 API version 8 开始支持，从 API version 9 开始废弃，建议使用AudioVolumeManager中的
> [on('volumeChange')](arkts-audio-audio-audiovolumemanager-i.md#onvolumechange)替代。
> 监听系统音量变化事件（当系统音量发生变化时触发）。使用callback异步回调。
> 目前此订阅接口在单进程多AudioManager实例的使用场景下，仅最后一个实例的订阅生效，其他实例的订阅会被覆盖（即使最后一个实例没有进行订阅），因此推荐使用单一AudioManager实例进行开发。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** volumeChange

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'volumeChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 是 |

## on('ringerModeChange')

```TypeScript
on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void
```

监听铃声模式变化事件（当[铃声模式](arkts-audio-audio-audioringmode-e.md)发生改变时触发）。使用callback异步回调。

> **说明：**
> 
> 从 API version 8 开始支持，从 API version 9 开始废弃，建议使用AudioVolumeGroupManager中的
> [on('ringerModeChange')](arkts-audio-audio-audiovolumegroupmanager-i.md#onringermodechange)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** ringerModeChange

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'ringerModeChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | 是 |

## reportPlaybackCaptureUserAllowed

```TypeScript
reportPlaybackCaptureUserAllowed(streamId: number, allowed: boolean): Promise<void>
```

报告用户允许的结果，以响应来自特定系统应用的播放捕获请求给音频系统。 系统将根据该结果继续启动播放捕获或返回失败。 该 API 使用 Promise 来返回结果。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamId | number | 是 |
| allowed | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## setAudioScene

```TypeScript
setAudioScene(scene: AudioScene, callback: AsyncCallback<void> ): void
```

设置音频场景模式。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scene | [AudioScene](arkts-audio-audio-audioscene-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setAudioScene

```TypeScript
setAudioScene(scene: AudioScene): Promise<void>
```

设置音频场景模式。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scene | [AudioScene](arkts-audio-audio-audioscene-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setExtraParameters

```TypeScript
setExtraParameters(mainKey: string, kvpairs: Record<string, string>): Promise<void>
```

音频扩展参数设置。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.MODIFY_AUDIO_SETTINGS

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mainKey | string | 是 |
| kvpairs | Record & lt;string, string & gt; | 是 |

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
