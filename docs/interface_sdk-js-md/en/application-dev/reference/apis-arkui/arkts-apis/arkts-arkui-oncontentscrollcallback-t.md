# OnContentScrollCallback

```TypeScript
export type OnContentScrollCallback = (totalOffsetX: double, totalOffsetY: double) => void
```

文本内容滚动回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnContentScrollCallback = (totalOffsetX: double, totalOffsetY: double) => void--><!--Device-unnamed-export type OnContentScrollCallback = (totalOffsetX: double, totalOffsetY: double) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| totalOffsetX | double | Yes | 文本在内容区的横坐标偏移，单位px。 |
| totalOffsetY | double | Yes | 文本在内容区的纵坐标偏移，单位px。 |

