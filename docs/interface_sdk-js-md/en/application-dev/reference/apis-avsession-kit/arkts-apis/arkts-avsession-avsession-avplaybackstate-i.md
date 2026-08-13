# AVPlaybackState

Used to indicate the playback state of the current media. If the playback state of the media changes, it needs to be updated synchronously

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-avSession-interface AVPlaybackState--><!--Device-avSession-interface AVPlaybackState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## activeItemId

```TypeScript
activeItemId?: int
```

Current active item id

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-activeItemId?: int--><!--Device-AVPlaybackState-activeItemId?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## bufferedTime

```TypeScript
bufferedTime?: long
```

The current buffered time, the maximum playable position, described by milliseconds.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-bufferedTime?: long--><!--Device-AVPlaybackState-bufferedTime?: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## duration

```TypeScript
duration?: int
```

The duration of this media asset, described by milliseconds.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AVPlaybackState-duration?: int--><!--Device-AVPlaybackState-duration?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## extras

```TypeScript
extras?: Record<string, Object>
```

Current custom media packets

**Type:** Record&lt;string, Object&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVPlaybackState-extras?: Record<string, Object>--><!--Device-AVPlaybackState-extras?: Record<string, Object>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## isFavorite

```TypeScript
isFavorite?: boolean
```

Current Favorite Status

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-isFavorite?: boolean--><!--Device-AVPlaybackState-isFavorite?: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## loopMode

```TypeScript
loopMode?: LoopMode
```

Current playback loop mode. See [LoopMode](arkts-avsession-avsession-loopmode-e.md#LoopMode)

**Type:** [LoopMode](arkts-avsession-avsession-loopmode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-loopMode?: LoopMode--><!--Device-AVPlaybackState-loopMode?: LoopMode-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## maxVolume

```TypeScript
maxVolume?: int
```

maximum volume

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-maxVolume?: int--><!--Device-AVPlaybackState-maxVolume?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## muted

```TypeScript
muted?: boolean
```

Current muted status

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-muted?: boolean--><!--Device-AVPlaybackState-muted?: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## position

```TypeScript
position?: PlaybackPosition
```

Current playback position of this media. See [PlaybackPosition](arkts-avsession-avsession-playbackposition-i.md#PlaybackPosition)

**Type:** [PlaybackPosition](arkts-avsession-avsession-playbackposition-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-position?: PlaybackPosition--><!--Device-AVPlaybackState-position?: PlaybackPosition-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## speed

```TypeScript
speed?: double
```

Current playback speed

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-speed?: double--><!--Device-AVPlaybackState-speed?: double-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## state

```TypeScript
state?: PlaybackState
```

Current playback state. See [PlaybackState](arkts-avsession-avsession-playbackstate-e.md#PlaybackState)

**Type:** PlaybackState

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-state?: PlaybackState--><!--Device-AVPlaybackState-state?: PlaybackState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## videoHeight

```TypeScript
videoHeight?: int
```

The video height of this media asset.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-videoHeight?: int--><!--Device-AVPlaybackState-videoHeight?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## videoWidth

```TypeScript
videoWidth?: int
```

The video width of this media asset.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-videoWidth?: int--><!--Device-AVPlaybackState-videoWidth?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## volume

```TypeScript
volume?: int
```

Current player volume

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-volume?: int--><!--Device-AVPlaybackState-volume?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

