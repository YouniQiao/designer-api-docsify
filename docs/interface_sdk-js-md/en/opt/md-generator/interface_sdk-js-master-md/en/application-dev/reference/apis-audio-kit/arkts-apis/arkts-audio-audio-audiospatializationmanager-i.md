# AudioSpatializationManager

Implements audio spatialization management.

**Since:** 18

<!--Device-audio-interface AudioSpatializationManager--><!--Device-audio-interface AudioSpatializationManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## isSpatializationEnabledForCurrentDevice

```TypeScript
isSpatializationEnabledForCurrentDevice(): boolean
```

Checks whether spatial audio rendering is enabled for the current device. This API returns the result synchronously.

**Since:** 18

<!--Device-AudioSpatializationManager-isSpatializationEnabledForCurrentDevice(): boolean--><!--Device-AudioSpatializationManager-isSpatializationEnabledForCurrentDevice(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## off('spatializationEnabledChangeForCurrentDevice')

```TypeScript
off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void
```

Unsubscribes from the spatial audio rendering status change event of the current device. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-AudioSpatializationManager-off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void--><!--Device-AudioSpatializationManager-off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'spatializationEnabledChangeForCurrentDevice' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## on('spatializationEnabledChangeForCurrentDevice')

```TypeScript
on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void
```

Subscribes to the spatial audio rendering status change event of the current device. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-AudioSpatializationManager-on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void--><!--Device-AudioSpatializationManager-on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'spatializationEnabledChangeForCurrentDevice' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
