# OnVideoSizeChangeHandler

```TypeScript
type OnVideoSizeChangeHandler = (width: int, height: int) => void
```

Describes the callback invoked for the video size change event.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-media-type OnVideoSizeChangeHandler = (width: int, height: int) => void--><!--Device-media-type OnVideoSizeChangeHandler = (width: int, height: int) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Video width, in px. |
| height | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Video height, in px. |

