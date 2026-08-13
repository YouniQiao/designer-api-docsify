# VideoPlayer

视频播放管理类，用于管理和播放视频媒体。在调用VideoPlayer的方法前，需要先通过 [createVideoPlayer()](arkts-media-media-createvideoplayer-f.md#createVideoPlayer)构建 一个VideoPlayer实例。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer](arkts-media-media-n.md#media)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [media](arkts-media-media-n.md#media)

<!--Device-unnamed-interface VideoPlayer--><!--Device-unnamed-interface VideoPlayer-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## getTrackDescription

```TypeScript
getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void
```

获取视频轨道信息。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.getTrackDescription](arkts-media-media-avplayer-i.md#getTrackDescription) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getTrackDescription](arkts-media-media-avplayer-i.md#getTrackDescription)(callback: AsyncCallback&lt;Array&lt;MediaDescription&gt;&gt;)

<!--Device-VideoPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void--><!--Device-VideoPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MediaDescription](arkts-media-multimedia-media-mediadescription-i.md)&gt;&gt; | 是 |

## getTrackDescription

```TypeScript
getTrackDescription(): Promise<Array<MediaDescription>>
```

获取视频轨道信息。通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.getTrackDescription](arkts-media-media-avplayer-i.md#getTrackDescription)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getTrackDescription](arkts-media-media-avplayer-i.md#getTrackDescription)()

<!--Device-VideoPlayer-getTrackDescription(): Promise<Array<MediaDescription>>--><!--Device-VideoPlayer-getTrackDescription(): Promise<Array<MediaDescription>>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[MediaDescription](arkts-media-multimedia-media-mediadescription-i.md)&gt;&gt; |

## on_audioInterrupt

```TypeScript
on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void
```

监听音频焦点变化事件，参考[audio.InterruptEvent](../../apis-audio-kit/arkts-apis/arkts-audio-audio-interruptevent-i.md#InterruptEvent)。 > **说明：** > > 从API version 9开始支持，从API version 9开始废弃，建议使用 > AVPlayer.on('audioInterrupt') > 替代。

**起始版本：** 9

**废弃版本：** 9

**替代接口：** on(type: 'audioInterrupt', callback: Callback&lt;audio.InterruptEvent&gt;)

<!--Device-VideoPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void--><!--Device-VideoPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioInterrupt' | 是 |
| callback | (info: audio.InterruptEvent) = & gt; void | 是 |

## on_bufferingUpdate

```TypeScript
on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void
```

开始监听视频缓存更新事件。仅网络播放支持该订阅事件。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > AVPlayer.on('bufferingUpdate') > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler)

<!--Device-VideoPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void--><!--Device-VideoPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'bufferingUpdate' | 是 |
| callback | (infoType: BufferingInfoType, value: number) = & gt; void | 是 |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

开始监听视频播放错误事件，当上报error错误事件后，用户需处理error事件，退出播放操作。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > AVPlayer.on('error')替 > 代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'error', callback: ErrorCallback)

<!--Device-VideoPlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-VideoPlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## on_playbackCompleted

```TypeScript
on(type: 'playbackCompleted', callback: Callback<void>): void
```

开始监听视频播放完成事件。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > AVPlayer.on('stateChange') > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-VideoPlayer-on(type: 'playbackCompleted', callback: Callback<void>): void--><!--Device-VideoPlayer-on(type: 'playbackCompleted', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playbackCompleted' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## on_startRenderFrame

```TypeScript
on(type: 'startRenderFrame', callback: Callback<void>): void
```

开始监听视频播放首帧送显上报事件。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > AVPlayer.on('startRenderFrame') > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'startRenderFrame', callback: Callback&lt;void&gt;)

<!--Device-VideoPlayer-on(type: 'startRenderFrame', callback: Callback<void>): void--><!--Device-VideoPlayer-on(type: 'startRenderFrame', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'startRenderFrame' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## on_videoSizeChanged

```TypeScript
on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void
```

开始监听视频播放宽高变化事件。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > AVPlayer.on('videoSizeChange') > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler)

<!--Device-VideoPlayer-on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void--><!--Device-VideoPlayer-on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'videoSizeChanged' | 是 |
| callback | (width: number, height: number) = & gt; void | 是 |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

通过回调方式暂停播放视频。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.pause](arkts-media-media-avplayer-i.md#pause)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [pause](arkts-media-media-avplayer-i.md#pause)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-pause(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-pause(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## pause

```TypeScript
pause(): Promise<void>
```

暂停播放视频。通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.pause](arkts-media-media-avplayer-i.md#pause) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [pause](arkts-media-media-avplayer-i.md#pause)()

<!--Device-VideoPlayer-pause(): Promise<void>--><!--Device-VideoPlayer-pause(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## play

```TypeScript
play(callback: AsyncCallback<void>): void
```

开始播放视频。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.play](arkts-media-media-avplayer-i.md#play)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [play](arkts-media-media-avplayer-i.md#play)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-play(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-play(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## play

```TypeScript
play(): Promise<void>
```

开始播放视频。通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.play](arkts-media-media-avplayer-i.md#play)替代 > 。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [play](arkts-media-media-avplayer-i.md#play)()

<!--Device-VideoPlayer-play(): Promise<void>--><!--Device-VideoPlayer-play(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## prepare

```TypeScript
prepare(callback: AsyncCallback<void>): void
```

准备播放视频。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.prepare](arkts-media-media-avplayer-i.md#prepare)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [prepare](arkts-media-media-avplayer-i.md#prepare)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-prepare(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-prepare(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## prepare

```TypeScript
prepare(): Promise<void>
```

准备播放视频。通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.prepare](arkts-media-media-avplayer-i.md#prepare)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [prepare](arkts-media-media-avplayer-i.md#prepare)()

<!--Device-VideoPlayer-prepare(): Promise<void>--><!--Device-VideoPlayer-prepare(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放视频资源。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.release](arkts-media-media-avplayer-i.md#release)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [release](arkts-media-media-avplayer-i.md#release)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-release(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## release

```TypeScript
release(): Promise<void>
```

释放视频资源。通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.release](arkts-media-media-avplayer-i.md#release)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [release](arkts-media-media-avplayer-i.md#release)()

<!--Device-VideoPlayer-release(): Promise<void>--><!--Device-VideoPlayer-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

重置播放视频。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.reset](arkts-media-media-avplayer-i.md#reset)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [reset](arkts-media-media-avplayer-i.md#reset)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-reset(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-reset(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## reset

```TypeScript
reset(): Promise<void>
```

重置播放视频。通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.reset](arkts-media-media-avplayer-i.md#reset) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [reset](arkts-media-media-avplayer-i.md#reset)()

<!--Device-VideoPlayer-reset(): Promise<void>--><!--Device-VideoPlayer-reset(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## seek

```TypeScript
seek(timeMs: number, callback: AsyncCallback<number>): void
```

跳转到指定播放位置，默认跳转到指定时间点的上一个关键帧。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](arkts-media-media-avplayer-i.md#seek)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-VideoPlayer-seek(timeMs: number, callback: AsyncCallback<number>): void--><!--Device-VideoPlayer-seek(timeMs: number, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeMs | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## seek

```TypeScript
seek(timeMs: number, mode: SeekMode, callback: AsyncCallback<number>): void
```

跳转到指定播放位置。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](arkts-media-media-avplayer-i.md#seek)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-VideoPlayer-seek(timeMs: number, mode: SeekMode, callback: AsyncCallback<number>): void--><!--Device-VideoPlayer-seek(timeMs: number, mode: SeekMode, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeMs | number | 是 |
| mode | [SeekMode](arkts-media-multimedia-media-seekmode-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## seek

```TypeScript
seek(timeMs: number, mode?: SeekMode): Promise<number>
```

跳转到指定播放位置，如果没有设置mode则跳转到指定时间点的上一个关键帧。通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](arkts-media-media-avplayer-i.md#seek)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-VideoPlayer-seek(timeMs: number, mode?: SeekMode): Promise<number>--><!--Device-VideoPlayer-seek(timeMs: number, mode?: SeekMode): Promise<number>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeMs | number | 是 |
| mode | [SeekMode](arkts-media-multimedia-media-seekmode-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## setDisplaySurface

```TypeScript
setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void
```

设置SurfaceId。通过回调函数获取返回值。 > **说明：** > > - SetDisplaySurface需要在设置url和Prepare之间，无音频的视频流必须设置Surface否则Prepare失败。 > > - 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.surfaceId](../../../reference/apis-media-kit/arkts-apis-media-AVPlayer.md#属性)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

<!--Device-VideoPlayer-setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setDisplaySurface

```TypeScript
setDisplaySurface(surfaceId: string): Promise<void>
```

设置SurfaceId。通过Promise获取返回值。 > **说明：** > > - SetDisplaySurface需要在设置url和Prepare之间，无音频的视频流必须设置Surface否则Prepare失败。 > > - 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.surfaceId](../../../reference/apis-media-kit/arkts-apis-media-AVPlayer.md#属性)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

<!--Device-VideoPlayer-setDisplaySurface(surfaceId: string): Promise<void>--><!--Device-VideoPlayer-setDisplaySurface(surfaceId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setSpeed

```TypeScript
setSpeed(speed: number, callback: AsyncCallback<number>): void
```

设置播放速度。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > AVPlayer.setSpeed替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** setSpeed

<!--Device-VideoPlayer-setSpeed(speed: number, callback: AsyncCallback<number>): void--><!--Device-VideoPlayer-setSpeed(speed: number, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speed | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## setSpeed

```TypeScript
setSpeed(speed: number): Promise<number>
```

设置播放速度。通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > AVPlayer.setSpeed替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** setSpeed

<!--Device-VideoPlayer-setSpeed(speed: number): Promise<number>--><!--Device-VideoPlayer-setSpeed(speed: number): Promise<number>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speed | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## setVolume

```TypeScript
setVolume(vol: number, callback: AsyncCallback<void>): void
```

设置音量。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.setVolume](arkts-media-media-avplayer-i.md#setVolume)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setVolume](arkts-media-media-avplayer-i.md#setVolume)

<!--Device-VideoPlayer-setVolume(vol: number, callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-setVolume(vol: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| vol | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setVolume

```TypeScript
setVolume(vol: number): Promise<void>
```

设置音量。通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.setVolume](arkts-media-media-avplayer-i.md#setVolume)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setVolume](arkts-media-media-avplayer-i.md#setVolume)

<!--Device-VideoPlayer-setVolume(vol: number): Promise<void>--><!--Device-VideoPlayer-setVolume(vol: number): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| vol | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

通过回调方式停止播放视频。通过回调函数获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [AVPlayer.stop](arkts-media-media-avplayer-i.md#stop)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stop](arkts-media-media-avplayer-i.md#stop)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-stop(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## stop

```TypeScript
stop(): Promise<void>
```

停止播放视频。通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.stop](arkts-media-media-avplayer-i.md#stop)替代 > 。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stop](arkts-media-media-avplayer-i.md#stop)()

<!--Device-VideoPlayer-stop(): Promise<void>--><!--Device-VideoPlayer-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## audioInterruptMode

```TypeScript
audioInterruptMode?: audio.InterruptMode
```

音频焦点模式。

**类型：** audio.InterruptMode

**起始版本：** 9

**废弃版本：** 9

**替代接口：** audioInterruptMode

<!--Device-VideoPlayer-audioInterruptMode?: audio.InterruptMode--><!--Device-VideoPlayer-audioInterruptMode?: audio.InterruptMode-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## currentTime

```TypeScript
readonly currentTime: number
```

视频的当前播放位置，单位为毫秒（ms）。

**类型：** number

**起始版本：** 8

**废弃版本：** 9

**替代接口：** currentTime

<!--Device-VideoPlayer-readonly currentTime: number--><!--Device-VideoPlayer-readonly currentTime: number-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## duration

```TypeScript
readonly duration: number
```

视频时长，单位为毫秒（ms），返回-1表示直播模式。

**类型：** number

**起始版本：** 8

**废弃版本：** 9

**替代接口：** duration

<!--Device-VideoPlayer-readonly duration: number--><!--Device-VideoPlayer-readonly duration: number-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

视频媒体文件描述，使用场景：应用中的视频资源被连续存储在同一个文件中。 **使用示例**： 假设一个连续存储的音乐文件: 视频1(地址偏移:0，字节长度:100) 视频2(地址偏移:101，字节长度:50) 视频3(地址偏移:151，字节长度:150) 1. 播放视频1：AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; } 2. 播放视频2：AVFileDescriptor { fd = 资源句柄; offset = 101; length = 50; } 3. 播放视频3：AVFileDescriptor { fd = 资源句柄; offset = 151; length = 150; } 假设是一个独立的视频文件: 请使用src=fd://xx

**类型：** [AVFileDescriptor](arkts-media-multimedia-media-avfiledescriptor-i.md)

**起始版本：** 9

**废弃版本：** 9

**替代接口：** fdSrc

<!--Device-VideoPlayer-fdSrc: AVFileDescriptor--><!--Device-VideoPlayer-fdSrc: AVFileDescriptor-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## height

```TypeScript
readonly height: number
```

视频高，单位为像素（px）。

**类型：** number

**起始版本：** 8

**废弃版本：** 9

**替代接口：** height

<!--Device-VideoPlayer-readonly height: number--><!--Device-VideoPlayer-readonly height: number-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## loop

```TypeScript
loop: boolean
```

视频循环播放属性，设置为'true'表示循环播放。

**类型：** boolean

**起始版本：** 8

**废弃版本：** 9

**替代接口：** loop

<!--Device-VideoPlayer-loop: boolean--><!--Device-VideoPlayer-loop: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## state

```TypeScript
readonly state: VideoPlayState
```

视频播放的状态。

**类型：** [VideoPlayState](arkts-media-videoplaystate-t.md)

**起始版本：** 8

**废弃版本：** 9

**替代接口：** state

<!--Device-VideoPlayer-readonly state: VideoPlayState--><!--Device-VideoPlayer-readonly state: VideoPlayState-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## url

```TypeScript
url: string
```

视频媒体URL，支持当前主流的视频格式(mp4、mpeg-ts、mkv)。 **支持路径示例**： 1. fd类型播放：fd://xx  2. http网络播放: http://xx 3. https网络播放: https://xx 4. hls网络播放路径：http://xx或者https://xx 5. file类型: file://xx **说明：** 从API version 11开始不支持webm。

**类型：** string

**起始版本：** 8

**废弃版本：** 9

**替代接口：** url

<!--Device-VideoPlayer-url: string--><!--Device-VideoPlayer-url: string-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## videoScaleType

```TypeScript
videoScaleType?: VideoScaleType
```

视频缩放模式。默认值为VIDEO_SCALE_TYPE_FIT。

**类型：** [VideoScaleType](arkts-media-multimedia-media-videoscaletype-e.md)

**起始版本：** 9

**废弃版本：** 9

**替代接口：** videoScaleType

<!--Device-VideoPlayer-videoScaleType?: VideoScaleType--><!--Device-VideoPlayer-videoScaleType?: VideoScaleType-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## width

```TypeScript
readonly width: number
```

视频宽，单位为像素（px）。

**类型：** number

**起始版本：** 8

**废弃版本：** 9

**替代接口：** width

<!--Device-VideoPlayer-readonly width: number--><!--Device-VideoPlayer-readonly width: number-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer
