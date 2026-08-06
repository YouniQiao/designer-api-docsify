# AVPlayer

AVPlayer is a playback management class. It provides APIs to manage and play media assets. Before calling any API in AVPlayer, you must use  
[createAVPlayer()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to create an AVPlayer instance.

When using the AVPlayer instance, you are advised to register the following callbacks to proactively obtain status changes: [on('stateChange')]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_:listens for AVPlayer state changes. [on('error')]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_:listens for error events.

Applications must properly manage AVPlayer instances according to their specific needs, creating and freeing them when necessary. Holding too many AVPlayer instances can lead to high memory usage, and in some cases, the system might terminate applications to free up resources.

For details about the audio and video playback demo, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ and  
\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-media-interface AVPlayer--><!--Device-media-interface AVPlayer-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## addPlaybackMediaSource

```TypeScript
addPlaybackMediaSource(src: MediaSource, id?: string): Promise<string>
```

Add a new playback source to the player's playlist.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-addPlaybackMediaSource(src: MediaSource, id?: string): Promise<string>--><!--Device-AVPlayer-addPlaybackMediaSource(src: MediaSource, id?: string): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Playback source to be added to the playlist. |
| id | string | No | Indicates the ID of a media source in the playlist. The newly added media source is inserted before the specified media source. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Default value:if empty, it means adding to the end of the list |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the result, if success, a unique ID corresponding to the media resource will be returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) | The media source ID does not exist in the playlist. Returned by promise. |

## addSubtitleFromFd

ArkTS-Dyn:
```TypeScript
addSubtitleFromFd(fd: number, offset?: number, length?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
addSubtitleFromFd(fd: int, offset?: long, length?: long): Promise<void>
```

Adds an external subtitle to a video based on the FD. Currently, the external subtitle must be set after  
**fdSrc** of the video resource is set in an AVPlayer instance. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-addSubtitleFromFd(fd: int, offset?: long, length?: long): Promise<void>--><!--Device-AVPlayer-addSubtitleFromFd(fd: int, offset?: long, length?: long): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Resource handle, which is obtained by calling [resourceManager.getRawFd]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| offset | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | No | Resource offset, which needs to be entered based on the preset asset information. An invalid value causes a failure to parse subtitle assets. The default value is **0**.unit:Byte. |
| length | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | No | Resource length, which needs to be entered based on the preset asset information. The default value is the remaining bytes from the offset in the file. An invalid value causes a failure to parse subtitle assets. The default value is **0**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## addSubtitleFromUrl

```TypeScript
addSubtitleFromUrl(url: string): Promise<void>
```

Adds an external subtitle to a video based on the URL. Currently, the external subtitle must be set after  
**fdSrc** of the video resource is set in an AVPlayer instance. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-addSubtitleFromUrl(url: string): Promise<void>--><!--Device-AVPlayer-addSubtitleFromUrl(url: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | Address of the external subtitle file. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## advanceToMediaSource

```TypeScript
advanceToMediaSource(id: string): Promise<void>
```

Ends playback of the current mediasource and starts playback of the specified mediasource in the mediasource list.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-advanceToMediaSource(id: string): Promise<void>--><!--Device-AVPlayer-advanceToMediaSource(id: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Indicates the ID of the media source to play. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) | The mediasource does not exist in the playlist. Returned via promise. |

## advanceToNextMediaSource

```TypeScript
advanceToNextMediaSource() : Promise<void>
```

Ends playback of the current mediasource and starts playback of the next mediasource in the mediasource list.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-advanceToNextMediaSource() : Promise<void>--><!--Device-AVPlayer-advanceToNextMediaSource() : Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed . Return by promise. |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) | The previous mediasource does not exist in the playlist. Returned via promise. |

## advanceToPrevMediaSource

```TypeScript
advanceToPrevMediaSource(): Promise<void>
```

Ends playback of the current mediasource and starts playback of the previous mediasource in the mediasource list.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-advanceToPrevMediaSource(): Promise<void>--><!--Device-AVPlayer-advanceToPrevMediaSource(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) | The next mediasource does not exist in the playlist. Returned via promise. |

## clearPlaybackList

```TypeScript
clearPlaybackList(): Promise<void>
```

Clears all the items in the player's playlist. Currently playing media will be terminated immediately.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-clearPlaybackList(): Promise<void>--><!--Device-AVPlayer-clearPlaybackList(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise is used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | operation not allowed . Returned via promise. |

## deselectTrack

ArkTS-Dyn:
```TypeScript
deselectTrack(index: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
deselectTrack(index: int): Promise<void>
```

Deselects the specified track when the AVPlayer plays multimedia resources with multiple audio or video tracks.This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-deselectTrack(index: int): Promise<void>--><!--Device-AVPlayer-deselectTrack(index: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Track index, which is obtained from [MediaDescription]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ by calling [getTrackDescription]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## getCurrentMediaSource

```TypeScript
getCurrentMediaSource(): MediaSource | undefined
```

Return the current mediasource.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-getCurrentMediaSource(): MediaSource | undefined--><!--Device-AVPlayer-getCurrentMediaSource(): MediaSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | current mediasource if the operation is successful; returns undefined otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## getCurrentPresentationTimestamp

ArkTS-Dyn:
```TypeScript
getCurrentPresentationTimestamp() : number
```

ArkTS-Sta:
```TypeScript
getCurrentPresentationTimestamp() : long
```

Obtains the current playback time. This API can be called only when the AVPlayer is in the **playing**,  
**paused**, or **completed** state.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVPlayer-getCurrentPresentationTimestamp() : long--><!--Device-AVPlayer-getCurrentPresentationTimestamp() : long-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Current playback time, in microseconds. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. |

## getCurrentTrack

ArkTS-Dyn:
```TypeScript
getCurrentTrack(trackType: MediaType): Promise<number>
```

ArkTS-Sta:
```TypeScript
getCurrentTrack(trackType: MediaType): Promise<int>
```

Obtains the selected track by the specified media type. This API can be called only when the AVPlayer is in the prepared, playing, or paused state. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-getCurrentTrack(trackType: MediaType): Promise<int>--><!--Device-AVPlayer-getCurrentTrack(trackType: MediaType): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| trackType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | specified media Type, see [MediaType]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Promise&lt;int&gt; | A Promise instance used to return selected track index. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) | No memory. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-io-error) | I/O error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## getLoadedTimeRanges

```TypeScript
getLoadedTimeRanges(): Promise<Array<Range>>
```

Obtains the list of loaded time ranges. This API uses a promise to return the result.
    **NOTE**  
    
    - For local media resources, the time range is from 0 to the entire media duration.  
    
    - For network media resources, the list of locally loaded time ranges is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-getLoadedTimeRanges(): Promise<Array<Range>>--><!--Device-AVPlayer-getLoadedTimeRanges(): Promise<Array<Range>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Range&gt;&gt; | Promise used to return the list of loaded time ranges on the player. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The time range is represented by the **[start, end]** position on the playback timeline, in milliseconds. |

## getMediaKeySystemInfos

```TypeScript
getMediaKeySystemInfos(): Array<drm.MediaKeySystemInfo>
```

Obtains the media key system information of the media asset that is being played. This API can be called only after the  
[on('mediaKeySystemInfoUpdate')]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_event is successfully triggered.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-getMediaKeySystemInfos(): Array<drm.MediaKeySystemInfo>--><!--Device-AVPlayer-getMediaKeySystemInfos(): Array<drm.MediaKeySystemInfo>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;drm.MediaKeySystemInfo&gt; | Array of MediaKeySystemInfo objects, each of which contains the **uuid** and **pssh** properties. If the return value is undefined, the mediaKeySystemInfoUpdate event is not triggered. |

## getMediaSources

```TypeScript
getMediaSources(): Array<MediaSource | undefined>
```

Return the array of mediasources in the playlist.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-getMediaSources(): Array<MediaSource | undefined>--><!--Device-AVPlayer-getMediaSources(): Array<MediaSource | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;MediaSource \| undefined&gt; | array of mediasources in the playlist. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## getPlaybackInfo

```TypeScript
getPlaybackInfo(): Promise<PlaybackInfo>
```

Obtains the playback information. This API can be called only when the AVPlayer is in the prepared, playing, or paused state. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVPlayer-getPlaybackInfo(): Promise<PlaybackInfo>--><!--Device-AVPlayer-getPlaybackInfo(): Promise<PlaybackInfo>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PlaybackInfo&gt; | Promise used to return **PlaybackInfo**. |

## getPlaybackPosition

ArkTS-Dyn:
```TypeScript
getPlaybackPosition() : number
```

ArkTS-Sta:
```TypeScript
getPlaybackPosition() : int
```

Obtains the current playback position. This API can be called only when the AVPlayer is in the prepared, playing,paused, or completed state.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-getPlaybackPosition() : int--><!--Device-AVPlayer-getPlaybackPosition() : int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Current playback time, in milliseconds. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. |

## getPlaybackRate

ArkTS-Dyn:
```TypeScript
getPlaybackRate(): Promise<number>
```

ArkTS-Sta:
```TypeScript
getPlaybackRate(): Promise<double>
```

Obtains the playback speed of an AVPlayer. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-AVPlayer-getPlaybackRate(): Promise<double>--><!--Device-AVPlayer-getPlaybackRate(): Promise<double>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Promise&lt;double&gt; | Promise object, which returns the playback speed. |

## getPlaybackStatisticMetrics

```TypeScript
getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>
```

Obtains the statistic metrics of the current player. This API can be called when the AVPlayer is in the prepared,playing, paused, completed, or stopped state. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-AVPlayer-getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>--><!--Device-AVPlayer-getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PlaybackMetrics&gt; | Promise used to return the playback metrics of the current AVPlayer. |

## getSeekableTimeRanges

```TypeScript
getSeekableTimeRanges(): Promise<Array<Range>>
```

Obtains the list of seekable time ranges. This API uses a promise to return the result.
    **NOTE**  
    
    - For local media resources and media resources that support segment-based requests, the time range is from 0  
    to the entire media duration.  
    
    - For media resources that support only chunk-based transmission, there is no seekable time range.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-getSeekableTimeRanges(): Promise<Array<Range>>--><!--Device-AVPlayer-getSeekableTimeRanges(): Promise<Array<Range>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Range&gt;&gt; | Promise used to return the list of seekable time ranges on the player. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The time range is represented by the **[start, end]** position on the playback timeline, in milliseconds. |

## getSelectedTracks

ArkTS-Dyn:
```TypeScript
getSelectedTracks(): Promise<Array<number>>
```

ArkTS-Sta:
```TypeScript
getSelectedTracks(): Promise<Array<int>>
```

Obtains the indexes of the selected audio or video tracks. This API can be called only when the AVPlayer is in the prepared, playing, or paused state. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-getSelectedTracks(): Promise<Array<int>>--><!--Device-AVPlayer-getSelectedTracks(): Promise<Array<int>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Promise&lt;Array&lt;int&gt;&gt; | Promise used to return the index array. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. |

## getTrackDescription

```TypeScript
getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void
```

Obtains the audio and video track information. This API can be called only when the AVPlayer is in the prepared,playing, or paused state. To obtain information about all audio and video tracks, this API must be called after the data loading callback is triggered. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void--><!--Device-AVPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;MediaDescription&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the MediaDescription array obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |

## getTrackDescription

```TypeScript
getTrackDescription(): Promise<Array<MediaDescription>>
```

Obtains the audio and video track information. This API can be called only when the AVPlayer is in the prepared,playing, or paused state. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-getTrackDescription(): Promise<Array<MediaDescription>>--><!--Device-AVPlayer-getTrackDescription(): Promise<Array<MediaDescription>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;MediaDescription&gt;&gt; | Promise used to return the MediaDescription array that holds the audio and video track information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## getTrackSelectionFilter

```TypeScript
getTrackSelectionFilter(): Promise<TrackSelectionFilter>
```

Obtains the track selection filter configured for the player. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-getTrackSelectionFilter(): Promise<TrackSelectionFilter>--><!--Device-AVPlayer-getTrackSelectionFilter(): Promise<TrackSelectionFilter>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;TrackSelectionFilter&gt; | Promise used to return the track selection filter configured for the player. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. |

## isSeekContinuousSupported

```TypeScript
isSeekContinuousSupported() : boolean
```

Checks whether the media source supports [seek]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ in SEEK\_CONTINUOUS mode (specified by  
[SeekMode]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_). The actual value is returned when this API is called in the prepared, playing, paused, or completed state. The value **false** is returned if it is called in other states. For devices that do not support the seek operation in SEEK\_CONTINUOUS mode, **false** is returned.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-isSeekContinuousSupported() : boolean--><!--Device-AVPlayer-isSeekContinuousSupported() : boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of the seek operation in **SEEK\_\_\_ESCAPED\_UNDERSCORE\_\_\_CONTINUOUS** mode. **true** to support, **false** otherwise. |

## off('mediaKeySystemInfoUpdate')

```TypeScript
off(type: 'mediaKeySystemInfoUpdate', callback?: Callback<Array<drm.MediaKeySystemInfo>>): void
```

Unsubscribes from media key system information changes.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'mediaKeySystemInfoUpdate', callback?: Callback<Array<drm.MediaKeySystemInfo>>): void--><!--Device-AVPlayer-off(type: 'mediaKeySystemInfoUpdate', callback?: Callback<Array<drm.MediaKeySystemInfo>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'mediaKeySystemInfoUpdate' | Yes | Event type, which is **'mediaKeySystemInfoUpdate'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;drm.MediaKeySystemInfo&gt;&gt; | No | Callback invoked when the event is triggered. It reports a **MediaKeySystemInfo** array. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **mediaKeySystemInfoUpdate** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: OnAVPlayerStateChangeHandle): void
```

Unsubscribes from [AVPlayerState]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ state changes.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-off(type: 'stateChange', callback?: OnAVPlayerStateChangeHandle): void--><!--Device-AVPlayer-off(type: 'stateChange', callback?: OnAVPlayerStateChangeHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'stateChange' | Yes | Event type, which is **'stateChange'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback invoked when the event is triggered. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **stateChange** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('volumeChange')

```TypeScript
off(type: 'volumeChange', callback?: Callback<double>): void
```

Unsubscribes from the event that checks whether the volume is successfully set.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'volumeChange', callback?: Callback<double>): void--><!--Device-AVPlayer-off(type: 'volumeChange', callback?: Callback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'volumeChange' | Yes | Event type, which is **'volumeChange'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;double&gt; | No | Callback invoked when the event is triggered. It reports the effective volume. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **volumeChange** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('endOfStream')

```TypeScript
off(type: 'endOfStream', callback?: Callback<void>): void
```

Unsubscribes from the event that indicates the end of the stream being played.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'endOfStream', callback?: Callback<void>): void--><!--Device-AVPlayer-off(type: 'endOfStream', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'endOfStream' | Yes | Event type, which is **'endOfStream'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Callback invoked when the event is triggered. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **endOfStream** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 19 |

## off('seekDone')

```TypeScript
off(type: 'seekDone', callback?: Callback<int>): void
```

Unsubscribes from the event that checks whether the seek operation takes effect.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-off(type: 'seekDone', callback?: Callback<int>): void--><!--Device-AVPlayer-off(type: 'seekDone', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'seekDone' | Yes | Event type, which is **'seekDone'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | No | Callback invoked when the event is triggered. It reports the time position requested by the user.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_For video playback, [SeekMode]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ may cause the actual position to be different from that requested by the user. The exact position can be obtained from the **currentTime** property. The time in this callback only means that the requested seek operation is complete. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **seekDone** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('speedDone')

```TypeScript
off(type: 'speedDone', callback?: Callback<int>): void
```

Unsubscribes from the event that checks whether the playback speed is successfully set.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'speedDone', callback?: Callback<int>): void--><!--Device-AVPlayer-off(type: 'speedDone', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'speedDone' | Yes | Event type, which is **'speedDone'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | No | Callback used to return the result. When the call of **setSpeed** is successful, the effective speed mode is reported. For details, see [PlaybackSpeed]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **speedDone** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('playbackRateDone')

```TypeScript
off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void
```

Unsubscribes from the event indicating that the playback rate set by calling  
[setPlaybackRate]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is applied.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVPlayer-off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void--><!--Device-AVPlayer-off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playbackRateDone' | Yes | Event type, which is **'playbackRateDone'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback invoked when the event is triggered. It reports the new playback rate. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **playbackRateDone** event will be unregistered. |

## off('bitrateDone')

```TypeScript
off(type: 'bitrateDone', callback?: Callback<int>): void
```

Unsubscribes from the event that checks whether the bitrate is successfully set.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'bitrateDone', callback?: Callback<int>): void--><!--Device-AVPlayer-off(type: 'bitrateDone', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bitrateDone' | Yes | Event type, which is **'bitrateDone'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | No | Callback invoked when the event is triggered. It reports the effective bitrate, in bit/s. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **bitrateDone** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 19 |

## off('timeUpdate')

```TypeScript
off(type: 'timeUpdate', callback?: Callback<int>): void
```

Unsubscribes from playback position changes.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-off(type: 'timeUpdate', callback?: Callback<int>): void--><!--Device-AVPlayer-off(type: 'timeUpdate', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'timeUpdate' | Yes | Event type, which is **'timeUpdate'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | No | Callback used to return the current time. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **timeUpdate** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('durationUpdate')

```TypeScript
off(type: 'durationUpdate', callback?: Callback<int>): void
```

Unsubscribes from media asset duration changes.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'durationUpdate', callback?: Callback<int>): void--><!--Device-AVPlayer-off(type: 'durationUpdate', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'durationUpdate' | Yes | Event type, which is **'durationUpdate'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | No | Callback used to return the resource duration. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **durationUpdate** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 19 |

## off('bufferingUpdate')

```TypeScript
off(type: 'bufferingUpdate', callback?: OnBufferingUpdateHandler): void
```

Unsubscribes from audio and video buffer changes.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'bufferingUpdate', callback?: OnBufferingUpdateHandler): void--><!--Device-AVPlayer-off(type: 'bufferingUpdate', callback?: OnBufferingUpdateHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bufferingUpdate' | Yes | Event type, which is **'bufferingUpdate'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback invoked when the event is triggered. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **bufferingUpdate** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('startRenderFrame')

```TypeScript
off(type: 'startRenderFrame', callback?: Callback<void>): void
```

Unsubscribes from the event that indicates rendering starts for the first frame.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVPlayer-off(type: 'startRenderFrame', callback?: Callback<void>): void--><!--Device-AVPlayer-off(type: 'startRenderFrame', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'startRenderFrame' | Yes | Event type, which is **'startRenderFrame'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Callback invoked when the event is triggered. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **startRenderFrame** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 19 |

## off('videoSizeChange')

```TypeScript
off(type: 'videoSizeChange', callback?: OnVideoSizeChangeHandler): void
```

Unsubscribes from video size changes.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'videoSizeChange', callback?: OnVideoSizeChangeHandler): void--><!--Device-AVPlayer-off(type: 'videoSizeChange', callback?: OnVideoSizeChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'videoSizeChange' | Yes | Event type, which is **'videoSizeChange'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback invoked when the event is triggered. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **videoSizeChange** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void
```

Unsubscribes from the audio interruption event.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void--><!--Device-AVPlayer-off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | Yes | Event type, which is **'audioInterrupt'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;audio.InterruptEvent&gt; | No | Callback invoked when the event is triggered. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **audioInterrupt** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('availableBitrates')

```TypeScript
off(type: 'availableBitrates', callback?: Callback<Array<int>>): void
```

Unsubscribes from available bitrates of HLS/DASH streams. This event is reported after  
[prepare]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is called.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'availableBitrates', callback?: Callback<Array<int>>): void--><!--Device-AVPlayer-off(type: 'availableBitrates', callback?: Callback<Array<int>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'availableBitrates' | Yes | Event type, which is **'availableBitrates'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;int&gt;&gt; | No | Callback invoked when the event is triggered. It returns an array that holds the available bitrates, in bit/s. If the array length is 0, no bitrate can be set. If this parameter is specified , only the specified callback is unregistered. Otherwise, all callbacks associated with the **availableBitrates** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from AVPlayer errors.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-off(type: 'error', callback?: ErrorCallback): void--><!--Device-AVPlayer-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type, which is **'error'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback used to return the error code ID and error message. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **error** event will be unregistered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## off('audioOutputDeviceChangeWithInfo')

```TypeScript
off(type: 'audioOutputDeviceChangeWithInfo', callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void
```

Unsubscribes from audio stream output device changes and reasons. This API uses an asynchronous callback to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'audioOutputDeviceChangeWithInfo', callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void--><!--Device-AVPlayer-off(type: 'audioOutputDeviceChangeWithInfo', callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioOutputDeviceChangeWithInfo' | Yes | Event type, which is **'audioOutputDeviceChangeWithInfo'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;audio.AudioStreamDeviceChangeInfo&gt; | No | Callback used to return the output device descriptor of the current audio stream and the change reason. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **audioOutputDeviceChangeWithInfo** event will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. 3.Parameter verification failed. |

## off('subtitleUpdate')

```TypeScript
off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void
```

Unsubscribes from subtitle update events.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void--><!--Device-AVPlayer-off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'subtitleUpdate' | Yes | Event type, which is **'subtitleUpdate'** in this case. The event is triggered when the external subtitle is updated. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;SubtitleInfo&gt; | No | Callback that has been registered to listen for subtitle update events. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **subtitleUpdate** event will be unregistered. |

## off('trackChange')

```TypeScript
off(type: 'trackChange', callback?: OnTrackChangeHandler): void
```

Unsubscribes from track change events.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'trackChange', callback?: OnTrackChangeHandler): void--><!--Device-AVPlayer-off(type: 'trackChange', callback?: OnTrackChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'trackChange' | Yes | Event type, which is **'trackChange'** in this case. The event is triggered when the track changes. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback that has been registered to listen for track changes. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **trackChange** event will be unregistered. |

## off('trackInfoUpdate')

```TypeScript
off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void
```

Unsubscribes from track information update events.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void--><!--Device-AVPlayer-off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'trackInfoUpdate' | Yes | Event type, which is **'trackInfoUpdate'** in this case. The event is triggered when the track information is updated. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;MediaDescription&gt;&gt; | No | Callback that has been registered to listen for track information updates. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **trackInfoUpdate** event will be unregistered. |

## off('amplitudeUpdate')

```TypeScript
off(type: 'amplitudeUpdate', callback?: Callback<Array<double>>): void
```

Unsubscribes from update events of the maximum amplitude.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

<!--Device-AVPlayer-off(type: 'amplitudeUpdate', callback?: Callback<Array<double>>): void--><!--Device-AVPlayer-off(type: 'amplitudeUpdate', callback?: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'amplitudeUpdate' | Yes | Event type, which is **'amplitudeUpdate'** in this case. The event is triggered when the amplitude changes. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;double&gt;&gt; | No | Callback that has been registered to listen for amplitude updates. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **amplitudeUpdate** event will be unregistered. |

## off('seiMessageReceived')

```TypeScript
off(type: 'seiMessageReceived', payloadTypes?: Array<int>, callback?: OnSeiMessageHandle): void
```

Unsubscribes from the events indicating that an SEI message is received.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-off(type: 'seiMessageReceived', payloadTypes?: Array<int>, callback?: OnSeiMessageHandle): void--><!--Device-AVPlayer-off(type: 'seiMessageReceived', payloadTypes?: Array<int>, callback?: OnSeiMessageHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'seiMessageReceived' | Yes | Event type, which is **'seiMessageReceived'** in this case. The event is triggered when an SEI message is received. |
| payloadTypes | Array&lt;int&gt; | No | Array of subscribed-to payload types of SEI messages. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback used to listen for SEI message events and receive the subscribed-to payload types. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **seiMessageReceived** event will be unregistered. |

## off('superResolutionChanged')

```TypeScript
off(type:'superResolutionChanged', callback?: OnSuperResolutionChanged): void
```

Unsubscribes from the event indicating that super resolution is enabled or disabled.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-off(type:'superResolutionChanged', callback?: OnSuperResolutionChanged): void--><!--Device-AVPlayer-off(type:'superResolutionChanged', callback?: OnSuperResolutionChanged): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'superResolutionChanged' | Yes | Event type, which is **'superResolutionChanged'** in this case. The event is triggered when super resolution is enabled or disabled. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback used to listen for super resolution status changes. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the **superResolutionChanged** event will be unregistered. |

## offAmplitudeUpdate

```TypeScript
offAmplitudeUpdate(callback?: Callback<Array<double>>): void
```

Unsubscribes from update events of the maximum amplitude.The event is triggered when the amplitude changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offAmplitudeUpdate(callback?: Callback<Array<double>>): void--><!--Device-AVPlayer-offAmplitudeUpdate(callback?: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;double&gt;&gt; | No | Callback that has been registered to listen for amplitude updates. |

## offAudioInterrupt

```TypeScript
offAudioInterrupt(callback?: Callback<audio.InterruptEvent>): void
```

Unregister listens for audio interrupt event, refer to \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offAudioInterrupt(callback?: Callback<audio.InterruptEvent>): void--><!--Device-AVPlayer-offAudioInterrupt(callback?: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;audio.InterruptEvent&gt; | No | Callback used to listen for the playback event return audio interrupt info. |

## offAudioOutputDeviceChangeWithInfo

```TypeScript
offAudioOutputDeviceChangeWithInfo(callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void
```

Unsubscribes from audio stream output device changes and reasons. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offAudioOutputDeviceChangeWithInfo(callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void--><!--Device-AVPlayer-offAudioOutputDeviceChangeWithInfo(callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;audio.AudioStreamDeviceChangeInfo&gt; | No | Callback used to return the output device descriptor of the current audio stream and the change reason. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## offAvailableBitrates

```TypeScript
offAvailableBitrates(callback?: Callback<Array<int>>): void
```

Unregister listens for available bitrate list collect completed events for HLS protocol stream playback.This event will be reported after the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ called.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offAvailableBitrates(callback?: Callback<Array<int>>): void--><!--Device-AVPlayer-offAvailableBitrates(callback?: Callback<Array<int>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;int&gt;&gt; | No | Callback used to listen for the playback event return available bitrate list. |

## offBitrateDone

```TypeScript
offBitrateDone(callback?: Callback<int>): void
```

Unsubscribes from the event that checks whether the bit rate is successfully set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offBitrateDone(callback?: Callback<int>): void--><!--Device-AVPlayer-offBitrateDone(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | No | Callback invoked when the event is triggered. It reports the effective bit rate. |

## offBufferingUpdate

```TypeScript
offBufferingUpdate(callback?: OnBufferingUpdateHandler): void
```

Unsubscribes from audio and video buffer changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offBufferingUpdate(callback?: OnBufferingUpdateHandler): void--><!--Device-AVPlayer-offBufferingUpdate(callback?: OnBufferingUpdateHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback invoked when the event is triggered, and return BufferingInfoType and the value. |

## offDurationUpdate

```TypeScript
offDurationUpdate(callback?: Callback<int>): void
```

Unsubscribes from media asset duration changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offDurationUpdate(callback?: Callback<int>): void--><!--Device-AVPlayer-offDurationUpdate(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | No | Callback used to return the resource duration. |

## offEndOfStream

```TypeScript
offEndOfStream(callback?: Callback<void>): void
```

Unregister listens for media playback endOfStream event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offEndOfStream(callback?: Callback<void>): void--><!--Device-AVPlayer-offEndOfStream(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Callback used to listen for the playback end of stream. |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from AVPlayer errors.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offError(callback?: ErrorCallback): void--><!--Device-AVPlayer-offError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback used to return the error code ID and error message. |

## offMediaKeySystemInfoUpdate

```TypeScript
offMediaKeySystemInfoUpdate(callback?: Callback<Array<drm.MediaKeySystemInfo>>): void
```

Unregister listens for mediaKeySystemInfoUpdate events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offMediaKeySystemInfoUpdate(callback?: Callback<Array<drm.MediaKeySystemInfo>>): void--><!--Device-AVPlayer-offMediaKeySystemInfoUpdate(callback?: Callback<Array<drm.MediaKeySystemInfo>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;drm.MediaKeySystemInfo&gt;&gt; | No | Callback for event. |

## offMetricsEvent

```TypeScript
offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void
```

Unsubscribes from metric events during playback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-AVPlayer-offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void--><!--Device-AVPlayer-offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;AVMetricsEvent&gt;&gt; | No | Callback invoked for metric events. This API uses an asynchronous callback to return the result. |

## offPlaybackContentChanged

```TypeScript
offPlaybackContentChanged(callback?: Callback<string>):void
```

Unregisters listener to detect when changes occur in the playback content.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-offPlaybackContentChanged(callback?: Callback<string>):void--><!--Device-AVPlayer-offPlaybackContentChanged(callback?: Callback<string>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string&gt; | No | Callback invoked when the event is triggered. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Default value:If this parameter is not specified, all callback functions for the event are unsubscribed. |

## offPlaybackRateDone

```TypeScript
offPlaybackRateDone(callback?: OnPlaybackRateDone): void
```

Unregister listens for media playbackRateDone event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offPlaybackRateDone(callback?: OnPlaybackRateDone): void--><!--Device-AVPlayer-offPlaybackRateDone(callback?: OnPlaybackRateDone): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback used to listen for the playbackRateDone event. |

## offSeekDone

```TypeScript
offSeekDone(callback?: Callback<int>): void
```

Unsubscribes from the event that checks whether the seek operation takes effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offSeekDone(callback?: Callback<int>): void--><!--Device-AVPlayer-offSeekDone(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | No | Callback invoked when the event is triggered. It reports the time position requested by the user. For video playback, SeekMode may cause the actual position to be different from that requested by the user. The exact position can be obtained from the currentTime attribute. The time in this callback only means that the requested seek operation is complete. |

## offSeiMessageReceived

```TypeScript
offSeiMessageReceived(payloadTypes?: Array<int>, callback?: OnSeiMessageHandle): void
```

Unsubscribes from the events indicating that an SEI message is received.The event is triggered when an SEI message is received.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offSeiMessageReceived(payloadTypes?: Array<int>, callback?: OnSeiMessageHandle): void--><!--Device-AVPlayer-offSeiMessageReceived(payloadTypes?: Array<int>, callback?: OnSeiMessageHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| payloadTypes | Array&lt;int&gt; | No | The payload types of the SEI message. Null means unsubscribe all payload types. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback used to listen for SEI message events and receive the subscribed-to payload types. |

## offSpeedDone

```TypeScript
offSpeedDone(callback?: Callback<int>): void
```

Unsubscribes from the event that checks whether the playback speed is successfully set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offSpeedDone(callback?: Callback<int>): void--><!--Device-AVPlayer-offSpeedDone(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | No | Callback used to return the result. When the call of setSpeed is successful, the effective speed mode is reported. For details, see \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

## offStartRenderFrame

```TypeScript
offStartRenderFrame(callback?: Callback<void>): void
```

Unregister listens for start render video frame events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offStartRenderFrame(callback?: Callback<void>): void--><!--Device-AVPlayer-offStartRenderFrame(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Callback used to listen for the playback event return . |

## offStateChange

```TypeScript
offStateChange(callback?: OnAVPlayerStateChangeHandle): void
```

Unregister listens for media playback stateChange event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offStateChange(callback?: OnAVPlayerStateChangeHandle): void--><!--Device-AVPlayer-offStateChange(callback?: OnAVPlayerStateChangeHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback invoked when the event is triggered. |

## offSubtitleUpdate

```TypeScript
offSubtitleUpdate(callback?: Callback<SubtitleInfo>): void
```

Unsubscribes from subtitle update events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offSubtitleUpdate(callback?: Callback<SubtitleInfo>): void--><!--Device-AVPlayer-offSubtitleUpdate(callback?: Callback<SubtitleInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;SubtitleInfo&gt; | No | Callback that has been registered to listen for subtitle update events. |

## offSuperResolutionChanged

```TypeScript
offSuperResolutionChanged(callback?: OnSuperResolutionChanged): void
```

Unsubscribes from the event indicating that super resolution is enabled or disabled.The event is triggered when super resolution is enabled or disabled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offSuperResolutionChanged(callback?: OnSuperResolutionChanged): void--><!--Device-AVPlayer-offSuperResolutionChanged(callback?: OnSuperResolutionChanged): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback used to listen for the super-resolution changed event. |

## offTimeUpdate

```TypeScript
offTimeUpdate(callback?: Callback<int>): void
```

Unsubscribes from playback position changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offTimeUpdate(callback?: Callback<int>): void--><!--Device-AVPlayer-offTimeUpdate(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | No | Callback used to return the current time. |

## offTimedMetaData

```TypeScript
offTimedMetaData(callback?: Callback<AVTimedMetaData>): void
```

Unregister listener to detect time-based metadata,Currently, only the #EXT-X-DATERANGE data of HLS and the Event Streams information of DASH are supported.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-offTimedMetaData(callback?: Callback<AVTimedMetaData>): void--><!--Device-AVPlayer-offTimedMetaData(callback?: Callback<AVTimedMetaData>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;AVTimedMetaData&gt; | No | Callback invoked when the event is triggered. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Default value:If this parameter is not specified, all callback functions for the event are unsubscribed. |

## offTrackChange

```TypeScript
offTrackChange(callback?: OnTrackChangeHandler): void
```

Unsubscribes from track change events.The event is triggered when the track changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offTrackChange(callback?: OnTrackChangeHandler): void--><!--Device-AVPlayer-offTrackChange(callback?: OnTrackChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback that has been registered to listen for track changes. |

## offTrackInfoUpdate

```TypeScript
offTrackInfoUpdate(callback?: Callback<Array<MediaDescription>>): void
```

Unsubscribes from track information update events.The event is triggered when the track information is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offTrackInfoUpdate(callback?: Callback<Array<MediaDescription>>): void--><!--Device-AVPlayer-offTrackInfoUpdate(callback?: Callback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;MediaDescription&gt;&gt; | No | Callback that has been registered to listen for track information updates. |

## offVideoSizeChange

```TypeScript
offVideoSizeChange(callback?: OnVideoSizeChangeHandler): void
```

Unsubscribes from video size changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offVideoSizeChange(callback?: OnVideoSizeChangeHandler): void--><!--Device-AVPlayer-offVideoSizeChange(callback?: OnVideoSizeChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback invoked when the event is triggered. |

## offVolumeChange

```TypeScript
offVolumeChange(callback?: Callback<double>): void
```

Unsubscribes from the event that checks whether the volume is successfully set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-offVolumeChange(callback?: Callback<double>): void--><!--Device-AVPlayer-offVolumeChange(callback?: Callback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;double&gt; | No | Callback invoked when the event is triggered. It reports the effective volume. |

## on('mediaKeySystemInfoUpdate')

```TypeScript
on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>): void
```

Subscribes to media key system information changes.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>): void--><!--Device-AVPlayer-on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'mediaKeySystemInfoUpdate' | Yes | Event type, which is **'mediaKeySystemInfoUpdate'** in this case. This event is triggered when the copyright protection information of the media asset being played changes. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;drm.MediaKeySystemInfo&gt;&gt; | Yes | Callback invoked when the event is triggered. It reports a **MediaKeySystemInfo** array.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle): void
```

Subscribes to AVPlayer state changes.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle): void--><!--Device-AVPlayer-on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'stateChange' | Yes | Event type, which is **'stateChange'** in this case. This event can be triggered by both user operations and the system. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback invoked when the event is triggered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## on('volumeChange')

```TypeScript
on(type: 'volumeChange', callback: Callback<double>): void
```

Subscribes to the event to check whether the volume is successfully set.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'volumeChange', callback: Callback<double>): void--><!--Device-AVPlayer-on(type: 'volumeChange', callback: Callback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'volumeChange' | Yes | Event type, which is **'volumeChange'** in this case. This event is triggered each time **setVolume()** is called. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;double&gt; | Yes | Callback invoked when the event is triggered. It reports the effective volume. |

## on('endOfStream')

```TypeScript
on(type: 'endOfStream', callback: Callback<void>): void
```

Subscribes to the event that indicates the end of the stream being played. If  
**\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ = true** is set, the AVPlayer seeks to the beginning of the stream and plays the stream again. If **loop** is not set, the completed state is reported through the  
[stateChange]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ event.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'endOfStream', callback: Callback<void>): void--><!--Device-AVPlayer-on(type: 'endOfStream', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'endOfStream' | Yes | Event type, which is **'endOfStream'** in this case. This event is triggered when the AVPlayer finishes playing the media asset. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback invoked when the event is triggered. |

## on('seekDone')

```TypeScript
on(type: 'seekDone', callback: Callback<int>): void
```

Subscribes to the event to check whether the seek operation takes effect.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-on(type: 'seekDone', callback: Callback<int>): void--><!--Device-AVPlayer-on(type: 'seekDone', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'seekDone' | Yes | Event type, which is **'seekDone'** in this case. This event is triggered each time **seek()** is called, except in SEEK\_\_\_ESCAPED\_UNDERSCORE\_\_\_CONTINUOUS mode. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback invoked when the event is triggered. It reports the time position requested by the user.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_For video playback, [SeekMode]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ may cause the actual position to be different from that requested by the user. The exact position can be obtained from the **currentTime** property. The time in this callback only means that the requested seek operation is complete. |

## on('speedDone')

```TypeScript
on(type: 'speedDone', callback: Callback<int>): void
```

Subscribes to the event to check whether the playback speed is successfully set.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'speedDone', callback: Callback<int>): void--><!--Device-AVPlayer-on(type: 'speedDone', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'speedDone' | Yes | Event type, which is **'speedDone'** in this case. This event is triggered each time **setSpeed()** is called. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback used to return the result. When the call of **setSpeed** is successful, the effective speed mode is reported. For details, see [PlaybackSpeed]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

## on('playbackRateDone')

```TypeScript
on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void
```

Subscribes to the event indicating that the playback rate set by calling  
[setPlaybackRate]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is applied.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVPlayer-on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void--><!--Device-AVPlayer-on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playbackRateDone' | Yes | Event type, which is **'playbackRateDone'** in this case. This event is triggered each time **setPlaybackRate** is called. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback invoked when the event is triggered. It reports the new playback rate. |

## on('bitrateDone')

```TypeScript
on(type: 'bitrateDone', callback: Callback<int>): void
```

Subscribes to the event to check whether the bitrate is successfully set.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'bitrateDone', callback: Callback<int>): void--><!--Device-AVPlayer-on(type: 'bitrateDone', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bitrateDone' | Yes | Event type, which is **'bitrateDone'** in this case. This event is triggered each time **setBitrate()** is called. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback invoked when the event is triggered. It reports the effective bitrate, in bit/s. |

## on('timeUpdate')

```TypeScript
on(type: 'timeUpdate', callback: Callback<int>): void
```

Subscribes to playback position changes. It is used to refresh the current position of the progress bar. By default, this event is reported every 100 ms. However, it is reported immediately upon a successful seek operation.
    **NOTE**  
    
    - The **'timeUpdate'** event is not supported in live streaming scenarios.  
    
    - When a seek operation is performed, the progress bar can be updated based on the **'timeUpdate'** event only  
    after the seek operation is complete (**'seekdone'** received).  
    
    - In the **pause** state, the player reports the timeUpdate event when the buffering ends.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-on(type: 'timeUpdate', callback: Callback<int>): void--><!--Device-AVPlayer-on(type: 'timeUpdate', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'timeUpdate' | Yes | Event type, which is **'timeUpdate'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback used to return the current time. |

## on('durationUpdate')

```TypeScript
on(type: 'durationUpdate', callback: Callback<int>): void
```

Subscribes to media asset duration changes. It is used to refresh the length of the progress bar. By default,this event is reported once in the prepared state. However, it can be repeatedly reported for special streams that trigger duration changes.
    **NOTE**  
    
    The **durationUpdate** event is not supported in live streaming scenarios.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'durationUpdate', callback: Callback<int>): void--><!--Device-AVPlayer-on(type: 'durationUpdate', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'durationUpdate' | Yes | Event type, which is **'durationUpdate'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback used to return the resource duration. |

## on('bufferingUpdate')

```TypeScript
on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler): void
```

Subscribes to audio and video buffer changes. This subscription is supported only in network playback scenarios.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler): void--><!--Device-AVPlayer-on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bufferingUpdate' | Yes | Event type, which is **'bufferingUpdate'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback invoked when the event is triggered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## on('startRenderFrame')

```TypeScript
on(type: 'startRenderFrame', callback: Callback<void>): void
```

Subscribes to the event that indicates rendering starts for the first frame. This subscription is supported only in video playback scenarios. This event only means that the playback service sends the first frame to the display module. The actual rendering effect depends on the rendering performance of the display service.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'startRenderFrame', callback: Callback<void>): void--><!--Device-AVPlayer-on(type: 'startRenderFrame', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'startRenderFrame' | Yes | Event type, which is **'startRenderFrame'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback invoked when the event is triggered. |

## on('videoSizeChange')

```TypeScript
on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler): void
```

Subscribes to video size (width and height) changes. This subscription is supported only in video playback scenarios. By default, this event is reported only once in the prepared state. However, it is also reported upon resolution changes in the case of HLS streams.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler): void--><!--Device-AVPlayer-on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'videoSizeChange' | Yes | Event type, which is **'videoSizeChange'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback invoked when the event is triggered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void
```

Subscribes to the audio interruption event. When multiple audio and video assets are played at the same time,this event is triggered based on the audio interruption mode  
[audio.InterruptMode]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. The application needs to perform corresponding processing based on different audio interruption events. For details, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void--><!--Device-AVPlayer-on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | Yes | Event type, which is **'audioInterrupt'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;audio.InterruptEvent&gt; | Yes | Callback invoked when the event is triggered.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## on('availableBitrates')

```TypeScript
on(type: 'availableBitrates', callback: Callback<Array<int>>): void
```

Subscribes to available bitrates of HLS/DASH streams. This event is reported only after the AVPlayer switches to the prepared state.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'availableBitrates', callback: Callback<Array<int>>): void--><!--Device-AVPlayer-on(type: 'availableBitrates', callback: Callback<Array<int>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'availableBitrates' | Yes | Event type, which is **'availableBitrates'** in this case. This event is triggered once after the AVPlayer switches to the prepared state. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;int&gt;&gt; | Yes | Callback invoked when the event is triggered. It returns an array that holds the available bitrates, in bit/s. If the array length is 0, no bitrate can be set.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to [AVPlayer]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ errors. This event is used only for error prompt and does not require the user to stop playback control. If the  
[AVPlayerState]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ is also switched to error, call  
[reset()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ or  
[release()]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ to exit the playback. If the playback remains in the error state after the [reset()]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ method is called, you are advised to directly invoke the  
[release()]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ method to exit the playback operation.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-AVPlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type, which is **'error'** in this case. This event can be triggered by both user operations and the system. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to return the error code ID and error message. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) | No memory. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. |
| [5400104](../errorcode-media.md#5400104-operation-timeout) | Time out. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. |
| [5411001](../errorcode-media.md#5411001-failed-to-parse-or-connect-to-the-server-address) | IO can not find host.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5411002](../errorcode-media.md#5411002-network-connection-timeout) | IO connection timeout.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5411003](../errorcode-media.md#5411003-data-or-link-exception-caused-by-network-exceptions) | IO network abnormal.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5411004](../errorcode-media.md#5411004-network-disabled) | IO network unavailable.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5411005](../errorcode-media.md#5411005-access-denied) | IO no permission.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5411006](../errorcode-media.md#5411006-client-request-parameter-is-incorrect-or-exceeds-the-processing-capability) | IO request denied.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5411007](../errorcode-media.md#5411007-no-resource-available) | IO resource not found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5411008](../errorcode-media.md#5411008-server-fails-to-verify-the-client-certificate) | IO SSL client cert needed.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5411009](../errorcode-media.md#5411009-ssl-connection-failed) | IO SSL connect fail.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5411010](../errorcode-media.md#5411010-client-fails-to-verify-the-server-certificate) | IO SSL server cert untrusted.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5411011](../errorcode-media.md#5411011-unsupported-request-due-to-network-protocol-errors) | IO unsupported request.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [5410002](../errorcode-media.md#5410002-seek-in-seekcontinuous-mode-is-not-supported) | Seek continuous unsupported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 18 and later |
| [5411012](../errorcode-media.md#5411012-request-not-supported-due-to-http-plaintext-interception) | Http cleartext traffic is not permitted.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |

## on('audioOutputDeviceChangeWithInfo')

```TypeScript
on(type: 'audioOutputDeviceChangeWithInfo', callback: Callback<audio.AudioStreamDeviceChangeInfo>): void
```

Subscribes to audio stream output device changes and reasons. This API uses an asynchronous callback to return the result.

When subscribing to this event, you are advised to implement the player behavior when the device is connected or disconnected by referring to  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'audioOutputDeviceChangeWithInfo', callback: Callback<audio.AudioStreamDeviceChangeInfo>): void--><!--Device-AVPlayer-on(type: 'audioOutputDeviceChangeWithInfo', callback: Callback<audio.AudioStreamDeviceChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioOutputDeviceChangeWithInfo' | Yes | Event type, which is **'audioOutputDeviceChangeWithInfo'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;audio.AudioStreamDeviceChangeInfo&gt; | Yes | Callback used to return the output device descriptor of the current audio stream and the change reason. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. 3.Parameter verification failed. |

## on('subtitleUpdate')

```TypeScript
on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void
```

Subscribes to subtitle update events. When external subtitles exist, the system notifies the application through the subscribed-to callback. An application can subscribe to only one subtitle update event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void--><!--Device-AVPlayer-on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'subtitleUpdate' | Yes | Event type, which is **'subtitleUpdate'** in this case. The event is triggered when the external subtitle is updated. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;SubtitleInfo&gt; | Yes | Callback invoked when the subtitle is updated. |

## on('trackChange')

```TypeScript
on(type: 'trackChange', callback: OnTrackChangeHandler): void
```

Subscribes to track change events. When the track changes, the system notifies the application through the subscribed-to callback. An application can subscribe to only one track change event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'trackChange', callback: OnTrackChangeHandler): void--><!--Device-AVPlayer-on(type: 'trackChange', callback: OnTrackChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'trackChange' | Yes | Event type, which is **'trackChange'** in this case. The event is triggered when the track changes. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback invoked when the event is triggered. |

## on('trackInfoUpdate')

```TypeScript
on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void
```

Subscribes to track information update events. When the track information is updated, the system notifies the application through the subscribed-to callback. An application can subscribe to only one track change event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void--><!--Device-AVPlayer-on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'trackInfoUpdate' | Yes | Event type, which is **'trackInfoUpdate'** in this case. The event is triggered when the track information is updated. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;MediaDescription&gt;&gt; | Yes | Callback invoked when the event is triggered. |

## on('amplitudeUpdate')

```TypeScript
on(type: 'amplitudeUpdate', callback: Callback<Array<double>>): void
```

Subscribes to update events of the maximum audio level value, which is periodically reported when audio resources are played.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

<!--Device-AVPlayer-on(type: 'amplitudeUpdate', callback: Callback<Array<double>>): void--><!--Device-AVPlayer-on(type: 'amplitudeUpdate', callback: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'amplitudeUpdate' | Yes | Event type, which is **'amplitudeUpdate'** in this case. The event is triggered when the amplitude changes. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;double&gt;&gt; | Yes | Callback invoked when the event is triggered. |

## on('seiMessageReceived')

```TypeScript
on(type: 'seiMessageReceived', payloadTypes: Array<int>, callback: OnSeiMessageHandle): void
```

Subscribes to events indicating that a Supplemental Enhancement Information (SEI) message is received. This applies only to HTTP-FLV live streaming and is triggered when SEI messages are present in the video stream. You must initiate the subscription before calling **prepare**. If you initiate multiple subscriptions to this event,the last subscription is applied.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-on(type: 'seiMessageReceived', payloadTypes: Array<int>, callback: OnSeiMessageHandle): void--><!--Device-AVPlayer-on(type: 'seiMessageReceived', payloadTypes: Array<int>, callback: OnSeiMessageHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'seiMessageReceived' | Yes | Event type, which is **'seiMessageReceived'** in this case. The event is triggered when an SEI message is received. |
| payloadTypes | Array&lt;int&gt; | Yes | Array of subscribed-to payload types of SEI messages. Currently, only payloadType = 5 is supported. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to listen for SEI message events and receive the subscribed-to payload types. |

## on('superResolutionChanged')

```TypeScript
on(type:'superResolutionChanged', callback: OnSuperResolutionChanged): void
```

Subscribes to the event indicating that super resolution is enabled or disabled.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-on(type:'superResolutionChanged', callback: OnSuperResolutionChanged): void--><!--Device-AVPlayer-on(type:'superResolutionChanged', callback: OnSuperResolutionChanged): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'superResolutionChanged' | Yes | Event type, which is **'superResolutionChanged'** in this case. The event is triggered when super resolution is enabled or disabled. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to listen for super resolution status changes. |

## onAmplitudeUpdate

```TypeScript
onAmplitudeUpdate(callback: Callback<Array<double>>): void
```

Subscribes to update events of the maximum audio level value, which is periodically reported when audio resources are played.The event is triggered when the amplitude changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onAmplitudeUpdate(callback: Callback<Array<double>>): void--><!--Device-AVPlayer-onAmplitudeUpdate(callback: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;double&gt;&gt; | Yes | Callback invoked when the event is triggered. |

## onAudioInterrupt

```TypeScript
onAudioInterrupt(callback: Callback<audio.InterruptEvent>): void
```

Register listens for audio interrupt event, refer to \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.The application needs to perform corresponding processing based on different audio interruption events.For details, see Handling Audio Interruption Events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onAudioInterrupt(callback: Callback<audio.InterruptEvent>): void--><!--Device-AVPlayer-onAudioInterrupt(callback: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;audio.InterruptEvent&gt; | Yes | Callback used to listen for the playback event return audio interrupt info. |

## onAudioOutputDeviceChangeWithInfo

```TypeScript
onAudioOutputDeviceChangeWithInfo(callback: Callback<audio.AudioStreamDeviceChangeInfo>): void
```

Subscribes to audio stream output device changes and reasons. This API uses an asynchronous callback to return the result.

When subscribing to this event, you are advised to implement the player behavior when the device is connected or disconnected by referring to Responding to Audio Output Device Changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onAudioOutputDeviceChangeWithInfo(callback: Callback<audio.AudioStreamDeviceChangeInfo>): void--><!--Device-AVPlayer-onAudioOutputDeviceChangeWithInfo(callback: Callback<audio.AudioStreamDeviceChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;audio.AudioStreamDeviceChangeInfo&gt; | Yes | Callback used to listen device change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## onAvailableBitrates

```TypeScript
onAvailableBitrates(callback: Callback<Array<int>>): void
```

Register listens for available bitrate list collect completed events for HLS protocol stream playback.This event will be reported after the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ called.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onAvailableBitrates(callback: Callback<Array<int>>): void--><!--Device-AVPlayer-onAvailableBitrates(callback: Callback<Array<int>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;int&gt;&gt; | Yes | Callback used to listen for the playback event return available bitrate list. It returns an array that holds the available bit rates. If the array length is 0, no bit rate can be set. |

## onBitrateDone

```TypeScript
onBitrateDone(callback: Callback<int>): void
```

Subscribes to the event to check whether the bit rate is successfully set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onBitrateDone(callback: Callback<int>): void--><!--Device-AVPlayer-onBitrateDone(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback invoked when the event is triggered. It reports the effective bit rate. |

## onBufferingUpdate

```TypeScript
onBufferingUpdate(callback: OnBufferingUpdateHandler): void
```

Subscribes to audio and video buffer changes. This subscription is supported only in network playback scenarios.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onBufferingUpdate(callback: OnBufferingUpdateHandler): void--><!--Device-AVPlayer-onBufferingUpdate(callback: OnBufferingUpdateHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback invoked when the event is triggered, and return BufferingInfoType and the value. |

## onDurationUpdate

```TypeScript
onDurationUpdate(callback: Callback<int>): void
```

Subscribes to media asset duration changes. It is used to refresh the length of the progress bar. By default, this event is reported once in the prepared state. However, it can be repeatedly reported for special streams that trigger duration changes. The **'durationUpdate'** event is not supported in live mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onDurationUpdate(callback: Callback<int>): void--><!--Device-AVPlayer-onDurationUpdate(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback used to return the resource duration. |

## onEndOfStream

```TypeScript
onEndOfStream(callback: Callback<void>): void
```

Subscribes to the event that indicates the end of the stream being played. If \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ = true is set,the AVPlayer seeks to the beginning of the stream and plays the stream again. If loop is not set,the completed state is reported through the \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onEndOfStream(callback: Callback<void>): void--><!--Device-AVPlayer-onEndOfStream(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback invoked when the event is triggered. |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Register listens for playback error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onError(callback: ErrorCallback): void--><!--Device-AVPlayer-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to listen for the playback error event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) | No memory. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. |
| [5400104](../errorcode-media.md#5400104-operation-timeout) | Time out. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. |
| [5410002](../errorcode-media.md#5410002-seek-in-seekcontinuous-mode-is-not-supported) | Seek continuous unsupported. |
| [5411001](../errorcode-media.md#5411001-failed-to-parse-or-connect-to-the-server-address) | IO can not find host. |
| [5411002](../errorcode-media.md#5411002-network-connection-timeout) | IO connection timeout. |
| [5411003](../errorcode-media.md#5411003-data-or-link-exception-caused-by-network-exceptions) | IO network abnormal. |
| [5411004](../errorcode-media.md#5411004-network-disabled) | IO network unavailable. |
| [5411005](../errorcode-media.md#5411005-access-denied) | IO no permission. |
| [5411006](../errorcode-media.md#5411006-client-request-parameter-is-incorrect-or-exceeds-the-processing-capability) | IO request denied. |
| [5411007](../errorcode-media.md#5411007-no-resource-available) | IO resource not found. |
| [5411008](../errorcode-media.md#5411008-server-fails-to-verify-the-client-certificate) | IO SSL client cert needed. |
| [5411009](../errorcode-media.md#5411009-ssl-connection-failed) | IO SSL connect fail. |
| [5411010](../errorcode-media.md#5411010-client-fails-to-verify-the-server-certificate) | IO SSL server cert untrusted. |
| [5411011](../errorcode-media.md#5411011-unsupported-request-due-to-network-protocol-errors) | IO unsupported request. |
| [5411012](../errorcode-media.md#5411012-request-not-supported-due-to-http-plaintext-interception) | Http cleartext traffic is not permitted. |

## onMediaKeySystemInfoUpdate

```TypeScript
onMediaKeySystemInfoUpdate( callback: Callback<Array<drm.MediaKeySystemInfo>>): void
```

Register listens for mediaKeySystemInfoUpdate events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onMediaKeySystemInfoUpdate( callback: Callback<Array<drm.MediaKeySystemInfo>>): void--><!--Device-AVPlayer-onMediaKeySystemInfoUpdate( callback: Callback<Array<drm.MediaKeySystemInfo>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;drm.MediaKeySystemInfo&gt;&gt; | Yes | Callback invoked when the event is triggered. It reports a **MediaKeySystemInfo** array. |

## onMetricsEvent

```TypeScript
onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void
```

Subscribes to metric events during playback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-AVPlayer-onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void--><!--Device-AVPlayer-onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;AVMetricsEvent&gt;&gt; | Yes | Callback invoked for metric events. This API uses an asynchronous callback to return the result. |

## onPlaybackContentChanged

```TypeScript
onPlaybackContentChanged(callback: Callback<string>):void
```

Registers a listener to detect when the playback content has changed.The value carried in the callback function is the ID of the media source that is being played in the playlist.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-onPlaybackContentChanged(callback: Callback<string>):void--><!--Device-AVPlayer-onPlaybackContentChanged(callback: Callback<string>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string&gt; | Yes | Callback invoked when the event is triggered. |

## onPlaybackRateDone

```TypeScript
onPlaybackRateDone(callback: OnPlaybackRateDone): void
```

Register listens for media playbackRateDone event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onPlaybackRateDone(callback: OnPlaybackRateDone): void--><!--Device-AVPlayer-onPlaybackRateDone(callback: OnPlaybackRateDone): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to listen for the playbackRateDone event. |

## onSeekDone

```TypeScript
onSeekDone(callback: Callback<int>): void
```

Subscribes to the event to check whether the seek operation takes effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onSeekDone(callback: Callback<int>): void--><!--Device-AVPlayer-onSeekDone(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback invoked when the event is triggered. It reports the time position requested by the user. For video playback, \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ may cause the actual position to be different from that requested by the user.The exact position can be obtained from the currentTime attribute. The time in this callback only means that the requested seek operation is complete. |

## onSeiMessageReceived

```TypeScript
onSeiMessageReceived(payloadTypes: Array<int>, callback: OnSeiMessageHandle): void
```

Subscribes to events indicating that a Supplemental Enhancement Information (SEI) message is received. This applies only to HTTP-FLV live streaming and is triggered when SEI messages are present in the video stream.You must initiate the subscription before calling \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. If you initiate multiple subscriptions to this event, the last subscription is applied.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onSeiMessageReceived(payloadTypes: Array<int>, callback: OnSeiMessageHandle): void--><!--Device-AVPlayer-onSeiMessageReceived(payloadTypes: Array<int>, callback: OnSeiMessageHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| payloadTypes | Array&lt;int&gt; | Yes | Array of subscribed-to payload types of SEI messages. Currently, only payloadType = 5 is supported. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to listen for SEI message events and receive the subscribed-to payload types. |

## onSpeedDone

```TypeScript
onSpeedDone(callback: Callback<int>): void
```

Subscribes to the event to check whether the playback speed is successfully set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onSpeedDone(callback: Callback<int>): void--><!--Device-AVPlayer-onSpeedDone(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback used to return the result. When the call of setSpeed is successful, the effective speed mode is reported. For details, see \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

## onStartRenderFrame

```TypeScript
onStartRenderFrame(callback: Callback<void>): void
```

Subscribes to the event that indicates rendering starts for the first frame. This subscription is supported only in video playback scenarios. This event only means that the playback service sends the first frame to the display module. The actual rendering effect depends on the rendering performance of the display service.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onStartRenderFrame(callback: Callback<void>): void--><!--Device-AVPlayer-onStartRenderFrame(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback invoked when the event is triggered. |

## onStateChange

```TypeScript
onStateChange(callback: OnAVPlayerStateChangeHandle): void
```

Register listens for media playback stateChange event.This event can be triggered by both user operations and the system.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onStateChange(callback: OnAVPlayerStateChangeHandle): void--><!--Device-AVPlayer-onStateChange(callback: OnAVPlayerStateChangeHandle): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback invoked when the event is triggered. |

## onSubtitleUpdate

```TypeScript
onSubtitleUpdate(callback: Callback<SubtitleInfo>): void
```

Subscribes to subtitle update events. When external subtitles exist, the system notifies the application through the subscribed-to callback. An application can subscribe to only one subtitle update event. When the application initiates multiple subscriptions to this event, the last subscription is applied.The event is triggered when the external subtitle is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onSubtitleUpdate(callback: Callback<SubtitleInfo>): void--><!--Device-AVPlayer-onSubtitleUpdate(callback: Callback<SubtitleInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;SubtitleInfo&gt; | Yes | Callback invoked when the subtitle is updated. |

## onSuperResolutionChanged

```TypeScript
onSuperResolutionChanged(callback: OnSuperResolutionChanged): void
```

Subscribes to the event indicating that super resolution is enabled or disabled.The event is triggered when super resolution is enabled or disabled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onSuperResolutionChanged(callback: OnSuperResolutionChanged): void--><!--Device-AVPlayer-onSuperResolutionChanged(callback: OnSuperResolutionChanged): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to listen for the super-resolution changed event. |

## onTimeUpdate

```TypeScript
onTimeUpdate(callback: Callback<int>): void
```

Subscribes to playback position changes. It is used to refresh the current position of the progress bar.By default, this event is reported every 100 ms. However, it is reported immediately upon a successful seek operation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onTimeUpdate(callback: Callback<int>): void--><!--Device-AVPlayer-onTimeUpdate(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback used to return the current time. |

## onTimedMetaData

```TypeScript
onTimedMetaData(callback: Callback<AVTimedMetaData>): void
```

Register listener to detect time-based metadata,Currently, only the #EXT-X-DATERANGE data of HLS and the Event Streams information of DASH are supported.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-onTimedMetaData(callback: Callback<AVTimedMetaData>): void--><!--Device-AVPlayer-onTimedMetaData(callback: Callback<AVTimedMetaData>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;AVTimedMetaData&gt; | Yes | Callback invoked when the event is triggered. |

## onTrackChange

```TypeScript
onTrackChange(callback: OnTrackChangeHandler): void
```

Subscribes to track change events. When the track changes, the system notifies the application through the subscribed-to callback. An application can subscribe to only one track change event. When the application initiates multiple subscriptions to this event, the last subscription is applied.The event is triggered when the track changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onTrackChange(callback: OnTrackChangeHandler): void--><!--Device-AVPlayer-onTrackChange(callback: OnTrackChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback invoked when the event is triggered. |

## onTrackInfoUpdate

```TypeScript
onTrackInfoUpdate(callback: Callback<Array<MediaDescription>>): void
```

Subscribes to track information update events. When the track information is updated, the system notifies the application through the subscribed-to callback. An application can subscribe to only one track change event.When the application initiates multiple subscriptions to this event, the last subscription is applied.The event is triggered when the track information is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onTrackInfoUpdate(callback: Callback<Array<MediaDescription>>): void--><!--Device-AVPlayer-onTrackInfoUpdate(callback: Callback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;MediaDescription&gt;&gt; | Yes | Callback invoked when the event is triggered. |

## onVideoSizeChange

```TypeScript
onVideoSizeChange(callback: OnVideoSizeChangeHandler): void
```

Subscribes to video size (width and height) changes. This subscription is supported only in video playback scenarios. By default, this event is reported only once in the prepared state. However, it is also reported upon resolution changes in the case of HLS streams.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onVideoSizeChange(callback: OnVideoSizeChangeHandler): void--><!--Device-AVPlayer-onVideoSizeChange(callback: OnVideoSizeChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback invoked when the event is triggered. |

## onVolumeChange

```TypeScript
onVolumeChange(callback: Callback<double>): void
```

Subscribes to the event to check whether the volume is successfully set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVPlayer-onVolumeChange(callback: Callback<double>): void--><!--Device-AVPlayer-onVolumeChange(callback: Callback<double>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;double&gt; | Yes | Callback invoked when the event is triggered. It reports the effective volume. |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses audio and video playback. This API can be called only when the AVPlayer is in the playing state. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-pause(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-pause(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |

## pause

```TypeScript
pause(): Promise<void>
```

Pauses audio and video playback. This API can be called only when the AVPlayer is in the playing state. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-pause(): Promise<void>--><!--Device-AVPlayer-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## play

```TypeScript
play(callback: AsyncCallback<void>): void
```

Starts to play an audio and video asset. This API can be called only when the AVPlayer is in the prepared, paused,or completed state. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-play(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-play(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |

## play

```TypeScript
play(): Promise<void>
```

Starts to play an audio and video asset. This API can be called only when the AVPlayer is in the prepared, paused,or completed state. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-play(): Promise<void>--><!--Device-AVPlayer-play(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## prepare

```TypeScript
prepare(callback: AsyncCallback<void>): void
```

Prepares for audio and video playback. This API can be called only when the AVPlayer is in the initialized state.The state changes can be detected by subscribing to the  
[stateChange]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ event. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-prepare(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-prepare(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Return by callback. |

## prepare

```TypeScript
prepare(): Promise<void>
```

Prepares for audio and video playback. This API can be called only when the AVPlayer is in the initialized state.The state changes can be detected by subscribing to the  
[stateChange]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ event. This API uses a promise to return the result.

If your application frequently switches between short videos, you can create multiple AVPlayer objects to prepare the next video in advance, thereby improving the switching performance. For details, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-prepare(): Promise<void>--><!--Device-AVPlayer-prepare(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Return by promise. |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the playback resources. This API can be called when the AVPlayer is in any state except released. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-release(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |

## release

```TypeScript
release(): Promise<void>
```

Releases the playback resources. This API can be called when the AVPlayer is in any state except released. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-release(): Promise<void>--><!--Device-AVPlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## removePlaybackMediaSource

```TypeScript
removePlaybackMediaSource(id: string): Promise<void>
```

Removes the specified playback media source from the player's playlist.If the id does not exist in the current playlist, the method returns immediately.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-removePlaybackMediaSource(id: string): Promise<void>--><!--Device-AVPlayer-removePlaybackMediaSource(id: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | ID returned after a media source is added to the playlist. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) | The media source ID does not exist in the playlist. Returned via promise. |

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

Resets audio and video playback. This API can be called only when the AVPlayer is in the initialized, prepared,playing, paused, completed, stopped, or error state. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-reset(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-reset(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |

## reset

```TypeScript
reset(): Promise<void>
```

Resets audio and video playback. This API can be called only when the AVPlayer is in the initialized, prepared,playing, paused, completed, stopped, or error state. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-reset(): Promise<void>--><!--Device-AVPlayer-reset(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## seek

ArkTS-Dyn:
```TypeScript
seek(timeMs: number, mode?: SeekMode): void
```

ArkTS-Sta:
```TypeScript
seek(timeMs: int, mode?: SeekMode): void
```

Seeks to the specified playback position. This API can be called only when the AVPlayer is in the prepared,playing, paused, or completed state. You can check whether the seek operation takes effect by subscribing to the  
[on('seekDone')]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ event.
    **NOTE**  
    
    Since API version 24, **seek** is supported in live streaming scenarios.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-seek(timeMs: int, mode?: SeekMode): void--><!--Device-AVPlayer-seek(timeMs: int, mode?: SeekMode): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeMs | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Position to seek to, in ms. The value range is \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_].\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_When the seek mode is [SEEK\_\_\_ESCAPED\_UNDERSCORE\_\_\_CONTINUOUS]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, you can set this parameter to **-1** to end the **SEEK\_\_\_ESCAPED\_UNDERSCORE\_\_\_CONTINUOUS** mode. |
| mode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Seek mode based on the video I frame. The default value is **SEEK\_\_\_ESCAPED\_UNDERSCORE\_\_\_PREV\_\_\_ESCAPED\_UNDERSCORE\_\_\_SYNC**. **Set this parameter only for video playback. |

## seekToDefaultPosition

```TypeScript
seekToDefaultPosition(): void
```

Seeks to the default access point of the playback source. For live streams, the latest recommended access point is used. For on-demand videos, the start position of the video is used (equivalent to **seek(0)**).

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-seekToDefaultPosition(): void--><!--Device-AVPlayer-seekToDefaultPosition(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |

## selectTrack

ArkTS-Dyn:
```TypeScript
selectTrack(index: number, mode?: SwitchMode): Promise<void>
```

ArkTS-Sta:
```TypeScript
selectTrack(index: int, mode?: SwitchMode): Promise<void>
```

Selects a track when the AVPlayer plays multimedia resources with multiple audio or video tracks. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-selectTrack(index: int, mode?: SwitchMode): Promise<void>--><!--Device-AVPlayer-selectTrack(index: int, mode?: SwitchMode): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Index of the track. You can call [getTrackDescription]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ to obtain all track information [MediaDescription]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ of the current resource. |
| mode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Video track mode. The default mode is **SMOOTH**. This parameter takes effect only for DASH/HLS network stream video track switching.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HLS network stream video is supported since API version 24.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## setBitrate

ArkTS-Dyn:
```TypeScript
setBitrate(bitrate: number): void
```

ArkTS-Sta:
```TypeScript
setBitrate(bitrate: int): void
```

Sets the bitrate for the streaming media. This API is valid only for HLS/DASH streams. By default, the AVPlayer selects a proper bitrate based on the network connection speed. This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state. You can check whether the setting takes effect by subscribing to the [bitrateDone]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ event.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setBitrate(bitrate: int): void--><!--Device-AVPlayer-setBitrate(bitrate: int): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bitrate | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Bitrate to set. You can obtain the available bitrates of the current HLS/DASH stream by subscribing to the [availableBitrates]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ event. If the bitrate to set is not in the list of the available bitrates, the AVPlayer selects from the list the bitrate that is closed to the bitrate to set. If the length of the available bitrate list obtained through the event is 0, no bitrate can be set and the **bitrateDone** callback will not be triggered, in bit/s. |

## setDecryptionConfig

```TypeScript
setDecryptionConfig(mediaKeySession: drm.MediaKeySession, secureVideoPath: boolean): void
```

Sets the decryption configuration. When receiving an  
[on('mediaKeySystemInfoUpdate')]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_event, create the related configuration and set the decryption configuration based on the information in the reported event. Otherwise, the playback fails.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setDecryptionConfig(mediaKeySession: drm.MediaKeySession, secureVideoPath: boolean): void--><!--Device-AVPlayer-setDecryptionConfig(mediaKeySession: drm.MediaKeySession, secureVideoPath: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mediaKeySession | drm.MediaKeySession | Yes | Decryption session. |
| secureVideoPath | boolean | Yes | Secure video channel. **true** if a secure video channel is selected, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. 3.Parameter verification failed. |

## setLoudnessGain

ArkTS-Dyn:
```TypeScript
setLoudnessGain(loudnessGain: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setLoudnessGain(loudnessGain: double): Promise<void>
```

Sets the loudness gain of the AVPlayer. After this API is called, the loudness gain takes effect immediately. This API uses a promise to return the result.
    **NOTE**  
    
    - This API can be called when the AVPlayer is in the prepared, playing, paused, completed, or stopped state.  
    
    - Before calling this API, ensure that the audio rendering information has been set in  
    **AVPlayer.audioRendererInfo** and the **usage** parameter in **audioRendererInfo** has been set to  
    [STREAM\_USAGE\_MUSIC]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_,  
    [STREAM\_USAGE\_MOVIE]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, or  
    [STREAM\_USAGE\_AUDIOBOOK]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-AVPlayer-setLoudnessGain(loudnessGain: double): Promise<void>--><!--Device-AVPlayer-setLoudnessGain(loudnessGain: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loudnessGain | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Loudness gain, in the range [-90.0, 24.0], in dB. The default value is 0.0 dB. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## setMediaMuted

```TypeScript
setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>
```

Mutes or unmutes the audio. Since API version 20, this API also supports whether to display the video image. This API uses a promise to return the result.

This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>--><!--Device-AVPlayer-setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mediaType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Media type.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_For API version 12 to 19, only **MEDIA\_\_\_ESCAPED\_UNDERSCORE\_\_\_TYPE\_\_\_ESCAPED\_UNDERSCORE\_\_\_AUD** is supported.&lt; br&gt;Since API version 20, **MEDIA\_\_\_ESCAPED\_UNDERSCORE\_\_\_TYPE\_\_\_ESCAPED\_UNDERSCORE\_\_\_VID** is supported. |
| muted | boolean | Yes | For API version 12 to 19, only audio playback strategies are supported. This parameter specifies whether to mute or unmute the audio. **true** to mute, **false** otherwise.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Since API version 20 , video playback strategies are also supported. This parameter specifies whether to disable or enable the video image. **true** to disable, false otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## setMediaSource

```TypeScript
setMediaSource(src: MediaSource, strategy?: PlaybackStrategy): Promise<void>
```

Sets a source of streaming media that can be pre-downloaded, downloads the media data, and temporarily stores the data in the memory. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setMediaSource(src: MediaSource, strategy?: PlaybackStrategy): Promise<void>--><!--Device-AVPlayer-setMediaSource(src: MediaSource, strategy?: PlaybackStrategy): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Source of the streaming media to pre-download. |
| strategy | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | strategy for playing the pre-downloaded streaming media. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. 3.Parameter verification failed. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## setPlaybackRange

ArkTS-Dyn:
```TypeScript
setPlaybackRange(startTimeMs: number, endTimeMs: number, mode?: SeekMode) : Promise<void>
```

ArkTS-Sta:
```TypeScript
setPlaybackRange(startTimeMs: int, endTimeMs: int, mode?: SeekMode) : Promise<void>
```

Sets the playback range and seeks to the start position of the range based on the specified  
[SeekMode]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. After the setting, only the content in the specified range of the audio or video file is played. This API uses a promise to return the result. It can be used in the initialized, prepared, paused, stopped, or completed state.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-setPlaybackRange(startTimeMs: int, endTimeMs: int, mode?: SeekMode) : Promise<void>--><!--Device-AVPlayer-setPlaybackRange(startTimeMs: int, endTimeMs: int, mode?: SeekMode) : Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startTimeMs | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Start position of the range, in ms. The value range is [0, duration). If **-1** is passed in, the system starts playing from position 0. |
| endTimeMs | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | End position of the range, in ms. The value range is (startTimeMs, duration]. If **-1** is passed in, the system plays the content until it reaches the final part of the asset. |
| mode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Seek mode, which can be **SeekMode.SEEK\_\_\_ESCAPED\_UNDERSCORE\_\_\_PREV\_\_\_ESCAPED\_UNDERSCORE\_\_\_SYNC** or **SeekMode.SEEK\_\_\_ESCAPED\_UNDERSCORE\_\_\_CLOSEST**.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The default value is **SeekMode.SEEK\_\_\_ESCAPED\_UNDERSCORE\_\_\_PREV\_\_\_ESCAPED\_UNDERSCORE\_\_\_SYNC**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## setPlaybackRate

ArkTS-Dyn:
```TypeScript
setPlaybackRate(rate: number): void
```

ArkTS-Sta:
```TypeScript
setPlaybackRate(rate: double): void
```

Sets the playback rate. This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state. The value range is [0.125, 4.0]. You can check whether the setting takes effect through the  
[playbackRateDone]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ event.
    **NOTE**  
    
    This API is not supported in live mode.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVPlayer-setPlaybackRate(rate: double): void--><!--Device-AVPlayer-setPlaybackRate(rate: double): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Playback rate, which is in the range [0.125, 4.0]. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) | The parameter check failed, parameter value out of range. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed, if invalid state or live stream. |

## setPlaybackStrategy

```TypeScript
setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>
```

Sets a playback strategy. This API can be called only when the AVPlayer is in the initialized state. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>--><!--Device-AVPlayer-setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| strategy | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Playback strategy. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## setSpeed

```TypeScript
setSpeed(speed: PlaybackSpeed): void
```

Sets the playback speed. This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state. You can check whether the speed setting takes effect by subscribing to the  
[on('speedDone')]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ event.
    **NOTE**  
    
    This method is not supported in live streaming scenarios.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setSpeed(speed: PlaybackSpeed): void--><!--Device-AVPlayer-setSpeed(speed: PlaybackSpeed): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Playback speed to set. |

## setSuperResolution

```TypeScript
setSuperResolution(enabled: boolean) : Promise<void>
```

Enables or disables super resolution. This API can be called when the AVPlayer is in the initialized, prepared,playing, paused, completed, or stopped state. This API uses a promise to return the result.

Before calling [prepare()]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, enable super resolution by using [PlaybackStrategy]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-setSuperResolution(enabled: boolean) : Promise<void>--><!--Device-AVPlayer-setSuperResolution(enabled: boolean) : Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable or disable super resolution. **true** to enable, **false** otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5410003](../errorcode-media.md#5410003-super-resolution-is-not-supported) | Super-resolution not supported. Return by promise. |
| [5410004](../errorcode-media.md#5410004-super-resolution-is-not-enabled) | Missing enable super-resolution feature in \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. Return by promise. |

## setTrackSelectionFilter

```TypeScript
setTrackSelectionFilter(filter : TrackSelectionFilter): Promise<void>
```

Sets a track selection filter for the player. The player will use this filter to select available tracks for playback. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-setTrackSelectionFilter(filter : TrackSelectionFilter): Promise<void>--><!--Device-AVPlayer-setTrackSelectionFilter(filter : TrackSelectionFilter): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Track selection filter. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. |

## setVideoWindowSize

ArkTS-Dyn:
```TypeScript
setVideoWindowSize(width: number, height: number) : Promise<void>
```

ArkTS-Sta:
```TypeScript
setVideoWindowSize(width: int, height: int) : Promise<void>
```

Sets the resolution of the output video after super resolution. This API can be called when the AVPlayer is in the initialized, prepared, playing, paused, completed, or stopped state. This API uses a promise to return the result.

The input parameter values must be in the range of 320 × 320 to 1920 × 1080 (in px).

Before calling [prepare()]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, enable super resolution by using [PlaybackStrategy]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AVPlayer-setVideoWindowSize(width: int, height: int) : Promise<void>--><!--Device-AVPlayer-setVideoWindowSize(width: int, height: int) : Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Target width of the output video after super resolution. The value range is [320-1920], in px. |
| height | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Target height of the output video after super resolution. The value range is [320-1080], in px. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5410003](../errorcode-media.md#5410003-super-resolution-is-not-supported) | Super-resolution not supported. Return by promise. |
| [5410004](../errorcode-media.md#5410004-super-resolution-is-not-enabled) | Missing enable super-resolution feature in \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. Return by promise. |

## setVolume

ArkTS-Dyn:
```TypeScript
setVolume(volume: number): void
```

ArkTS-Sta:
```TypeScript
setVolume(volume: double): void
```

Sets the playback volume. This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state. You can check whether the volume setting takes effect by subscribing to the  
[on('volumeChange')]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ event.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-setVolume(volume: double): void--><!--Device-AVPlayer-setVolume(volume: double): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volume | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the maximum volume (100%). |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops audio and video playback. This API can be called only when the AVPlayer is in the prepared, playing, paused,or completed state. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-stop(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |

## stop

```TypeScript
stop(): Promise<void>
```

Stops audio and video playback. This API can be called only when the AVPlayer is in the prepared, playing, paused,or completed state. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-stop(): Promise<void>--><!--Device-AVPlayer-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |

## audioEffectMode

```TypeScript
audioEffectMode ?: audio.AudioEffectMode
```

Audio effect mode. The audio effect mode is a dynamic property and is restored to the default value  
**EFFECT\_DEFAULT** when **usage** of **audioRendererInfo** is changed. It can be set only when the AVPlayer is in the prepared, playing, paused, or completed state.

**Type:** audio.AudioEffectMode

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-audioEffectMode ?: audio.AudioEffectMode--><!--Device-AVPlayer-audioEffectMode ?: audio.AudioEffectMode-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## audioInterruptMode

```TypeScript
audioInterruptMode?: audio.InterruptMode
```

Audio interruption mode. The default value is **SHARE\_MODE**. It is a dynamic property

and can be set only when the AVPlayer is in the prepared, playing, paused, or completed state.

To take effect, this property must be set before  
[play()]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is called for the first time.

**Type:** audio.InterruptMode

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-audioInterruptMode?: audio.InterruptMode--><!--Device-AVPlayer-audioInterruptMode?: audio.InterruptMode-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## audioRendererInfo

```TypeScript
audioRendererInfo?: audio.AudioRendererInfo
```

Audio renderer information. If the media source contains videos, the default value of **usage** is  
**STREAM\_USAGE\_MOVIE**. Otherwise, the default value of **usage** is **STREAM\_USAGE\_MUSIC**. The default value of  
**rendererFlags** is 0. If the default value of **usage** does not meet the requirements, configure  
[audio.AudioRendererInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

This parameter can be set only when the AVPlayer is in the initialized state.

To take effect, this property must be set before  
[prepare()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ is called for the first time.

**Type:** audio.AudioRendererInfo

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-audioRendererInfo?: audio.AudioRendererInfo--><!--Device-AVPlayer-audioRendererInfo?: audio.AudioRendererInfo-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## currentTime

```TypeScript
readonly currentTime: int
```

Current video playback position, in ms. It can be used as a query parameter when the AVPlayer is in the prepared,playing, paused, or completed state.

The value **-1** indicates an invalid value.

In live mode, **-1** is returned by default.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-readonly currentTime: int--><!--Device-AVPlayer-readonly currentTime: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## dataSrc

```TypeScript
dataSrc?: AVDataSrcDescriptor
```

Descriptor of a streaming media asset. It can be set only when the AVPlayer is in the idle state.

**Use scenario**: An application plays a file that has been downloaded from a remote source and saved locally.When the application has not yet downloaded the complete audio or video resources, it can start playing the data that has already been retrieved. By writing the retrieved data to a local file and simultaneously reading from that file, the application can achieve the capability of playing while caching.

The video formats MP4, MPEG-TS, and MKV are supported.

The audio formats M4A, AAC, MP3, OGG, WAV, FLAC, AMR, and APE are supported.

A user is obtaining an audio and video file from a remote server and wants to play the downloaded file content.To implement this scenario, do as follows:

1. Obtain the total file size, in bytes. If the total size cannot be obtained, set **fileSize** to **-1**.2. Implement the **func** callback to fill in data. If **fileSize** is **-1**, the format of **func** is **func(buffer: ArrayBuffer, length: number)**, and the AVPlayer obtains data in sequence; otherwise, the format is **func(buffer: ArrayBuffer, length: number, pos: number)**, and the AVPlayer seeks and obtains data in the required positions.3. Set **AVDataSrcDescriptor {fileSize = size, callback = func}**.

**Notes:**

If the media file to play is in MP4/M4A format, ensure that the **moov** field (specifying the media information)is before the **mdat** field (specifying the media data) or the fields before the **moov** field is less than 10MB. Otherwise, the parsing fails and the media file cannot be played.

**NOTE**

WebM is no longer supported since API version 11.

**Type:** AVDataSrcDescriptor

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-dataSrc?: AVDataSrcDescriptor--><!--Device-AVPlayer-dataSrc?: AVDataSrcDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## duration

```TypeScript
readonly duration: int
```

Video duration, in ms. It can be used as a query parameter when the AVPlayer is in the prepared, playing, paused,or completed state.

The value **-1** indicates an invalid value.

In live mode, **-1** is returned by default.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

**NOTE**

WebM is no longer supported since API version 11.

**Type:** AVFileDescriptor

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-fdSrc?: AVFileDescriptor--><!--Device-AVPlayer-fdSrc?: AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## height

```TypeScript
readonly height: int
```

Video height, in px. It can be used as a query parameter when the AVPlayer is in the prepared, playing, paused,or completed state.

The value **0** indicates an invalid value.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-loop: boolean--><!--Device-AVPlayer-loop: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## playlistLoopMode

```TypeScript
playlistLoopMode?: PlaylistLoopMode
```

Set the loop mode when playing the media source playlist.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value:PLAYLIST\_LOOP\_MODE\_ALL, which means loops all items in the playlist.

**Type:** PlaylistLoopMode

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-playlistLoopMode?: PlaylistLoopMode--><!--Device-AVPlayer-playlistLoopMode?: PlaylistLoopMode-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## privacyType

```TypeScript
privacyType?: audio.AudioPrivacyType
```

Audio privacy configuration. For more information, see \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.Default value: PRIVACY\_TYPE\_PUBLIC.

**Type:** audio.AudioPrivacyType

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-privacyType?: audio.AudioPrivacyType--><!--Device-AVPlayer-privacyType?: audio.AudioPrivacyType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## state

```TypeScript
readonly state: AVPlayerState
```

AVPlayer state. It can be used as a query parameter when the AVPlayer is in any state.

**Type:** AVPlayerState

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

[Create a surface ID through XComponent]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

![](../../../reference/apis-media-kit/figures/en-us\_image\_url.png)

2. HTTP: http://xx3. HTTPS: https://xx4. HLS: http://xx or https://xx

**NOTE**

- To set the playback URL, you need to declare the  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_permission. The related error code is  
\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.  
- WebM is no longer supported since API version 11.  
- After the resource handle (FD) is transferred to an AVPlayer instance, do not use the resource handle to  
perform other read and write operations, including but not limited to transferring this handle to other AVPlayer,AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. Competition occurs when multiple AVPlayers use the same resource handle to read and write files at the same time, resulting in errors in obtaining data.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVPlayer-url?: string--><!--Device-AVPlayer-url?: string-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## videoScaleType

```TypeScript
videoScaleType?: VideoScaleType
```

Video scale type. The default value is **VIDEO\_SCALE\_TYPE\_FIT**. It is a dynamic property

and can be set only when the AVPlayer is in the prepared, playing, paused, or completed state.

**Type:** VideoScaleType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-videoScaleType?: VideoScaleType--><!--Device-AVPlayer-videoScaleType?: VideoScaleType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## width

```TypeScript
readonly width: int
```

Video width, in px. It can be used as a query parameter when the AVPlayer is in the prepared, playing, paused, or completed state.

The value **0** indicates an invalid value.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlayer-readonly width: int--><!--Device-AVPlayer-readonly width: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

