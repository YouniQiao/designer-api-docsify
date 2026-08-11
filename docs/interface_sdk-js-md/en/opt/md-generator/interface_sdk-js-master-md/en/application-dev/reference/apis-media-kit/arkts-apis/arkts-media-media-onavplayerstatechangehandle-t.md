# OnAVPlayerStateChangeHandle

```TypeScript
type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void
```

Describes the callback invoked for the AVPlayer state change event.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-media-type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void--><!--Device-media-type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | [AVPlayerState](arkts-media-media-avplayerstate-t.md) | Yes |
| reason | [StateChangeReason](arkts-media-media-statechangereason-e.md) | Yes |
