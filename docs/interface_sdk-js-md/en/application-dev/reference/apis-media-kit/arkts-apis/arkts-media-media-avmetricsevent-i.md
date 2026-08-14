# AVMetricsEvent

Describes the information of an Metrics Event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-media-interface AVMetricsEvent--><!--Device-media-interface AVMetricsEvent-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## Modules to Import

```TypeScript
import { media } from 'media';
```

## details

```TypeScript
details: Record<string, Object>
```

The detailed information of the event.

**Type:** Record&lt;string, Object&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMetricsEvent-details: Record<string, Object>--><!--Device-AVMetricsEvent-details: Record<string, Object>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## event

```TypeScript
event: AVMetricsEventType
```

Type of the metrics event.

**Type:** [AVMetricsEventType](arkts-media-media-avmetricseventtype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMetricsEvent-event: AVMetricsEventType--><!--Device-AVMetricsEvent-event: AVMetricsEventType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## playbackPosition

```TypeScript
playbackPosition: int
```

The playback progress position when the event occurs.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AVMetricsEvent-playbackPosition: int--><!--Device-AVMetricsEvent-playbackPosition: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## timeStamp

```TypeScript
timeStamp: long
```

Absolute timestamp when the event occurred.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AVMetricsEvent-timeStamp: long--><!--Device-AVMetricsEvent-timeStamp: long-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

