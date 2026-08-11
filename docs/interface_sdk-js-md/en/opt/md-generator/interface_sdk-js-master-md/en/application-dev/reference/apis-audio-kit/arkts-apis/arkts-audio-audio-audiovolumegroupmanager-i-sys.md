# AudioVolumeGroupManager

This interface implements volume management for an audio group.

Before calling any API in AudioVolumeGroupManager, you must use  
[getVolumeGroupManager](arkts-audio-audio-audiovolumemanager-i.md#getvolumegroupmanager)to obtain an AudioVolumeGroupManager instance.

> **NOTE：**
> 
> - The initial APIs of this interface are supported since API version 9.

**Since:** 9

<!--Device-audio-interface AudioVolumeGroupManager--><!--Device-audio-interface AudioVolumeGroupManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## adjustSystemVolumeByStep

```TypeScript
adjustSystemVolumeByStep(volumeType: AudioVolumeType, adjustType: VolumeAdjustType, callback: AsyncCallback<void>): void
```

Adjusts system volume by step for target volume type.This method uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-adjustSystemVolumeByStep(volumeType: AudioVolumeType, adjustType: VolumeAdjustType, callback: AsyncCallback<void>): void--><!--Device-AudioVolumeGroupManager-adjustSystemVolumeByStep(volumeType: AudioVolumeType, adjustType: VolumeAdjustType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md) | Yes |
| adjustType | [VolumeAdjustType](arkts-audio-audio-volumeadjusttype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.adjustSystemVolumeByStep(audio.AudioVolumeType.MEDIA, audio.VolumeAdjustType.VOLUME_UP, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to adjust the system volume by step ${err}`);
  } else {
    console.info('Success to adjust the system volume by step.');
  }
});
```

## adjustSystemVolumeByStep

```TypeScript
adjustSystemVolumeByStep(volumeType: AudioVolumeType, adjustType: VolumeAdjustType): Promise<void>
```

Adjusts system volume by step for target volume type.This method uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-adjustSystemVolumeByStep(volumeType: AudioVolumeType, adjustType: VolumeAdjustType): Promise<void>--><!--Device-AudioVolumeGroupManager-adjustSystemVolumeByStep(volumeType: AudioVolumeType, adjustType: VolumeAdjustType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md) | Yes |
| adjustType | [VolumeAdjustType](arkts-audio-audio-volumeadjusttype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.adjustSystemVolumeByStep(audio.AudioVolumeType.MEDIA, audio.VolumeAdjustType.VOLUME_UP).then(() => {
  console.info('Success to adjust the system volume by step.');
}).catch((error: BusinessError) => {
  console.error('Fail to adjust the system volume by step.');
});
```

## adjustVolumeByStep

```TypeScript
adjustVolumeByStep(adjustType: VolumeAdjustType, callback: AsyncCallback<void>): void
```

Adjusts system volume by step, volume type is decided by system.This method uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-adjustVolumeByStep(adjustType: VolumeAdjustType, callback: AsyncCallback<void>): void--><!--Device-AudioVolumeGroupManager-adjustVolumeByStep(adjustType: VolumeAdjustType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| adjustType | [VolumeAdjustType](arkts-audio-audio-volumeadjusttype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.adjustVolumeByStep(audio.VolumeAdjustType.VOLUME_UP, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to adjust the volume by step. ${err}`);
    return;
  } else {
    console.info('Success to adjust the volume by step.');
  }
});
```

## adjustVolumeByStep

```TypeScript
adjustVolumeByStep(adjustType: VolumeAdjustType): Promise<void>
```

Adjusts system volume by step, volume type is decided by system.This method uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-adjustVolumeByStep(adjustType: VolumeAdjustType): Promise<void>--><!--Device-AudioVolumeGroupManager-adjustVolumeByStep(adjustType: VolumeAdjustType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| adjustType | [VolumeAdjustType](arkts-audio-audio-volumeadjusttype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.adjustVolumeByStep(audio.VolumeAdjustType.VOLUME_UP).then(() => {
  console.info('Success to adjust the volume by step.');
}).catch((error: BusinessError) => {
  console.error('Fail to adjust the volume by step.');
});
```

## getActiveVolumeTypeSync

```TypeScript
getActiveVolumeTypeSync(uid: number): AudioVolumeType
```

Obtains the active volume type in the calling moment. This method returns in sync mode.

**Since:** 13

<!--Device-AudioVolumeGroupManager-getActiveVolumeTypeSync(uid: int): AudioVolumeType--><!--Device-AudioVolumeGroupManager-getActiveVolumeTypeSync(uid: int): AudioVolumeType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let uid: number = 20010041; // Application ID.

let value = audioVolumeGroupManager.getActiveVolumeTypeSync(uid);
```

## isPersistentMicMute

```TypeScript
isPersistentMicMute(): boolean
```

Checks whether the persistent microphone status is muted.

**Since:** 12

**Required permissions:** ohos.permission.MICROPHONE_CONTROL

<!--Device-AudioVolumeGroupManager-isPersistentMicMute(): boolean--><!--Device-AudioVolumeGroupManager-isPersistentMicMute(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let value: boolean = audioVolumeGroupManager.isPersistentMicMute();
```

## mute

```TypeScript
mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void
```

Mutes a stream. This method uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioVolumeGroupManager-mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md) | Yes |
| [mute](#mute) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.mute(audio.AudioVolumeType.MEDIA, true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to mute the stream. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the stream is muted.');
});
```

## mute

```TypeScript
mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>
```

Mutes a stream. This method uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>--><!--Device-AudioVolumeGroupManager-mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md) | Yes |
| [mute](#mute) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
audioVolumeGroupManager.mute(audio.AudioVolumeType.MEDIA, true).then(() => {
  console.info('Promise returned to indicate that the stream is muted.');
});
```

## setMicMute

```TypeScript
setMicMute(mute: boolean): Promise<void>
```

Mutes or unmutes the microphone. This method uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeGroupManager-setMicMute(mute: boolean): Promise<void>--><!--Device-AudioVolumeGroupManager-setMicMute(mute: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [mute](#mute) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
audioVolumeGroupManager.setMicMute(true).then(() => {
  console.info('Promise returned to indicate that the mic is muted.');
});
```

## setMicMutePersistent

```TypeScript
setMicMutePersistent(mute: boolean, type: PolicyType): Promise<void>
```

Mutes or unmutes the microphone. This method uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.MICROPHONE_CONTROL

<!--Device-AudioVolumeGroupManager-setMicMutePersistent(mute: boolean, type: PolicyType): Promise<void>--><!--Device-AudioVolumeGroupManager-setMicMutePersistent(mute: boolean, type: PolicyType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [mute](#mute) | boolean | Yes |
| type | [PolicyType](../../apis-mdm-kit/arkts-apis/arkts-mdm-systemmanager-policytype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
audioVolumeGroupManager.setMicMutePersistent(true, audio.PolicyType.PRIVACY).then(() => {
  console.info('Succeeded in setting mic mute.');
});
```

## setRingerMode

```TypeScript
setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void
```

Sets the ringer mode. This method uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void--><!--Device-AudioVolumeGroupManager-setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AudioRingMode](arkts-audio-audio-audioringmode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.setRingerMode(audio.AudioRingMode.RINGER_MODE_NORMAL, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the ringer mode. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate a successful setting of the ringer mode.');
});
```

## setRingerMode

```TypeScript
setRingerMode(mode: AudioRingMode): Promise<void>
```

Sets the ringer mode. This method uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-setRingerMode(mode: AudioRingMode): Promise<void>--><!--Device-AudioVolumeGroupManager-setRingerMode(mode: AudioRingMode): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AudioRingMode](arkts-audio-audio-audioringmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
audioVolumeGroupManager.setRingerMode(audio.AudioRingMode.RINGER_MODE_NORMAL).then(() => {
  console.info('Promise returned to indicate a successful setting of the ringer mode.');
});
```

## setVolume

```TypeScript
setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void
```

Sets the volume for a stream. This method uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-setVolume(volumeType: AudioVolumeType, volume: int, callback: AsyncCallback<void>): void--><!--Device-AudioVolumeGroupManager-setVolume(volumeType: AudioVolumeType, volume: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md) | Yes |
| volume | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.setVolume(audio.AudioVolumeType.MEDIA, 10, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the volume. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate a successful volume setting.');
});
```

## setVolume

```TypeScript
setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>
```

Sets the volume for a stream. This method uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-setVolume(volumeType: AudioVolumeType, volume: int): Promise<void>--><!--Device-AudioVolumeGroupManager-setVolume(volumeType: AudioVolumeType, volume: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md) | Yes |
| volume | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
audioVolumeGroupManager.setVolume(audio.AudioVolumeType.MEDIA, 10).then(() => {
  console.info('Promise returned to indicate a successful volume setting.');
});
```

## setVolumeWithFlag

```TypeScript
setVolumeWithFlag(volumeType: AudioVolumeType, volume: number, flags: number): Promise<void>
```

Sets the volume for a stream. This method uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeGroupManager-setVolumeWithFlag(volumeType: AudioVolumeType, volume: int, flags: int): Promise<void>--><!--Device-AudioVolumeGroupManager-setVolumeWithFlag(volumeType: AudioVolumeType, volume: int, flags: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md) | Yes |
| volume | number | Yes |
| flags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
audioVolumeGroupManager.setVolumeWithFlag(audio.AudioVolumeType.MEDIA, 10, 1).then(() => {
  console.info('Promise returned to indicate a successful volume setting.');
});
```
