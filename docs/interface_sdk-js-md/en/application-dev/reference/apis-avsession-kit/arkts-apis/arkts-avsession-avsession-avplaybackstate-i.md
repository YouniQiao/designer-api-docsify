# AVPlaybackState

媒体播放状态的相关属性。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVPlaybackState--><!--Device-avSession-interface AVPlaybackState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## activeItemId

```TypeScript
activeItemId?: int
```

正在播放的媒体ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-activeItemId?: int--><!--Device-AVPlaybackState-activeItemId?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## bufferedTime

```TypeScript
bufferedTime?: long
```

缓冲时间。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-bufferedTime?: long--><!--Device-AVPlaybackState-bufferedTime?: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## duration

```TypeScript
duration?: int
```

当前媒体资源的时长，单位为毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVPlaybackState-duration?: int--><!--Device-AVPlaybackState-duration?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## extras

```TypeScript
extras?: {[key: string]: Object}
```

自定义媒体数据。

**Type:** {[key: string]: Object}

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-extras?: {[key: string]: Object}--><!--Device-AVPlaybackState-extras?: {[key: string]: Object}-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## isFavorite

```TypeScript
isFavorite?: boolean
```

表示是否收藏。true表示收藏，false表示不收藏。

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-isFavorite?: boolean--><!--Device-AVPlaybackState-isFavorite?: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## loopMode

```TypeScript
loopMode?: LoopMode
```

循环模式。

**Type:** [LoopMode](arkts-avsession-avsession-loopmode-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-loopMode?: LoopMode--><!--Device-AVPlaybackState-loopMode?: LoopMode-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## maxVolume

```TypeScript
maxVolume?: int
```

最大音量。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-maxVolume?: int--><!--Device-AVPlaybackState-maxVolume?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## muted

```TypeScript
muted?: boolean
```

当前是否是静音状态。true表示是，false表示不是。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-muted?: boolean--><!--Device-AVPlaybackState-muted?: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## position

```TypeScript
position?: PlaybackPosition
```

播放位置。

**Type:** [PlaybackPosition](arkts-avsession-avsession-playbackposition-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-position?: PlaybackPosition--><!--Device-AVPlaybackState-position?: PlaybackPosition-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## speed

```TypeScript
speed?: double
```

播放倍速。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-speed?: double--><!--Device-AVPlaybackState-speed?: double-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## state

```TypeScript
state?: PlaybackState
```

播放状态。

**Type:** [PlaybackState](arkts-avsession-avsession-playbackstate-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-state?: PlaybackState--><!--Device-AVPlaybackState-state?: PlaybackState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## videoHeight

```TypeScript
videoHeight?: int
```

媒体资源的视频高度，单位为像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-videoHeight?: int--><!--Device-AVPlaybackState-videoHeight?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## videoWidth

```TypeScript
videoWidth?: int
```

媒体资源的视频宽度，单位为像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-videoWidth?: int--><!--Device-AVPlaybackState-videoWidth?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## volume

```TypeScript
volume?: int
```

正在播放的媒体音量。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVPlaybackState-volume?: int--><!--Device-AVPlaybackState-volume?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

