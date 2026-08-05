# OnAVPlayerStateChangeHandle

```TypeScript
type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void
```

Describes the callback invoked for the AVPlayer state change event.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-media-type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void--><!--Device-media-type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | State of the AVPlayer.  |
| reason | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Reason for the state change.  |

