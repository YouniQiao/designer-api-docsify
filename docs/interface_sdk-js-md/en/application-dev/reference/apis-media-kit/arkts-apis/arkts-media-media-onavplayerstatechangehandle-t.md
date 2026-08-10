# OnAVPlayerStateChangeHandle

```TypeScript
type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void
```

播放状态机切换事件回调方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-media-type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void--><!--Device-media-type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [AVPlayerState](arkts-media-media-avplayerstate-t.md) | Yes | 当前播放状态。 |
| reason | [StateChangeReason](arkts-media-media-statechangereason-e.md) | Yes | 当前播放状态的切换原因。 |

