# AudioSessionManager

音频会话管理。

在使用AudioSessionManager的接口之前，需先通过[getSessionManager](arkts-audio-audio-audiomanager-i.md#getsessionmanager)获取AudioSessionManager实例。

> **说明：**
> 
> - 本Interface首批接口从API version 12开始支持。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioSessionManager--><!--Device-audio-interface AudioSessionManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## activateAudioSession

```TypeScript
activateAudioSession(strategy: AudioSessionStrategy): Promise<void>
```

激活音频会话。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-activateAudioSession(strategy: AudioSessionStrategy): Promise<void>--><!--Device-AudioSessionManager-activateAudioSession(strategy: AudioSessionStrategy): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| strategy | [AudioSessionStrategy](arkts-audio-audio-audiosessionstrategy-i.md) | Yes | 音频会话策略。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 6800301 | System error. Possible causes: 1.Focus preemption failure. 2.Audio server process died. |

## clearSelectedMediaInputDevice

```TypeScript
clearSelectedMediaInputDevice(): Promise<void>
```

清空通过[selectMediaInputDevice](arkts-audio-audio-audiosessionmanager-i.md#selectmediainputdevice)设置的媒体输入设备。使用Promise异步回调。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioSessionManager-clearSelectedMediaInputDevice(): Promise<void>--><!--Device-AudioSessionManager-clearSelectedMediaInputDevice(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

## deactivateAudioSession

```TypeScript
deactivateAudioSession(): Promise<void>
```

停用音频会话。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-deactivateAudioSession(): Promise<void>--><!--Device-AudioSessionManager-deactivateAudioSession(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800301 | System error. Possible causes: 1.The audio session is not existed or has been released. 2.Audio server process died. |

## enableMuteSuggestionWhenMixWithOthers

```TypeScript
enableMuteSuggestionWhenMixWithOthers(enable: boolean): void
```

启用混音播放下接收静音播放建议通知功能。

通常，当使用混音模式时，如果其他应用同时播放音频，会和其他应用进行混音播放。但在某些场景下（如游戏或广播），应用自身会通过静音自身的音频以给用户提供更好的体验。

如果启用此功能，当订阅音频会话状态更改事件后静音建议和取消静音建议提示将通过[AudioSessionStateChangedEvent](arkts-audio-audio-audiosessionstatechangedevent-i.md)回调发送。收到静音建议表示其他应用程序开始播放音频，且播放的音频和本应用的音频不能混音。

此功能仅支持已设置[AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md)并激活模式模式为CONCURRENCY_MIX_WITH_OTHERS的音频会话使用。并且仅在激活音频会话期间生效一次，每次激活音频会话前都必须重新启用。

详细说明请参考[启用混音播放下静音建议通知](../../../media/audio/audio-session-management.md#启用混音播放下静音建议通知)。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionManager-enableMuteSuggestionWhenMixWithOthers(enable: boolean): void--><!--Device-AudioSessionManager-enableMuteSuggestionWhenMixWithOthers(enable: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 是否启用混音播放下接收静音播放建议通知功能。true表示启用，false表示不启用。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800103 | Function is called without setting {@link #AudioSessionScene} or called after audio session activation. |
| 6800301 | Audio client call audio service error, system internal error. |

## getAvailableDevices

```TypeScript
getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors
```

获取音频可选设备列表。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioSessionManager-getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors--><!--Device-AudioSessionManager-getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | Yes | 音频设备类型（根据用途分类）。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) | 返回设备列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## getBluetoothAndNearlinkPreferredRecordCategory

```TypeScript
getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory
```

获取通过  
[setBluetoothAndNearlinkPreferredRecordCategory](arkts-audio-audio-audiosessionmanager-i.md#setbluetoothandnearlinkpreferredrecordcategory)设置的在使用蓝牙或星闪进行录音时的设备偏好分类。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioSessionManager-getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory--><!--Device-AudioSessionManager-getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| [BluetoothAndNearlinkPreferredRecordCategory](arkts-audio-audio-bluetoothandnearlinkpreferredrecordcategory-e.md) | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

## getDefaultOutputDevice

```TypeScript
getDefaultOutputDevice(): DeviceType
```

获取通过[setDefaultOutputDevice](arkts-audio-audio-audiosessionmanager-i.md#setdefaultoutputdevice)设置的默认发声设备。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioSessionManager-getDefaultOutputDevice(): DeviceType--><!--Device-AudioSessionManager-getDefaultOutputDevice(): DeviceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md) | 设备类型。 &lt;br&gt;仅支持以下设备：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800103 | Operation not permit at current state. Return by promise. |
| 6800101 | Parameter verification failed. |

## getSelectedMediaInputDevice

```TypeScript
getSelectedMediaInputDevice(): AudioDeviceDescriptor
```

获得通过[selectMediaInputDevice](arkts-audio-audio-audiosessionmanager-i.md#selectmediainputdevice)设置的媒体输入设备。如果没有设置，返回一个deviceType属性为INVALID的设备。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioSessionManager-getSelectedMediaInputDevice(): AudioDeviceDescriptor--><!--Device-AudioSessionManager-getSelectedMediaInputDevice(): AudioDeviceDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 媒体输入设备信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

## isAudioSessionActivated

```TypeScript
isAudioSessionActivated(): boolean
```

检查音频会话是否已激活。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-isAudioSessionActivated(): boolean--><!--Device-AudioSessionManager-isAudioSessionActivated(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 音频会话是否处于激活状态。true表示已激活，false表示已停用。 |

## isOtherMediaPlaying

```TypeScript
isOtherMediaPlaying(): boolean
```

检查是否有其他应用正在播放MUSIC、MOVIE、AUDIOBOOK、GAME四种媒体类型的音频，已激活媒体类型的音频会话也将会被检查。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionManager-isOtherMediaPlaying(): boolean--><!--Device-AudioSessionManager-isOtherMediaPlaying(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否有其他应用正在播放媒体类型的音频。true表示有，false表示没有。 |

## off('audioSessionDeactivated')

```TypeScript
off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void
```

取消监听音频会话停用事件。使用callback异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void--><!--Device-AudioSessionManager-off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioSessionDeactivated' | Yes | 事件回调类型，支持的事件为'audioSessionDeactivated'，当取消监听音频会话停用事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionDeactivatedEvent&gt; | No | 回调函数，返回音频会话停用原因。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

## off('audioSessionStateChanged')

```TypeScript
off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void
```

取消监听音频会话状态变更事件。使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AudioSessionManager-off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void--><!--Device-AudioSessionManager-off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioSessionStateChanged' | Yes | 事件回调类型，支持的事件为'audioSessionStateChanged'，当音频会话状态变更时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionStateChangedEvent&gt; | No | 回调函数，返回音频会话变更提示信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## off('currentOutputDeviceChanged')

```TypeScript
off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void
```

取消监听当前输出设备的变化事件，并使用callback进行异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AudioSessionManager-off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'currentOutputDeviceChanged' | Yes | 事件回调类型，支持的事件为'currentOutputDeviceChanged'，当前输出设备发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentOutputDeviceChangedEvent&gt; | No | 回调函数，用于返回当前输出设备变化的信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## off('availableDeviceChange')

```TypeScript
off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void
```

取消监听音频可选设备连接状态变化事件。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-AudioSessionManager-off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void--><!--Device-AudioSessionManager-off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'availableDeviceChange' | Yes | 事件回调类型，支持的事件为'availableDeviceChange'，当取消监听音频可选设备连接变化事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceChangeAction&gt; | No | 回调函数，返回可选设备更新详情。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

## off('currentInputDeviceChanged')

```TypeScript
off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void
```

取消监听当前输入设备的变化事件。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-AudioSessionManager-off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'currentInputDeviceChanged' | Yes | 事件回调类型，支持的事件为'currentInputDeviceChanged'，当前输入设备发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentInputDeviceChangedEvent&gt; | No | 回调函数，用于返回当前输入设备变化的信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

## offAudioSessionDeactivated

```TypeScript
offAudioSessionDeactivated(callback?: Callback<AudioSessionDeactivatedEvent>): void
```

取消订阅音频会话去激活事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-offAudioSessionDeactivated(callback?: Callback<AudioSessionDeactivatedEvent>): void--><!--Device-AudioSessionManager-offAudioSessionDeactivated(callback?: Callback<AudioSessionDeactivatedEvent>): void-End-->

**System capability:** 
- API version 23 and later: SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionDeactivatedEvent&gt; | No | Callback invoked for the audio session deactivated event.<br>**Since:** 23 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed.<br>**Applicable version:** 23 and later |

## offAudioSessionStateChanged

```TypeScript
offAudioSessionStateChanged(callback?: Callback<AudioSessionStateChangedEvent>): void
```

Unsubscribes to audio session deactivated event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioSessionManager-offAudioSessionStateChanged(callback?: Callback<AudioSessionStateChangedEvent>): void--><!--Device-AudioSessionManager-offAudioSessionStateChanged(callback?: Callback<AudioSessionStateChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionStateChangedEvent&gt; | No | Callback invoked for the audio session state change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## offAvailableDeviceChange

```TypeScript
offAvailableDeviceChange(callback?: Callback<DeviceChangeAction>): void
```

Unsubscribes to available device change events.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-AudioSessionManager-offAvailableDeviceChange(callback?: Callback<DeviceChangeAction>): void--><!--Device-AudioSessionManager-offAvailableDeviceChange(callback?: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceChangeAction&gt; | No | Callback used in subscribe. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

## offCurrentInputDeviceChanged

```TypeScript
offCurrentInputDeviceChanged(callback?: Callback<CurrentInputDeviceChangedEvent>): void
```

Unsubscribes current input device change events.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-AudioSessionManager-offCurrentInputDeviceChanged(callback?: Callback<CurrentInputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-offCurrentInputDeviceChanged(callback?: Callback<CurrentInputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentInputDeviceChangedEvent&gt; | No | Callback used in subscribe. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

## offCurrentOutputDeviceChanged

```TypeScript
offCurrentOutputDeviceChanged(callback?: Callback<CurrentOutputDeviceChangedEvent>): void
```

Unsubscribes output device change event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioSessionManager-offCurrentOutputDeviceChanged(callback?: Callback<CurrentOutputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-offCurrentOutputDeviceChanged(callback?: Callback<CurrentOutputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentOutputDeviceChangedEvent&gt; | No | Callback used to listen device change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## on('audioSessionDeactivated')

```TypeScript
on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void
```

监听音频会话停用事件（当音频会话停用时触发）。使用callback异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void--><!--Device-AudioSessionManager-on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioSessionDeactivated' | Yes | 事件回调类型，支持的事件为'audioSessionDeactivated'，当音频会话停用时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionDeactivatedEvent&gt; | Yes | 回调函数，返回音频会话停用原因。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

## on('audioSessionStateChanged')

```TypeScript
on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void
```

监听音频会话状态变更事件（当音频会话焦点变更时触发）。使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AudioSessionManager-on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void--><!--Device-AudioSessionManager-on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioSessionStateChanged' | Yes | 事件回调类型，支持的事件为'audioSessionStateChanged'，当音频会话状态变更时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionStateChangedEvent&gt; | Yes | 回调函数，返回音频会话变更提示信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800102 | Allocate memory failed. |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## on('currentOutputDeviceChanged')

```TypeScript
on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void
```

监听当前输出设备变化事件（当前输出设备发生变化时触发）。使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AudioSessionManager-on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'currentOutputDeviceChanged' | Yes | 事件回调类型，支持的事件为'currentOutputDeviceChanged'，当前输出设备变更时触发。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentOutputDeviceChangedEvent&gt; | Yes | 回调函数，返回当前输出设备信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800102 | Allocate memory failed. |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## on('availableDeviceChange')

```TypeScript
on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void
```

监听音频可选设备连接状态变化事件（当音频可选设备连接状态发生变化时触发）。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-AudioSessionManager-on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void--><!--Device-AudioSessionManager-on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'availableDeviceChange' | Yes | 事件回调类型，支持的事件为'availableDeviceChange'，当音频可选设备连接状态发生变化时，触发该事件。 |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | Yes | 音频设备类型（根据用途分类）。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceChangeAction&gt; | Yes | 回调函数，返回设备更新详情。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## on('currentInputDeviceChanged')

```TypeScript
on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void
```

监听当前输入设备变化事件（当前输入设备发生变化时触发）。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-AudioSessionManager-on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'currentInputDeviceChanged' | Yes | 事件回调类型，支持的事件为'currentInputDeviceChanged'，当前输入设备发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentInputDeviceChangedEvent&gt; | Yes | 回调函数，返回当前输入设备信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## onAudioSessionDeactivated

```TypeScript
onAudioSessionDeactivated(callback: Callback<AudioSessionDeactivatedEvent>): void
```

Listens for audio session deactivated event. When the audio session is deactivated,registered clients will receive the callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-onAudioSessionDeactivated(callback: Callback<AudioSessionDeactivatedEvent>): void--><!--Device-AudioSessionManager-onAudioSessionDeactivated(callback: Callback<AudioSessionDeactivatedEvent>): void-End-->

**System capability:** 
- API version 23 and later: SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionDeactivatedEvent&gt; | Yes | Callback invoked for the audio session deactivated event.<br>**Since:** 23 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed.<br>**Applicable version:** 23 and later |

## onAudioSessionStateChanged

```TypeScript
onAudioSessionStateChanged(callback: Callback<AudioSessionStateChangedEvent>): void
```

Listens for audio session state change event. When the audio session state change,registered clients will receive the callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioSessionManager-onAudioSessionStateChanged(callback: Callback<AudioSessionStateChangedEvent>): void--><!--Device-AudioSessionManager-onAudioSessionStateChanged(callback: Callback<AudioSessionStateChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionStateChangedEvent&gt; | Yes | Callback invoked for the audio session state change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800102 | Allocate memory failed. |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## onAvailableDeviceChange

```TypeScript
onAvailableDeviceChange(deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void
```

Subscribes to available device change events. When a device is connected/disconnected, registered clients will receive the callback.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-AudioSessionManager-onAvailableDeviceChange(deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void--><!--Device-AudioSessionManager-onAvailableDeviceChange(deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | Yes | Audio device usage to filter available devices. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceChangeAction&gt; | Yes | Callback used to obtain the device update details. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## onCurrentInputDeviceChanged

```TypeScript
onCurrentInputDeviceChanged(callback: Callback<CurrentInputDeviceChangedEvent>): void
```

Subscribes input device change event callback. The event is triggered when current input device change.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-AudioSessionManager-onCurrentInputDeviceChanged(callback: Callback<CurrentInputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-onCurrentInputDeviceChanged(callback: Callback<CurrentInputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentInputDeviceChangedEvent&gt; | Yes | Callback used to listen input device change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## onCurrentOutputDeviceChanged

```TypeScript
onCurrentOutputDeviceChanged(callback: Callback<CurrentOutputDeviceChangedEvent>): void
```

Subscribes output device change event callback.The event is triggered when device change.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioSessionManager-onCurrentOutputDeviceChanged(callback: Callback<CurrentOutputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-onCurrentOutputDeviceChanged(callback: Callback<CurrentOutputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentOutputDeviceChangedEvent&gt; | Yes | Callback used to listen device change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800102 | Allocate memory failed. |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## selectMediaInputDevice

```TypeScript
selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>
```

设置媒体输入设备。使用Promise异步回调。

> **说明：**
> 
> - 本接口不适用于VoIP通话录音，即[SourceType](arkts-audio-audio-sourcetype-e.md)为SOURCE_TYPE_VOICE_COMMUNICATION的场景不适用。
> 
> - 本接口调用前需要先调用[getAvailableDevices](arkts-audio-audio-audiosessionmanager-i.md#getavailabledevices)接口查询到当前可用输入设备列表，从列表中选择输入
> 设备。
> 
> - 当系统中存在其他更高优先级的应用录音流时，实际使用的输入设备会跟随其他高优先级应用所选的输入设备。
> 
> - 应用程序可以监听
> [currentInputDeviceChanged](audio.AudioSessionManager.on(type: 'currentInputDeviceChanged', callback: Callback&lt;CurrentInputDeviceChangedEvent&gt;))
> 事件来获得实际的输入设备。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioSessionManager-selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>--><!--Device-AudioSessionManager-selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputAudioDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | Yes | 媒体输入设备。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed, for example, the selected device does not exist. |
| 6800301 | Audio client call audio service error, System error. |

## setAudioSessionBehavior

ArkTS-Dyn:
```TypeScript
setAudioSessionBehavior(behavior: number): void
```

ArkTS-Sta:
```TypeScript
setAudioSessionBehavior(behavior: int): void
```

设置音频会话行为参数，支持多种标志位的组合使用。

> **说明：**
> 
> 当音频会话在激活状态时调用此接口后，必须重新调用接口[activateAudioSession](arkts-audio-audio-audiosessionmanager-i.md#activateaudiosession)使其生效。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionManager-setAudioSessionBehavior(behavior: int): void--><!--Device-AudioSessionManager-setAudioSessionBehavior(behavior: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| behavior | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 用于设置音频会话行为。 &lt;br&gt;该参数可以是单个标志，也可以是多个标志的按位OR组合。 &lt;br&gt;当前支持的音频会话行为详见[AudioSessionBehaviorFlags](arkts-audio-audio-audiosessionbehaviorflags-e.md)中定义的标志。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800103 | Operation not permitted in the current state. |
| 6800101 | Parameter verification failed. |

## setAudioSessionScene

```TypeScript
setAudioSessionScene(scene: AudioSessionScene): void
```

设置音频会话场景参数。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioSessionManager-setAudioSessionScene(scene: AudioSessionScene): void--><!--Device-AudioSessionManager-setAudioSessionScene(scene: AudioSessionScene): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scene | [AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md) | Yes | 音频会话场景。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800103 | Operation not permit at current state. |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## setBluetoothAndNearlinkPreferredRecordCategory

```TypeScript
setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>
```

设置在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。使用Promise异步回调。

> **说明：**
> 
> - 应用程序可以在蓝牙或星闪连接之前设置此分类，系统将在设备连接时优先使用蓝牙或星闪进行录音。
> 
> - 当系统中存在其他更高优先级的应用录音流时，实际使用的输入设备会跟随其他高优先级应用所选的输入设备。
> 
> - 应用程序可以监听
> [currentInputDeviceChanged](audio.AudioSessionManager.on(type: 'currentInputDeviceChanged', callback: Callback&lt;CurrentInputDeviceChangedEvent&gt;))
> 事件来获得实际的输入设备。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioSessionManager-setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>--><!--Device-AudioSessionManager-setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| category | [BluetoothAndNearlinkPreferredRecordCategory](arkts-audio-audio-bluetoothandnearlinkpreferredrecordcategory-e.md) | Yes | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

## setCapturerMuteHint

```TypeScript
setCapturerMuteHint(mute: boolean): Promise<void>
```

应用将当前音频会话内录音流的自身静音状态传递给系统音频模块。&lt;!--RP1--&gt;该接口不会触发录音流静音，当前仅在部分PC/2in1设备上用于优化设备功耗。&lt;!--RP1End--&gt;使用Promise异步回调。

> **说明：**
> 
> - 该接口用于向系统音频模块上报当前音频会话内录音流的静音状态，不会改变录音流的实际静音状态。
> 
> - 该接口仅在当前音频会话存在运行中的录音流时允许调用，否则返回错误码6800103。
> 
> - 若某条录音流同时调用了流级接口[AudioCapturer.setMuteHint](arkts-audio-audio-audiocapturer-i.md#setmutehint)和本接口，流级接口设置优先级更高，以流级接口设置值为准。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionManager-setCapturerMuteHint(mute: boolean): Promise<void>--><!--Device-AudioSessionManager-setCapturerMuteHint(mute: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mute | boolean | Yes | 应用自身给系统音频模块上报的静音状态。true表示应用将当前流静音，false表示取消静音。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800103 | Operation not permitted at current state, there is no audio capturer running. |

## setDefaultOutputDevice

```TypeScript
setDefaultOutputDevice(deviceType: DeviceType): Promise<void>
```

设置默认发声设备。使用Promise方式进行异步回调。

> **说明：**
> 
> - 本接口适用于以下情况：当设置的[AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md)为VoIP场景时，激活AudioSession后立即生效。若
> [AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md)为非VoIP场景，激活AudioSession时不会生效，仅在启动播放的
> [StreamUsage](arkts-audio-audio-streamusage-e.md)为语音消息、VoIP语音通话或VoIP视频通话时才生效。支持听筒、扬声器和系统默认设备。
> 
> - 本接口允许在AudioSessionManager创建后随时调用，系统会记录应用设置的默认本机内置发声设备。但只有激活AudioSession后才能生效。应用启动播放时，若外接设备如蓝牙耳机或有线耳机已接入，系统优先从
> 外接设备发声。否则，系统遵循应用设置的默认本机内置发声设备。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioSessionManager-setDefaultOutputDevice(deviceType: DeviceType): Promise<void>--><!--Device-AudioSessionManager-setDefaultOutputDevice(deviceType: DeviceType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md) | Yes | 设备类型。 &lt;br&gt;仅支持以下设备：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800102 | Allocate memory failed. Return by promise. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | Audio client call audio service error, System error. |

## setMediaOutputDevice

```TypeScript
setMediaOutputDevice(deviceType: DeviceType): Promise<void>
```

当连接其他音频外设（如蓝牙耳机或有线耳机）时，将媒体输出设备切换为内置扬声器。使用Promise异步回调。

> **说明：**
> 
> - 本接口仅适用于媒体播放场景，并且会作用于应用内发起的所有媒体流。
> 
> - 若存在更高优先级的并发播放流或用户手动选择输出设备，则应用程序实际使用的输出设备将与本接口设置的设备不同。应用程序可通过监听
> [CurrentOutputDeviceChangedEvent](arkts-audio-audio-currentoutputdevicechangedevent-i.md)事件获取当前活跃的输出设备。
> 
> - 当应用程序需要清除之前通过接口设置的扬声器输出配置时，可通过调用接口将媒体输出设备设置为DEFAULT（系统默认设备）来实现。该设置仅在应用程序运行期间有效，当应用程序退出时，此接口的设置将自动清除。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionManager-setMediaOutputDevice(deviceType: DeviceType): Promise<void>--><!--Device-AudioSessionManager-setMediaOutputDevice(deviceType: DeviceType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md) | Yes | 设备类型。 &lt;br&gt;仅支持以下设备：SPEAKER（扬声器）和DEFAULT（系统默认设备）。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed, for example, the selected device type is not supported. |
| 6800301 | System error. Possible causes: 1.Internal variable memory allocation failed. 2.Audio server process died. 3.Speaker device is not available. |

