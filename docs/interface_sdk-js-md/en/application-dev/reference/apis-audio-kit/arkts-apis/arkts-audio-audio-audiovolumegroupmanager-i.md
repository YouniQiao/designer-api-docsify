# AudioVolumeGroupManager

This interface implements volume management for an audio group. Before calling any API in AudioVolumeGroupManager, you must use [getVolumeGroupManager](arkts-audio-audio-audiovolumemanager-i.md#getvolumegroupmanager) to obtain an AudioVolumeGroupManager instance. &gt; **NOTE：**&gt; &gt; - The initial APIs of this interface are supported since API version 9.

**Since:** 23

<!--Device-audio-interface AudioVolumeGroupManager--><!--Device-audio-interface AudioVolumeGroupManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
import { audioHaptic } from '@kit.AudioKit';
```

## getMaxAmplitudeForInputDevice

```TypeScript
getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<double>
```

Obtains the maximum amplitude (in the range [0, 1]) of the audio stream for an input device. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioVolumeGroupManager-getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<double>--><!--Device-AudioVolumeGroupManager-getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<double>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | Yes | Descriptor of the target device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;double&gt; | Promise used to return the maximum amplitude, which is in the range [0, 1]. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by promise. |
| [6800301](../errorcode-audio.md#6800301-system-error) | System error. Return by promise. |

## getMaxAmplitudeForOutputDevice

```TypeScript
getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<double>
```

Obtains the maximum amplitude (in the range [0, 1]) of the audio stream for an output device. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioVolumeGroupManager-getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<double>--><!--Device-AudioVolumeGroupManager-getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<double>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| outputDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | Yes | Descriptor of the target device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;double&gt; | Promise used to return the maximum amplitude, which is in the range [0, 1]. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by promise. |
| [6800301](../errorcode-audio.md#6800301-system-error) | System error. Return by promise. |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void
```

Obtains the maximum volume level of a stream. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)

<!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void--><!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the maximum stream volume level obtained; otherwise, **err** is an error object. |

## getMaxVolume

```TypeScript
getMaxVolume(volumeType: AudioVolumeType): Promise<int>
```

Obtains the maximum volume level of a stream. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)

<!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType): Promise<int>--><!--Device-AudioVolumeGroupManager-getMaxVolume(volumeType: AudioVolumeType): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the maximum volume level. |

## getMaxVolumeSync

```TypeScript
getMaxVolumeSync(volumeType: AudioVolumeType): int
```

Obtains the maximum volume level of a stream. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMaxVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getmaxvolumebystream)

<!--Device-AudioVolumeGroupManager-getMaxVolumeSync(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeGroupManager-getMaxVolumeSync(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Maximum volume level. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void
```

Obtains the minimum volume level of a stream. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)

<!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void--><!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the minimum stream volume level obtained; otherwise, **err** is an error object. |

## getMinVolume

```TypeScript
getMinVolume(volumeType: AudioVolumeType): Promise<int>
```

Obtains the minimum volume level of a stream. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)

<!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType): Promise<int>--><!--Device-AudioVolumeGroupManager-getMinVolume(volumeType: AudioVolumeType): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the minimum volume level. |

## getMinVolumeSync

```TypeScript
getMinVolumeSync(volumeType: AudioVolumeType): int
```

Obtains the minimum volume level of a stream. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getMinVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getminvolumebystream)

<!--Device-AudioVolumeGroupManager-getMinVolumeSync(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeGroupManager-getMinVolumeSync(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Minimum volume level. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## getRingerMode

```TypeScript
getRingerMode(callback: AsyncCallback<AudioRingMode>): void
```

Obtains the ringer mode. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioVolumeGroupManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-getRingerMode(callback: AsyncCallback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the ringer mode obtained; otherwise, **err** is an error object. |

## getRingerMode

```TypeScript
getRingerMode(): Promise<AudioRingMode>
```

Obtains the ringer mode. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioVolumeGroupManager-getRingerMode(): Promise<AudioRingMode>--><!--Device-AudioVolumeGroupManager-getRingerMode(): Promise<AudioRingMode>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | Promise used to return the ringer mode. |

## getRingerModeSync

```TypeScript
getRingerModeSync(): AudioRingMode
```

Obtains the ringer mode. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioVolumeGroupManager-getRingerModeSync(): AudioRingMode--><!--Device-AudioVolumeGroupManager-getRingerModeSync(): AudioRingMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| Type | Description |
| --- | --- |
| [AudioRingMode](arkts-audio-audio-audioringmode-e.md) | Ringer mode. |

## getSystemVolumeInDb

```TypeScript
getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType, callback: AsyncCallback<double>): void
```

Obtains the volume gain. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)

<!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType, callback: AsyncCallback<double>): void--><!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType, callback: AsyncCallback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |
| volumeLevel | int | Yes | Volume level. |
| device | DeviceType | Yes | Device type. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;double&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the volume gain obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by callback. |
| [6800301](../errorcode-audio.md#6800301-system-error) | System error. Return by callback. |

## getSystemVolumeInDb

```TypeScript
getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): Promise<double>
```

Obtains the volume gain. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)

<!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): Promise<double>--><!--Device-AudioVolumeGroupManager-getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): Promise<double>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |
| volumeLevel | int | Yes | Volume level. |
| device | DeviceType | Yes | Device type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;double&gt; | Promise used to return the volume gain (in dB). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by promise. |
| [6800301](../errorcode-audio.md#6800301-system-error) | System error. Return by promise. |

## getSystemVolumeInDbSync

```TypeScript
getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double
```

Obtains the volume gain. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeInUnitOfDbByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumeinunitofdbbystream)

<!--Device-AudioVolumeGroupManager-getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double--><!--Device-AudioVolumeGroupManager-getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |
| volumeLevel | int | Yes | Volume level. |
| device | DeviceType | Yes | Device type. |

**Return value:**

| Type | Description |
| --- | --- |
| double | Volume gain (in dB). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void
```

Obtains the volume level of a stream. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)

<!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void--><!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the stream volume level obtained; otherwise, **err** is an error object. The volume range of a specified stream can be obtained by calling [getMinVolume](#getminvolume) and [getMaxVolume](#getmaxvolume) . |

## getVolume

```TypeScript
getVolume(volumeType: AudioVolumeType): Promise<int>
```

Obtains the volume level of a stream. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)

<!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType): Promise<int>--><!--Device-AudioVolumeGroupManager-getVolume(volumeType: AudioVolumeType): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the stream volume level. The volume range of a specified stream can be obtained by calling [getMinVolume]{ |

## getVolumeSync

```TypeScript
getVolumeSync(volumeType: AudioVolumeType): int
```

Obtains the volume level of a stream. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [getVolumeByStream](arkts-audio-audio-audiovolumemanager-i.md#getvolumebystream)

<!--Device-AudioVolumeGroupManager-getVolumeSync(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeGroupManager-getVolumeSync(volumeType: AudioVolumeType): int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Volume level of the stream. The volume range of a specified stream can be obtained by calling [getMinVolume]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(callback: AsyncCallback<boolean>): void
```

Checks whether the microphone is muted. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioVolumeGroupManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void--><!--Device-AudioVolumeGroupManager-isMicrophoneMute(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the microphone is muted or **false** if not muted; otherwise, **err** is an error object. |

## isMicrophoneMute

```TypeScript
isMicrophoneMute(): Promise<boolean>
```

Checks whether the microphone is muted. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioVolumeGroupManager-isMicrophoneMute(): Promise<boolean>--><!--Device-AudioVolumeGroupManager-isMicrophoneMute(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result, indicating whether the microphone is muted. **true** if muted, **false** otherwise. |

## isMicrophoneMuteSync

```TypeScript
isMicrophoneMuteSync(): boolean
```

Checks whether the microphone is muted. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioVolumeGroupManager-isMicrophoneMuteSync(): boolean--><!--Device-AudioVolumeGroupManager-isMicrophoneMuteSync(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the microphone is muted. **true** if muted, **false** otherwise. |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

Checks whether a stream is muted. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)

<!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the stream is muted or **false** if not muted; otherwise , **err** is an error object. |

## isMute

```TypeScript
isMute(volumeType: AudioVolumeType): Promise<boolean>
```

Checks whether a stream is muted. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)

<!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioVolumeGroupManager-isMute(volumeType: AudioVolumeType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result, indicating whether the stream is muted. **true** if muted, **false** otherwise. |

## isMuteSync

```TypeScript
isMuteSync(volumeType: AudioVolumeType): boolean
```

Checks whether a stream is muted. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [isSystemMutedForStream](arkts-audio-audio-audiovolumemanager-i.md#issystemmutedforstream)

<!--Device-AudioVolumeGroupManager-isMuteSync(volumeType: AudioVolumeType): boolean--><!--Device-AudioVolumeGroupManager-isMuteSync(volumeType: AudioVolumeType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | Audio volume type. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the stream is muted. **true** if muted, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## isVolumeUnadjustable

```TypeScript
isVolumeUnadjustable(): boolean
```

Checks whether the fixed volume mode is enabled. When the fixed volume mode is enabled, the volume cannot be adjusted. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioVolumeGroupManager-isVolumeUnadjustable(): boolean--><!--Device-AudioVolumeGroupManager-isVolumeUnadjustable(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the fixed volume mode is enabled. **true** if enabled, **false** otherwise. |

## offMicStateChange

```TypeScript
offMicStateChange(callback?: Callback<MicStateChangeEvent>): void
```

Unsubscribes to the microphone state change events.

**Since:** 23

<!--Device-AudioVolumeGroupManager-offMicStateChange(callback?: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-offMicStateChange(callback?: Callback<MicStateChangeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | No | Callback used to get the system microphone state change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offRingerModeChange

```TypeScript
offRingerModeChange(callback?: Callback<AudioRingMode>): void
```

Unsubscribes to the ringer mode state change events.

**Since:** 23

<!--Device-AudioVolumeGroupManager-offRingerModeChange(callback?: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-offRingerModeChange(callback?: Callback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | No | Callback used to get the updated ringer mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('micStateChange')

```TypeScript
off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void
```

Unsubscribes from the microphone state change event. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-AudioVolumeGroupManager-off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'micStateChange' | Yes | Event type. The event **'micStateChange'** is triggered when the microphone state is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | No | Callback used to return the changed microphone state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters missing; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('ringerModeChange')

```TypeScript
off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void
```

Unsubscribes from the ringer mode change event. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-AudioVolumeGroupManager-off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'ringerModeChange' | Yes | Event type. The event **'ringerModeChange'** is triggered when the ringer mode is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | No | Callback used to return the changed ringer mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onMicStateChange

```TypeScript
onMicStateChange(callback: Callback<MicStateChangeEvent>): void
```

Listens for system microphone state change events. This method uses a callback to get microphone change events.

**Since:** 23

<!--Device-AudioVolumeGroupManager-onMicStateChange(callback: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-onMicStateChange(callback: Callback<MicStateChangeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | Yes | Callback used to get the system microphone state change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onRingerModeChange

```TypeScript
onRingerModeChange(callback: Callback<AudioRingMode>): void
```

Listens for ringer mode change events. This method uses a callback to get ringer mode changes.

**Since:** 23

<!--Device-AudioVolumeGroupManager-onRingerModeChange(callback: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-onRingerModeChange(callback: Callback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | Yes | Callback used to get the updated ringer mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('micStateChange')

```TypeScript
on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void
```

Subscribes to the microphone state change event, which is triggered when the microphone state is changed. This API uses an asynchronous callback to return the result. Currently, when multiple AudioManager instances are used in a single process, only the subscription of the last instance takes effect, and the subscription of other instances is overwritten (even if the last instance does not initiate a subscription). Therefore, you are advised to use a single AudioManager instance.

**Since:** 9

<!--Device-AudioVolumeGroupManager-on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'micStateChange' | Yes | Event type. The event **'micStateChange'** is triggered when the microphone state is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | Yes | Callback used to return the changed microphone state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('ringerModeChange')

```TypeScript
on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void
```

Subscribes to the ringer mode change event, which is triggered when the [AudioRingMode](arkts-audio-audio-audioringmode-e.md) changes. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-AudioVolumeGroupManager-on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void--><!--Device-AudioVolumeGroupManager-on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'ringerModeChange' | Yes | Event type. The event **'ringerModeChange'** is triggered when the ringer mode is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | Yes | Callback used to return the changed ringer mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mute | boolean | Yes | Mute status to set. The value true means to mute the microphone, and false means the opposite. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mute | boolean | Yes | Mute status to set. The value true means to mute the microphone, and false means the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

