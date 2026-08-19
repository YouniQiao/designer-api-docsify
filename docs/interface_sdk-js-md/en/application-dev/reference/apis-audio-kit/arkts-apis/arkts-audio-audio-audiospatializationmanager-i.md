# AudioSpatializationManager

Implements audio spatialization management.

**Since:** 23

<!--Device-audio-interface AudioSpatializationManager--><!--Device-audio-interface AudioSpatializationManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
import { audioHaptic } from '@kit.AudioKit';
```

## isSpatializationEnabledForCurrentDevice

```TypeScript
isSpatializationEnabledForCurrentDevice(): boolean
```

Checks whether spatial audio rendering is enabled for the current device. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioSpatializationManager-isSpatializationEnabledForCurrentDevice(): boolean--><!--Device-AudioSpatializationManager-isSpatializationEnabledForCurrentDevice(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether spatial audio rendering is enabled. **true** if enabled, **false** otherwise. |

## offSpatializationEnabledChangeForCurrentDevice

```TypeScript
offSpatializationEnabledChangeForCurrentDevice(callback?: Callback<boolean>): void
```

Unsubscribes to the spatialization enable state change events by the current device.

**Since:** 23

<!--Device-AudioSpatializationManager-offSpatializationEnabledChangeForCurrentDevice(callback?: Callback<boolean>): void--><!--Device-AudioSpatializationManager-offSpatializationEnabledChangeForCurrentDevice(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | No | Callback used to get the spatialization enable state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off('spatializationEnabledChangeForCurrentDevice')

```TypeScript
off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void
```

Unsubscribes from the spatial audio rendering status change event of the current device. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-AudioSpatializationManager-off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void--><!--Device-AudioSpatializationManager-off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'spatializationEnabledChangeForCurrentDevice' | Yes | Event type. The event **'spatializationEnabledChangeForCurrentDevice'** is triggered when the spatial audio rendering status is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | No | Callback used to return the result, indicating whether spatial audio rendering is enabled. **true** if enabled, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onSpatializationEnabledChangeForCurrentDevice

```TypeScript
onSpatializationEnabledChangeForCurrentDevice(callback: Callback<boolean>): void
```

Subscribes to the spatialization enable state change events by the current device. When the spatialization enable state changes, registered clients will receive the callback.

**Since:** 23

<!--Device-AudioSpatializationManager-onSpatializationEnabledChangeForCurrentDevice(callback: Callback<boolean>): void--><!--Device-AudioSpatializationManager-onSpatializationEnabledChangeForCurrentDevice(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | Yes | Callback used to get the spatialization enable state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on('spatializationEnabledChangeForCurrentDevice')

```TypeScript
on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void
```

Subscribes to the spatial audio rendering status change event of the current device. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-AudioSpatializationManager-on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void--><!--Device-AudioSpatializationManager-on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'spatializationEnabledChangeForCurrentDevice' | Yes | Event type. The event **'spatializationEnabledChangeForCurrentDevice'** is triggered when the spatial audio rendering status is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result, indicating whether spatial audio rendering is enabled. **true** if enabled, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

