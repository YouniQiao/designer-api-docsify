# AVPlayer

AVPlayer is a playback management class. It provides APIs to manage and play media assets. Before calling any API in AVPlayer, you must use   
[createAVPlayer()](arkts-media-media-createavplayer-f.md#createAVPlayer) to create an AVPlayer instance.

When using the AVPlayer instance, you are advised to register the following callbacks to proactively obtain status changes: [on('stateChange')](media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)): listens for AVPlayer state changes. [on('error')](media.AVPlayer.on(type: 'error', callback: ErrorCallback)):listens for error events.

Applications must properly manage AVPlayer instances according to their specific needs, creating and freeing them when necessary. Holding too many AVPlayer instances can lead to high memory usage, and in some cases, the system might terminate applications to free up resources.

For details about the audio and video playback demo, see   
[Audio Playback](../../../media/media/using-avplayer-for-playback.md) and   
[Video Playback](../../../media/media/video-playback.md).

**Since:** 9

<!--Device-media-interface AVPlayer--><!--Device-media-interface AVPlayer-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## addPlaybackMediaSource

```TypeScript
addPlaybackMediaSource(src: MediaSource, id?: string): Promise<string>
```

Add a new playback source to the player's playlist.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-addPlaybackMediaSource(src: MediaSource, id?: string): Promise<string>--><!--Device-AVPlayer-addPlaybackMediaSource(src: MediaSource, id?: string): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [MediaSource](arkts-media-media-mediasource-i.md) | Yes |
| id | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400108](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## addSubtitleFromFd

```TypeScript
addSubtitleFromFd(fd: number, offset?: number, length?: number): Promise<void>
```

Adds an external subtitle to a video based on the FD. Currently, the external subtitle must be set after   
**fdSrc** of the video resource is set in an AVPlayer instance. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-addSubtitleFromFd(fd: int, offset?: long, length?: long): Promise<void>--><!--Device-AVPlayer-addSubtitleFromFd(fd: int, offset?: long, length?: long): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| offset | number | No |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## addSubtitleFromUrl

```TypeScript
addSubtitleFromUrl(url: string): Promise<void>
```

Adds an external subtitle to a video based on the URL. Currently, the external subtitle must be set after   
**fdSrc** of the video resource is set in an AVPlayer instance. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-addSubtitleFromUrl(url: string): Promise<void>--><!--Device-AVPlayer-addSubtitleFromUrl(url: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [url](#url) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## advanceToMediaSource

```TypeScript
advanceToMediaSource(id: string): Promise<void>
```

Ends playback of the current mediasource and starts playback of the specified mediasource in the mediasource list.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-advanceToMediaSource(id: string): Promise<void>--><!--Device-AVPlayer-advanceToMediaSource(id: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400108](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## advanceToNextMediaSource

```TypeScript
advanceToNextMediaSource() : Promise<void>
```

Ends playback of the current mediasource and starts playback of the next mediasource in the mediasource list.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-advanceToNextMediaSource() : Promise<void>--><!--Device-AVPlayer-advanceToNextMediaSource() : Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400108](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## advanceToPrevMediaSource

```TypeScript
advanceToPrevMediaSource(): Promise<void>
```

Ends playback of the current mediasource and starts playback of the previous mediasource in the mediasource list.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-advanceToPrevMediaSource(): Promise<void>--><!--Device-AVPlayer-advanceToPrevMediaSource(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400108](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## clearPlaybackList

```TypeScript
clearPlaybackList(): Promise<void>
```

Clears all the items in the player's playlist. Currently playing media will be terminated immediately.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-clearPlaybackList(): Promise<void>--><!--Device-AVPlayer-clearPlaybackList(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## deselectTrack

```TypeScript
deselectTrack(index: number): Promise<void>
```

Deselects the specified track when the AVPlayer plays multimedia resources with multiple audio or video tracks. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-deselectTrack(index: int): Promise<void>--><!--Device-AVPlayer-deselectTrack(index: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## getCurrentMediaSource

```TypeScript
getCurrentMediaSource(): MediaSource | undefined
```

Return the current mediasource.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-getCurrentMediaSource(): MediaSource | undefined--><!--Device-AVPlayer-getCurrentMediaSource(): MediaSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaSource](arkts-media-media-mediasource-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## getCurrentPresentationTimestamp

```TypeScript
getCurrentPresentationTimestamp() : number
```

Obtains the current playback time. This API can be called only when the AVPlayer is in the **playing**,   
**paused**, or **completed** state.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVPlayer-getCurrentPresentationTimestamp() : long--><!--Device-AVPlayer-getCurrentPresentationTimestamp() : long-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## getCurrentTrack

```TypeScript
getCurrentTrack(trackType: MediaType): Promise<number>
```

Obtains the selected track by the specified media type. This API can be called only when the AVPlayer is in the prepared, playing, or paused state. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-getCurrentTrack(trackType: MediaType): Promise<int>--><!--Device-AVPlayer-getCurrentTrack(trackType: MediaType): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| trackType | [MediaType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-mediatype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## getLoadedTimeRanges

```TypeScript
getLoadedTimeRanges(): Promise<Array<Range>>
```

Obtains the list of loaded time ranges. This API uses a promise to return the result.

> **NOTE：**
> 
> - For local media resources, the time range is from 0 to the entire media duration.
> 
> - For network media resources, the list of locally loaded time ranges is returned.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-getLoadedTimeRanges(): Promise<Array<Range>>--><!--Device-AVPlayer-getLoadedTimeRanges(): Promise<Array<Range>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;Range & gt; & gt; |

## getMediaKeySystemInfos

```TypeScript
getMediaKeySystemInfos(): Array<drm.MediaKeySystemInfo>
```

Obtains the media key system information of the media asset that is being played. This API can be called only after the   
[on('mediaKeySystemInfoUpdate')](media.AVPlayer.on(type: 'mediaKeySystemInfoUpdate', callback: Callback&lt;Array<drm.MediaKeySystemInfo>&gt;&lt;drm.MediaKeySystemInfo&gt;>))event is successfully triggered.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-getMediaKeySystemInfos(): Array<drm.MediaKeySystemInfo>--><!--Device-AVPlayer-getMediaKeySystemInfos(): Array<drm.MediaKeySystemInfo>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;drm.MediaKeySystemInfo & gt; |

## getMediaSources

```TypeScript
getMediaSources(): Array<MediaSource | undefined>
```

Return the array of mediasources in the playlist.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-getMediaSources(): Array<MediaSource | undefined>--><!--Device-AVPlayer-getMediaSources(): Array<MediaSource | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[MediaSource](arkts-media-media-mediasource-i.md) \| undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## getPlaybackInfo

```TypeScript
getPlaybackInfo(): Promise<PlaybackInfo>
```

Obtains the playback information. This API can be called only when the AVPlayer is in the prepared, playing, or paused state. This API uses a promise to return the result.

**Since:** 12

<!--Device-AVPlayer-getPlaybackInfo(): Promise<PlaybackInfo>--><!--Device-AVPlayer-getPlaybackInfo(): Promise<PlaybackInfo>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PlaybackInfo & gt; |

## getPlaybackPosition

```TypeScript
getPlaybackPosition() : number
```

Obtains the current playback position. This API can be called only when the AVPlayer is in the prepared, playing,paused, or completed state.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-getPlaybackPosition() : int--><!--Device-AVPlayer-getPlaybackPosition() : int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## getPlaybackRate

```TypeScript
getPlaybackRate(): Promise<number>
```

Obtains the playback speed of an AVPlayer. This API uses a promise to return the result.

**Since:** 23

<!--Device-AVPlayer-getPlaybackRate(): Promise<double>--><!--Device-AVPlayer-getPlaybackRate(): Promise<double>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getPlaybackStatisticMetrics

```TypeScript
getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>
```

Obtains the statistic metrics of the current player. This API can be called when the AVPlayer is in the prepared,playing, paused, completed, or stopped state. This API uses a promise to return the result.

**Since:** 23

<!--Device-AVPlayer-getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>--><!--Device-AVPlayer-getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PlaybackMetrics](arkts-media-media-playbackmetrics-t.md)&gt; |

## getSeekableTimeRanges

```TypeScript
getSeekableTimeRanges(): Promise<Array<Range>>
```

Obtains the list of seekable time ranges. This API uses a promise to return the result.

> **NOTE：**
> 
> - For local media resources and media resources that support segment-based requests, the time range is from 0
> to the entire media duration.
> 
> - For media resources that support only chunk-based transmission, there is no seekable time range.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-getSeekableTimeRanges(): Promise<Array<Range>>--><!--Device-AVPlayer-getSeekableTimeRanges(): Promise<Array<Range>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;Range & gt; & gt; |

## getSelectedTracks

```TypeScript
getSelectedTracks(): Promise<Array<number>>
```

Obtains the indexes of the selected audio or video tracks. This API can be called only when the AVPlayer is in the prepared, playing, or paused state. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-getSelectedTracks(): Promise<Array<int>>--><!--Device-AVPlayer-getSelectedTracks(): Promise<Array<int>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## getTrackDescription

```TypeScript
getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void
```

Obtains the audio and video track information. This API can be called only when the AVPlayer is in the prepared, playing, or paused state. To obtain information about all audio and video tracks, this API must be called after the data loading callback is triggered. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void--><!--Device-AVPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MediaDescription](arkts-media-media-mediadescription-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## getTrackDescription

```TypeScript
getTrackDescription(): Promise<Array<MediaDescription>>
```

Obtains the audio and video track information. This API can be called only when the AVPlayer is in the prepared, playing, or paused state. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-getTrackDescription(): Promise<Array<MediaDescription>>--><!--Device-AVPlayer-getTrackDescription(): Promise<Array<MediaDescription>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[MediaDescription](arkts-media-media-mediadescription-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## getTrackSelectionFilter

```TypeScript
getTrackSelectionFilter(): Promise<TrackSelectionFilter>
```

Obtains the track selection filter configured for the player. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-getTrackSelectionFilter(): Promise<TrackSelectionFilter>--><!--Device-AVPlayer-getTrackSelectionFilter(): Promise<TrackSelectionFilter>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[TrackSelectionFilter](arkts-media-media-trackselectionfilter-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## isSeekContinuousSupported

```TypeScript
isSeekContinuousSupported() : boolean
```

Checks whether the media source supports [seek](#seek) in SEEK_CONTINUOUS mode (specified by   
[SeekMode](arkts-media-media-seekmode-e.md#SeekMode)). The actual value is returned when this API is called in the prepared, playing, paused, or completed state. The value **false** is returned if it is called in other states. For devices that do not support the seek operation in SEEK_CONTINUOUS mode, **false** is returned.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-isSeekContinuousSupported() : boolean--><!--Device-AVPlayer-isSeekContinuousSupported() : boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## off('mediaKeySystemInfoUpdate')

```TypeScript
off(type: 'mediaKeySystemInfoUpdate', callback?: Callback<Array<drm.MediaKeySystemInfo>>): void
```

Unsubscribes from media key system information changes.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'mediaKeySystemInfoUpdate', callback?: Callback<Array<drm.MediaKeySystemInfo>>): void--><!--Device-AVPlayer-off(type: 'mediaKeySystemInfoUpdate', callback?: Callback<Array<drm.MediaKeySystemInfo>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mediaKeySystemInfoUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;drm.MediaKeySystemInfo&gt;&gt; | No |

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: OnAVPlayerStateChangeHandle): void
```

Unsubscribes from [AVPlayerState](arkts-media-media-avplayerstate-t.md#AVPlayerState) state changes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-off(type: 'stateChange', callback?: OnAVPlayerStateChangeHandle): void--><!--Device-AVPlayer-off(type: 'stateChange', callback?: OnAVPlayerStateChangeHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [OnAVPlayerStateChangeHandle](arkts-media-media-onavplayerstatechangehandle-t.md) | No |

## off('volumeChange')

```TypeScript
off(type: 'volumeChange', callback?: Callback<number>): void
```

Unsubscribes from the event that checks whether the volume is successfully set.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'volumeChange', callback?: Callback<double>): void--><!--Device-AVPlayer-off(type: 'volumeChange', callback?: Callback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'volumeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## off('endOfStream')

```TypeScript
off(type: 'endOfStream', callback?: Callback<void>): void
```

Unsubscribes from the event that indicates the end of the stream being played.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'endOfStream', callback?: Callback<void>): void--><!--Device-AVPlayer-off(type: 'endOfStream', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'endOfStream' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## off('seekDone')

```TypeScript
off(type: 'seekDone', callback?: Callback<number>): void
```

Unsubscribes from the event that checks whether the seek operation takes effect.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-off(type: 'seekDone', callback?: Callback<int>): void--><!--Device-AVPlayer-off(type: 'seekDone', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'seekDone' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## off('speedDone')

```TypeScript
off(type: 'speedDone', callback?: Callback<number>): void
```

Unsubscribes from the event that checks whether the playback speed is successfully set.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'speedDone', callback?: Callback<int>): void--><!--Device-AVPlayer-off(type: 'speedDone', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'speedDone' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## off('playbackRateDone')

```TypeScript
off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void
```

Unsubscribes from the event indicating that the playback rate set by calling   
[setPlaybackRate](#setPlaybackRate) is applied.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVPlayer-off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void--><!--Device-AVPlayer-off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playbackRateDone' | Yes |
| callback | [OnPlaybackRateDone](arkts-media-media-onplaybackratedone-t.md) | No |

## off('bitrateDone')

```TypeScript
off(type: 'bitrateDone', callback?: Callback<number>): void
```

Unsubscribes from the event that checks whether the bitrate is successfully set.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'bitrateDone', callback?: Callback<int>): void--><!--Device-AVPlayer-off(type: 'bitrateDone', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'bitrateDone' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## off('timeUpdate')

```TypeScript
off(type: 'timeUpdate', callback?: Callback<number>): void
```

Unsubscribes from playback position changes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-off(type: 'timeUpdate', callback?: Callback<int>): void--><!--Device-AVPlayer-off(type: 'timeUpdate', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'timeUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## off('durationUpdate')

```TypeScript
off(type: 'durationUpdate', callback?: Callback<number>): void
```

Unsubscribes from media asset duration changes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'durationUpdate', callback?: Callback<int>): void--><!--Device-AVPlayer-off(type: 'durationUpdate', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'durationUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## off('bufferingUpdate')

```TypeScript
off(type: 'bufferingUpdate', callback?: OnBufferingUpdateHandler): void
```

Unsubscribes from audio and video buffer changes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'bufferingUpdate', callback?: OnBufferingUpdateHandler): void--><!--Device-AVPlayer-off(type: 'bufferingUpdate', callback?: OnBufferingUpdateHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'bufferingUpdate' | Yes |
| callback | [OnBufferingUpdateHandler](arkts-media-media-onbufferingupdatehandler-t.md) | No |

## off('startRenderFrame')

```TypeScript
off(type: 'startRenderFrame', callback?: Callback<void>): void
```

Unsubscribes from the event that indicates rendering starts for the first frame.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'startRenderFrame', callback?: Callback<void>): void--><!--Device-AVPlayer-off(type: 'startRenderFrame', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'startRenderFrame' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## off('videoSizeChange')

```TypeScript
off(type: 'videoSizeChange', callback?: OnVideoSizeChangeHandler): void
```

Unsubscribes from video size changes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'videoSizeChange', callback?: OnVideoSizeChangeHandler): void--><!--Device-AVPlayer-off(type: 'videoSizeChange', callback?: OnVideoSizeChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'videoSizeChange' | Yes |
| callback | [OnVideoSizeChangeHandler](arkts-media-media-onvideosizechangehandler-t.md) | No |

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void
```

Unsubscribes from the audio interruption event.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void--><!--Device-AVPlayer-off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioInterrupt' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | No |

## off('availableBitrates')

```TypeScript
off(type: 'availableBitrates', callback?: Callback<Array<number>>): void
```

Unsubscribes from available bitrates of HLS/DASH streams. This event is reported after   
[prepare](#prepare) is called.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'availableBitrates', callback?: Callback<Array<int>>): void--><!--Device-AVPlayer-off(type: 'availableBitrates', callback?: Callback<Array<int>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'availableBitrates' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;number&gt;&gt; | No |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from AVPlayer errors.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-off(type: 'error', callback?: ErrorCallback): void--><!--Device-AVPlayer-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## off('audioOutputDeviceChangeWithInfo')

```TypeScript
off(type: 'audioOutputDeviceChangeWithInfo', callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void
```

Unsubscribes from audio stream output device changes and reasons. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'audioOutputDeviceChangeWithInfo', callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void--><!--Device-AVPlayer-off(type: 'audioOutputDeviceChangeWithInfo', callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioOutputDeviceChangeWithInfo' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.AudioStreamDeviceChangeInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## off('subtitleUpdate')

```TypeScript
off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void
```

Unsubscribes from subtitle update events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void--><!--Device-AVPlayer-off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'subtitleUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SubtitleInfo](arkts-media-media-subtitleinfo-i.md)&gt; | No |

## off('trackChange')

```TypeScript
off(type: 'trackChange', callback?: OnTrackChangeHandler): void
```

Unsubscribes from track change events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'trackChange', callback?: OnTrackChangeHandler): void--><!--Device-AVPlayer-off(type: 'trackChange', callback?: OnTrackChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'trackChange' | Yes |
| callback | [OnTrackChangeHandler](arkts-media-media-ontrackchangehandler-t.md) | No |

## off('trackInfoUpdate')

```TypeScript
off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void
```

Unsubscribes from track information update events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void--><!--Device-AVPlayer-off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'trackInfoUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[MediaDescription](arkts-media-media-mediadescription-i.md)&gt;&gt; | No |

## off('amplitudeUpdate')

```TypeScript
off(type: 'amplitudeUpdate', callback?: Callback<Array<number>>): void
```

Unsubscribes from update events of the maximum amplitude.

**Since:** 13

<!--Device-AVPlayer-off(type: 'amplitudeUpdate', callback?: Callback<Array<double>>): void--><!--Device-AVPlayer-off(type: 'amplitudeUpdate', callback?: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'amplitudeUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;number&gt;&gt; | No |

## off('seiMessageReceived')

```TypeScript
off(type: 'seiMessageReceived', payloadTypes?: Array<number>, callback?: OnSeiMessageHandle): void
```

Unsubscribes from the events indicating that an SEI message is received.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-off(type: 'seiMessageReceived', payloadTypes?: Array<int>, callback?: OnSeiMessageHandle): void--><!--Device-AVPlayer-off(type: 'seiMessageReceived', payloadTypes?: Array<int>, callback?: OnSeiMessageHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'seiMessageReceived' | Yes |
| payloadTypes | Array & lt;number & gt; | No |
| callback | [OnSeiMessageHandle](arkts-media-media-onseimessagehandle-t.md) | No |

## off('superResolutionChanged')

```TypeScript
off(type:'superResolutionChanged', callback?: OnSuperResolutionChanged): void
```

Unsubscribes from the event indicating that super resolution is enabled or disabled.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-off(type:'superResolutionChanged', callback?: OnSuperResolutionChanged): void--><!--Device-AVPlayer-off(type:'superResolutionChanged', callback?: OnSuperResolutionChanged): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'superResolutionChanged' | Yes |
| callback | [OnSuperResolutionChanged](arkts-media-media-onsuperresolutionchanged-t.md) | No |

## offMetricsEvent

```TypeScript
offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void
```

Unsubscribes from metric events during playback.

**Since:** 23

<!--Device-AVPlayer-offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void--><!--Device-AVPlayer-offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVMetricsEvent](arkts-media-media-avmetricsevent-i.md)&gt;&gt; | No |

## offPlaybackContentChanged

```TypeScript
offPlaybackContentChanged(callback?: Callback<string>):void
```

Unregisters listener to detect when changes occur in the playback content.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-offPlaybackContentChanged(callback?: Callback<string>):void--><!--Device-AVPlayer-offPlaybackContentChanged(callback?: Callback<string>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No |

## offTimedMetaData

```TypeScript
offTimedMetaData(callback?: Callback<AVTimedMetaData>): void
```

Unregister listener to detect time-based metadata,Currently, only the #EXT-X-DATERANGE data of HLS and the Event Streams information of DASH are supported.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-offTimedMetaData(callback?: Callback<AVTimedMetaData>): void--><!--Device-AVPlayer-offTimedMetaData(callback?: Callback<AVTimedMetaData>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVTimedMetaData](arkts-media-media-avtimedmetadata-i.md)&gt; | No |

## on('mediaKeySystemInfoUpdate')

```TypeScript
on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>): void
```

Subscribes to media key system information changes.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>): void--><!--Device-AVPlayer-on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mediaKeySystemInfoUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;drm.MediaKeySystemInfo&gt;&gt; | Yes |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle): void
```

Subscribes to AVPlayer state changes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle): void--><!--Device-AVPlayer-on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [OnAVPlayerStateChangeHandle](arkts-media-media-onavplayerstatechangehandle-t.md) | Yes |

## on('volumeChange')

```TypeScript
on(type: 'volumeChange', callback: Callback<number>): void
```

Subscribes to the event to check whether the volume is successfully set.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'volumeChange', callback: Callback<double>): void--><!--Device-AVPlayer-on(type: 'volumeChange', callback: Callback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'volumeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('endOfStream')

```TypeScript
on(type: 'endOfStream', callback: Callback<void>): void
```

Subscribes to the event that indicates the end of the stream being played. If   
**[loop](../../../reference/apis-media-kit/arkts-apis-media-AVPlayer.md#properties) = true** is set, the AVPlayer seeks to the beginning of the stream and plays the stream again. If **loop** is not set, the completed state is reported through the   
[stateChange](media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)) event.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'endOfStream', callback: Callback<void>): void--><!--Device-AVPlayer-on(type: 'endOfStream', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'endOfStream' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## on('seekDone')

```TypeScript
on(type: 'seekDone', callback: Callback<number>): void
```

Subscribes to the event to check whether the seek operation takes effect.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-on(type: 'seekDone', callback: Callback<int>): void--><!--Device-AVPlayer-on(type: 'seekDone', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'seekDone' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('speedDone')

```TypeScript
on(type: 'speedDone', callback: Callback<number>): void
```

Subscribes to the event to check whether the playback speed is successfully set.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'speedDone', callback: Callback<int>): void--><!--Device-AVPlayer-on(type: 'speedDone', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'speedDone' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('playbackRateDone')

```TypeScript
on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void
```

Subscribes to the event indicating that the playback rate set by calling   
[setPlaybackRate](#setPlaybackRate) is applied.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVPlayer-on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void--><!--Device-AVPlayer-on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playbackRateDone' | Yes |
| callback | [OnPlaybackRateDone](arkts-media-media-onplaybackratedone-t.md) | Yes |

## on('bitrateDone')

```TypeScript
on(type: 'bitrateDone', callback: Callback<number>): void
```

Subscribes to the event to check whether the bitrate is successfully set.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'bitrateDone', callback: Callback<int>): void--><!--Device-AVPlayer-on(type: 'bitrateDone', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'bitrateDone' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('timeUpdate')

```TypeScript
on(type: 'timeUpdate', callback: Callback<number>): void
```

Subscribes to playback position changes. It is used to refresh the current position of the progress bar. By default, this event is reported every 100 ms. However, it is reported immediately upon a successful seek operation.

> **NOTE：**
> 
> - The **'timeUpdate'** event is not supported in live streaming scenarios.
> 
> - When a seek operation is performed, the progress bar can be updated based on the **'timeUpdate'** event only
> after the seek operation is complete (**'seekdone'** received).
> 
> - In the **pause** state, the player reports the timeUpdate event when the buffering ends.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-on(type: 'timeUpdate', callback: Callback<int>): void--><!--Device-AVPlayer-on(type: 'timeUpdate', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'timeUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('durationUpdate')

```TypeScript
on(type: 'durationUpdate', callback: Callback<number>): void
```

Subscribes to media asset duration changes. It is used to refresh the length of the progress bar. By default, this event is reported once in the prepared state. However, it can be repeatedly reported for special streams that trigger duration changes.

> **NOTE：**
> 
> The **durationUpdate** event is not supported in live streaming scenarios.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'durationUpdate', callback: Callback<int>): void--><!--Device-AVPlayer-on(type: 'durationUpdate', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'durationUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('bufferingUpdate')

```TypeScript
on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler): void
```

Subscribes to audio and video buffer changes. This subscription is supported only in network playback scenarios.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler): void--><!--Device-AVPlayer-on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'bufferingUpdate' | Yes |
| callback | [OnBufferingUpdateHandler](arkts-media-media-onbufferingupdatehandler-t.md) | Yes |

## on('startRenderFrame')

```TypeScript
on(type: 'startRenderFrame', callback: Callback<void>): void
```

Subscribes to the event that indicates rendering starts for the first frame. This subscription is supported only in video playback scenarios. This event only means that the playback service sends the first frame to the display module. The actual rendering effect depends on the rendering performance of the display service.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'startRenderFrame', callback: Callback<void>): void--><!--Device-AVPlayer-on(type: 'startRenderFrame', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'startRenderFrame' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## on('videoSizeChange')

```TypeScript
on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler): void
```

Subscribes to video size (width and height) changes. This subscription is supported only in video playback scenarios. By default, this event is reported only once in the prepared state. However, it is also reported upon resolution changes in the case of HLS streams.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler): void--><!--Device-AVPlayer-on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'videoSizeChange' | Yes |
| callback | [OnVideoSizeChangeHandler](arkts-media-media-onvideosizechangehandler-t.md) | Yes |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void
```

Subscribes to the audio interruption event. When multiple audio and video assets are played at the same time, this event is triggered based on the audio interruption mode   
[audio.InterruptMode](../../apis-audio-kit/arkts-apis/arkts-audio-audio-interruptmode-e.md#InterruptMode). The application needs to perform corresponding processing based on different audio interruption events. For details, see   
[Handling Audio Interruption Events](../../../media/audio/audio-playback-concurrency.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void--><!--Device-AVPlayer-on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioInterrupt' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | Yes |

## on('availableBitrates')

```TypeScript
on(type: 'availableBitrates', callback: Callback<Array<number>>): void
```

Subscribes to available bitrates of HLS/DASH streams. This event is reported only after the AVPlayer switches to the prepared state.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'availableBitrates', callback: Callback<Array<int>>): void--><!--Device-AVPlayer-on(type: 'availableBitrates', callback: Callback<Array<int>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'availableBitrates' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;number&gt;&gt; | Yes |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to [AVPlayer](arkts-multimedia-media.md#media) errors. This event is used only for error prompt and does not require the user to stop playback control. If the   
[AVPlayerState](arkts-media-media-avplayerstate-t.md#AVPlayerState) is also switched to error, call   
[reset()](#reset) or   
[release()](#release) to exit the playback. If the playback remains in the error state after the [reset()](#reset) method is called, you are advised to directly invoke the   
[release()](#release) method to exit the playback operation.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-AVPlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5410002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5410002-seek-in-seekcontinuous-mode-is-not-supported) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [5411002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411002-network-connection-timeout) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [5411003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411003-data-or-link-exception-caused-by-network-exceptions) |
| [5411001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411001-failed-to-parse-or-connect-to-the-server-address) |
| [5411006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411006-client-request-parameter-is-incorrect-or-exceeds-the-processing-capability) |
| [5411007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411007-no-resource-available) |
| [5411004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411004-network-disabled) |
| [5411005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411005-access-denied) |
| [5411010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411010-client-fails-to-verify-the-server-certificate) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5411011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411011-unsupported-request-due-to-network-protocol-errors) |
| [5411008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411008-server-fails-to-verify-the-client-certificate) |
| [5411009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411009-ssl-connection-failed) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5411012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5411012-request-not-supported-due-to-http-plaintext-interception) |
| [5400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |
| [5400106](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400106-format-not-supported) |
| [5400104](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400104-operation-timeout) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## on('audioOutputDeviceChangeWithInfo')

```TypeScript
on(type: 'audioOutputDeviceChangeWithInfo', callback: Callback<audio.AudioStreamDeviceChangeInfo>): void
```

Subscribes to audio stream output device changes and reasons. This API uses an asynchronous callback to return the result.

When subscribing to this event, you are advised to implement the player behavior when the device is connected or disconnected by referring to   
[Handling Output Device Changes Gracefully](../../../media/audio/audio-output-device-change.md).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'audioOutputDeviceChangeWithInfo', callback: Callback<audio.AudioStreamDeviceChangeInfo>): void--><!--Device-AVPlayer-on(type: 'audioOutputDeviceChangeWithInfo', callback: Callback<audio.AudioStreamDeviceChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioOutputDeviceChangeWithInfo' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.AudioStreamDeviceChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## on('subtitleUpdate')

```TypeScript
on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void
```

Subscribes to subtitle update events. When external subtitles exist, the system notifies the application through the subscribed-to callback. An application can subscribe to only one subtitle update event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void--><!--Device-AVPlayer-on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'subtitleUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SubtitleInfo](arkts-media-media-subtitleinfo-i.md)&gt; | Yes |

## on('trackChange')

```TypeScript
on(type: 'trackChange', callback: OnTrackChangeHandler): void
```

Subscribes to track change events. When the track changes, the system notifies the application through the subscribed-to callback. An application can subscribe to only one track change event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'trackChange', callback: OnTrackChangeHandler): void--><!--Device-AVPlayer-on(type: 'trackChange', callback: OnTrackChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'trackChange' | Yes |
| callback | [OnTrackChangeHandler](arkts-media-media-ontrackchangehandler-t.md) | Yes |

## on('trackInfoUpdate')

```TypeScript
on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void
```

Subscribes to track information update events. When the track information is updated, the system notifies the application through the subscribed-to callback. An application can subscribe to only one track change event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void--><!--Device-AVPlayer-on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'trackInfoUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[MediaDescription](arkts-media-media-mediadescription-i.md)&gt;&gt; | Yes |

## on('amplitudeUpdate')

```TypeScript
on(type: 'amplitudeUpdate', callback: Callback<Array<number>>): void
```

Subscribes to update events of the maximum audio level value, which is periodically reported when audio resources are played.

**Since:** 13

<!--Device-AVPlayer-on(type: 'amplitudeUpdate', callback: Callback<Array<double>>): void--><!--Device-AVPlayer-on(type: 'amplitudeUpdate', callback: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'amplitudeUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;number&gt;&gt; | Yes |

## on('seiMessageReceived')

```TypeScript
on(type: 'seiMessageReceived', payloadTypes: Array<number>, callback: OnSeiMessageHandle): void
```

Subscribes to events indicating that a Supplemental Enhancement Information (SEI) message is received. This applies only to HTTP-FLV live streaming and is triggered when SEI messages are present in the video stream. You must initiate the subscription before calling **prepare**. If you initiate multiple subscriptions to this event, the last subscription is applied.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-on(type: 'seiMessageReceived', payloadTypes: Array<int>, callback: OnSeiMessageHandle): void--><!--Device-AVPlayer-on(type: 'seiMessageReceived', payloadTypes: Array<int>, callback: OnSeiMessageHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'seiMessageReceived' | Yes |
| payloadTypes | Array & lt;number & gt; | Yes |
| callback | [OnSeiMessageHandle](arkts-media-media-onseimessagehandle-t.md) | Yes |

## on('superResolutionChanged')

```TypeScript
on(type:'superResolutionChanged', callback: OnSuperResolutionChanged): void
```

Subscribes to the event indicating that super resolution is enabled or disabled.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-on(type:'superResolutionChanged', callback: OnSuperResolutionChanged): void--><!--Device-AVPlayer-on(type:'superResolutionChanged', callback: OnSuperResolutionChanged): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'superResolutionChanged' | Yes |
| callback | [OnSuperResolutionChanged](arkts-media-media-onsuperresolutionchanged-t.md) | Yes |

## onMetricsEvent

```TypeScript
onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void
```

Subscribes to metric events during playback.

**Since:** 23

<!--Device-AVPlayer-onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void--><!--Device-AVPlayer-onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVMetricsEvent](arkts-media-media-avmetricsevent-i.md)&gt;&gt; | Yes |

## onPlaybackContentChanged

```TypeScript
onPlaybackContentChanged(callback: Callback<string>):void
```

Registers a listener to detect when the playback content has changed.The value carried in the callback function is the ID of the media source that is being played in the playlist.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-onPlaybackContentChanged(callback: Callback<string>):void--><!--Device-AVPlayer-onPlaybackContentChanged(callback: Callback<string>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

## onTimedMetaData

```TypeScript
onTimedMetaData(callback: Callback<AVTimedMetaData>): void
```

Register listener to detect time-based metadata,Currently, only the #EXT-X-DATERANGE data of HLS and the Event Streams information of DASH are supported.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-onTimedMetaData(callback: Callback<AVTimedMetaData>): void--><!--Device-AVPlayer-onTimedMetaData(callback: Callback<AVTimedMetaData>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVTimedMetaData](arkts-media-media-avtimedmetadata-i.md)&gt; | Yes |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses audio and video playback. This API can be called only when the AVPlayer is in the playing state. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-pause(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-pause(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## pause

```TypeScript
pause(): Promise<void>
```

Pauses audio and video playback. This API can be called only when the AVPlayer is in the playing state. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-pause(): Promise<void>--><!--Device-AVPlayer-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## play

```TypeScript
play(callback: AsyncCallback<void>): void
```

Starts to play an audio and video asset. This API can be called only when the AVPlayer is in the prepared, paused,or completed state. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-play(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-play(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## play

```TypeScript
play(): Promise<void>
```

Starts to play an audio and video asset. This API can be called only when the AVPlayer is in the prepared, paused,or completed state. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-play(): Promise<void>--><!--Device-AVPlayer-play(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## prepare

```TypeScript
prepare(callback: AsyncCallback<void>): void
```

Prepares for audio and video playback. This API can be called only when the AVPlayer is in the initialized state.The state changes can be detected by subscribing to the   
[stateChange](media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)) event. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-prepare(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-prepare(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400106-format-not-supported) |

## prepare

```TypeScript
prepare(): Promise<void>
```

Prepares for audio and video playback. This API can be called only when the AVPlayer is in the initialized state.The state changes can be detected by subscribing to the   
[stateChange](media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)) event. This API uses a promise to return the result.

If your application frequently switches between short videos, you can create multiple AVPlayer objects to prepare the next video in advance, thereby improving the switching performance. For details, see   
[Smooth Switchover Between Online Short Videos](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-smooth-switching).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-prepare(): Promise<void>--><!--Device-AVPlayer-prepare(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400106-format-not-supported) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the playback resources. This API can be called when the AVPlayer is in any state except released. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-release(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## release

```TypeScript
release(): Promise<void>
```

Releases the playback resources. This API can be called when the AVPlayer is in any state except released. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-release(): Promise<void>--><!--Device-AVPlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## removePlaybackMediaSource

```TypeScript
removePlaybackMediaSource(id: string): Promise<void>
```

Removes the specified playback media source from the player's playlist.If the id does not exist in the current playlist, the method returns immediately.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-removePlaybackMediaSource(id: string): Promise<void>--><!--Device-AVPlayer-removePlaybackMediaSource(id: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400108](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

Resets audio and video playback. This API can be called only when the AVPlayer is in the initialized, prepared, playing, paused, completed, stopped, or error state. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-reset(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-reset(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## reset

```TypeScript
reset(): Promise<void>
```

Resets audio and video playback. This API can be called only when the AVPlayer is in the initialized, prepared, playing, paused, completed, stopped, or error state. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-reset(): Promise<void>--><!--Device-AVPlayer-reset(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## seek

```TypeScript
seek(timeMs: number, mode?: SeekMode): void
```

Seeks to the specified playback position. This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state. You can check whether the seek operation takes effect by subscribing to the   
[on('seekDone')](media.AVPlayer.on(type: 'seekDone', callback: Callback&lt;int&gt;)) event.

> **NOTE：**
> 
> Since API version 24, **seek** is supported in live streaming scenarios.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-seek(timeMs: int, mode?: SeekMode): void--><!--Device-AVPlayer-seek(timeMs: int, mode?: SeekMode): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeMs | number | Yes |
| mode | [SeekMode](arkts-media-media-seekmode-e.md) | No |

## seekToDefaultPosition

```TypeScript
seekToDefaultPosition(): void
```

Seeks to the default access point of the playback source. For live streams, the latest recommended access point is used. For on-demand videos, the start position of the video is used (equivalent to **seek(0)**).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-seekToDefaultPosition(): void--><!--Device-AVPlayer-seekToDefaultPosition(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## selectTrack

```TypeScript
selectTrack(index: number, mode?: SwitchMode): Promise<void>
```

Selects a track when the AVPlayer plays multimedia resources with multiple audio or video tracks. This API uses a promise to return the result.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-selectTrack(index: int, mode?: SwitchMode): Promise<void>--><!--Device-AVPlayer-selectTrack(index: int, mode?: SwitchMode): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| mode | [SwitchMode](arkts-media-media-switchmode-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## setBitrate

```TypeScript
setBitrate(bitrate: number): void
```

Sets the bitrate for the streaming media. This API is valid only for HLS/DASH streams. By default, the AVPlayer selects a proper bitrate based on the network connection speed. This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state. You can check whether the setting takes effect by subscribing to the [bitrateDone](media.AVPlayer.on(type: 'bitrateDone', callback: Callback&lt;int&gt;)) event.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setBitrate(bitrate: int): void--><!--Device-AVPlayer-setBitrate(bitrate: int): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bitrate | number | Yes |

## setDecryptionConfig

```TypeScript
setDecryptionConfig(mediaKeySession: drm.MediaKeySession, secureVideoPath: boolean): void
```

Sets the decryption configuration. When receiving an   
[on('mediaKeySystemInfoUpdate')](media.AVPlayer.on(type: 'mediaKeySystemInfoUpdate', callback: Callback&lt;Array<drm.MediaKeySystemInfo>&gt;&lt;drm.MediaKeySystemInfo&gt;>))event, create the related configuration and set the decryption configuration based on the information in the reported event. Otherwise, the playback fails.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setDecryptionConfig(mediaKeySession: drm.MediaKeySession, secureVideoPath: boolean): void--><!--Device-AVPlayer-setDecryptionConfig(mediaKeySession: drm.MediaKeySession, secureVideoPath: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaKeySession | drm.MediaKeySession | Yes |
| secureVideoPath | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setLoudnessGain

```TypeScript
setLoudnessGain(loudnessGain: number): Promise<void>
```

Sets the loudness gain of the AVPlayer. After this API is called, the loudness gain takes effect immediately. This API uses a promise to return the result.

> **NOTE：**
> 
> - This API can be called when the AVPlayer is in the prepared, playing, paused, completed, or stopped state.
> 
> - Before calling this API, ensure that the audio rendering information has been set in
> **AVPlayer.audioRendererInfo** and the **usage** parameter in **audioRendererInfo** has been set to
> [STREAM_USAGE_MUSIC](../../apis-audio-kit/arkts-apis/arkts-audio-audio-streamusage-e.md#StreamUsage),
> [STREAM_USAGE_MOVIE](../../apis-audio-kit/arkts-apis/arkts-audio-audio-streamusage-e.md#StreamUsage), or
> [STREAM_USAGE_AUDIOBOOK](../../apis-audio-kit/arkts-apis/arkts-audio-audio-streamusage-e.md#StreamUsage).

**Since:** 21

<!--Device-AVPlayer-setLoudnessGain(loudnessGain: double): Promise<void>--><!--Device-AVPlayer-setLoudnessGain(loudnessGain: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| loudnessGain | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setMediaMuted

```TypeScript
setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>
```

Mutes or unmutes the audio. Since API version 20, this API also supports whether to display the video image. This API uses a promise to return the result.

This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>--><!--Device-AVPlayer-setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaType | [MediaType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-mediatype-e.md) | Yes |
| muted | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## setMediaSource

```TypeScript
setMediaSource(src: MediaSource, strategy?: PlaybackStrategy): Promise<void>
```

Sets a source of streaming media that can be pre-downloaded, downloads the media data, and temporarily stores the data in the memory. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setMediaSource(src: MediaSource, strategy?: PlaybackStrategy): Promise<void>--><!--Device-AVPlayer-setMediaSource(src: MediaSource, strategy?: PlaybackStrategy): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [MediaSource](arkts-media-media-mediasource-i.md) | Yes |
| strategy | [PlaybackStrategy](arkts-media-media-playbackstrategy-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## setPlaybackRange

```TypeScript
setPlaybackRange(startTimeMs: number, endTimeMs: number, mode?: SeekMode) : Promise<void>
```

Sets the playback range and seeks to the start position of the range based on the specified   
[SeekMode](arkts-media-media-seekmode-e.md#SeekMode). After the setting, only the content in the specified range of the audio or video file is played. This API uses a promise to return the result. It can be used in the initialized, prepared, paused, stopped, or completed state.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-setPlaybackRange(startTimeMs: int, endTimeMs: int, mode?: SeekMode) : Promise<void>--><!--Device-AVPlayer-setPlaybackRange(startTimeMs: int, endTimeMs: int, mode?: SeekMode) : Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startTimeMs | number | Yes |
| endTimeMs | number | Yes |
| mode | [SeekMode](arkts-media-media-seekmode-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## setPlaybackRate

```TypeScript
setPlaybackRate(rate: number): void
```

Sets the playback rate. This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state. The value range is [0.125, 4.0]. You can check whether the setting takes effect through the   
[playbackRateDone](media.AVPlayer.on(type: 'playbackRateDone', callback: OnPlaybackRateDone)) event.

> **NOTE：**
> 
> This API is not supported in live mode.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVPlayer-setPlaybackRate(rate: double): void--><!--Device-AVPlayer-setPlaybackRate(rate: double): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rate | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400108](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## setPlaybackStrategy

```TypeScript
setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>
```

Sets a playback strategy. This API can be called only when the AVPlayer is in the initialized state. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>--><!--Device-AVPlayer-setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [PlaybackStrategy](arkts-media-media-playbackstrategy-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## setSpeed

```TypeScript
setSpeed(speed: PlaybackSpeed): void
```

Sets the playback speed. This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state. You can check whether the speed setting takes effect by subscribing to the   
[on('speedDone')](media.AVPlayer.on(type: 'speedDone', callback: Callback&lt;int&gt;)) event.

> **NOTE：**
> 
> This method is not supported in live streaming scenarios.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setSpeed(speed: PlaybackSpeed): void--><!--Device-AVPlayer-setSpeed(speed: PlaybackSpeed): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| speed | [PlaybackSpeed](../../apis-arkui/arkts-components/arkts-arkui-playbackspeed-e.md) | Yes |

## setSuperResolution

```TypeScript
setSuperResolution(enabled: boolean) : Promise<void>
```

Enables or disables super resolution. This API can be called when the AVPlayer is in the initialized, prepared, playing, paused, completed, or stopped state. This API uses a promise to return the result.

Before calling [prepare()](#prepare), enable super resolution by using [PlaybackStrategy](arkts-media-media-playbackstrategy-i.md#PlaybackStrategy).

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-setSuperResolution(enabled: boolean) : Promise<void>--><!--Device-AVPlayer-setSuperResolution(enabled: boolean) : Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5410003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5410003-super-resolution-is-not-supported) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5410004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5410004-super-resolution-is-not-enabled) |

## setTrackSelectionFilter

```TypeScript
setTrackSelectionFilter(filter : TrackSelectionFilter): Promise<void>
```

Sets a track selection filter for the player. The player will use this filter to select available tracks for playback. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-setTrackSelectionFilter(filter : TrackSelectionFilter): Promise<void>--><!--Device-AVPlayer-setTrackSelectionFilter(filter : TrackSelectionFilter): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [TrackSelectionFilter](arkts-media-media-trackselectionfilter-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## setVideoWindowSize

```TypeScript
setVideoWindowSize(width: number, height: number) : Promise<void>
```

Sets the resolution of the output video after super resolution. This API can be called when the AVPlayer is in the initialized, prepared, playing, paused, completed, or stopped state. This API uses a promise to return the result.

The input parameter values must be in the range of 320 × 320 to 1920 × 1080 (in px).

Before calling [prepare()](#prepare), enable super resolution by using [PlaybackStrategy](arkts-media-media-playbackstrategy-i.md#PlaybackStrategy).

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-setVideoWindowSize(width: int, height: int) : Promise<void>--><!--Device-AVPlayer-setVideoWindowSize(width: int, height: int) : Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [width](#width) | number | Yes |
| [height](#height) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5410003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5410003-super-resolution-is-not-supported) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5410004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5410004-super-resolution-is-not-enabled) |

## setVolume

```TypeScript
setVolume(volume: number): void
```

Sets the playback volume. This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state. You can check whether the volume setting takes effect by subscribing to the   
[on('volumeChange')](media.AVPlayer.on(type: 'volumeChange', callback: Callback&lt;double&gt;)) event.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setVolume(volume: double): void--><!--Device-AVPlayer-setVolume(volume: double): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volume | number | Yes |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops audio and video playback. This API can be called only when the AVPlayer is in the prepared, playing, paused,or completed state. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-stop(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## stop

```TypeScript
stop(): Promise<void>
```

Stops audio and video playback. This API can be called only when the AVPlayer is in the prepared, playing, paused,or completed state. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-stop(): Promise<void>--><!--Device-AVPlayer-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## audioEffectMode

```TypeScript
audioEffectMode ?: audio.AudioEffectMode
```

Audio effect mode. The audio effect mode is a dynamic property and is restored to the default value   
**EFFECT_DEFAULT** when **usage** of **audioRendererInfo** is changed. It can be set only when the AVPlayer is in the prepared, playing, paused, or completed state.

**Type:** audio.AudioEffectMode

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-audioEffectMode ?: audio.AudioEffectMode--><!--Device-AVPlayer-audioEffectMode ?: audio.AudioEffectMode-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## audioInterruptMode

```TypeScript
audioInterruptMode?: audio.InterruptMode
```

Audio interruption mode. The default value is **SHARE_MODE**. It is a dynamic property

and can be set only when the AVPlayer is in the prepared, playing, paused, or completed state.

To take effect, this property must be set before   
[play()](#play) is called for the first time.

**Type:** audio.InterruptMode

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-audioInterruptMode?: audio.InterruptMode--><!--Device-AVPlayer-audioInterruptMode?: audio.InterruptMode-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## audioRendererInfo

```TypeScript
audioRendererInfo?: audio.AudioRendererInfo
```

Audio renderer information. If the media source contains videos, the default value of **usage** is   
**STREAM_USAGE_MOVIE**. Otherwise, the default value of **usage** is **STREAM_USAGE_MUSIC**. The default value of  
**rendererFlags** is 0. If the default value of **usage** does not meet the requirements, configure   
[audio.AudioRendererInfo](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audiorendererinfo-i.md#AudioRendererInfo).

This parameter can be set only when the AVPlayer is in the initialized state.

To take effect, this property must be set before   
[prepare()](#prepare) is called for the first time.

**Type:** audio.AudioRendererInfo

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-audioRendererInfo?: audio.AudioRendererInfo--><!--Device-AVPlayer-audioRendererInfo?: audio.AudioRendererInfo-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## currentTime

```TypeScript
readonly currentTime: number
```

Current video playback position, in ms. It can be used as a query parameter when the AVPlayer is in the prepared,playing, paused, or completed state.

The value **-1** indicates an invalid value.

In live mode, **-1** is returned by default.

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-readonly currentTime: int--><!--Device-AVPlayer-readonly currentTime: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## dataSrc

```TypeScript
dataSrc?: AVDataSrcDescriptor
```

Descriptor of a streaming media asset. It can be set only when the AVPlayer is in the idle state.

**Use scenario**: An application plays a file that has been downloaded from a remote source and saved locally. When the application has not yet downloaded the complete audio or video resources, it can start playing the data that has already been retrieved. By writing the retrieved data to a local file and simultaneously reading from that file, the application can achieve the capability of playing while caching.

The video formats MP4, MPEG-TS, and MKV are supported.

The audio formats M4A, AAC, MP3, OGG, WAV, FLAC, AMR, and APE are supported.

A user is obtaining an audio and video file from a remote server and wants to play the downloaded file content. To implement this scenario, do as follows:

1. Obtain the total file size, in bytes. If the total size cannot be obtained, set **fileSize** to **-1**.2. Implement the **func** callback to fill in data. If **fileSize** is **-1**, the format of **func** is **func(buffer: ArrayBuffer, length: number)**, and the AVPlayer obtains data in sequence; otherwise, the format is **func(buffer: ArrayBuffer, length: number, pos: number)**, and the AVPlayer seeks and obtains data in the required positions.3. Set **AVDataSrcDescriptor {fileSize = size, callback = func}**.

**Notes:**

If the media file to play is in MP4/M4A format, ensure that the **moov** field (specifying the media information)is before the **mdat** field (specifying the media data) or the fields before the **moov** field is less than 10 MB. Otherwise, the parsing fails and the media file cannot be played.

**NOTE：**

WebM is no longer supported since API version 11.

**Type:** [AVDataSrcDescriptor](arkts-media-media-avdatasrcdescriptor-i.md)

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-dataSrc?: AVDataSrcDescriptor--><!--Device-AVPlayer-dataSrc?: AVDataSrcDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## duration

```TypeScript
readonly duration: number
```

Video duration, in ms. It can be used as a query parameter when the AVPlayer is in the prepared, playing, paused,or completed state.

The value **-1** indicates an invalid value.

In live mode, **-1** is returned by default.

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-readonly duration: int--><!--Device-AVPlayer-readonly duration: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## fdSrc

```TypeScript
fdSrc?: AVFileDescriptor
```

FD of the media asset. It can be set only when the AVPlayer is in the idle state.

**Use scenario**: This property is required when media assets of an application are continuously stored in a file.

The video formats MP4, MPEG-TS, and MKV are supported.

The audio formats M4A, AAC, MP3, OGG, WAV, FLAC, AMR, and APE are supported.

Assume that a media file that stores continuous assets consists of the following:

Video 1 (address offset: 0, byte length: 100)

Video 2 (address offset: 101; byte length: 50)

Video 3 (address offset: 151, byte length: 150)

1. To play video 1: AVFileDescriptor { fd = resource handle; offset = 0; length = 100; }2. To play video 2: AVFileDescriptor { fd = resource handle; offset = 101; length = 50; }3. To play video 3: AVFileDescriptor { fd = resource handle; offset = 151; length = 150; }

To play an independent media file, use **src=fd://xx**.

**NOTE：**

WebM is no longer supported since API version 11.

**Type:** [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md)

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-fdSrc?: AVFileDescriptor--><!--Device-AVPlayer-fdSrc?: AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## height

```TypeScript
readonly height: number
```

Video height, in px. It can be used as a query parameter when the AVPlayer is in the prepared, playing, paused, or completed state.

The value **0** indicates an invalid value.

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-readonly height: int--><!--Device-AVPlayer-readonly height: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## loop

```TypeScript
loop: boolean
```

Whether to loop playback. **true** to loop, **false** otherwise. The default value is **false**. It is a dynamic property

and can be set only when the AVPlayer is in the prepared, playing, paused, or completed state.

This setting is not supported in live mode.

**Type:** boolean

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-loop: boolean--><!--Device-AVPlayer-loop: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## playlistLoopMode

```TypeScript
playlistLoopMode?: PlaylistLoopMode
```

Set the loop mode when playing the media source playlist.&lt;br&gt;Default value:PLAYLIST_LOOP_MODE_ALL, which means loops all items in the playlist.

**Type:** [PlaylistLoopMode](arkts-media-media-playlistloopmode-e.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-playlistLoopMode?: PlaylistLoopMode--><!--Device-AVPlayer-playlistLoopMode?: PlaylistLoopMode-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## privacyType

```TypeScript
privacyType?: audio.AudioPrivacyType
```

Audio privacy configuration. For more information, see [AudioPrivacyType](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioprivacytype-e.md#AudioPrivacyType).Default value: PRIVACY_TYPE_PUBLIC.

**Type:** audio.AudioPrivacyType

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-privacyType?: audio.AudioPrivacyType--><!--Device-AVPlayer-privacyType?: audio.AudioPrivacyType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## state

```TypeScript
readonly state: AVPlayerState
```

AVPlayer state. It can be used as a query parameter when the AVPlayer is in any state.

**Type:** [AVPlayerState](arkts-media-media-avplayerstate-t.md)

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-readonly state: AVPlayerState--><!--Device-AVPlayer-readonly state: AVPlayerState-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## surfaceId

```TypeScript
surfaceId?: string
```

Video window ID. By default, there is no video window.

This property can be set for the first time only when the AVPlayer is in the initialized state.

It can be updated when the AVPlayer is in the prepared, playing, paused, completed, or stopped state. After the reset, the video is played in the new window.

**Use scenario**: It is used to render the window for video playback (not involved in audio-only playback scenarios).

[Create a surface ID through XComponent](../../apis-arkui/arkts-components/arkts-arkui-xcomponentcontroller-c.md#getXComponentSurfaceId).

**Type:** string

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-surfaceId?: string--><!--Device-AVPlayer-surfaceId?: string-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## url

```TypeScript
url?: string
```

URL of the media asset. It can be set only when the AVPlayer is in the idle state. 

Supported video formats: MP4, MPEG-TS, and MKV.

Supported audio formats: M4A, AAC, MP3, OGG, WAV, FLAC, AMR, and APE.

**Example of supported URLs**:

1. FD: fd://xx

![](../../../reference/apis-media-kit/figures/en-us_image_url.png)

2. HTTP: http://xx3. HTTPS: https://xx4. HLS: http://xx or https://xx

**NOTE：**

- To set the playback URL, you need to declare the   
[ohos.permission.INTERNET](../../../security/AccessToken/permissions-for-all.md#ohospermissioninternet) permission. The related error code is   
[201 Permission Denied](../../../reference/errorcode-universal.md#201-permission-denied).  
- WebM is no longer supported since API version 11.  
- After the resource handle (FD) is transferred to an AVPlayer instance, do not use the resource handle to   
perform other read and write operations, including but not limited to transferring this handle to other AVPlayer,AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. Competition occurs when multiple AVPlayers use the same resource handle to read and write files at the same time, resulting in errors in obtaining data.

**Type:** string

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-url?: string--><!--Device-AVPlayer-url?: string-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## videoScaleType

```TypeScript
videoScaleType?: VideoScaleType
```

Video scale type. The default value is **VIDEO_SCALE_TYPE_FIT**. It is a dynamic property

and can be set only when the AVPlayer is in the prepared, playing, paused, or completed state.

**Type:** [VideoScaleType](arkts-media-media-videoscaletype-e.md)

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-videoScaleType?: VideoScaleType--><!--Device-AVPlayer-videoScaleType?: VideoScaleType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## width

```TypeScript
readonly width: number
```

Video width, in px. It can be used as a query parameter when the AVPlayer is in the prepared, playing, paused, or completed state.

The value **0** indicates an invalid value.

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-readonly width: int--><!--Device-AVPlayer-readonly width: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer
