# VideoPlayStateChangedCallback

```TypeScript
export type VideoPlayStateChangedCallback = (state: VideoPlayerState) => void
```

The callback of onVideoPlayStateChanged event

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type VideoPlayStateChangedCallback = (state: VideoPlayerState) => void--><!--Device-unnamed-export type VideoPlayStateChangedCallback = (state: VideoPlayerState) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [VideoPlayerState](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-videoplayerstate-e.md) | Yes | Indicates the video player state. |

