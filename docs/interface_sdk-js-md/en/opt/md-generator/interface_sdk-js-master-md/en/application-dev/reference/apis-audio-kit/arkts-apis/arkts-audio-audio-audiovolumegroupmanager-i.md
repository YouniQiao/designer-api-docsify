# AudioVolumeGroupManager

This interface implements volume management for an audio group. Before calling any API in AudioVolumeGroupManager, you must use [getVolumeGroupManager](arkts-audio-audio-audiovolumemanager-i.md#getVolumeGroupManager) to obtain an AudioVolumeGroupManager instance. > **NOTE：**> > - The initial APIs of this interface are supported since API version 9.

**Since:** 23

**Deprecated since:** -1

<!--Device-audio-interface AudioVolumeGroupManager--><!--Device-audio-interface AudioVolumeGroupManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## getMaxAmplitudeForInputDevice

```TypeScript
getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>
```

Obtains the maximum amplitude (in the range [0, 1]) of the audio stream for an input device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<double>--><!--Device-AudioVolumeGroupManager-getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<double>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## getMaxAmplitudeForOutputDevice

```TypeScript
getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<number>
```

Obtains the maximum amplitude (in the range [0, 1]) of the audio stream for an output device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<double>--><!--Device-AudioVolumeGroupManager-getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<double>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| outputDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

Obtains the maximum volume level of a stream. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getMaxVolumeByStream)

<!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void--><!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void-End-->

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

Obtains the maximum volume level of a stream. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getMaxVolumeByStream)

<!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType): Promise<int>--><!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getMaxVolumeSync

```TypeScript
getMaxVolumeSync(volumeType: AudioVolumeType): number
```

Obtains the maximum volume level of a stream. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getMaxVolumeByStream)

<!--Device-AudioVolumeGroupManager-getMaxVolumeSync(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeGroupManager-getMaxVolumeSync(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

Obtains the minimum volume level of a stream. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getMinVolumeByStream)

<!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void--><!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void-End-->

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

Obtains the minimum volume level of a stream. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getMinVolumeByStream)

<!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType): Promise<int>--><!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getMinVolumeSync

```TypeScript
getMinVolumeSync(volumeType: AudioVolumeType): number
```

Obtains the minimum volume level of a stream. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getMinVolumeByStream)

<!--Device-AudioVolumeGroupManager-getMinVolumeSync(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeGroupManager-getMinVolumeSync(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getRingerMode

```TypeScript
getRingerMode(callback: AsyncCallback<AudioRingMode>): void
```

Obtains the ringer mode. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | Yes |

## getRingerMode

```TypeScript
getRingerMode(): Promise<AudioRingMode>
```

Obtains the ringer mode. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-getRingerMode(): Promise<AudioRingMode>--><!--Device-AudioVolumeGroupManager-getRingerMode(): Promise<AudioRingMode>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; |

## getRingerModeSync

```TypeScript
getRingerModeSync(): AudioRingMode
```

Obtains the ringer mode. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-getRingerModeSync(): AudioRingMode--><!--Device-AudioVolumeGroupManager-getRingerModeSync(): AudioRingMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioRingMode](arkts-audio-audio-audioringmode-e.md) |

## getSystemVolumeInDb

```TypeScript
getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void
```

Obtains the volume gain. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getVolumeInUnitOfDbByStream)

<!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType, callback: AsyncCallback<double>): void--><!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType, callback: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| [volumeLevel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md) | number | Yes |
| device | [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## getSystemVolumeInDb

```TypeScript
getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>
```

Obtains the volume gain. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getVolumeInUnitOfDbByStream)

<!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): Promise<double>--><!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): Promise<double>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| [volumeLevel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md) | number | Yes |
| device | [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## getSystemVolumeInDbSync

```TypeScript
getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number
```

Obtains the volume gain. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getVolumeInUnitOfDbByStream)

<!--Device-AudioVolumeGroupManager-getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double--><!--Device-AudioVolumeGroupManager-getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| [volumeLevel](arkts-audio-multimedia-avvolumepanel-avvolumepanel-s.md) | number | Yes |
| device | [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void
```

Obtains the volume level of a stream. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getVolumeByStream)

<!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void--><!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void-End-->

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

Obtains the volume level of a stream. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getVolumeByStream)

<!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType): Promise<int>--><!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getVolumeSync

```TypeScript
getVolumeSync(volumeType: AudioVolumeType): number
```

Obtains the volume level of a stream. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getVolumeByStream)

<!--Device-AudioVolumeGroupManager-getVolumeSync(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeGroupManager-getVolumeSync(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(callback: AsyncCallback<boolean>): void
```

Checks whether the microphone is muted. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void--><!--Device-AudioVolumeGroupManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(): Promise<boolean>
```

Checks whether the microphone is muted. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-isMicrophoneMute(): Promise<boolean>--><!--Device-AudioVolumeGroupManager-isMicrophoneMute(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isMicrophoneMuteSync

```TypeScript
isMicrophoneMuteSync(): boolean
```

Checks whether the microphone is muted. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-isMicrophoneMuteSync(): boolean--><!--Device-AudioVolumeGroupManager-isMicrophoneMuteSync(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

Checks whether a stream is muted. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#isSystemMutedForStream)

<!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

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

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#isSystemMutedForStream)

<!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isMuteSync

```TypeScript
isMuteSync(volumeType: AudioVolumeType): boolean
```

Checks whether a stream is muted. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#isSystemMutedForStream)

<!--Device-AudioVolumeGroupManager-isMuteSync(volumeType: AudioVolumeType): boolean--><!--Device-AudioVolumeGroupManager-isMuteSync(volumeType: AudioVolumeType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## isVolumeUnadjustable

```TypeScript
isVolumeUnadjustable(): boolean
```

Checks whether the fixed volume mode is enabled. When the fixed volume mode is enabled, the volume cannot be adjusted. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-isVolumeUnadjustable(): boolean--><!--Device-AudioVolumeGroupManager-isVolumeUnadjustable(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## offMicStateChange

```TypeScript
offMicStateChange(callback?: Callback<MicStateChangeEvent>): void
```

Unsubscribes to the microphone state change events.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-offMicStateChange(callback?: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-offMicStateChange(callback?: Callback<MicStateChangeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## offRingerModeChange

```TypeScript
offRingerModeChange(callback?: Callback<AudioRingMode>): void
```

Unsubscribes to the ringer mode state change events.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-offRingerModeChange(callback?: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-offRingerModeChange(callback?: Callback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## off_micStateChange

```TypeScript
off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void
```

Unsubscribes from the microphone state change event. This API uses an asynchronous callback to return the result.

**Since:** 12

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'micStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## off_ringerModeChange

```TypeScript
off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void
```

Unsubscribes from the ringer mode change event. This API uses an asynchronous callback to return the result.

**Since:** 18

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'ringerModeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## onMicStateChange

```TypeScript
onMicStateChange(callback: Callback<MicStateChangeEvent>): void
```

Listens for system microphone state change events. This method uses a callback to get microphone change events.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-onMicStateChange(callback: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-onMicStateChange(callback: Callback<MicStateChangeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## onRingerModeChange

```TypeScript
onRingerModeChange(callback: Callback<AudioRingMode>): void
```

Listens for ringer mode change events. This method uses a callback to get ringer mode changes.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-onRingerModeChange(callback: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-onRingerModeChange(callback: Callback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## on_micStateChange

```TypeScript
on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void
```

Subscribes to the microphone state change event, which is triggered when the microphone state is changed. This API uses an asynchronous callback to return the result. Currently, when multiple AudioManager instances are used in a single process, only the subscription of the last instance takes effect, and the subscription of other instances is overwritten (even if the last instance does not initiate a subscription). Therefore, you are advised to use a single AudioManager instance.

**Since:** 9

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'micStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## on_ringerModeChange

```TypeScript
on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void
```

Subscribes to the ringer mode change event, which is triggered when the [AudioRingMode](arkts-audio-audio-audioringmode-e.md#AudioRingMode) changes. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** -1

<!--Device-AudioVolumeGroupManager-on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'ringerModeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void
```

Mutes or unmutes the microphone. This method uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeGroupManager-setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioVolumeGroupManager-setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mute | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setMicrophoneMute

```TypeScript
setMicrophoneMute(mute: boolean): Promise<void>
```

Mutes or unmutes the microphone. This method uses a promise to return the result.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeGroupManager-setMicrophoneMute(mute: boolean): Promise<void>--><!--Device-AudioVolumeGroupManager-setMicrophoneMute(mute: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mute | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
