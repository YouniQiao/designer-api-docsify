# SwipeActionOptions

Defines the SwipeActionOption of swipeAction attribute method.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onOffsetChange

```TypeScript
onOffsetChange?: (offset: double) => void
```

Called when swipe action offset changed.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | double | Yes |

## edgeEffect

```TypeScript
edgeEffect?: SwipeEdgeEffect
```

Sets whether sliding to a boundary has a spring effect.

**Type:** [SwipeEdgeEffect](arkts-arkui-listitem-swipeedgeeffect-e.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end?: CustomBuilder | SwipeActionItem
```

An action item that appears when a list item slides left (when list direction is Vertical) or slides up (when list direction Horizontal).

**Type:** [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [SwipeActionItem](arkts-arkui-listitem-swipeactionitem-i.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: CustomBuilder | SwipeActionItem
```

An action item that appears when a list item slides right (when list direction is Vertical) or slides down (when list direction Horizontal).

**Type:** [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [SwipeActionItem](arkts-arkui-listitem-swipeactionitem-i.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
