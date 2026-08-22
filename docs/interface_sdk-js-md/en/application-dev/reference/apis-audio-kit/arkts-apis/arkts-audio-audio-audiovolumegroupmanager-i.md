# AudioVolumeGroupManager

This interface implements volume management for an audio group.

Before calling any API in AudioVolumeGroupManager, you must use [getVolumeGroupManager](arkts-audio-audio-audiovolumemanager-i.md#getvolumegroupmanager) to obtain an AudioVolumeGroupManager instance.

> **NOTE：**
> 
> - The initial APIs of this interface are supported since API version 9.

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let capturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

audio.getAudioManager().getRoutingManager().getPreferredInputDeviceForCapturerInfo(capturerInfo).then((data) => {
  audioVolumeGroupManager.getMaxAmplitudeForInputDevice(data[0]).then((value) => {
    console.info(`Succeeded in getting maxAmplitude for input device. Amplitude: ${value}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get maxAmplitude for input device. Code: ${err.code}, message: ${err.message}`);
  })
}).catch((err: BusinessError) => {
  console.error(`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`);
})
```

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let rendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};

audio.getAudioManager().getRoutingManager().getPreferOutputDeviceForRendererInfo(rendererInfo).then((data) => {
  audioVolumeGroupManager.getMaxAmplitudeForOutputDevice(data[0]).then((value) => {
    console.info(`Succeeded in getting maxAmplitude for input device. Amplitude: ${value}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get maxAmplitude for input device. Code: ${err.code}, message: ${err.message}`);
  })
}).catch((err: BusinessError) => {
  console.error(`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`);
})
```

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
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the maximum stream volume level obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getMaxVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the maximum volume. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the maximum volume is obtained. ${value}`);
});
```

```TypeScript
audioManager.getMaxVolume(audio.AudioVolumeType.MEDIA).then((data: number) => {
  console.info('Promised returned to indicate that the maximum volume is obtained.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getMaxVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to get maxVolume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
});
```

```TypeScript
audioVolumeGroupManager.getMaxVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
});
```

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

**Examples**

See [getMaxVolume](#getmaxvolume)

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getMaxVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get maxVolume. Code: ${error.code}, message: ${error.message}`);
}
```

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
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the minimum stream volume level obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getMinVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the minimum volume. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the minimum volume is obtained. ${value}`);
});
```

```TypeScript
audioManager.getMinVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Promised returned to indicate that the minimum volume is obtained. ${value}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getMinVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to get minVolume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
});
```

```TypeScript
audioVolumeGroupManager.getMinVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
});
```

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

**Examples**

See [getMinVolume](#getminvolume)

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getMinVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get minVolume. Code: ${error.code}, message: ${error.message}`);
}
```

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
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the ringer mode obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getRingerMode((err: BusinessError, value: audio.AudioRingMode) => {
  if (err) {
    console.error(`Failed to obtain the ringer mode. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the ringer mode is obtained ${value}.`);
});
```

```TypeScript
audioManager.getRingerMode().then((value: audio.AudioRingMode) => {
  console.info(`Promise returned to indicate that the ringer mode is obtained ${value}.`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getRingerMode((err: BusinessError, value: audio.AudioRingMode) => {
  if (err) {
    console.error(`Failed to get ringerMode. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getRingerMode().then((value: audio.AudioRingMode) => {
  console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get ringerMode. Code: ${err.code}, message: ${err.message}`);
});
```

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

**Examples**

See [getRingerMode](#getringermode)

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: audio.AudioRingMode = audioVolumeGroupManager.getRingerModeSync();
  console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get ringerMode. Code: ${error.code}, message: ${error.message}`);
}
```

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
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;double&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the volume gain obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by callback. |
| [6800301](../errorcode-audio.md#6800301-system-error) | System error. Return by callback. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to get system volume in db. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting system volume in db. DB: ${value}.`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER).then((value: number) => {
  console.info(`Succeeded in getting system volume in db. DB: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get system volume in db. Code: ${err.code}, message: ${err.message}`);
});
```

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

**Examples**

See [getSystemVolumeInDb](#getsystemvolumeindb)

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getSystemVolumeInDbSync(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER);
  console.info(`Succeeded in getting system volume in db. DB: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get system volume in db. Code: ${error.code}, message: ${error.message}`);
}
```

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
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the stream volume level obtained; otherwise, **err** is an error object. The volume range of a specified stream can be obtained by calling [getMinVolume](#getminvolume) and [getMaxVolume](#getmaxvolume) . |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the volume. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the volume is obtained.');
});
```

```TypeScript
audioManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Promise returned to indicate that the volume is obtained ${value} .`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getVolume();
  console.info(`Indicate that the volume is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume, error ${error}.`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to get volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting volume. Volume: ${value}.`);
});
```

```TypeScript
audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in getting volume. Volume: ${value}.`);
});
```

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

**Examples**

See [getVolume](#getvolume)

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(`Succeeded in getting volume. Volume: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get volume. Code: ${error.code}, message: ${error.message}`);
}
```

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
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the microphone is muted or **false** if not muted; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isMicrophoneMute((err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to obtain the mute status of the microphone. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the mute status of the microphone is obtained ${value}.`);
});
```

```TypeScript
audioManager.isMicrophoneMute().then((value: boolean) => {
  console.info(`Promise returned to indicate that the mute status of the microphone is obtained ${value}.`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMicrophoneMute((err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to use isMicrophoneMute function. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in using isMicrophoneMute function. MuteState: ${value}.`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMicrophoneMute().then((value: boolean) => {
  console.info(`Succeeded in using isMicrophoneMute function. MuteState: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to use isMicrophoneMute function. Code: ${err.code}, message: ${err.message}`);
});
```

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

**Examples**

See [isMicrophoneMute](#ismicrophonemute)

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioVolumeGroupManager.isMicrophoneMuteSync();
  console.info(`Succeeded in using isMicrophoneMuteSync function. MuteState: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to use isMicrophoneMuteSync function. Code: ${error.code}, message: ${error.message}`);
}
```

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
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the stream is muted or **false** if not muted; otherwise , **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isMute(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to obtain the mute status. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the mute status of the stream is obtained. ${value}`);
});
```

```TypeScript
audioManager.isMute(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(`Promise returned to indicate that the mute status of the stream is obtained ${value}.`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMute(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to use isMute function. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in using isMute function. MuteState: ${value}.`);
});
```

```TypeScript
audioVolumeGroupManager.isMute(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(`Succeeded in using isMute function. MuteState: ${value}.`);
});
```

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

**Examples**

See [isMute](#ismute)

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioVolumeGroupManager.isMuteSync(audio.AudioVolumeType.MEDIA);
  console.info(`Succeeded in using isMuteSync function. MuteState: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to use isMuteSync function. Code: ${error.code}, message: ${error.message}`);
}
```

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

**Examples**

```TypeScript
let volumeAdjustSwitch: boolean = audioVolumeGroupManager.isVolumeUnadjustable();
console.info(`Succeeded in using isVolumeUnadjustable function. VolumeUnadjustable: ${volumeAdjustSwitch}.`);
```

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
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | No | Callback used to return the changed microphone state. |

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
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | No | Callback used to return the changed ringer mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

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
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | No | Callback used to get the system microphone state change event. |

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
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | No | Callback used to get the updated ringer mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('micStateChange')

```TypeScript
on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void
```

Subscribes to the microphone state change event, which is triggered when the microphone state is changed. This API uses an asynchronous callback to return the result.

Currently, when multiple AudioManager instances are used in a single process, only the subscription of the last instance takes effect, and the subscription of other instances is overwritten (even if the last instance does not initiate a subscription). Therefore, you are advised to use a single AudioManager instance.

**Since:** 9

<!--Device-AudioVolumeGroupManager-on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void--><!--Device-AudioVolumeGroupManager-on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'micStateChange' | Yes | Event type. The event **'micStateChange'** is triggered when the microphone state is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | Yes | Callback used to return the changed microphone state. |

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
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | Yes | Callback used to return the changed ringer mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
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
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MicStateChangeEvent](arkts-audio-audio-micstatechangeevent-i.md)&gt; | Yes | Callback used to get the system microphone state change event. |

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
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRingMode](arkts-audio-audio-audioringmode-e.md)&gt; | Yes | Callback used to get the updated ringer mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
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
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setMicrophoneMute(true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to mute the microphone. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the microphone is muted.');
});
```

```TypeScript
audioManager.setMicrophoneMute(true).then(() => {
  console.info('Promise returned to indicate that the microphone is muted.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.setMicrophoneMute(true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set microphone mute. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting microphone mute.');
});
```

```TypeScript
audioVolumeGroupManager.setMicrophoneMute(true).then(() => {
  console.info('Succeeded in setting microphone mute.');
});
```

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

**Examples**

See [setMicrophoneMute](#setmicrophonemute)

