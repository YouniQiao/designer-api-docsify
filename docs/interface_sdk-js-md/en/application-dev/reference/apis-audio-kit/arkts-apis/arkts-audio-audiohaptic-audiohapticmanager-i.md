# AudioHapticManager

Manages the audio-haptic feature. Before calling any API in AudioHapticManager, you must use [getAudioHapticManager](arkts-audio-audiohaptic-getaudiohapticmanager-f.md) to create an AudioHapticManager instance.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## Modules to Import

```TypeScript
import { audioHaptic } from 'kits/@kit.AudioKit';
```

## createPlayer

```TypeScript
createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>
```

Create an audio haptic player. This method uses a promise to return the result. If haptics is needed, caller should have the permission of ohos.permission.VIBRATE.

**Since:** 11

**Required permissions:** ohos.permission.VIBRATE

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| options | [AudioHapticPlayerOptions](arkts-audio-audiohaptic-audiohapticplayeroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioHapticPlayer](arkts-audio-audiohaptic-audiohapticplayer-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400106](../../apis-media-kit/errorcode-media.md#5400106-format-not-supported) |

## registerSource

```TypeScript
registerSource(audioUri: string, hapticUri: string): Promise<number>
```

Registers audio and haptic resources via URIs. This API uses a promise to return the result.

> **NOTE：**&gt;
> A maximum of 128 resources can be registered at the same time for an application. Any attempt to register
> beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number
> of registered resources. For resources that are no longer used, you are advised to unregister them in a timely
> manner.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [audioUri](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-audio-c.md) | string | Yes |
| hapticUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## registerSourceFromFd

```TypeScript
registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<number>
```

Registers audio and haptic resources via file descriptors. This API uses a promise to return the result.

> **NOTE：**&gt;
> A maximum of 128 resources can be registered at the same time for an application. Any attempt to register
> beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number
> of registered resources. For resources that are no longer used, you are advised to unregister them in a timely
> manner.

**Since:** 20

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| audioFd | [AudioHapticFileDescriptor](arkts-audio-audiohaptic-audiohapticfiledescriptor-i.md) | Yes |
| [hapticFd](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefromfile-i.md) | [AudioHapticFileDescriptor](arkts-audio-audiohaptic-audiohapticfiledescriptor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## setAudioLatencyMode

```TypeScript
setAudioLatencyMode(id:number, latencyMode: AudioLatencyMode): void
```

Sets the latency mode for an audio-haptic source.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| latencyMode | [AudioLatencyMode](arkts-audio-audiohaptic-audiolatencymode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## setStreamUsage

```TypeScript
setStreamUsage(id: number, usage: audio.StreamUsage): void
```

Sets the stream usage for an audio-haptic source.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| usage | audio.StreamUsage | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## unregisterSource

```TypeScript
unregisterSource(id: number): Promise<void>
```

Unregisters an audio-haptic source. This API uses a promise to return the result.

> **NOTE：**&gt;
> For resources that are no longer used, you are advised to unregister them in a timely manner to avoid issues
> such as resource leaks or the number of resources exceeding the upper limit.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
