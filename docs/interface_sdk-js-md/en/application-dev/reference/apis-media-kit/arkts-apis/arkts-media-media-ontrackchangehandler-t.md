# OnTrackChangeHandler

```TypeScript
type OnTrackChangeHandler = (index: int, isSelected: boolean) => void
```

Describes the callback invoked for the track change event.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-media-type OnTrackChangeHandler = (index: int, isSelected: boolean) => void--><!--Device-media-type OnTrackChangeHandler = (index: int, isSelected: boolean) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the track that has changed. |
| isSelected | boolean | Yes | Whether the track at the current index is selected. **true** if selected, **false** otherwise. |

