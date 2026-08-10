# AudioManager

音频音量和设备管理。

在使用AudioManager的接口之前，需先通过[getAudioManager](arkts-audio-audio-getaudiomanager-f.md#getaudiomanager)获取AudioManager实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioManager--><!--Device-audio-interface AudioManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## getAudioParameter

```TypeScript
getAudioParameter(key: string, callback: AsyncCallback<string>): void
```

获取指定音频参数值。使用callback异步回调。

本接口的使用场景为：根据硬件设备的支持能力扩展音频配置。在不同的设备平台上，所支持的音频参数会存在差异。示例代码内使用样例参数，实际支持的音频配置参数见具体设备平台的资料描述。

> **说明：**
> 
> 从API version 7开始支持，从API version 11开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

<!--Device-AudioManager-getAudioParameter(key: string, callback: AsyncCallback<string>): void--><!--Device-AudioManager-getAudioParameter(key: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 待获取的音频参数的键。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数。当获取指定音频参数值成功，err为undefined，data为获取到的指定音频参数值；否则为错误对象。 |

## getAudioParameter

```TypeScript
getAudioParameter(key: string): Promise<string>
```

获取指定音频参数值。使用Promise异步回调。

本接口的使用场景为：根据硬件设备的支持能力扩展音频配置。在不同的设备平台上，所支持的音频参数会存在差异。示例代码内使用样例参数，实际支持的音频配置参数见具体设备平台的资料描述。

> **说明：**
> 
> 从API version 7开始支持，从API version 11开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

<!--Device-AudioManager-getAudioParameter(key: string): Promise<string>--><!--Device-AudioManager-getAudioParameter(key: string): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 待获取的音频参数的键。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回获取的音频参数值。 |

## getAudioScene

```TypeScript
getAudioScene(callback: AsyncCallback<AudioScene>): void
```

获取音频场景模式。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioManager-getAudioScene(callback: AsyncCallback<AudioScene>): void--><!--Device-AudioManager-getAudioScene(callback: AsyncCallback<AudioScene>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioScene&gt; | Yes | 回调函数。当获取音频场景模式成功，err为undefined，data为获取到的音频场景模式；否则为错误对象。 |

## getAudioScene

```TypeScript
getAudioScene(): Promise<AudioScene>
```

获取音频场景模式。使用Promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioManager-getAudioScene(): Promise<AudioScene>--><!--Device-AudioManager-getAudioScene(): Promise<AudioScene>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioScene&gt; | Promise对象，返回音频场景模式。 |

## getAudioSceneSync

```TypeScript
getAudioSceneSync(): AudioScene
```

获取音频场景模式。同步返回结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AudioManager-getAudioSceneSync(): AudioScene--><!--Device-AudioManager-getAudioSceneSync(): AudioScene-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Return value:**

| Type | Description |
| --- | --- |
| [AudioScene](arkts-audio-audio-audioscene-e.md) | 音频场景模式。 |

## getDebuggingManager

```TypeScript
getDebuggingManager(): AudioDebuggingManager
```

获取音频调试管理器实例。该实例为单例，获取后可重复使用。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioManager-getDebuggingManager(): AudioDebuggingManager--><!--Device-AudioManager-getDebuggingManager(): AudioDebuggingManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDebuggingManager](arkts-audio-audio-audiodebuggingmanager-i.md) | 返回AudioDebuggingManager实例。 |

## getDeviceEnhanceManager

```TypeScript
getDeviceEnhanceManager(): AudioDeviceEnhanceManager
```

获取音频设备增强管理器实例。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioManager-getDeviceEnhanceManager(): AudioDeviceEnhanceManager--><!--Device-AudioManager-getDeviceEnhanceManager(): AudioDeviceEnhanceManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.DeviceEnhance

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDeviceEnhanceManager](arkts-audio-audio-audiodeviceenhancemanager-i.md) | 返回一个AudioDeviceEnhanceManager实例。 |

## getDevices

```TypeScript
getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void
```

获取音频设备列表。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#getDevices

<!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void--><!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-audio-audio-deviceflag-e.md) | Yes | 音频设备类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioDeviceDescriptors&gt; | Yes | 回调函数。当获取音频设备列表成功，err为undefined，data为获取到的音频设备列表；否则为错误对 象。 |

## getDevices

```TypeScript
getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>
```

获取音频设备列表。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#getDevices

<!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>--><!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-audio-audio-deviceflag-e.md) | Yes | 音频设备类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioDeviceDescriptors&gt; | Promise对象，返回设备列表。 |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

获取指定流的最大音量等级。使用callback异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getMaxVolume

<!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void--><!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 回调函数。当获取指定流的最大音量成功，err为undefined，data为获取到的指定流的最大音量等级；否则为错误对象。 |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType): Promise<number>
```

获取指定流的最大音量等级。使用Promise异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getMaxVolume

<!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType): Promise<number>--><!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType): Promise<number>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回最大音量等级。 |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

获取指定流的最小音量等级。使用callback异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getMinVolume

<!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void--><!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 回调函数。当获取指定流的最小音量成功，err为undefined，data为获取到的指定流的最小音量等级；否则为错误对象。 |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType): Promise<number>
```

获取指定流的最小音量等级。使用Promise异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getMinVolume

<!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType): Promise<number>--><!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType): Promise<number>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回最小音量等级。 |

## getRingerMode

```TypeScript
getRingerMode(callback: AsyncCallback<AudioRingMode>): void
```

获取铃声模式。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getRingerMode

<!--Device-AudioManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void--><!--Device-AudioManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioRingMode&gt; | Yes | 回调函数。当获取铃声模式成功，err为undefined，data为获取到的铃声模式；否则为错误对象。 |

## getRingerMode

```TypeScript
getRingerMode(): Promise<AudioRingMode>
```

获取铃声模式。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getRingerMode

<!--Device-AudioManager-getRingerMode(): Promise<AudioRingMode>--><!--Device-AudioManager-getRingerMode(): Promise<AudioRingMode>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioRingMode&gt; | Promise对象，返回系统的铃声模式。 |

## getRoutingManager

```TypeScript
getRoutingManager(): AudioRoutingManager
```

获取音频路由管理器。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioManager-getRoutingManager(): AudioRoutingManager--><!--Device-AudioManager-getRoutingManager(): AudioRoutingManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| [AudioRoutingManager](arkts-audio-audio-audioroutingmanager-i.md) | AudioRoutingManager实例。 |

## getSessionManager

```TypeScript
getSessionManager(): AudioSessionManager
```

获取音频会话管理器。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioManager-getSessionManager(): AudioSessionManager--><!--Device-AudioManager-getSessionManager(): AudioSessionManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md) | AudioSessionManager实例。 |

## getSpatializationManager

```TypeScript
getSpatializationManager(): AudioSpatializationManager
```

获取空间音频管理器。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AudioManager-getSpatializationManager(): AudioSpatializationManager--><!--Device-AudioManager-getSpatializationManager(): AudioSpatializationManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Return value:**

| Type | Description |
| --- | --- |
| [AudioSpatializationManager](arkts-audio-audio-audiospatializationmanager-i.md) | AudioSpatializationManager实例。 |

## getStreamManager

```TypeScript
getStreamManager(): AudioStreamManager
```

获取音频流管理器。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioManager-getStreamManager(): AudioStreamManager--><!--Device-AudioManager-getStreamManager(): AudioStreamManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AudioStreamManager](arkts-audio-audio-audiostreammanager-i.md) | AudioStreamManager实例。 |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

获取指定流的音量等级。使用callback异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getVolume

<!--Device-AudioManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void--><!--Device-AudioManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 回调函数。当获取指定流的音量成功，err为undefined，data为获取到的指定流的音量等级；否则为错误对象。指定流的音量等级范围可通 过 [getMinVolume](arkts-audio-audio-audiomanager-i.md#getminvolume) 和 [getMaxVolume](arkts-audio-audio-audiomanager-i.md#getmaxvolume) 获取。 |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType): Promise<number>
```

获取指定流的音量等级。使用Promise异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getVolume

<!--Device-AudioManager-getVolume(volumeType: AudioVolumeType): Promise<number>--><!--Device-AudioManager-getVolume(volumeType: AudioVolumeType): Promise<number>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回指定流的音量等级。指定流的音量等级范围可通过 [getMinVolume]{ |

## getVolumeManager

```TypeScript
getVolumeManager(): AudioVolumeManager
```

获取音频音量管理器。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AudioManager-getVolumeManager(): AudioVolumeManager--><!--Device-AudioManager-getVolumeManager(): AudioVolumeManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| Type | Description |
| --- | --- |
| [AudioVolumeManager](arkts-audio-audio-audiovolumemanager-i.md) | AudioVolumeManager实例。 |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

获取指定音量流的活跃状态。使用callback异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioStreamManager#isActive

<!--Device-AudioManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当获取指定音量流的活跃状态成功，err为undefined，data为true表示活跃，false表示不活跃；否则为错误对象。 |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType): Promise<boolean>
```

获取指定音量流的活跃状态。使用Promise异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioStreamManager#isActive

<!--Device-AudioManager-isActive(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioManager-isActive(volumeType: AudioVolumeType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示流状态为活跃；返回false表示流状态不活跃。 |

## isDeviceActive

```TypeScript
isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void
```

获取指定设备的激活状态。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#isCommunicationDeviceActive

<!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | Yes | 活跃音频设备类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当获取指定设备的激活状态成功，err为undefined，data为true表示激活，false表示未激活；否则为错误对象。 |

## isDeviceActive

```TypeScript
isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>
```

获取指定设备的激活状态。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#isCommunicationDeviceActive

<!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>--><!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | Yes | 活跃音频设备类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示设备已激活；返回false表示设备未激活。 |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(callback: AsyncCallback<boolean>): void
```

获取麦克风静音状态。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#isMicrophoneMute

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当获取麦克风静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(): Promise<boolean>
```

获取麦克风静音状态。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#isMicrophoneMute

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioManager-isMicrophoneMute(): Promise<boolean>--><!--Device-AudioManager-isMicrophoneMute(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示麦克风被静音；返回false表示麦克风未被静音。 |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

获取指定音量流的静音状态。使用callback异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#isMute

<!--Device-AudioManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当获取指定音量流的静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType): Promise<boolean>
```

获取指定音量流的静音状态。使用Promise异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。在API version 9-19

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#isMute

<!--Device-AudioManager-isMute(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioManager-isMute(volumeType: AudioVolumeType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示静音；返回false表示非静音。 |

## mute

```TypeScript
mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void
```

设置指定音量流静音。使用callback异步回调。

当该音量流可设置的最小音量不能为0时，不支持静音操作。例如：闹钟和通话。

> **说明：**
> 
> - 从API version 7开始支持，从API version 9开始废弃。
> 
> - 应用无法直接静音流音量，建议通过系统音量面板组件进行静音。具体样例和介绍请参考API文档
> [@ohos.multimedia.avVolumePanel (音量面板)](arkts-multimedia-avvolumepanel.md)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.avVolumePanel.AVVolumePanel

<!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |
| mute | boolean | Yes | 是否设置指定音量流为静音状态。true表示静音，false表示非静音。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当设置指定音量流静音成功，err为undefined，否则为错误对象。 |

## mute

```TypeScript
mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>
```

设置指定音量流静音。使用Promise异步回调。

当该音量流可设置的最小音量不能为0时，不支持静音操作。例如：闹钟和通话。

> **说明：**
> 
> - 从API version 7开始支持，从API version 9开始废弃。
> 
> - 应用无法直接静音流音量，建议通过系统音量面板组件进行静音。具体样例和介绍请参考API文档
> [@ohos.multimedia.avVolumePanel (音量面板)](arkts-multimedia-avvolumepanel.md)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.avVolumePanel.AVVolumePanel

<!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>--><!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |
| mute | boolean | Yes | 是否设置指定音量流为静音状态。true表示静音，false表示非静音。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

## off('audioSceneChange')

```TypeScript
off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void
```

取消监听音频场景变化事件。使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AudioManager-off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void--><!--Device-AudioManager-off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioSceneChange' | Yes | 事件回调类型，支持的事件为'audioSceneChange'，当取消监听当前音频场景变化事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioScene&gt; | No | 回调函数，返回当前音频场景模式。 |

## off('deviceChange')

```TypeScript
off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void
```

取消监听音频设备连接变化事件。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#event:deviceChange

<!--Device-AudioManager-off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void--><!--Device-AudioManager-off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceChange' | Yes | 事件回调类型，支持的事件为'deviceChange'，当取消监听音频设备连接变化事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceChangeAction&gt; | No | 回调函数，返回设备更新详情。 |

## off('interrupt')

```TypeScript
off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void
```

取消监听音频打断事件。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Substitutes:** ohos.multimedia.audio.AudioRenderer#event:audioInterrupt

<!--Device-AudioManager-off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void--><!--Device-AudioManager-off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'interrupt' | Yes | 事件回调类型，支持的事件为'interrupt'，当取消监听音频打断事件时，触发该事件。 |
| interrupt | [AudioInterrupt](arkts-audio-audio-audiointerrupt-i.md) | Yes | 音频打断事件类型的参数。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;InterruptAction&gt; | No | 回调函数，返回打断事件信息。 |

## offAudioSceneChange

```TypeScript
offAudioSceneChange(callback?: Callback<AudioScene>): void
```

Unsubscribes to audio scene change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioManager-offAudioSceneChange(callback?: Callback<AudioScene>): void--><!--Device-AudioManager-offAudioSceneChange(callback?: Callback<AudioScene>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioScene&gt; | No | Callback used in subscription. |

## on('audioSceneChange')

```TypeScript
on(type: 'audioSceneChange', callback: Callback<AudioScene>): void
```

监听音频场景变化事件。使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AudioManager-on(type: 'audioSceneChange', callback: Callback<AudioScene>): void--><!--Device-AudioManager-on(type: 'audioSceneChange', callback: Callback<AudioScene>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioSceneChange' | Yes | 事件回调类型，支持的事件为'audioSceneChange'，当音频场景模式发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioScene&gt; | Yes | 回调函数，返回当前音频场景模式。 |

## on('deviceChange')

```TypeScript
on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void
```

监听音频设备连接变化事件（当音频设备连接状态发生变化时触发）。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#event:deviceChange

<!--Device-AudioManager-on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void--><!--Device-AudioManager-on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceChange' | Yes | 事件回调类型，支持的事件为'deviceChange'，当音频设备连接状态发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceChangeAction&gt; | Yes | 回调函数，返回设备更新详情。 |

## on('interrupt')

```TypeScript
on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void
```

监听音频打断事件（当音频焦点发生变化时触发）。使用callback异步回调。

与[on('audioInterrupt')](audio.AudioRenderer.on(type: 'audioInterrupt', callback: Callback&lt;InterruptEvent&gt;))作用一致，均用于监听焦点变化。为无音频流的场景（未曾创建AudioRenderer对象），比如FM、语音唤醒等提供焦点变化监听功能。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Substitutes:** ohos.multimedia.audio.AudioRenderer#event:audioInterrupt

<!--Device-AudioManager-on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void--><!--Device-AudioManager-on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'interrupt' | Yes | 事件回调类型，支持的事件为'interrupt'，当音频焦点状态发生变化时，触发该事件。 |
| interrupt | [AudioInterrupt](arkts-audio-audio-audiointerrupt-i.md) | Yes | 音频打断事件类型的参数。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;InterruptAction&gt; | Yes | 回调函数，返回打断事件信息。 |

## onAudioSceneChange

```TypeScript
onAudioSceneChange(callback: Callback<AudioScene>): void
```

Subscribes to audio scene change events. When system changes communication scene status, registered clients will receive the callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioManager-onAudioSceneChange(callback: Callback<AudioScene>): void--><!--Device-AudioManager-onAudioSceneChange(callback: Callback<AudioScene>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioScene&gt; | Yes | Callback used to obtain the latest audio scene. |

## setAudioParameter

```TypeScript
setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void
```

音频参数设置。使用callback异步回调。

接口根据硬件设备的支持能力扩展音频配置。支持的参数与产品和设备强相关，非通用参数，示例代码内使用样例参数。

> **说明：**
> 
> 从API version 7开始支持，从API version 11开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Required permissions:** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioManager-setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 被设置的音频参数的键。 |
| value | string | Yes | 被设置的音频参数的值。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当音频参数设置成功，err为undefined，否则为错误对象。 |

## setAudioParameter

```TypeScript
setAudioParameter(key: string, value: string): Promise<void>
```

音频参数设置。使用Promise异步回调。

接口根据硬件设备的支持能力扩展音频配置。支持的参数与产品和设备强相关，非通用参数，示例代码内使用样例参数。

> **说明：**
> 
> 从API version 7开始支持，从API version 11开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Required permissions:** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioManager-setAudioParameter(key: string, value: string): Promise<void>--><!--Device-AudioManager-setAudioParameter(key: string, value: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 被设置的音频参数的键。 |
| value | string | Yes | 被设置的音频参数的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

## setDeviceActive

```TypeScript
setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void
```

设置设备激活状态。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#setCommunicationDevice

<!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | Yes | 活跃音频设备类型。 |
| active | boolean | Yes | 是否设置设备为激活状态。true表示已激活，false表示未激活。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当设置设备激活状态成功，err为undefined，否则为错误对象。 |

## setDeviceActive

```TypeScript
setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>
```

设置设备激活状态。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#setCommunicationDevice

<!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>--><!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | Yes | 活跃音频设备类型。 |
| active | boolean | Yes | 是否设置设备为激活状态。true表示已激活，false表示未激活。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void
```

设置麦克风静音状态。使用callback异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioManager-setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mute | boolean | Yes | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当设置麦克风静音状态成功，err为undefined，否则为错误对象。 |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean): Promise<void>
```

设置麦克风静音状态。使用Promise异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioManager-setMicrophoneMute(mute: boolean): Promise<void>--><!--Device-AudioManager-setMicrophoneMute(mute: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mute | boolean | Yes | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

## setRingerMode

```TypeScript
setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void
```

设置铃声模式。使用callback异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [AudioRingMode](arkts-audio-audio-audioringmode-e.md) | Yes | 音频铃声模式。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当设置铃声模式成功，err为undefined，否则为错误对象。 |

## setRingerMode

```TypeScript
setRingerMode(mode: AudioRingMode): Promise<void>
```

设置铃声模式。使用Promise异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setRingerMode(mode: AudioRingMode): Promise<void>--><!--Device-AudioManager-setRingerMode(mode: AudioRingMode): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [AudioRingMode](arkts-audio-audio-audioringmode-e.md) | Yes | 音频铃声模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

## setVolume

```TypeScript
setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void
```

设置指定流的音量等级。使用callback异步回调。

> **说明：**
> 
> - 从API version 7开始支持，从API version 9开始废弃。
> 
> - 应用无法直接调节系统音量，建议通过系统音量面板组件调节音量。具体样例和介绍请参考API文档
> [@ohos.multimedia.avVolumePanel (音量面板)](arkts-multimedia-avvolumepanel.md)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.avVolumePanel.AVVolumePanel

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |
| volume | number | Yes | 音量等级，可设置范围通过 [getMinVolume](arkts-audio-audio-audiomanager-i.md#getminvolume) 和 [getMaxVolume](arkts-audio-audio-audiomanager-i.md#getmaxvolume) 获取。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当设置指定流的音量成功，err为undefined，否则为错误对象。 |

## setVolume

```TypeScript
setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>
```

设置指定流的音量等级。使用Promise异步回调。

> **说明：**
> 
> - 从API version 7开始支持，从API version 9开始废弃。
> 
> - 应用无法直接调节系统音量，建议通过系统音量面板组件调节音量。具体样例和介绍请参考API文档
> [@ohos.multimedia.avVolumePanel (音量面板)](arkts-multimedia-avvolumepanel.md)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.avVolumePanel.AVVolumePanel

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>--><!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频音量类型。 |
| volume | number | Yes | 音量等级，可设置范围通过 [getMinVolume](arkts-audio-audio-audiomanager-i.md#getminvolume) 和 [getMaxVolume](arkts-audio-audio-audiomanager-i.md#getmaxvolume) 获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

