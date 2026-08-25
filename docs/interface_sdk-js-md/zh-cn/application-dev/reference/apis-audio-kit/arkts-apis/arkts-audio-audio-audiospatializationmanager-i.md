# AudioSpatializationManager

空间音频管理。在使用AudioSpatializationManager的接口前，需要使用 [getSpatializationManager](arkts-audio-audio-audiomanager-i.md#getspatializationmanager)获取 AudioSpatializationManager实例。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## isSpatializationEnabledForCurrentDevice

```TypeScript
isSpatializationEnabledForCurrentDevice(): boolean
```

获取当前设备空间音频渲染是否开启。同步返回结果。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**返回值：**

| 类型 |
| --- |
| boolean |

## off('spatializationEnabledChangeForCurrentDevice')

```TypeScript
off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void
```

取消监听当前设备空间音频渲染开关状态变化事件。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'spatializationEnabledChangeForCurrentDevice' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('spatializationEnabledChangeForCurrentDevice')

```TypeScript
on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void
```

监听当前设备空间音频渲染开关状态变化事件。使用callback异步回调。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'spatializationEnabledChangeForCurrentDevice' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
