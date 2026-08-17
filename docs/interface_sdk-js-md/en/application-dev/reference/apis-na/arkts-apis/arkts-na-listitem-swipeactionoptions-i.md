# SwipeActionOptions

Defines the SwipeActionOption of swipeAction attribute method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface SwipeActionOptions--><!--Device-unnamed-export declare interface SwipeActionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## edgeEffect

```TypeScript
edgeEffect?: SwipeEdgeEffect
```

Sets whether sliding to a boundary has a spring effect.

**Type:** [SwipeEdgeEffect](arkts-na-listitem-swipeedgeeffect-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionOptions-edgeEffect?: SwipeEdgeEffect--><!--Device-SwipeActionOptions-edgeEffect?: SwipeEdgeEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end?: CustomBuilder | SwipeActionItem
```

An action item that appears when a list item slides left (when list direction is Vertical) or slides up (when list direction Horizontal).

**Type:** CustomBuilder \| [SwipeActionItem](arkts-na-listitem-swipeactionitem-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionOptions-end?: CustomBuilder | SwipeActionItem--><!--Device-SwipeActionOptions-end?: CustomBuilder | SwipeActionItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onOffsetChange

```TypeScript
onOffsetChange?: (offset: double) => void
```

Called when swipe action offset changed.

**Type:** (offset: double) =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionOptions-onOffsetChange?: (offset: double) => void--><!--Device-SwipeActionOptions-onOffsetChange?: (offset: double) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: CustomBuilder | SwipeActionItem
```

An action item that appears when a list item slides right (when list direction is Vertical) or slides down (when list direction Horizontal).

**Type:** CustomBuilder \| [SwipeActionItem](arkts-na-listitem-swipeactionitem-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeActionOptions-start?: CustomBuilder | SwipeActionItem--><!--Device-SwipeActionOptions-start?: CustomBuilder | SwipeActionItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

