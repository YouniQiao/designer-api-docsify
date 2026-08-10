# OnTrackChangeHandler

```TypeScript
type OnTrackChangeHandler = (index: int, isSelected: boolean) => void
```

track变更事件回调方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-media-type OnTrackChangeHandler = (index: int, isSelected: boolean) => void--><!--Device-media-type OnTrackChangeHandler = (index: int, isSelected: boolean) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 当前变更的track索引。 |
| isSelected | boolean | Yes | 当前变更的track索引是否被选中。true表示处于选中状态，false表示处于非选中状态。 |

