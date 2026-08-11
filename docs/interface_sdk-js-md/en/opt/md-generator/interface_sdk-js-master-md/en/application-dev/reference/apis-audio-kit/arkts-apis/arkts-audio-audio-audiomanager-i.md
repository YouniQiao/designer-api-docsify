# AudioManager

This interface implements audio volume and device management.

Before calling any API in AudioManager, you must use  
[getAudioManager](arkts-audio-audio-getaudiomanager-f.md#getaudiomanager) to obtain an AudioManager instance.

**Since:** 7

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

Obtains the value of an audio parameter. This method uses an asynchronous callback to return the query result.

**Since:** 7

**Deprecated since:** 11

<!--Device-AudioManager-getAudioParameter(key: string, callback: AsyncCallback<string>): void--><!--Device-AudioManager-getAudioParameter(key: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getAudioParameter

```TypeScript
getAudioParameter(key: string): Promise<string>
```

Obtains the value of an audio parameter. This method uses a promise to return the query result.

**Since:** 7

**Deprecated since:** 11

<!--Device-AudioManager-getAudioParameter(key: string): Promise<string>--><!--Device-AudioManager-getAudioParameter(key: string): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

## getAudioScene

```TypeScript
getAudioScene(callback: AsyncCallback<AudioScene>): void
```

Obtains the audio scene. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-AudioManager-getAudioScene(callback: AsyncCallback<AudioScene>): void--><!--Device-AudioManager-getAudioScene(callback: AsyncCallback<AudioScene>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioScene&gt; | Yes |

## getAudioScene

```TypeScript
getAudioScene(): Promise<AudioScene>
```

Obtains the audio scene. This API uses a promise to return the result.

**Since:** 8

<!--Device-AudioManager-getAudioScene(): Promise<AudioScene>--><!--Device-AudioManager-getAudioScene(): Promise<AudioScene>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;AudioScene&gt; |

## getAudioSceneSync

```TypeScript
getAudioSceneSync(): AudioScene
```

Obtains the audio scene. This API returns the result synchronously.

**Since:** 10

<!--Device-AudioManager-getAudioSceneSync(): AudioScene--><!--Device-AudioManager-getAudioSceneSync(): AudioScene-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioScene](arkts-audio-audio-audioscene-e.md) |

## getDebuggingManager

```TypeScript
getDebuggingManager(): AudioDebuggingManager
```

Obtains an AudioDebuggingManager instance.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:The {@link #AudioDebuggingManager} instance is a singleton.&lt;/p&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioManager-getDebuggingManager(): AudioDebuggingManager--><!--Device-AudioManager-getDebuggingManager(): AudioDebuggingManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioDebuggingManager](arkts-audio-audio-audiodebuggingmanager-i.md) |

## getDeviceEnhanceManager

```TypeScript
getDeviceEnhanceManager(): AudioDeviceEnhanceManager
```

Obtains a device enhancement manager instance.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioManager-getDeviceEnhanceManager(): AudioDeviceEnhanceManager--><!--Device-AudioManager-getDeviceEnhanceManager(): AudioDeviceEnhanceManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.DeviceEnhance

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioDeviceEnhanceManager](arkts-audio-audio-audiodeviceenhancemanager-i.md) |

## getDevices

```TypeScript
getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void
```

Obtains the audio devices with a specific flag. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#getDevices

<!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void--><!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-audio-audio-deviceflag-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioDeviceDescriptors&gt; | Yes |

## getDevices

```TypeScript
getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>
```

Obtains the audio devices with a specific flag. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#getDevices

<!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>--><!--Device-AudioManager-getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-audio-audio-deviceflag-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;AudioDeviceDescriptors&gt; |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

Obtains the maximum volume allowed for a stream. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getMaxVolume

<!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void--><!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType): Promise<number>
```

Obtains the maximum volume allowed for a stream. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getMaxVolume

<!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType): Promise<number>--><!--Device-AudioManager-getMaxVolume(volumeType: AudioVolumeType): Promise<number>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

Obtains the minimum volume allowed for a stream. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getMinVolume

<!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void--><!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType): Promise<number>
```

Obtains the minimum volume allowed for a stream. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getMinVolume

<!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType): Promise<number>--><!--Device-AudioManager-getMinVolume(volumeType: AudioVolumeType): Promise<number>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## getRecordingManager

```TypeScript
getRecordingManager(): AudioRecordingManager
```

Obtains a recording manager instance. Provides recording strategy management, including collaborative recording and recording control capabilities.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioManager-getRecordingManager(): AudioRecordingManager--><!--Device-AudioManager-getRecordingManager(): AudioRecordingManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioRecordingManager](arkts-audio-audio-audiorecordingmanager-i.md) |

## getRingerMode

```TypeScript
getRingerMode(callback: AsyncCallback<AudioRingMode>): void
```

Obtains the ringer mode. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getRingerMode

<!--Device-AudioManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void--><!--Device-AudioManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioRingMode&gt; | Yes |

## getRingerMode

```TypeScript
getRingerMode(): Promise<AudioRingMode>
```

Obtains the ringer mode. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getRingerMode

<!--Device-AudioManager-getRingerMode(): Promise<AudioRingMode>--><!--Device-AudioManager-getRingerMode(): Promise<AudioRingMode>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;AudioRingMode&gt; |

## getRoutingManager

```TypeScript
getRoutingManager(): AudioRoutingManager
```

Obtains an AudioRoutingManager instance.

**Since:** 9

<!--Device-AudioManager-getRoutingManager(): AudioRoutingManager--><!--Device-AudioManager-getRoutingManager(): AudioRoutingManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioRoutingManager](arkts-audio-audio-audioroutingmanager-i.md) |

## getSessionManager

```TypeScript
getSessionManager(): AudioSessionManager
```

Obtains an AudioSessionManager instance.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioManager-getSessionManager(): AudioSessionManager--><!--Device-AudioManager-getSessionManager(): AudioSessionManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md) |

## getSpatializationManager

```TypeScript
getSpatializationManager(): AudioSpatializationManager
```

Obtains an AudioSpatializationManager instance.

**Since:** 18

<!--Device-AudioManager-getSpatializationManager(): AudioSpatializationManager--><!--Device-AudioManager-getSpatializationManager(): AudioSpatializationManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioSpatializationManager](arkts-audio-audio-audiospatializationmanager-i.md) |

## getStreamManager

```TypeScript
getStreamManager(): AudioStreamManager
```

Obtains an AudioStreamManager instance.

**Since:** 9

<!--Device-AudioManager-getStreamManager(): AudioStreamManager--><!--Device-AudioManager-getStreamManager(): AudioStreamManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioStreamManager](arkts-audio-audio-audiostreammanager-i.md) |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

Obtains the volume of a stream. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getVolume

<!--Device-AudioManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void--><!--Device-AudioManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType): Promise<number>
```

Obtains the volume of a stream. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#getVolume

<!--Device-AudioManager-getVolume(volumeType: AudioVolumeType): Promise<number>--><!--Device-AudioManager-getVolume(volumeType: AudioVolumeType): Promise<number>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## getVolumeManager

```TypeScript
getVolumeManager(): AudioVolumeManager
```

Obtains an AudioVolumeManager instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AudioManager-getVolumeManager(): AudioVolumeManager--><!--Device-AudioManager-getVolumeManager(): AudioVolumeManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioVolumeManager](arkts-audio-audio-audiovolumemanager-i.md) |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

Checks whether a stream is active. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioStreamManager#isActive

<!--Device-AudioManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType): Promise<boolean>
```

Checks whether a stream is active. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioStreamManager#isActive

<!--Device-AudioManager-isActive(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioManager-isActive(volumeType: AudioVolumeType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## isDeviceActive

```TypeScript
isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void
```

Checks whether a device is active. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#isCommunicationDeviceActive

<!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isDeviceActive

```TypeScript
isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>
```

Checks whether a device is active. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#isCommunicationDeviceActive

<!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>--><!--Device-AudioManager-isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(callback: AsyncCallback<boolean>): void
```

Checks whether the microphone is muted. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#isMicrophoneMute

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(): Promise<boolean>
```

Checks whether the microphone is muted. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#isMicrophoneMute

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioManager-isMicrophoneMute(): Promise<boolean>--><!--Device-AudioManager-isMicrophoneMute(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

Checks whether a stream is muted. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#isMute

<!--Device-AudioManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType): Promise<boolean>
```

Checks whether a stream is muted. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#isMute

<!--Device-AudioManager-isMute(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioManager-isMute(volumeType: AudioVolumeType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## mute

```TypeScript
mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void
```

Mutes a volume type. This method uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.avVolumePanel.AVVolumePanel

<!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| [mute](#mute) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## mute

```TypeScript
mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>
```

Mutes a volume type. This method uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.avVolumePanel.AVVolumePanel

<!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>--><!--Device-AudioManager-mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| [mute](#mute) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## off('audioSceneChange')

```TypeScript
off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void
```

Unsubscribes from the audio scene change event. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-AudioManager-off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void--><!--Device-AudioManager-off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioSceneChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioScene&gt; | No |

## off('deviceChange')

```TypeScript
off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void
```

Unsubscribes from the audio device change event. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#event:deviceChange

<!--Device-AudioManager-off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void--><!--Device-AudioManager-off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceChangeAction&gt; | No |

## off('interrupt')

```TypeScript
off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void
```

Unsubscribes from the audio interruption event. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** ohos.multimedia.audio.AudioRenderer#event:audioInterrupt

<!--Device-AudioManager-off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void--><!--Device-AudioManager-off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'interrupt' | Yes |
| interrupt | [AudioInterrupt](arkts-audio-audio-audiointerrupt-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;InterruptAction&gt; | No |

## on('audioSceneChange')

```TypeScript
on(type: 'audioSceneChange', callback: Callback<AudioScene>): void
```

Subscribes to the audio scene change event. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-AudioManager-on(type: 'audioSceneChange', callback: Callback<AudioScene>): void--><!--Device-AudioManager-on(type: 'audioSceneChange', callback: Callback<AudioScene>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioSceneChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioScene&gt; | Yes |

## on('deviceChange')

```TypeScript
on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void
```

Subscribes to the event indicating that the connection status of an audio device is changed. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#event:deviceChange

<!--Device-AudioManager-on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void--><!--Device-AudioManager-on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceChangeAction&gt; | Yes |

## on('interrupt')

```TypeScript
on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void
```

Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an asynchronous callback to return the result.

Same as  
[on('audioInterrupt')](@ohos.multimedia.audio:audio.AudioRenderer.on(type: 'audioInterrupt', callback: Callback&lt;InterruptEvent&gt;)), this API is used to listen for focus changes. However, this API is used in scenarios without audio streams (no AudioRenderer instance is created), such as frequency modulation (FM) and voice wakeup.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** ohos.multimedia.audio.AudioRenderer#event:audioInterrupt

<!--Device-AudioManager-on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void--><!--Device-AudioManager-on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'interrupt' | Yes |
| interrupt | [AudioInterrupt](arkts-audio-audio-audiointerrupt-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;InterruptAction&gt; | Yes |

## setAudioParameter

```TypeScript
setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void
```

Sets an audio parameter. This method uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 11

**Required permissions:** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioManager-setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setAudioParameter

```TypeScript
setAudioParameter(key: string, value: string): Promise<void>
```

Sets an audio parameter. This method uses a promise to return the result.

**Since:** 7

**Deprecated since:** 11

**Required permissions:** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioManager-setAudioParameter(key: string, value: string): Promise<void>--><!--Device-AudioManager-setAudioParameter(key: string, value: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## setDeviceActive

```TypeScript
setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void
```

Sets a device to the active state. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#setCommunicationDevice

<!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | Yes |
| active | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setDeviceActive

```TypeScript
setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>
```

Sets a device to the active state. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRoutingManager#setCommunicationDevice

<!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>--><!--Device-AudioManager-setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-audio-audio-activedevicetype-e.md) | Yes |
| active | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void
```

Mutes or unmutes the microphone. This method uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioManager-setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [mute](#mute) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean): Promise<void>
```

Mutes or unmutes the microphone. This method uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioManager-setMicrophoneMute(mute: boolean): Promise<void>--><!--Device-AudioManager-setMicrophoneMute(mute: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [mute](#mute) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## setRingerMode

```TypeScript
setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void
```

Sets the ringer mode. This method uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AudioRingMode](arkts-audio-audio-audioringmode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setRingerMode

```TypeScript
setRingerMode(mode: AudioRingMode): Promise<void>
```

Sets the ringer mode. This method uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setRingerMode(mode: AudioRingMode): Promise<void>--><!--Device-AudioManager-setRingerMode(mode: AudioRingMode): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AudioRingMode](arkts-audio-audio-audioringmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## setVolume

```TypeScript
setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void
```

Sets the volume for a volume type. This method uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.avVolumePanel.AVVolumePanel

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void--><!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| volume | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setVolume

```TypeScript
setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>
```

Sets the volume for a volume type. This method uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.avVolumePanel.AVVolumePanel

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>--><!--Device-AudioManager-setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| volume | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |
