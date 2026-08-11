# AudioPlayer

AudioPlayer is a class for audio playback management. It provides APIs to manage and play audio. Before calling any API in AudioPlayer, you must use [createAudioPlayer()](arkts-media-media-createaudioplayer-f.md#createaudioplayer) to create an AudioPlayer instance.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.multimedia.media:media](arkts-multimedia-media.md)

<!--Device-media-interface AudioPlayer--><!--Device-media-interface AudioPlayer-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## getTrackDescription

```TypeScript
getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void
```

Obtains the audio track information. It can be called only after the **'dataLoad'** event is triggered. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.multimedia.media:media.AVPlayer.getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)(callback:

<!--Device-AudioPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void--><!--Device-AudioPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;MediaDescription&gt;&gt; | Yes |

## getTrackDescription

```TypeScript
getTrackDescription(): Promise<Array<MediaDescription>>
```

Obtains the audio track information. It can be called only after the **'dataLoad'** event is triggered. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.multimedia.media:media.AVPlayer.getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)()

<!--Device-AudioPlayer-getTrackDescription(): Promise<Array<MediaDescription>>--><!--Device-AudioPlayer-getTrackDescription(): Promise<Array<MediaDescription>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;MediaDescription&gt;&gt; |

## on('bufferingUpdate')

```TypeScript
on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void
```

Subscribes to the audio buffering update event. This API works only under online playback.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void--><!--Device-AudioPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'bufferingUpdate' | Yes |
| callback | (infoType: BufferingInfoType, value: number) =&gt; void | Yes |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes |
| callback | () =&gt; void | Yes |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes |
| callback | () =&gt; void | Yes |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes |
| callback | () =&gt; void | Yes |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes |
| callback | () =&gt; void | Yes |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes |
| callback | () =&gt; void | Yes |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes |
| callback | () =&gt; void | Yes |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes |
| callback | () =&gt; void | Yes |

## on('timeUpdate')

```TypeScript
on(type: 'timeUpdate', callback: Callback<number>): void
```

Subscribes to the **'timeUpdate'** event. This event is reported every second when the audio playback is in progress.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'timeUpdate', callback: Callback<number>): void--><!--Device-AudioPlayer-on(type: 'timeUpdate', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'timeUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void
```

Subscribes to the audio interruption event. For details, see   
[audio.InterruptEvent](../../apis-audio-kit/arkts-apis/arkts-audio-audio-interruptevent-i.md/arkts-audio-audio-interruptevent-i.md).

**Since:** 9

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void--><!--Device-AudioPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioInterrupt' | Yes |
| callback | (info: audio.InterruptEvent) =&gt; void | Yes |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to audio playback error events. After an error event is reported, you must handle the event and exit the playback.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** @ohos.multimedia.media:media.AVPlayer.on(type:

<!--Device-AudioPlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-AudioPlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## pause

```TypeScript
pause(): void
```

Pauses audio playback.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.multimedia.media:media.AVPlayer.pause](arkts-media-media-avplayer-i.md#pause)(callback:

<!--Device-AudioPlayer-pause(): void--><!--Device-AudioPlayer-pause(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## play

```TypeScript
play(): void
```

Starts to play an audio asset. This API can be called only after the **'dataLoad'** event is triggered.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.multimedia.media:media.AVPlayer.play](arkts-media-media-avplayer-i.md#play)(callback:

<!--Device-AudioPlayer-play(): void--><!--Device-AudioPlayer-play(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## release

```TypeScript
release(): void
```

Releases the audio playback resources.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.multimedia.media:media.AVPlayer.release](arkts-media-media-avplayer-i.md#release)(callback:

<!--Device-AudioPlayer-release(): void--><!--Device-AudioPlayer-release(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## reset

```TypeScript
reset(): void
```

Resets the audio asset to be played.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.multimedia.media:media.AVPlayer.reset](arkts-media-media-avplayer-i.md#reset)(callback:

<!--Device-AudioPlayer-reset(): void--><!--Device-AudioPlayer-reset(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## seek

```TypeScript
seek(timeMs: number): void
```

Seeks to the specified playback position.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.multimedia.media:media.AVPlayer.seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-AudioPlayer-seek(timeMs: number): void--><!--Device-AudioPlayer-seek(timeMs: number): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeMs | number | Yes |

## setVolume

```TypeScript
setVolume(vol: number): void
```

Sets the volume.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.multimedia.media:media.AVPlayer.setVolume](arkts-media-media-avplayer-i.md#setvolume)

<!--Device-AudioPlayer-setVolume(vol: number): void--><!--Device-AudioPlayer-setVolume(vol: number): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| vol | number | Yes |

## stop

```TypeScript
stop(): void
```

Stops audio playback.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.multimedia.media:media.AVPlayer.stop](arkts-media-media-avplayer-i.md#stop)(callback:

<!--Device-AudioPlayer-stop(): void--><!--Device-AudioPlayer-stop(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## audioInterruptMode

```TypeScript
audioInterruptMode?: audio.InterruptMode
```

Audio interruption mode.

**Type:** audio.InterruptMode

**Since:** 9

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVPlayer#audioInterruptMode

<!--Device-AudioPlayer-audioInterruptMode?: audio.InterruptMode--><!--Device-AudioPlayer-audioInterruptMode?: audio.InterruptMode-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## currentTime

```TypeScript
readonly currentTime: number
```

Current audio playback position, in ms.

**Type:** number

**Since:** 6

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVPlayer#currentTime

<!--Device-AudioPlayer-readonly currentTime: number--><!--Device-AudioPlayer-readonly currentTime: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## duration

```TypeScript
readonly duration: number
```

Audio duration, in ms.

**Type:** number

**Since:** 6

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVPlayer#duration

<!--Device-AudioPlayer-readonly duration: number--><!--Device-AudioPlayer-readonly duration: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

Description of the audio file. This property is required when audio assets of an application are continuously stored in a file.

Assume that a music file that stores continuous music assets consists of the following:

Music 1 (address offset: 0, byte length: 100)

Music 2 (address offset: 101; byte length: 50)

Music 3 (address offset: 151, byte length: 150)

1. To play music 1: AVFileDescriptor { fd = resource handle; offset = 0; length = 100; }2. To play music 2: AVFileDescriptor { fd = resource handle; offset = 101; length = 50; }3. To play music 3: AVFileDescriptor { fd = resource handle; offset = 151; length = 150; }

To play an independent music file, use **src=fd://xx**.

**Type:** [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md)

**Since:** 9

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVPlayer#fdSrc

<!--Device-AudioPlayer-fdSrc: AVFileDescriptor--><!--Device-AudioPlayer-fdSrc: AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## loop

```TypeScript
loop: boolean
```

Whether to loop audio playback. **true** to loop, **false** otherwise.

**Type:** boolean

**Since:** 6

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVPlayer#loop

<!--Device-AudioPlayer-loop: boolean--><!--Device-AudioPlayer-loop: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## src

```TypeScript
src: string
```

Audio file URI. The mainstream audio formats (M4A, AAC, MP3, OGG, WAV, and AMR) are supported.

**Example of supported URLs**:

1. FD: fd://xx

![](../../../reference/apis-media-kit/figures/en-us_image_url.png)

2. HTTP: http://xx3. HTTPS: https://xx4. HLS: http://xx or https://xx

ohos.permission.READ_MEDIA or ohos.permission.INTERNET

**Type:** string

**Since:** 6

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVPlayer#url

**Required permissions:** ohos.permission.READ_MEDIA or ohos.permission.INTERNET

<!--Device-AudioPlayer-src: string--><!--Device-AudioPlayer-src: string-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## state

```TypeScript
readonly state: AudioState
```

Audio playback state. This state cannot be used as the condition for triggering the call of **play()**,   
**pause()**, or **stop()**.

**Type:** [AudioState](arkts-media-media-audiostate-t.md)

**Since:** 6

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVPlayer#state

<!--Device-AudioPlayer-readonly state: AudioState--><!--Device-AudioPlayer-readonly state: AudioState-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer
