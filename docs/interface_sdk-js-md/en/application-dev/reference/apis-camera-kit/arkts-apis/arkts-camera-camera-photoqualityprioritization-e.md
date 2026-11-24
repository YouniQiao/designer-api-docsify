# PhotoQualityPrioritization

```TypeScript
enum PhotoQualityPrioritization
```

Enumerates the photo quality prioritization strategies.

**Since:** 21

<!--Device-camera-enum PhotoQualityPrioritization--><!--Device-camera-enum PhotoQualityPrioritization-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## HIGH_QUALITY

```TypeScript
HIGH_QUALITY = 0
```

Focuses on image quality, which may increase the time required for capturing photos to ensure high-quality output.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PhotoQualityPrioritization-HIGH_QUALITY = 0--><!--Device-PhotoQualityPrioritization-HIGH_QUALITY = 0-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## LOW_QUALITY

```TypeScript
LOW_QUALITY = 2
```

Focuses on low overhead, prioritizing the shortest capture time with reduced image quality.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PhotoQualityPrioritization-LOW_QUALITY = 2--><!--Device-PhotoQualityPrioritization-LOW_QUALITY = 2-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## SPEED

```TypeScript
SPEED = 1
```

Focuses on performance, trading off image quality for faster capture times.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PhotoQualityPrioritization-SPEED = 1--><!--Device-PhotoQualityPrioritization-SPEED = 1-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core
