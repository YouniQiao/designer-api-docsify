# AudioSessionManager

音频会话管理。 在使用AudioSessionManager的接口之前，需先通过 [getSessionManager](arkts-audio-audio-audiomanager-i.md#getsessionmanager)获取AudioSessionManager实例。

> **说明：**

> - 本Interface首批接口从API version 12开始支持。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Core

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
```

## activateAudioSession

```TypeScript
activateAudioSession(strategy: AudioSessionStrategy): Promise<void>
```

激活音频会话。使用Promise异步回调。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strategy | [AudioSessionStrategy](arkts-audio-audio-audiosessionstrategy-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 设置音频会话并发模式为混音模式。
let strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS
};

audioSessionManager.activateAudioSession(strategy).then(() => {
  console.info('Succeeded in activating the audio session.');
}).catch((err: BusinessError) => {
  console.error(`Failed to activate the audio session. Code: ${err.code}, message: ${err.message}`);
});
```

## clearSelectedMediaInputDevice

```TypeScript
clearSelectedMediaInputDevice(): Promise<void>
```

清空通过[selectMediaInputDevice](#selectmediainputdevice)设置的媒体输入设备。使用Promise异步回调。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.clearSelectedMediaInputDevice().then(() => {
  console.info('Succeeded in clearing the selected media input device.');
}).catch((err: BusinessError) => {
  console.error(`Failed to clear the selected media input device. Code: ${err.code}, message: ${err.message}`);
});
```

## deactivateAudioSession

```TypeScript
deactivateAudioSession(): Promise<void>
```

停用音频会话。使用Promise异步回调。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.deactivateAudioSession().then(() => {
  console.info('Succeeded in deactivating the audio session.');
}).catch((err: BusinessError) => {
  console.error(`Failed to deactivate the audio session. Code: ${err.code}, message: ${err.message}`);
});
```

## enableMuteSuggestionWhenMixWithOthers

```TypeScript
enableMuteSuggestionWhenMixWithOthers(enable: boolean): void
```

启用混音播放下接收静音播放建议通知功能。 通常，当使用混音模式时，如果其他应用同时播放音频，会和其他应用进行混音播放。但在某些场景下（如游戏或广播），应用自身会通过静音自身的音频以给用户提供更好的体验。 如果启用此功能，当订阅音频会话状态更改事件后静音建议和取消静音建议提示将通过 [AudioSessionStateChangedEvent](arkts-audio-audio-audiosessionstatechangedevent-i.md)回调发送。收到静音建议表示其他应 用程序开始播放音频，且播放的音频和本应用的音频不能混音。 此功能仅支持已设置[AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md)并激活模式模式为 CONCURRENCY_MIX_WITH_OTHERS的音频会话使用。并且仅在激活音频会话期间生效一次，每次激活音频会话前都必须重新启用。 详细说明请参考启用混音播放下静音建议通知文档。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
audioSessionManager.enableMuteSuggestionWhenMixWithOthers(true);
```

## getAvailableDevices

```TypeScript
getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors
```

获取音频可选设备列表。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data: audio.AudioDeviceDescriptors = audioRoutingManager.getAvailableDevices(audio.DeviceUsage.MEDIA_OUTPUT_DEVICES);
  console.info(`Succeeded in obtaining available devices, audioDeviceDescriptors: ${JSON.stringify(data)}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain available devices. Code: ${error.code}, message: ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data: audio.AudioDeviceDescriptors = audioSessionManager.getAvailableDevices(audio.DeviceUsage.MEDIA_OUTPUT_DEVICES);
  console.info(`Succeeded in obtaining available devices, audioDeviceDescriptors: ${JSON.stringify(data)}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain available devices. Code: ${error.code}, message: ${error.message}`);
}
```

## getBluetoothAndNearlinkPreferredRecordCategory

```TypeScript
getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory
```

获取通过 [setBluetoothAndNearlinkPreferredRecordCategory](#setbluetoothandnearlinkpreferredrecordcategory) 设置的在使用蓝牙或星闪进行录音时的设备偏好分类。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 |
| --- |
| [BluetoothAndNearlinkPreferredRecordCategory](arkts-audio-audio-bluetoothandnearlinkpreferredrecordcategory-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let category: audio.BluetoothAndNearlinkPreferredRecordCategory = audioSessionManager.getBluetoothAndNearlinkPreferredRecordCategory();
  console.info(`Succeeded in obtaining the bluetooth and nearlink preferred record category, category: ${category}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the bluetooth and nearlink preferred record category. Code: ${error.code}, message: ${error.message}`);
}
```

## getDefaultOutputDevice

```TypeScript
getDefaultOutputDevice(): DeviceType
```

获取通过[setDefaultOutputDevice](#setdefaultoutputdevice)设置的默认发声设备。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 |
| --- |
| [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |

**示例**

```TypeScript
let deviceType = audioSessionManager.getDefaultOutputDevice();
```

## getSelectedMediaInputDevice

```TypeScript
getSelectedMediaInputDevice(): AudioDeviceDescriptor
```

获得通过[selectMediaInputDevice](#selectmediainputdevice)设置的媒体输入设备。如果没有设置，返回一个 deviceType属性为INVALID的设备。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 |
| --- |
| [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let device: audio.AudioDeviceDescriptor = audioSessionManager.getSelectedMediaInputDevice();
  console.info(`Succeeded in obtaining the selected media input device, audioDeviceDescriptor: ${JSON.stringify(device)}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the selected media input device. Code: ${error.code}, message: ${error.message}`);
}
```

## isAudioSessionActivated

```TypeScript
isAudioSessionActivated(): boolean
```

检查音频会话是否已激活。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
let isActivated = audioSessionManager.isAudioSessionActivated();
```

## isOtherMediaPlaying

```TypeScript
isOtherMediaPlaying(): boolean
```

检查是否有其他应用正在播放MUSIC、MOVIE、AUDIOBOOK、GAME四种媒体类型的音频，已激活媒体类型的音频会话也将会被检查。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
let isExistence = audioSessionManager.isOtherMediaPlaying();
```

## off('audioSessionDeactivated')

```TypeScript
off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void
```

取消监听音频会话停用事件。使用callback异步回调。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioSessionDeactivated' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSessionDeactivatedEvent](arkts-audio-audio-audiosessiondeactivatedevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## off('audioSessionStateChanged')

```TypeScript
off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void
```

取消监听音频会话状态变更事件。使用callback异步回调。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioSessionStateChanged' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSessionStateChangedEvent](arkts-audio-audio-audiosessionstatechangedevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## off('currentOutputDeviceChanged')

```TypeScript
off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void
```

取消监听当前输出设备的变化事件，并使用callback进行异步回调。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'currentOutputDeviceChanged' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CurrentOutputDeviceChangedEvent](arkts-audio-audio-currentoutputdevicechangedevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## off('availableDeviceChange')

```TypeScript
off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void
```

取消监听音频可选设备连接状态变化事件。

**起始版本：** 21

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为21。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'availableDeviceChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## off('currentInputDeviceChanged')

```TypeScript
off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void
```

取消监听当前输入设备的变化事件。

**起始版本：** 21

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为21。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'currentInputDeviceChanged' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CurrentInputDeviceChangedEvent](arkts-audio-audio-currentinputdevicechangedevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## offAudioSessionDeactivated

```TypeScript
offAudioSessionDeactivated(callback?: Callback<AudioSessionDeactivatedEvent>): void
```

取消监听音频会话停用事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本23+：SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSessionDeactivatedEvent](arkts-audio-audio-audiosessiondeactivatedevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioSessionManager.offAudioSessionDeactivated();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let audioSessionDeactivatedCallback = (audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
  console.info(`Audio session deactivated, audioSessionDeactivatedEvent: ${JSON.stringify(audioSessionDeactivatedEvent)}.`);
};

audioSessionManager.onAudioSessionDeactivated(audioSessionDeactivatedCallback);

audioSessionManager.offAudioSessionDeactivated(audioSessionDeactivatedCallback);
```

## offAudioSessionStateChanged

```TypeScript
offAudioSessionStateChanged(callback?: Callback<AudioSessionStateChangedEvent>): void
```

取消监听音频会话状态变更事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSessionStateChangedEvent](arkts-audio-audio-audiosessionstatechangedevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioSessionManager.offAudioSessionStateChanged();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let audioSessionStateChangedCallback = (audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
  console.info(`Audio session state changed, audioSessionStateChangedEvent: ${JSON.stringify(audioSessionStateChangedEvent)}.`);
};

audioSessionManager.onAudioSessionStateChanged(audioSessionStateChangedCallback);

audioSessionManager.offAudioSessionStateChanged(audioSessionStateChangedCallback);
```

## offAvailableDeviceChange

```TypeScript
offAvailableDeviceChange(callback?: Callback<DeviceChangeAction>): void
```

取消监听音频可选设备连接状态变化事件。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioRoutingManager.offAvailableDeviceChange();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let availableDeviceChangeCallback = (deviceChangeAction: audio.DeviceChangeAction) => {
  console.info(`Available device changed, deviceChangeAction: ${JSON.stringify(deviceChangeAction)}.`);
};

audioRoutingManager.onAvailableDeviceChange(audio.DeviceUsage.MEDIA_OUTPUT_DEVICES, availableDeviceChangeCallback);

audioRoutingManager.offAvailableDeviceChange(availableDeviceChangeCallback);
```

```TypeScript
// 取消该事件的所有监听。
audioSessionManager.offAvailableDeviceChange();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let availableDeviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
  console.info(`Available device changed, deviceChangeAction: ${JSON.stringify(deviceChanged)}.`);
};

audioSessionManager.onAvailableDeviceChange(audio.DeviceUsage.MEDIA_INPUT_DEVICES, availableDeviceChangeCallback);

audioSessionManager.offAvailableDeviceChange(availableDeviceChangeCallback);
```

## offCurrentInputDeviceChanged

```TypeScript
offCurrentInputDeviceChanged(callback?: Callback<CurrentInputDeviceChangedEvent>): void
```

取消监听当前输入设备的变化事件。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CurrentInputDeviceChangedEvent](arkts-audio-audio-currentinputdevicechangedevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioSessionManager.offCurrentInputDeviceChanged();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
  console.info(`Current input device changed, currentInputDeviceChangedEvent: ${JSON.stringify(currentInputDeviceChangedEvent)}.`);
};

audioSessionManager.onCurrentInputDeviceChanged(currentInputDeviceChangedCallback);

audioSessionManager.offCurrentInputDeviceChanged(currentInputDeviceChangedCallback);
```

## offCurrentOutputDeviceChanged

```TypeScript
offCurrentOutputDeviceChanged(callback?: Callback<CurrentOutputDeviceChangedEvent>): void
```

Unsubscribes output device change event callback.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CurrentOutputDeviceChangedEvent](arkts-audio-audio-currentoutputdevicechangedevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioSessionManager.offCurrentOutputDeviceChanged();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
  console.info(`Current output device changed, currentOutputDeviceChangedEvent: ${JSON.stringify(currentOutputDeviceChangedEvent)}.`);
};

audioSessionManager.onCurrentOutputDeviceChanged(currentOutputDeviceChangedCallback);

audioSessionManager.offCurrentOutputDeviceChanged(currentOutputDeviceChangedCallback);
```

## on('audioSessionDeactivated')

```TypeScript
on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void
```

监听音频会话停用事件（当音频会话停用时触发）。使用callback异步回调。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioSessionDeactivated' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSessionDeactivatedEvent](arkts-audio-audio-audiosessiondeactivatedevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('audioSessionStateChanged')

```TypeScript
on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void
```

监听音频会话状态变更事件（当音频会话焦点变更时触发）。使用callback异步回调。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioSessionStateChanged' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSessionStateChangedEvent](arkts-audio-audio-audiosessionstatechangedevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800102](../errorcode-audio.md#6800102-分配内存失败) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## on('currentOutputDeviceChanged')

```TypeScript
on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void
```

监听当前输出设备变化事件（当前输出设备发生变化时触发）。使用callback异步回调。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'currentOutputDeviceChanged' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CurrentOutputDeviceChangedEvent](arkts-audio-audio-currentoutputdevicechangedevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800102](../errorcode-audio.md#6800102-分配内存失败) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## on('availableDeviceChange')

```TypeScript
on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void
```

监听音频可选设备连接状态变化事件（当音频可选设备连接状态发生变化时触发）。

**起始版本：** 21

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为21。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'availableDeviceChange' | 是 |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## on('currentInputDeviceChanged')

```TypeScript
on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void
```

监听当前输入设备变化事件（当前输入设备发生变化时触发）。

**起始版本：** 21

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为21。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'currentInputDeviceChanged' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CurrentInputDeviceChangedEvent](arkts-audio-audio-currentinputdevicechangedevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## onAudioSessionDeactivated

```TypeScript
onAudioSessionDeactivated(callback: Callback<AudioSessionDeactivatedEvent>): void
```

监听音频会话停用事件（当音频会话停用时触发）。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本23+：SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSessionDeactivatedEvent](arkts-audio-audio-audiosessiondeactivatedevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

**示例**

```TypeScript
audioSessionManager.onAudioSessionDeactivated((audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
  console.info(`Audio session deactivated, audioSessionDeactivatedEvent: ${JSON.stringify(audioSessionDeactivatedEvent)}.`);
});
```

## onAudioSessionStateChanged

```TypeScript
onAudioSessionStateChanged(callback: Callback<AudioSessionStateChangedEvent>): void
```

监听音频会话状态变更事件（当音频会话焦点变更时触发）。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSessionStateChangedEvent](arkts-audio-audio-audiosessionstatechangedevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800102](../errorcode-audio.md#6800102-分配内存失败) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
audioSessionManager.onAudioSessionStateChanged((audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
  console.info(`Audio session state changed, audioSessionStateChangedEvent: ${JSON.stringify(audioSessionStateChangedEvent)}.`);
});
```

## onAvailableDeviceChange

```TypeScript
onAvailableDeviceChange(deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void
```

监听音频可选设备连接状态变化事件（当音频可选设备连接状态发生变化时触发）。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
audioRoutingManager.onAvailableDeviceChange(audio.DeviceUsage.MEDIA_OUTPUT_DEVICES, (deviceChangeAction: audio.DeviceChangeAction) => {
  console.info(`Available device changed, deviceChangeAction: ${JSON.stringify(deviceChangeAction)}.`);
});
```

```TypeScript
audioSessionManager.onAvailableDeviceChange(audio.DeviceUsage.MEDIA_INPUT_DEVICES, (deviceChanged: audio.DeviceChangeAction) => {
  console.info(`Available device changed, deviceChangeAction: ${JSON.stringify(deviceChanged)}.`);
});
```

## onCurrentInputDeviceChanged

```TypeScript
onCurrentInputDeviceChanged(callback: Callback<CurrentInputDeviceChangedEvent>): void
```

监听当前输入设备变化事件（当前输入设备发生变化时触发）。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CurrentInputDeviceChangedEvent](arkts-audio-audio-currentinputdevicechangedevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
  console.info(`Current input device changed, currentInputDeviceChangedEvent: ${JSON.stringify(currentInputDeviceChangedEvent)}.`);
};

audioSessionManager.onCurrentInputDeviceChanged(currentInputDeviceChangedCallback);
```

## onCurrentOutputDeviceChanged

```TypeScript
onCurrentOutputDeviceChanged(callback: Callback<CurrentOutputDeviceChangedEvent>): void
```

监听当前输出设备变化事件（当前输出设备发生变化时触发）。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CurrentOutputDeviceChangedEvent](arkts-audio-audio-currentoutputdevicechangedevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800102](../errorcode-audio.md#6800102-分配内存失败) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
  console.info(`Current output device changed, currentOutputDeviceChangedEvent: ${JSON.stringify(currentOutputDeviceChangedEvent)}.`);
};

audioSessionManager.onCurrentOutputDeviceChanged(currentOutputDeviceChangedCallback);
```

## selectMediaInputDevice

```TypeScript
selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>
```

设置媒体输入设备。使用Promise异步回调。

> **说明：**&gt;
> - 本接口不适用于VoIP通话录音，即[SourceType](arkts-audio-audio-sourcetype-e.md)为SOURCE_TYPE_VOICE_COMMUNICATION的
> 场景不适用。&gt;
> - 本接口调用前需要先调用[getAvailableDevices](#getavailabledevices)接口查询到当前可用输入设备列表，从列表中选择输入
> 设备。&gt;
> - 当系统中存在其他更高优先级的应用录音流时，实际使用的输入设备会跟随其他高优先级应用所选的输入设备。&gt;
> - 应用程序可以监听[currentInputDeviceChanged](#oncurrentinputdevicechanged)事件来获得实际的输入设备
> 。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inputAudioDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 获取可用音频输入设备列表，用于后续选择输入设备
  let data: audio.AudioDeviceDescriptors = audioSessionManager.getAvailableDevices(audio.DeviceUsage.MEDIA_INPUT_DEVICES);
  console.info(`Succeeded in obtaining available devices, audioDeviceDescriptors: ${JSON.stringify(data)}.`);

  if (data[0]) {
    // 选择第一个可用设备作为音频输入设备。
    audioSessionManager.selectMediaInputDevice(data[0]).then(() => {
      console.info('Succeeded in selecting the media input device.');
    }).catch((selectErr: BusinessError) => {
      console.error(`Failed to select the media input device. Code: ${selectErr.code}, message: ${selectErr.message}`);
    });
  }
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain available devices. Code: ${error.code}, message: ${error.message}`);
}
```

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

> **说明：**&gt;
> 当音频会话在激活状态时调用此接口后，必须重新调用接口
> [activateAudioSession](#activateaudiosession)使其生效。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| behavior | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |

**示例**

```TypeScript
// 设置音频会话行为为被打断时静音，当音频被其他应用打断时自动静音。
let behavior = audio.AudioSessionBehaviorFlags.MUTE_WHEN_INTERRUPTED;
audioSessionManager.setAudioSessionBehavior(behavior);
```

## setAudioSessionScene

```TypeScript
setAudioSessionScene(scene: AudioSessionScene): void
```

设置音频会话场景参数。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scene | [AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
audioSessionManager.setAudioSessionScene(audio.AudioSessionScene.AUDIO_SESSION_SCENE_MEDIA);
```

## setBluetoothAndNearlinkPreferredRecordCategory

```TypeScript
setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>
```

设置在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。使用Promise异步回调。

> **说明：**&gt;
> - 应用程序可以在蓝牙或星闪连接之前设置此分类，系统将在设备连接时优先使用蓝牙或星闪进行录音。&gt;
> - 当系统中存在其他更高优先级的应用录音流时，实际使用的输入设备会跟随其他高优先级应用所选的输入设备。&gt;
> - 应用程序可以监听[currentInputDeviceChanged](#oncurrentinputdevicechanged)事件来获得实际的输入设备
> 。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| category | [BluetoothAndNearlinkPreferredRecordCategory](arkts-audio-audio-bluetoothandnearlinkpreferredrecordcategory-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 设置蓝牙和星闪录音偏好为低延迟模式，优先使用低延迟设备。
let category = audio.BluetoothAndNearlinkPreferredRecordCategory.PREFERRED_LOW_LATENCY;

audioSessionManager.setBluetoothAndNearlinkPreferredRecordCategory(category).then(() => {
  console.info('Succeeded in setting the bluetooth and nearlink preferred record category.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the bluetooth and nearlink preferred record category. Code: ${err.code}, message: ${err.message}`);
});
```

## setCapturerMuteHint

```TypeScript
setCapturerMuteHint(mute: boolean): Promise<void>
```

应用将当前音频会话内录音流的自身静音状态传递给系统音频模块。<!--RP1-->该接口不会触发录音流静音，当前仅在部分PC/2in1设备上用于优化设备功耗。<!--RP1End-->使用Promise异步回调。

> **说明：**&gt;
> - 该接口用于向系统音频模块上报当前音频会话内录音流的静音状态，不会改变录音流的实际静音状态。&gt;
> - 该接口仅在当前音频会话存在运行中的录音流时允许调用，否则返回错误码6800103。&gt;
> - 若某条录音流同时调用了流级接口[AudioCapturer.setMuteHint](arkts-audio-audio-audiocapturer-i.md#setmutehint)和本接口，
> 流级接口设置优先级更高，以流级接口设置值为准。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mute | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.setCapturerMuteHint(true).then(() => {
  console.info('Succeeded in setting the capturer mute hint.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the capturer mute hint. Code: ${err.code}, message: ${err.message}`);
});
```

## setDefaultOutputDevice

```TypeScript
setDefaultOutputDevice(deviceType: DeviceType): Promise<void>
```

设置默认发声设备。使用Promise方式进行异步回调。

> **说明：**&gt;
> - 本接口适用于以下情况：当设置的[AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md)为VoIP场景时，激活
> AudioSession后立即生效。若[AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md)为非VoIP场景，激活
> AudioSession时不会生效，仅在启动播放的[StreamUsage](arkts-audio-audio-streamusage-e.md)为语音消息、VoIP语音通话或VoIP视频通话时才
> 生效。支持听筒、扬声器和系统默认设备。&gt;
> - 本接口允许在AudioSessionManager创建后随时调用，系统会记录应用设置的默认本机内置发声设备。但只有激活AudioSession后才能生效。应用启动播放时，若外接设备如蓝牙耳机或有线耳机已接入，系统优先从
> 外接设备发声。否则，系统遵循应用设置的默认本机内置发声设备。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceType | [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800102](../errorcode-audio.md#6800102-分配内存失败) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 本接口允许在AudioRenderer创建以后的任何时间被调用。
// 未播放时调用，系统会记录应用设置的默认本机内置发声设备，当应用启动播放时从设置的默认本机内置发声设备发声。
// 正在播放时调用，在没有外接设备如蓝牙耳机/有线耳机，系统会立即切换到设置的默认本机内置发声设备发声；否则系统会先记录应用设置的默认本机内置发声设备，等外接设备移除后再切换到设置的默认本机内置发声设备发声。
audioRenderer.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('setDefaultOutputDevice Success!');
}).catch((err: BusinessError) => {
  console.error(`setDefaultOutputDevice Fail: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('Succeeded in setting the default output device.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the default output device. Code: ${err.code}, message: ${err.message}`);
});
```

## setMediaOutputDevice

```TypeScript
setMediaOutputDevice(deviceType: DeviceType): Promise<void>
```

当连接其他音频外设（如蓝牙耳机或有线耳机）时，将媒体输出设备切换为内置扬声器。使用Promise异步回调。

> **说明：**&gt;
> - 本接口仅适用于媒体播放场景，并且会作用于应用内发起的所有媒体流。&gt;
> - 若存在更高优先级的并发播放流或用户手动选择输出设备，则应用程序实际使用的输出设备将与本接口设置的设备不同。应用程序可通过监听
> [CurrentOutputDeviceChangedEvent](arkts-audio-audio-currentoutputdevicechangedevent-i.md)事件获取当前活跃的输
> 出设备。&gt;
> - 当应用程序需要清除之前通过接口设置的扬声器输出配置时，可通过调用接口将媒体输出设备设置为DEFAULT（系统默认设备）来实现。该设置仅在应用程序运行期间有效，当应用程序退出时，此接口的设置将自动清除。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceType | [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.setMediaOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('Succeeded in setting the media output device.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the media output device. Code: ${err.code}, message: ${err.message}`);
});
```
