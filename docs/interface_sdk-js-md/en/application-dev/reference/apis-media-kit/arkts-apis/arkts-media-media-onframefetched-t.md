# OnFrameFetched

```TypeScript
type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void
```

Describes the callback invoked when thumbnails are obtained in batches.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-media-type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void--><!--Device-media-type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frameInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Thumbnail information.  |
| err | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | Error that occurs when the thumbnail is obtained. The default value is **null**.  |

