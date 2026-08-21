# CapsuleSegmentButtonConstructionOptions

Represents configuration options for creating a **SegmentButton** component consisting of capsule-style segmented buttons.

Inherits from [CommonSegmentButtonOptions](../../apis-default/arkts-apis/arkts-arkuiadvancedsegmentbutton-commonsegmentbuttonoptions-i.md).

**Inheritance/Implementation:** CapsuleSegmentButtonConstructionOptions extends [CommonSegmentButtonOptions](../../apis-default/arkts-apis/arkts-arkuiadvancedsegmentbutton-commonsegmentbuttonoptions-i.md)

**Since:** 11

<!--Device-unnamed-interface CapsuleSegmentButtonConstructionOptions--><!--Device-unnamed-interface CapsuleSegmentButtonConstructionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SegmentButton, SegmentButtonOptions, SegmentButtonItemOptionsArray, TabSegmentButtonOptions, TabSegmentButtonConstructionOptions, CapsuleSegmentButtonOptions, CapsuleSegmentButtonConstructionOptions, SegmentButtonTextItem, SegmentButtonIconItem, SegmentButtonIconTextItem, DimensionNoPercentage, CommonSegmentButtonOptions, ItemRestriction, SegmentButtonItemTuple, SegmentButtonItemArray, SegmentButtonItemOptionsConstructorOptions, SegmentButtonItemOptions, BorderRadiusMode } from '@kit.ArkUI';
import { SegmentButtonV2ItemOptions, OnSelectedIndexChange, OnSelectedIndexesChange, SegmentButtonV2Item, SegmentButtonV2Items, TabSegmentButtonV2, CapsuleSegmentButtonV2, MultiCapsuleSegmentButtonV2 } from '@kit.ArkUI';
```

## buttons

```TypeScript
buttons: SegmentButtonItemTuple
```

Button information.

**Type:** [SegmentButtonItemTuple](../../apis-default/arkts-apis/arkts-segmentbuttonitemtuple-t.md)

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CapsuleSegmentButtonConstructionOptions-buttons: SegmentButtonItemTuple--><!--Device-CapsuleSegmentButtonConstructionOptions-buttons: SegmentButtonItemTuple-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiply

```TypeScript
multiply?: boolean
```

Whether multiple items can be selected.

Default value: **false**

If the value is **undefined**, the default value is used.

**true**: Multi-selection is allowed.

**false**: Multi-selection is not allowed.

**Type:** boolean

**Default:** false

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CapsuleSegmentButtonConstructionOptions-multiply?: boolean--><!--Device-CapsuleSegmentButtonConstructionOptions-multiply?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

