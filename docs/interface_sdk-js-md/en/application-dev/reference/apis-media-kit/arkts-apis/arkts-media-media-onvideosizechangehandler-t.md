# OnVideoSizeChangeHandler

```TypeScript
type OnVideoSizeChangeHandler = (width: int, height: int) => void
```

Describes the callback invoked for the video size change event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-media-type OnVideoSizeChangeHandler = (width: int, height: int) => void--><!--Device-media-type OnVideoSizeChangeHandler = (width: int, height: int) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | int | Yes | Video width, in px. |
| height | int | Yes | Video height, in px. |

