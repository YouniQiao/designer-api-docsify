# MediaSource

媒体数据信息。来源于  
[createMediaSourceWithUrl](arkts-media-media-createmediasourcewithurl-f.md#createmediasourcewithurl)。

> **说明：**
> 
> - 本Interface首批接口从API version 12开始支持。

**起始版本：** 12

<!--Device-unnamed-interface MediaSource--><!--Device-unnamed-interface MediaSource-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

## enableOfflineCache

```TypeScript
enableOfflineCache(enable: boolean): void
```

是否在视频播放期间启用离线缓存。

**起始版本：** 23

<!--Device-MediaSource-enableOfflineCache(enable: boolean): void--><!--Device-MediaSource-enableOfflineCache(enable: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

## getID

```TypeScript
getID(): string
```

获取媒体源的标识符。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSource-getID(): string--><!--Device-MediaSource-getID(): string-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**返回值：**

| 类型 |
| --- |
| string |

## getTrackSelectionFilter

```TypeScript
getTrackSelectionFilter(): TrackSelectionFilter | undefined
```

Obtains the configured audio and video feature filtering values.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MediaSource-getTrackSelectionFilter(): TrackSelectionFilter | undefined--><!--Device-MediaSource-getTrackSelectionFilter(): TrackSelectionFilter | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**返回值：**

| 类型 |
| --- |
| [TrackSelectionFilter](arkts-media-media-trackselectionfilter-i.md) |

## setMediaResourceLoaderDelegate

```TypeScript
setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void
```

设置MediaSourceLoader，帮助播放器请求媒体数据。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSource-setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void--><!--Device-MediaSource-setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceLoader | [MediaSourceLoader](arkts-media-multimedia-media-mediasourceloader-i.md) | 是 |

## setMimeType

```TypeScript
setMimeType(mimeType: AVMimeTypes): void
```

设置媒体MIME类型，以帮助播放器处理扩展的媒体源。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSource-setMimeType(mimeType: AVMimeTypes): void--><!--Device-MediaSource-setMimeType(mimeType: AVMimeTypes): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mimeType | [AVMimeTypes](arkts-media-multimedia-media-avmimetypes-e.md) | 是 |

## setTrackSelectionFilter

```TypeScript
setTrackSelectionFilter(filter: TrackSelectionFilter): void
```

Set the audio and video feature filtering items of the MediaSource,After the user defines the audio and video filtering items of the MediaSource,When playing or downloading MediaSource data offline,Preferentially perform a corresponding operation in the filtering feature.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MediaSource-setTrackSelectionFilter(filter: TrackSelectionFilter): void--><!--Device-MediaSource-setTrackSelectionFilter(filter: TrackSelectionFilter): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [TrackSelectionFilter](arkts-media-media-trackselectionfilter-i.md) | 是 |
