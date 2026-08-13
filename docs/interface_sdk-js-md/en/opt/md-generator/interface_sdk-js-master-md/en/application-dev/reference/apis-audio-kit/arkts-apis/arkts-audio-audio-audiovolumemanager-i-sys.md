# AudioVolumeManager

This interface implements audio volume management. Before calling any API in AudioVolumeManager, you must use [getVolumeManager](arkts-audio-audio-audiomanager-i.md#getVolumeManager) to obtain an AudioVolumeManager instance. > **NOTE：**> > - The initial APIs of this interface are supported since API version 9.

**Since:** 23

**Deprecated since:** -1

<!--Device-audio-interface AudioVolumeManager--><!--Device-audio-interface AudioVolumeManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## forceVolumeKeyControlType

```TypeScript
forceVolumeKeyControlType(volumeType: AudioVolumeType, duration: number): void
```

Interface for forcibly setting the volume type by pressing the volume key.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioVolumeManager-forceVolumeKeyControlType(volumeType: AudioVolumeType, duration: int): void--><!--Device-AudioVolumeManager-forceVolumeKeyControlType(volumeType: AudioVolumeType, duration: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| duration | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## getActiveStreamsVolumeInfo

```TypeScript
getActiveStreamsVolumeInfo(): ActiveStreamsVolumeInfoArray
```

Obtains the Volume information of the active audio streams.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioVolumeManager-getActiveStreamsVolumeInfo(): ActiveStreamsVolumeInfoArray--><!--Device-AudioVolumeManager-getActiveStreamsVolumeInfo(): ActiveStreamsVolumeInfoArray-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ActiveStreamsVolumeInfoArray](arkts-audio-audio-activestreamsvolumeinfoarray-t-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## getAppVolumePercentageForUid

```TypeScript
getAppVolumePercentageForUid(uid: number): Promise<number>
```

Get the volume for specified app with range from 0 to 100. Applications with same uid share the same volume.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-getAppVolumePercentageForUid(uid: int): Promise<int>--><!--Device-AudioVolumeManager-getAppVolumePercentageForUid(uid: int): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let uid: number = 20010041; // Application ID.

audioVolumeManager.getAppVolumePercentageForUid(20010041).then((value: number) => {
  console.info(`app volume is ${value}.`);
});
```

## getAudioVolumeTypeByStreamUsage

```TypeScript
getAudioVolumeTypeByStreamUsage(streamUsage: StreamUsage): AudioVolumeType
```

Obtains volume type by stream type.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getAudioVolumeTypeByStreamUsage(streamUsage: StreamUsage): AudioVolumeType--><!--Device-AudioVolumeManager-getAudioVolumeTypeByStreamUsage(streamUsage: StreamUsage): AudioVolumeType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getMaxSystemVolume

```TypeScript
getMaxSystemVolume(volumeType: AudioVolumeType): number
```

Obtains the maximum volume allowed for a volume type.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getMaxSystemVolume(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeManager-getMaxSystemVolume(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

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
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getMinSystemVolume

```TypeScript
getMinSystemVolume(volumeType: AudioVolumeType): number
```

Obtains the minimum volume allowed for a volume type.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getMinSystemVolume(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeManager-getMinSystemVolume(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

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
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getMinSystemVolumePercentage

```TypeScript
getMinSystemVolumePercentage(volumeType: AudioVolumeType): number
```

Gets the minimum system volume percentage application can set for specified volume type.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getMinSystemVolumePercentage(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeManager-getMinSystemVolumePercentage(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

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
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getStreamUsagesByVolumeType

```TypeScript
getStreamUsagesByVolumeType(volumeType: AudioVolumeType): StreamUsageArray
```

Obtains stream types by volume type.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getStreamUsagesByVolumeType(volumeType: AudioVolumeType): StreamUsageArray--><!--Device-AudioVolumeManager-getStreamUsagesByVolumeType(volumeType: AudioVolumeType): StreamUsageArray-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StreamUsageArray](arkts-audio-audio-streamusagearray-t-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getSupportedAudioVolumeTypes

```TypeScript
getSupportedAudioVolumeTypes(): Array<Readonly<AudioVolumeType>>
```

Obtains system supported volume types.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getSupportedAudioVolumeTypes(): Array<Readonly<AudioVolumeType>>--><!--Device-AudioVolumeManager-getSupportedAudioVolumeTypes(): Array<Readonly<AudioVolumeType>>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;[AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getSystemVolume

```TypeScript
getSystemVolume(volumeType: AudioVolumeType): number
```

Obtains the volume of a volume type.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getSystemVolume(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeManager-getSystemVolume(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

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
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getSystemVolumeByUid

```TypeScript
getSystemVolumeByUid(volumeType: AudioVolumeType, callingUid: number): number
```

Obtains the volume of streams in specific uid application.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getSystemVolumeByUid(volumeType: AudioVolumeType, callingUid: int): int--><!--Device-AudioVolumeManager-getSystemVolumeByUid(volumeType: AudioVolumeType, callingUid: int): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| callingUid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## getSystemVolumePercentage

```TypeScript
getSystemVolumePercentage(volumeType: AudioVolumeType): number
```

Gets the current system volume percentage for specified volume type.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getSystemVolumePercentage(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeManager-getSystemVolumePercentage(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

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
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getVolumeGroupInfos

```TypeScript
getVolumeGroupInfos(networkId: string, callback: AsyncCallback<VolumeGroupInfos>): void
```

Get the volume group list for a networkId. This method uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getVolumeGroupInfos(networkId: string, callback: AsyncCallback<VolumeGroupInfos>): void--><!--Device-AudioVolumeManager-getVolumeGroupInfos(networkId: string, callback: AsyncCallback<VolumeGroupInfos>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[VolumeGroupInfos](arkts-audio-audio-volumegroupinfos-t-sys.md)&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeManager.getVolumeGroupInfos(audio.LOCAL_NETWORK_ID, (err: BusinessError, value: audio.VolumeGroupInfos) => {
  if (err) {
    console.error(`Failed to obtain the volume group infos list. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the volume group infos list is obtained.');
});
```

## getVolumeGroupInfos

```TypeScript
getVolumeGroupInfos(networkId: string): Promise<VolumeGroupInfos>
```

Get the volume group list for a networkId. This method uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getVolumeGroupInfos(networkId: string): Promise<VolumeGroupInfos>--><!--Device-AudioVolumeManager-getVolumeGroupInfos(networkId: string): Promise<VolumeGroupInfos>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[VolumeGroupInfos](arkts-audio-audio-volumegroupinfos-t-sys.md)&gt; |

## Examples

```TypeScript
async function getVolumeGroupInfos(){
  let volumegroupinfos: audio.VolumeGroupInfos = await audio.getAudioManager().getVolumeManager().getVolumeGroupInfos(audio.LOCAL_NETWORK_ID);
  console.info('Promise returned to indicate that the volumeGroup list is obtained.'+JSON.stringify(volumegroupinfos))
}
```

## getVolumeGroupInfosSync

```TypeScript
getVolumeGroupInfosSync(networkId: string): VolumeGroupInfos
```

Get the volume group list for a networkId.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getVolumeGroupInfosSync(networkId: string): VolumeGroupInfos--><!--Device-AudioVolumeManager-getVolumeGroupInfosSync(networkId: string): VolumeGroupInfos-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VolumeGroupInfos](arkts-audio-audio-volumegroupinfos-t-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let volumegroupinfos: audio.VolumeGroupInfos = audioVolumeManager.getVolumeGroupInfosSync(audio.LOCAL_NETWORK_ID);
  console.info(`Indicate that the volumeGroup list is obtained. ${JSON.stringify(volumegroupinfos)}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volumeGroup list ${error}`);
}
```

## getVolumeInUnitOfDb

```TypeScript
getVolumeInUnitOfDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number
```

Gets the volume db value that system calculate by volume type, volume level and device type.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-getVolumeInUnitOfDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double--><!--Device-AudioVolumeManager-getVolumeInUnitOfDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

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
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isAppVolumeMutedForUid

```TypeScript
isAppVolumeMutedForUid(uid: number, owned: boolean): Promise<boolean>
```

Checks whether the app volume is muted. If there are multiple callers setting muted states, only when all callers cancel muted state the volume of this app will be truly unmuted.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-isAppVolumeMutedForUid(uid: int, owned: boolean): Promise<boolean>--><!--Device-AudioVolumeManager-isAppVolumeMutedForUid(uid: int, owned: boolean): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |
| owned | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isSystemMuted

```TypeScript
isSystemMuted(volumeType: AudioVolumeType): boolean
```

Checks whether a volume type is muted.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-isSystemMuted(volumeType: AudioVolumeType): boolean--><!--Device-AudioVolumeManager-isSystemMuted(volumeType: AudioVolumeType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

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
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offActiveVolumeTypeChange

```TypeScript
offActiveVolumeTypeChange(callback?: Callback<AudioVolumeType>): void
```

Unsubscribes from active volume type changes.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-offActiveVolumeTypeChange(callback?: Callback<AudioVolumeType>): void--><!--Device-AudioVolumeManager-offActiveVolumeTypeChange(callback?: Callback<AudioVolumeType>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offAppVolumeChangeForUid

```TypeScript
offAppVolumeChangeForUid(callback?: Callback<VolumeEvent>): void
```

Unsubscribes to the app volume change events..

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-offAppVolumeChangeForUid(callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-offAppVolumeChangeForUid(callback?: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offSystemVolumeChange

```TypeScript
offSystemVolumeChange(callback?: Callback<VolumeEvent>): void
```

Unsubscribes to the system volume change events.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-offSystemVolumeChange(callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-offSystemVolumeChange(callback?: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offSystemVolumeChangeByFilter

```TypeScript
offSystemVolumeChangeByFilter(callback?: Callback<VolumeEvent>): void
```

Unsubscribes from the system volume change events.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioVolumeManager-offSystemVolumeChangeByFilter(callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-offSystemVolumeChangeByFilter(callback?: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offVolumePercentageChange

```TypeScript
offVolumePercentageChange(callback?: Callback<VolumeEvent>): void
```

Unsubscribes from system volume percentage change events.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-offVolumePercentageChange(callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-offVolumePercentageChange(callback?: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off_activeVolumeTypeChange

```TypeScript
off(type: 'activeVolumeTypeChange', callback?: Callback<AudioVolumeType>): void
```

Unsubscribes from active volume type changes.

**Since:** 20

**Deprecated since:** -1

<!--Device-AudioVolumeManager-off(type: 'activeVolumeTypeChange', callback?: Callback<AudioVolumeType>): void--><!--Device-AudioVolumeManager-off(type: 'activeVolumeTypeChange', callback?: Callback<AudioVolumeType>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'activeVolumeTypeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off_appVolumeChangeForUid

```TypeScript
off(type: 'appVolumeChangeForUid', callback?: Callback<VolumeEvent>): void
```

Unsubscribes to the app volume change events..

**Since:** 19

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-off(type: 'appVolumeChangeForUid', callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-off(type: 'appVolumeChangeForUid', callback?: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'appVolumeChangeForUid' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off_systemVolumeChange

```TypeScript
off(type: 'systemVolumeChange', callback?: Callback<VolumeEvent>): void
```

Unsubscribes to the system volume change events.

**Since:** 20

**Deprecated since:** -1

<!--Device-AudioVolumeManager-off(type: 'systemVolumeChange', callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-off(type: 'systemVolumeChange', callback?: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemVolumeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onActiveVolumeTypeChange

```TypeScript
onActiveVolumeTypeChange(callback: Callback<AudioVolumeType>): void
```

Subscribes to active volume type changes.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-onActiveVolumeTypeChange(callback: Callback<AudioVolumeType>): void--><!--Device-AudioVolumeManager-onActiveVolumeTypeChange(callback: Callback<AudioVolumeType>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onAppVolumeChangeForUid

```TypeScript
onAppVolumeChangeForUid(uid: number, callback: Callback<VolumeEvent>): void
```

Listens for specified app volume change events. The app volume may changed by [setAppVolumePercentageForUid](#setAppVolumePercentageForUid).

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-onAppVolumeChangeForUid(uid: int, callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-onAppVolumeChangeForUid(uid: int, callback: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onSystemVolumeChange

```TypeScript
onSystemVolumeChange(callback: Callback<VolumeEvent>): void
```

Listens for system volume change events. This method uses a callback to get volume change events.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-onSystemVolumeChange(callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-onSystemVolumeChange(callback: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onSystemVolumeChangeByFilter

```TypeScript
onSystemVolumeChangeByFilter(filter: SystemVolumeFilter, callback: Callback<VolumeEvent>): void
```

Subscribes to system volume change events. When the system volume for the target filter changes, registered clients will receive a callback.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioVolumeManager-onSystemVolumeChangeByFilter(filter: SystemVolumeFilter, callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-onSystemVolumeChangeByFilter(filter: SystemVolumeFilter, callback: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [SystemVolumeFilter](arkts-audio-audio-systemvolumefilter-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onVolumePercentageChange

```TypeScript
onVolumePercentageChange(callback: Callback<VolumeEvent>): void
```

Subscribes to system volume percentage change events.

**Since:** 23

**Deprecated since:** -1

<!--Device-AudioVolumeManager-onVolumePercentageChange(callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-onVolumePercentageChange(callback: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on_activeVolumeTypeChange

```TypeScript
on(type: 'activeVolumeTypeChange', callback: Callback<AudioVolumeType>): void
```

Subscribes to active volume type changes.

**Since:** 20

**Deprecated since:** -1

<!--Device-AudioVolumeManager-on(type: 'activeVolumeTypeChange', callback: Callback<AudioVolumeType>): void--><!--Device-AudioVolumeManager-on(type: 'activeVolumeTypeChange', callback: Callback<AudioVolumeType>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'activeVolumeTypeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on_appVolumeChangeForUid

```TypeScript
on(type: 'appVolumeChangeForUid', uid: number, callback: Callback<VolumeEvent>): void
```

Listens for specified app volume change events. The app volume may changed by [setAppVolumePercentageForUid](#setAppVolumePercentageForUid).

**Since:** 19

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-on(type: 'appVolumeChangeForUid', uid: int, callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-on(type: 'appVolumeChangeForUid', uid: int, callback: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'appVolumeChangeForUid' | Yes |
| uid | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on_systemVolumeChange

```TypeScript
on(type: 'systemVolumeChange', callback: Callback<VolumeEvent>): void
```

Listens for system volume change events. This method uses a callback to get volume change events.

**Since:** 20

**Deprecated since:** -1

<!--Device-AudioVolumeManager-on(type: 'systemVolumeChange', callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-on(type: 'systemVolumeChange', callback: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemVolumeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setAppVolumeMutedForUid

```TypeScript
setAppVolumeMutedForUid(uid: number, muted: boolean): Promise<void>
```

Change mute state of specified application volume. If there are multiple callers setting muted states, only when all callers cancel muted state the volume of this app will be truly unmuted.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-setAppVolumeMutedForUid(uid: int, muted: boolean): Promise<void>--><!--Device-AudioVolumeManager-setAppVolumeMutedForUid(uid: int, muted: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |
| muted | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## setAppVolumePercentageForUid

```TypeScript
setAppVolumePercentageForUid(uid: number, volume: number): Promise<void>
```

Sets the volume for specified app with range from 0 to 100. Applications with same uid share the same volume.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-setAppVolumePercentageForUid(uid: int, volume: int): Promise<void>--><!--Device-AudioVolumeManager-setAppVolumePercentageForUid(uid: int, volume: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |
| volume | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## Examples

```TypeScript
let uid: number = 20010041; // Application ID.
let volume: number = 20;    // Volume to set.

audioVolumeManager.setAppVolumePercentageForUid(uid, volume).then(() => {
  console.info(`set app volume success.`);
});
```

## setSystemVolumeByUid

```TypeScript
setSystemVolumeByUid(volumeType: AudioVolumeType, volume: number, callingUid: number): Promise<void>
```

Sets the volume for specific uid application. This method uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeManager-setSystemVolumeByUid(volumeType: AudioVolumeType, volume: int, callingUid: int): Promise<void>--><!--Device-AudioVolumeManager-setSystemVolumeByUid(volumeType: AudioVolumeType, volume: int, callingUid: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| volume | number | Yes |
| callingUid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## setSystemVolumePercentage

```TypeScript
setSystemVolumePercentage(volumeType: AudioVolumeType, percentage: number): Promise<void>
```

Sets the system volume percentage, using an integer ranging from minimum system volume percentage to 100. The volume percentage corresponds to volume levels, with each level tied to a specific percentage. When the volume level changes, the volume percentage adjusts accordingly and is mapped within the range of volume levels. Zero volume is mapped to 0, and the maximum volume is mapped to 100%. Intermediate volume levels are evenly distributed beween 1 and 99. When the volume percentage changes, the volume level changes accordingly.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-setSystemVolumePercentage(volumeType: AudioVolumeType, percentage: int): Promise<void>--><!--Device-AudioVolumeManager-setSystemVolumePercentage(volumeType: AudioVolumeType, percentage: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| [percentage](arkts-audio-audio-volumeevent-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## setVoipCapturerMuteForUid

```TypeScript
setVoipCapturerMuteForUid(uid: number, streamId: number, muted: boolean): Promise<void>
```

Sets the mute state for the VoIP audio capture stream of a specified application. If there are multiple callers setting muted states for the same uid and streamId, only when all callers cancel muted state the VoIP capture stream will be truly unmuted. When the application abnormally exits, the application releases the audio stream and restarts it, or the audio service abnormally exits and restarts, the mute state set for this audio stream will automatically become invalid. In these cases, you need to call this API again to apply the mute state.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.MUTE_VOIP_CAPTURE

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioVolumeManager-setVoipCapturerMuteForUid(uid: int, streamId: long, muted: boolean): Promise<void>--><!--Device-AudioVolumeManager-setVoipCapturerMuteForUid(uid: int, streamId: long, muted: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |
| streamId | number | Yes |
| muted | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## setVoipRendererMuteForUid

```TypeScript
setVoipRendererMuteForUid(uid: number, streamId: number, muted: boolean): Promise<void>
```

Sets the mute state for the VoIP audio renderer stream of a specified application. If there are multiple callers setting muted states for the same uid and streamId, only when all callers cancel muted state the VoIP renderer stream will be truly unmuted. When the application abnormally exits, the application releases the audio stream and restarts it, or the audio service abnormally exits and restarts, the mute state set for this audio stream will automatically become invalid. In these cases, you need to call this API again to apply the mute state.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.MUTE_VOIP_PLAYBACK

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioVolumeManager-setVoipRendererMuteForUid(uid: int, streamId: long, muted: boolean): Promise<void>--><!--Device-AudioVolumeManager-setVoipRendererMuteForUid(uid: int, streamId: long, muted: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |
| streamId | number | Yes |
| muted | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |
