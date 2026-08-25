# AudioHapticPlayer

Implements audio-haptic playback. Before calling any API in AudioHapticPlayer, you must use [createPlayer](arkts-audio-audiohaptic-audiohapticmanager-i.md#createplayer) to create an AudioHapticPlayer instance.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## Modules to Import

```TypeScript
import { audioHaptic } from 'kits/@kit.AudioKit';
```

## isMuted

```TypeScript
isMuted(type: AudioHapticType): boolean
```

Checks whether an audio-haptic type is muted.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AudioHapticType](arkts-audio-audiohaptic-audiohaptictype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off('endOfStream')

```TypeScript
off(type: 'endOfStream', callback?: Callback<void>): void
```

Unsubscribes from the EOS event. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'endOfStream' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void
```

Unsubscribes from the audio interruption event. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioInterrupt' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | No |

## on('endOfStream')

```TypeScript
on(type: 'endOfStream', callback: Callback<void>): void
```

Subscribes to end of stream (EOS) event, which is triggered when the audio stream playback ends. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'endOfStream' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void
```

Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioInterrupt' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | Yes |

## release

```TypeScript
release(): Promise<void>
```

Releases this audio-haptic player. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## setLoop

```TypeScript
setLoop(loop: boolean): Promise<void>
```

Sets this audio-haptic player to play in a loop. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API must be called before the audio-haptic player is released.

**Since:** 20

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| loop | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## setVolume

```TypeScript
setVolume(volume: number): Promise<void>
```

Sets the volume for this audio-haptic player. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API must be called before the audio-haptic player is released.

**Since:** 20

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volume | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |
| [5400108](../../apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## start

```TypeScript
start(): Promise<void>
```

Starts playback. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## stop

```TypeScript
stop(): Promise<void>
```

Stops playback. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |
