# AudioSpatializationManager

空间音频管理。

在使用AudioSpatializationManager的接口之前，需先通过  
[getSpatializationManager](arkts-audio-audio-audiomanager-i.md#getspatializationmanager)获取AudioSpatializationManager实例。

> **说明：**
> 
> - 本Interface首批接口从API version 18开始支持。

**起始版本：** 18

<!--Device-audio-interface AudioSpatializationManager--><!--Device-audio-interface AudioSpatializationManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

## isSpatializationEnabledForCurrentDevice

```TypeScript
isSpatializationEnabledForCurrentDevice(): boolean
```

获取当前设备空间音频渲染是否开启。同步返回结果。

**起始版本：** 18

<!--Device-AudioSpatializationManager-isSpatializationEnabledForCurrentDevice(): boolean--><!--Device-AudioSpatializationManager-isSpatializationEnabledForCurrentDevice(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**返回值：**

| 类型 |
| --- |
| boolean |

## off('spatializationEnabledChangeForCurrentDevice')

```TypeScript
off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void
```

取消监听当前设备空间音频渲染开关状态变化事件。使用callback异步回调。

**起始版本：** 18

<!--Device-AudioSpatializationManager-off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void--><!--Device-AudioSpatializationManager-off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'spatializationEnabledChangeForCurrentDevice' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

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

<!--Device-AudioSpatializationManager-on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void--><!--Device-AudioSpatializationManager-on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'spatializationEnabledChangeForCurrentDevice' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
