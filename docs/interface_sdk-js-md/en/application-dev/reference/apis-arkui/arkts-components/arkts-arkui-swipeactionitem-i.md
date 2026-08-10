# SwipeActionItem

SwipeActionItem用于配置[SwipeActionOptions](arkts-arkui-swipeactionoptions-i.md)中的start或end划出项，包括划出时显示的操作项、长距离操作区域的距离阈值，以及进入、退出长距离操作区域、抬手触发操作和状态变化时的回调。

作为start划出项时，List为垂直布局时显示在ListItem左侧，List为水平布局时显示在ListItem上方；作为end划出项时，List为垂直布局时显示在ListItem右侧，List为水平布局时显示在ListItem下方。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface SwipeActionItem--><!--Device-unnamed-declare interface SwipeActionItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAction

```TypeScript
onAction?: () => void
```

组件进入长距删除区后抬手时触发。滑动后松手的位置超过或等于设置的距离阈值，并且设置的距离阈值有效时才会触发。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwipeActionItem-onAction?: () => void--><!--Device-SwipeActionItem-onAction?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onEnterActionArea

```TypeScript
onEnterActionArea?: () => void
```

在滑动条目进入删除区域时调用，只触发一次，当再次进入时仍触发。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwipeActionItem-onEnterActionArea?: () => void--><!--Device-SwipeActionItem-onEnterActionArea?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onExitActionArea

```TypeScript
onExitActionArea?: () => void
```

当滑动条目退出删除区域时调用，只触发一次，当再次退出时仍触发。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwipeActionItem-onExitActionArea?: () => void--><!--Device-SwipeActionItem-onExitActionArea?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onStateChange

```TypeScript
onStateChange?: (state: SwipeActionState) => void
```

当列表项滑动状态变化时候触发。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeActionItem-onStateChange?: (state: SwipeActionState) => void--><!--Device-SwipeActionItem-onStateChange?: (state: SwipeActionState) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [SwipeActionState](arkts-arkui-swipeactionstate-e.md) | Yes |  |

## actionAreaDistance

```TypeScript
actionAreaDistance?: Length
```

设置组件长距离滑动删除距离阈值。即划出组件被完全滑进视窗后，继续滑动触发删除的距离阈值。不支持设置百分比。删除距离阈值大于item宽度减去划出组件宽度，或删除距离阈值小于等于0就不会设置删除区域。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Default:** 56vp

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwipeActionItem-actionAreaDistance?: Length--><!--Device-SwipeActionItem-actionAreaDistance?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder?: CustomBuilder
```

当列表项向左或向右滑动（当列表方向为"垂直"时），向上或向下滑动（当列表方向为"水平"时）时显示的操作项。

**Type:** [CustomBuilder](arkts-arkui-custombuilder-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwipeActionItem-builder?: CustomBuilder--><!--Device-SwipeActionItem-builder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builderComponent

```TypeScript
builderComponent?: ComponentContent
```

当列表项向左或向右滑动（当列表方向为"垂直"时），向上或向下滑动（当列表方向为"水平"时）时显示的操作项。该参数的优先级高于参数builder。即同时设置builder和builderComponent时，以builderComponent设置的值为准。同一个builderComponent不推荐同时给不同的start/end使用，否则会导致显示问题。

**Type:** [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SwipeActionItem-builderComponent?: ComponentContent--><!--Device-SwipeActionItem-builderComponent?: ComponentContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

