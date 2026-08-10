# AVPlayer

播放管理类，用于管理和播放媒体资源。在调用AVPlayer的方法前，需要先通过  
[createAVPlayer()](arkts-media-media-createavplayer-f.md#createavplayer)构建一个AVPlayer实例。

在使用AVPlayer实例的方法时，建议开发者注册相关回调，主动获取当前状态变化。  
[on('stateChange')](media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle))：监听播放状态机AVPlayerState切换。[on('error')](media.AVPlayer.on(type: 'error', callback: ErrorCallback))：监听错误事件。

应用需要按照实际业务需求合理使用AVPlayer对象，按需创建并及时释放，避免持有过多AVPlayer实例导致内存消耗过大，否则在一定情况下可能导致系统终止应用。

Audio/Video播放demo可参考：[音频播放开发指导](../../../media/media/using-avplayer-for-playback.md)、  
[视频播放开发指导](../../../media/media/video-playback.md)。

> **说明：**
> 
> - 本Interface首批API从API version 9开始支持。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-media-interface AVPlayer--><!--Device-media-interface AVPlayer-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## forceLoadVideo

```TypeScript
forceLoadVideo(force: boolean): Promise<void>
```

Specifies whether to forcibly load the video. This API can be called only when the AVPlayer is in the prepared, playing, or paused state. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVPlayer-forceLoadVideo(force: boolean): Promise<void>--><!--Device-AVPlayer-forceLoadVideo(force: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| force | boolean | Yes | specified whether to forcibly load the video. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return when forceLoadVideo completed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Called from Non-System applications. Return by promise. |

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

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| trackType | [MediaType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-mediatype-e.md) | Yes | specified media Type, see [MediaType](#MediaType). |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | A Promise instance used to return selected track index. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | I/O error. Return by promise. |
| 5400101 | No memory. Return by promise. |
| 202 | Called from Non-System applications. Return by promise. |
| 5400105 | Service died. Return by promise. |

