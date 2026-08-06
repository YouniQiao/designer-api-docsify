# OnPlaybackRateDone

```TypeScript
type OnPlaybackRateDone = (rate: double) => void
```

Describes the callback invoked for the event indicating that the playback rate setting is complete.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-media-type OnPlaybackRateDone = (rate: double) => void--><!--Device-media-type OnPlaybackRateDone = (rate: double) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Playback rate.  |

