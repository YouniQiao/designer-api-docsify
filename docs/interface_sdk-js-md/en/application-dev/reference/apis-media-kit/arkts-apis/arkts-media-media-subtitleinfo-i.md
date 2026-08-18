# SubtitleInfo

Provides subtitle information. When a subtitle update event is subscribed to, the information about the external subtitle is returned through a callback. Can be synchronized to the time reported by AVPlayer#timeUpdate event

**Since:** 23

<!--Device-media-interface SubtitleInfo--><!--Device-media-interface SubtitleInfo-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## duration

```TypeScript
duration?: int
```

Duration of the text to be displayed, as milliseconds.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SubtitleInfo-duration?: int--><!--Device-SubtitleInfo-duration?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## startTime

```TypeScript
startTime?: int
```

Display start time of the text, as milliseconds.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SubtitleInfo-startTime?: int--><!--Device-SubtitleInfo-startTime?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## text

```TypeScript
text?: string
```

Text information of current update event.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SubtitleInfo-text?: string--><!--Device-SubtitleInfo-text?: string-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

