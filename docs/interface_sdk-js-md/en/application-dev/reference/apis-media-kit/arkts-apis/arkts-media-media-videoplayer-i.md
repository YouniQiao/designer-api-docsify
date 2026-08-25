# VideoPlayer

VideoPlayer is a class for video playback management. It provides APIs to manage and play videos. Before calling any API in VideoPlayer, you must use [createVideoPlayer()](arkts-media-media-createvideoplayer-f.md) to create a VideoPlayer instance.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [media](arkts-multimedia-media.md)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## getTrackDescription

```TypeScript
getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void
```

Obtains the video track information. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)(callback: AsyncCallback&lt;Array&lt;MediaDescription&gt;&gt;)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MediaDescription](arkts-media-media-mediadescription-i.md)&gt;&gt; | Yes |

## getTrackDescription

```TypeScript
getTrackDescription(): Promise<Array<MediaDescription>>
```

Obtains the video track information. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)()

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[MediaDescription](arkts-media-media-mediadescription-i.md)&gt;&gt; |

## on('playbackCompleted')

```TypeScript
on(type: 'playbackCompleted', callback: Callback<void>): void
```

Subscribes to the video playback completion event.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onstatechange)(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playbackCompleted' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## on('bufferingUpdate')

```TypeScript
on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void
```

Subscribes to the video buffering update event. This API works only under online playback.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onbufferingupdate)(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'bufferingUpdate' | Yes |
| callback | (infoType: BufferingInfoType, value: number) = & gt; void | Yes |

## on('startRenderFrame')

```TypeScript
on(type: 'startRenderFrame', callback: Callback<void>): void
```

Subscribes to the frame rendering start event.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onstartrenderframe)(type: 'startRenderFrame', callback: Callback&lt;void&gt;)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'startRenderFrame' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## on('videoSizeChanged')

```TypeScript
on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void
```

Subscribes to the video width and height change event.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onvideosizechange)(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'videoSizeChanged' | Yes |
| callback | (width: number, height: number) = & gt; void | Yes |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void
```

Subscribes to the audio interruption event. For details, see [audio.InterruptEvent](../../apis-audio-kit/arkts-apis/arkts-audio-audio-interruptevent-i.md).

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onaudiointerrupt)(type: 'audioInterrupt', callback: Callback&lt;audio.InterruptEvent&gt;)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioInterrupt' | Yes |
| callback | (info: audio.InterruptEvent) = & gt; void | Yes |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to video playback error events. After an error event is reported, you must handle the event and exit the playback.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onerror)(type: 'error', callback: ErrorCallback)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses video playback. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [pause](arkts-media-media-avplayer-i.md#pause)(callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## pause

```TypeScript
pause(): Promise<void>
```

Pauses video playback. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [pause](arkts-media-media-avplayer-i.md#pause)()

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## play

```TypeScript
play(callback: AsyncCallback<void>): void
```

Starts video playback. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [play](arkts-media-media-avplayer-i.md#play)(callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## play

```TypeScript
play(): Promise<void>
```

Starts video playback. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [play](arkts-media-media-avplayer-i.md#play)()

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## prepare

```TypeScript
prepare(callback: AsyncCallback<void>): void
```

Prepares for video playback. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [prepare](arkts-media-media-avplayer-i.md#prepare)(callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## prepare

```TypeScript
prepare(): Promise<void>
```

Prepares for video playback. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [prepare](arkts-media-media-avplayer-i.md#prepare)()

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the video playback resources. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [release](arkts-media-media-avplayer-i.md#release)(callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## release

```TypeScript
release(): Promise<void>
```

Releases the video playback resources. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [release](arkts-media-media-avplayer-i.md#release)()

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

Resets video playback. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [reset](arkts-media-media-avplayer-i.md#reset)(callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## reset

```TypeScript
reset(): Promise<void>
```

Resets video playback. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [reset](arkts-media-media-avplayer-i.md#reset)()

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## seek

```TypeScript
seek(timeMs: number, callback: AsyncCallback<number>): void
```

Seeks to the specified playback position. The previous key frame at the specified position is played. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [seek](arkts-media-media-avplayer-i.md#seek)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeMs | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## seek

```TypeScript
seek(timeMs: number, mode: SeekMode, callback: AsyncCallback<number>): void
```

Seeks to the specified playback position. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [seek](arkts-media-media-avplayer-i.md#seek)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeMs | number | Yes |
| mode | [SeekMode](arkts-media-media-seekmode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## seek

```TypeScript
seek(timeMs: number, mode?: SeekMode): Promise<number>
```

Seeks to the specified playback position. If **mode** is not specified, the previous key frame at the specified position is played. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [seek](arkts-media-media-avplayer-i.md#seek)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeMs | number | Yes |
| mode | [SeekMode](arkts-media-media-seekmode-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## setDisplaySurface

```TypeScript
setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void
```

Sets a surface ID. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - **SetDisplaySurface** must be called between the URL setting and the calling of **prepare**. A surface must
> be set for video streams without audio. Otherwise, the calling of **prepare** fails.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| surfaceId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setDisplaySurface

```TypeScript
setDisplaySurface(surfaceId: string): Promise<void>
```

Sets a surface ID. This API uses a promise to return the result.

> **NOTE：**&gt;
> - **SetDisplaySurface** must be called between the URL setting and the calling of **prepare**. A surface must
> be set for video streams without audio. Otherwise, the calling of **prepare** fails.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| surfaceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setSpeed

```TypeScript
setSpeed(speed: number, callback: AsyncCallback<number>): void
```

Sets the playback speed. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setSpeed](arkts-media-media-avplayer-i.md#setspeed)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| speed | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## setSpeed

```TypeScript
setSpeed(speed: number): Promise<number>
```

Sets the playback speed. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setSpeed](arkts-media-media-avplayer-i.md#setspeed)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| speed | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## setVolume

```TypeScript
setVolume(vol: number, callback: AsyncCallback<void>): void
```

Sets the volume. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setVolume](arkts-media-media-avplayer-i.md#setvolume)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| vol | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setVolume

```TypeScript
setVolume(vol: number): Promise<void>
```

Sets the volume. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setVolume](arkts-media-media-avplayer-i.md#setvolume)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| vol | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops video playback. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [stop](arkts-media-media-avplayer-i.md#stop)(callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## stop

```TypeScript
stop(): Promise<void>
```

Stops video playback. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [stop](arkts-media-media-avplayer-i.md#stop)()

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## audioInterruptMode

```TypeScript
audioInterruptMode?: audio.InterruptMode
```

Audio interruption mode.

**Type:** audio.InterruptMode

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [audioInterruptMode](arkts-media-media-avplayer-i.md#audiointerruptmode)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## currentTime

```TypeScript
readonly currentTime: number
```

Current video playback position, in ms.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [currentTime](arkts-media-media-avplayer-i.md#currenttime)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## duration

```TypeScript
readonly duration: number
```

Video duration, in ms. The value **-1** indicates the live mode.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [duration](arkts-media-media-avplayer-i.md#duration)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

Description of a video file. This property is required when video assets of an application are continuously stored in a file.Assume that a music file that stores continuous music assets consists of the following:Video 1 (address offset: 0, byte length: 100)Video 2 (address offset: 101; byte length: 50)Video 3 (address offset: 151, byte length: 150)
1. To play video 1: AVFileDescriptor { fd = resource handle; offset = 0; length = 100; }
2. To play video 2: AVFileDescriptor { fd = resource handle; offset = 101; length = 50; }
3. To play video 3: AVFileDescriptor { fd = resource handle; offset = 151; length = 150; }
To play an independent video file, use **src=fd://xx**.

**Type:** [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md)

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [fdSrc](arkts-media-media-avplayer-i.md#fdsrc)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## height

```TypeScript
readonly height: number
```

Video height, in px.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [height](arkts-media-media-avplayer-i.md#height)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## loop

```TypeScript
loop: boolean
```

Whether to loop video playback. **true** to loop, **false** otherwise.

**Type:** boolean

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [loop](arkts-media-media-avplayer-i.md#loop)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## state

```TypeScript
readonly state: VideoPlayState
```

Video playback state.

**Type:** [VideoPlayState](arkts-media-media-videoplaystate-t.md)

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [state](arkts-media-media-avplayer-i.md#state)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## url

```TypeScript
url: string
```

Video URL. The video formats MP4, MPEG-TS, and MKV are supported.  
**Example of supported URLs**:
1. FD: fd://xx

2. HTTP: http://xx
3. HTTPS: https://xx
4. HLS: http://xx or https://xx
5. File type: file://xx  
**NOTE：**WebM is no longer supported since API version 11.

**Type:** string

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [url](arkts-media-media-avplayer-i.md#url)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## videoScaleType

```TypeScript
videoScaleType?: VideoScaleType
```

Video scale type. The default value is **VIDEO_SCALE_TYPE_FIT**.

**Type:** [VideoScaleType](arkts-media-media-videoscaletype-e.md)

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [videoScaleType](arkts-media-media-avplayer-i.md#videoscaletype)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## width

```TypeScript
readonly width: number
```

Video width, in px.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [width](arkts-media-media-avplayer-i.md#width)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer
