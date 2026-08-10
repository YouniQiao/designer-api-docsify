# MediaSource

媒体数据信息。来源于  
[createMediaSourceWithUrl](arkts-media-media-createmediasourcewithurl-f.md#createmediasourcewithurl)。

> **说明：**
> 
> - 本Interface首批接口从API version 12开始支持。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-interface MediaSource--><!--Device-unnamed-interface MediaSource-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## enableOfflineCache

```TypeScript
enableOfflineCache(enable: boolean): void
```

是否在视频播放期间启用离线缓存。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-MediaSource-enableOfflineCache(enable: boolean): void--><!--Device-MediaSource-enableOfflineCache(enable: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 是否在视频播放期间启用离线缓存。true表示启用，false表示不启用。 |

## getID

```TypeScript
getID(): string
```

获取媒体源的标识符。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MediaSource-getID(): string--><!--Device-MediaSource-getID(): string-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回媒体源的标识符，失败时返回空字符串。 |

## getTrackSelectionFilter

```TypeScript
getTrackSelectionFilter(): TrackSelectionFilter | undefined
```

Obtains the configured audio and video feature filtering values.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaSource-getTrackSelectionFilter(): TrackSelectionFilter | undefined--><!--Device-MediaSource-getTrackSelectionFilter(): TrackSelectionFilter | undefined-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Return value:**

| Type | Description |
| --- | --- |
| [TrackSelectionFilter](arkts-media-media-trackselectionfilter-i.md) | If the TrackSelectionFilter object exists, the TrackSelectionFilter object is returned. Otherwise, the TrackSelectionFilter object is returned. |

## setMediaResourceLoaderDelegate

```TypeScript
setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void
```

设置MediaSourceLoader，帮助播放器请求媒体数据。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSource-setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void--><!--Device-MediaSource-setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceLoader | [MediaSourceLoader](arkts-media-multimedia-media-mediasourceloader-i.md) | Yes | 应用实现的媒体数据获取接口，方便播放器获取数据。 |

## setMimeType

```TypeScript
setMimeType(mimeType: AVMimeTypes): void
```

设置媒体MIME类型，以帮助播放器处理扩展的媒体源。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaSource-setMimeType(mimeType: AVMimeTypes): void--><!--Device-MediaSource-setMimeType(mimeType: AVMimeTypes): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | [AVMimeTypes](arkts-media-multimedia-media-avmimetypes-e.md) | Yes | 媒体MIME类型。 |

## setTrackSelectionFilter

```TypeScript
setTrackSelectionFilter(filter: TrackSelectionFilter): void
```

Set the audio and video feature filtering items of the MediaSource,After the user defines the audio and video filtering items of the MediaSource,When playing or downloading MediaSource data offline,Preferentially perform a corresponding operation in the filtering feature.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaSource-setTrackSelectionFilter(filter: TrackSelectionFilter): void--><!--Device-MediaSource-setTrackSelectionFilter(filter: TrackSelectionFilter): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [TrackSelectionFilter](arkts-media-media-trackselectionfilter-i.md) | Yes | Specifies the audio and video features of the pre-downloaded streaming media. |

