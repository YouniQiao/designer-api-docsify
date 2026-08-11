# AVPlayerState

```TypeScript
type AVPlayerState = 'idle' | 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' | 'released' | 'error'
```

Describes the state of the [AVPlayer](arkts-multimedia-media.md). Your application can proactively obtain the AVPlayer state through the **state** property or obtain the reported AVPlayer state by subscribing to the   
[stateChange](@ohos.multimedia.media:media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle))event. For details about the rules for state transition, see   
[Audio Playback](../../../media/media/using-avplayer-for-playback.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-media-type AVPlayerState = 'idle' | 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' | 'released' | 'error'--><!--Device-media-type AVPlayerState = 'idle' | 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' | 'released' | 'error'-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| 'idle' |
| 'initialized' |
| 'prepared' |
| 'playing' |
| 'paused' |
| 'completed' |
| 'stopped' |
| 'released' |
| 'error' |
