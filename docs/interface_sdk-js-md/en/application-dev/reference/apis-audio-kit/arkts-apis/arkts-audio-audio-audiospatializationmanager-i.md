# AudioSpatializationManager

空间音频管理。

在使用AudioSpatializationManager的接口之前，需先通过  
[getSpatializationManager](arkts-audio-audio-audiomanager-i.md#getspatializationmanager)获取AudioSpatializationManager实例。

> **说明：**
> 
> - 本Interface首批接口从API version 18开始支持。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioSpatializationManager--><!--Device-audio-interface AudioSpatializationManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## isSpatializationEnabledForCurrentDevice

```TypeScript
isSpatializationEnabledForCurrentDevice(): boolean
```

获取当前设备空间音频渲染是否开启。同步返回结果。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AudioSpatializationManager-isSpatializationEnabledForCurrentDevice(): boolean--><!--Device-AudioSpatializationManager-isSpatializationEnabledForCurrentDevice(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前设备空间音频渲染是否开启。true表示开启，false表示未开启。 |

## off('spatializationEnabledChangeForCurrentDevice')

```TypeScript
off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void
```

取消监听当前设备空间音频渲染开关状态变化事件。使用callback异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-AudioSpatializationManager-off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void--><!--Device-AudioSpatializationManager-off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'spatializationEnabledChangeForCurrentDevice' | Yes | 事件回调类型，支持的事件为' spatializationEnabledChangeForCurrentDevice'，当取消订阅当前设备空间音频渲染开关状态变化事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | 回调函数。返回true表示打开空间音频渲染状态；返回false表示关闭空间音频渲染状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## offSpatializationEnabledChangeForCurrentDevice

```TypeScript
offSpatializationEnabledChangeForCurrentDevice(callback?: Callback<boolean>): void
```

Unsubscribes to the spatialization enable state change events by the current device.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioSpatializationManager-offSpatializationEnabledChangeForCurrentDevice(callback?: Callback<boolean>): void--><!--Device-AudioSpatializationManager-offSpatializationEnabledChangeForCurrentDevice(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | Callback used to get the spatialization enable state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## on('spatializationEnabledChangeForCurrentDevice')

```TypeScript
on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void
```

监听当前设备空间音频渲染开关状态变化事件。使用callback异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-AudioSpatializationManager-on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void--><!--Device-AudioSpatializationManager-on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'spatializationEnabledChangeForCurrentDevice' | Yes | 事件回调类型，支持的事件为' spatializationEnabledChangeForCurrentDevice'，当空间音频渲染开关状态变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | 回调函数。返回true表示打开空间音频渲染状态；返回false表示关闭空间音频渲染状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## onSpatializationEnabledChangeForCurrentDevice

```TypeScript
onSpatializationEnabledChangeForCurrentDevice(callback: Callback<boolean>): void
```

Subscribes to the spatialization enable state change events by the current device.When the spatialization enable state changes, registered clients will receive the callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioSpatializationManager-onSpatializationEnabledChangeForCurrentDevice(callback: Callback<boolean>): void--><!--Device-AudioSpatializationManager-onSpatializationEnabledChangeForCurrentDevice(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | Callback used to get the spatialization enable state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

