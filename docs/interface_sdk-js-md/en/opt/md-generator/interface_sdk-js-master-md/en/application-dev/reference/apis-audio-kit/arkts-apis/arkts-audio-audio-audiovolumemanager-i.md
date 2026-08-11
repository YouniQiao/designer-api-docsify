# AudioVolumeManager

This interface implements audio volume management.

Before calling any API in AudioVolumeManager, you must use  
[getVolumeManager](arkts-audio-audio-audiomanager-i.md#getvolumemanager) to obtain an AudioVolumeManager instance.

> **NOTE：**
> 
> - The initial APIs of this interface are supported since API version 9.

**Since:** 9

<!--Device-audio-interface AudioVolumeManager--><!--Device-audio-interface AudioVolumeManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## getAppVolumePercentage

```TypeScript
getAppVolumePercentage(): Promise<number>
```

Obtains the volume of the application. (The volume range is 0 to 100.) This API uses a promise to return the result.

**Since:** 19

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AudioVolumeManager-getAppVolumePercentage(): Promise<int>--><!--Device-AudioVolumeManager-getAppVolumePercentage(): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## getMaxVolumeByStream

```TypeScript
getMaxVolumeByStream(streamUsage: StreamUsage): number
```

Obtains the maximum volume of a specified audio stream.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AudioVolumeManager-getMaxVolumeByStream(streamUsage: StreamUsage): int--><!--Device-AudioVolumeManager-getMaxVolumeByStream(streamUsage: StreamUsage): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getMinVolumeByStream

```TypeScript
getMinVolumeByStream(streamUsage: StreamUsage): number
```

Obtains the minimum volume of a specified audio stream.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AudioVolumeManager-getMinVolumeByStream(streamUsage: StreamUsage): int--><!--Device-AudioVolumeManager-getMinVolumeByStream(streamUsage: StreamUsage): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getVolumeByStream

```TypeScript
getVolumeByStream(streamUsage: StreamUsage): number
```

Obtains the volume of a specified audio stream.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AudioVolumeManager-getVolumeByStream(streamUsage: StreamUsage): int--><!--Device-AudioVolumeManager-getVolumeByStream(streamUsage: StreamUsage): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getVolumeGroupManager

```TypeScript
getVolumeGroupManager(groupId: number, callback: AsyncCallback<AudioVolumeGroupManager>): void
```

Obtains a VolumeGroupManager instance. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-AudioVolumeManager-getVolumeGroupManager(groupId: int, callback: AsyncCallback<AudioVolumeGroupManager>): void--><!--Device-AudioVolumeManager-getVolumeGroupManager(groupId: int, callback: AsyncCallback<AudioVolumeGroupManager>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| groupId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioVolumeGroupManager&gt; | Yes |

## getVolumeGroupManager

```TypeScript
getVolumeGroupManager(groupId: number): Promise<AudioVolumeGroupManager>
```

Obtains a VolumeGroupManager instance. This API uses a promise to return the result.

**Since:** 9

<!--Device-AudioVolumeManager-getVolumeGroupManager(groupId: int): Promise<AudioVolumeGroupManager>--><!--Device-AudioVolumeManager-getVolumeGroupManager(groupId: int): Promise<AudioVolumeGroupManager>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| groupId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;AudioVolumeGroupManager&gt; |

## getVolumeGroupManagerSync

```TypeScript
getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager
```

Obtains a VolumeGroupManager instance. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AudioVolumeManager-getVolumeGroupManagerSync(groupId: int): AudioVolumeGroupManager--><!--Device-AudioVolumeManager-getVolumeGroupManagerSync(groupId: int): AudioVolumeGroupManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| groupId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioVolumeGroupManager](arkts-audio-audio-audiovolumegroupmanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getVolumeInUnitOfDbByStream

```TypeScript
getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: number, device: DeviceType): number
```

Obtains the volume (in dB) calculated by the system based on the audio stream, volume level, and device type.

**Since:** 20

<!--Device-AudioVolumeManager-getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: int, device: DeviceType): double--><!--Device-AudioVolumeManager-getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: int, device: DeviceType): double-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |
| volumeLevel | number | Yes |
| device | [DeviceType](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-devicetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## isSystemMutedForStream

```TypeScript
isSystemMutedForStream(streamUsage: StreamUsage): boolean
```

Checks whether a specified audio stream is muted.

**Since:** 20

<!--Device-AudioVolumeManager-isSystemMutedForStream(streamUsage: StreamUsage): boolean--><!--Device-AudioVolumeManager-isSystemMutedForStream(streamUsage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## off('volumeChange')

```TypeScript
off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void
```

Unsubscribes from the system volume change event. This API uses an asynchronous callback to return the result.

**Since:** 12

**Deprecated since:** 20

**Substitutes:** ohos.multimedia.audio.AudioVolumeManager#event:streamVolumeChange

<!--Device-AudioVolumeManager-off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'volumeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VolumeEvent&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## off('appVolumeChange')

```TypeScript
off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void
```

Unsubscribes from the application-level volume change event of the application. This API uses an asynchronous callback to return the result.

**Since:** 19

<!--Device-AudioVolumeManager-off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'appVolumeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VolumeEvent&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## off('streamVolumeChange')

```TypeScript
off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void
```

Unsubscribes from the system audio volume change event, which is triggered when the system audio volume is changed. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-AudioVolumeManager-off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void--><!--Device-AudioVolumeManager-off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'streamVolumeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StreamVolumeEvent&gt; | No |

## on('volumeChange')

```TypeScript
on(type: 'volumeChange', callback: Callback<VolumeEvent>): void
```

Subscribes to the system volume change event, which is triggered when the system volume is changed. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** ohos.multimedia.audio.AudioVolumeManager#event:streamVolumeChange

<!--Device-AudioVolumeManager-on(type: 'volumeChange', callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-on(type: 'volumeChange', callback: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'volumeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VolumeEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## on('appVolumeChange')

```TypeScript
on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void
```

Subscribes to the application-level volume change event of the application (triggered when the application-level volume is changed). This API uses an asynchronous callback to return the result.

**Since:** 19

<!--Device-AudioVolumeManager-on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'appVolumeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VolumeEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## on('streamVolumeChange')

```TypeScript
on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void
```

Subscribes to the system audio volume change event, which is triggered when the system audio volume is changed.This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-AudioVolumeManager-on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void--><!--Device-AudioVolumeManager-on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'streamVolumeChange' | Yes |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StreamVolumeEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## setAppVolumePercentage

```TypeScript
setAppVolumePercentage(volume: number): Promise<void>
```

Sets the volume (within a range of 0 to 100) for the application. This API uses a promise to return the result.

**Since:** 19

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AudioVolumeManager-setAppVolumePercentage(volume: int): Promise<void>--><!--Device-AudioVolumeManager-setAppVolumePercentage(volume: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volume | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |
