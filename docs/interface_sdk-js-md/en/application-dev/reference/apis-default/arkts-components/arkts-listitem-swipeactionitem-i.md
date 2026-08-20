# SwipeActionItem

Defines the swipe action item for SwipeActionOptions.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface SwipeActionItem--><!--Device-unnamed-export declare interface SwipeActionItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## actionAreaDistance

```TypeScript
actionAreaDistance?: Length
```

Defines distance for the delete area.

**Type:** [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)

**Default:** 56vp

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionItem-actionAreaDistance?: Length--><!--Device-SwipeActionItem-actionAreaDistance?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder?: CustomBuilder
```

An action item that appears when a list item slides right (when list direction is Vertical) or slides down (when list direction Horizontal).

**Type:** [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionItem-builder?: CustomBuilder--><!--Device-SwipeActionItem-builder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builderComponent

```TypeScript
builderComponent?: ComponentContentBase
```

An action item that appears when a list item slides right (when list direction is Vertical) or slides down (when list direction Horizontal).

**Type:** [ComponentContentBase](../arkts-apis/arkts-componentcontent-componentcontentbase-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionItem-builderComponent?: ComponentContentBase--><!--Device-SwipeActionItem-builderComponent?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAction

```TypeScript
onAction?: () => void
```

Called when ListItem need to be deleted.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionItem-onAction?: () => void--><!--Device-SwipeActionItem-onAction?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onEnterActionArea

```TypeScript
onEnterActionArea?: () => void
```

Called when swipe entry delete area.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionItem-onEnterActionArea?: () => void--><!--Device-SwipeActionItem-onEnterActionArea?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onExitActionArea

```TypeScript
onExitActionArea?: () => void
```

Called when swipe exit delete area.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionItem-onExitActionArea?: () => void--><!--Device-SwipeActionItem-onExitActionArea?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onStateChange

```TypeScript
onStateChange?: (state: SwipeActionState) => void
```

Called when component swipe action state changed.

**Type:** (state: SwipeActionState) =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionItem-onStateChange?: (state: SwipeActionState) => void--><!--Device-SwipeActionItem-onStateChange?: (state: SwipeActionState) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

