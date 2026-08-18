# AVPlayer

AVPlayer is a playback management class. It provides APIs to manage and play media assets. Before calling any API in AVPlayer, you must use [createAVPlayer()](arkts-media-media-createavplayer-f.md#createavplayer) to create an AVPlayer instance. When using the AVPlayer instance, you are advised to register the following callbacks to proactively obtain status changes: [on('stateChange')](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate): listens for AVPlayer state changes. [on('error')](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate): listens for error events. Applications must properly manage AVPlayer instances according to their specific needs, creating and freeing them when necessary. Holding too many AVPlayer instances can lead to high memory usage, and in some cases, the system might terminate applications to free up resources. For details about the audio and video playback demo, see [Audio Playback](../../../media/media/using-avplayer-for-playback.md) and [Video Playback](../../../media/media/video-playback.md).

**Since:** 23

<!--Device-media-interface AVPlayer--><!--Device-media-interface AVPlayer-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## Modules to Import

```TypeScript
```

## enableCameraPostprocessing

```TypeScript
enableCameraPostprocessing(): Promise<void>
```

Enable the post-processing function of Camera for video playback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVPlayer-enableCameraPostprocessing(): Promise<void>--><!--Device-AVPlayer-enableCameraPostprocessing(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## forceLoadVideo

```TypeScript
forceLoadVideo(force: boolean): Promise<void>
```

Specifies whether to forcibly load the video. This API can be called only when the AVPlayer is in the prepared, playing, or paused state. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-forceLoadVideo(force: boolean): Promise<void>--><!--Device-AVPlayer-forceLoadVideo(force: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| force | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## enableStartFrameRateOpt

```TypeScript
enableStartFrameRateOpt?: boolean
```

Whether a slower synchronization policy is used at the start of playback to reduce subjective image jitter caused by insufficient frame rate. Default value: false, means that the slower synchronization policy will not be used.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-enableStartFrameRateOpt?: boolean--><!--Device-AVPlayer-enableStartFrameRateOpt?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**System API:** This is a system API.
