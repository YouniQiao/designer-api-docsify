# VideoPlayStateChangedCallback

```TypeScript
export type VideoPlayStateChangedCallback = (state: VideoPlayerState) => void
```

The callback of onVideoPlayStateChanged event

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export type VideoPlayStateChangedCallback = (state: VideoPlayerState) => void--><!--Device-unnamed-export type VideoPlayStateChangedCallback = (state: VideoPlayerState) => void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [VideoPlayerState](arkts-medialibrary-file-photopickercomponent-videoplayerstate-e.md) | 是 | Indicates the video player state. |

