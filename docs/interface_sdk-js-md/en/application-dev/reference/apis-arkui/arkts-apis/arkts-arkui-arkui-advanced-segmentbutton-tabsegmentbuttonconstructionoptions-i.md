# TabSegmentButtonConstructionOptions

Creates a SegmentButtonOptions object of the tab type.

Inherits from [CommonSegmentButtonOptions](../../apis-default/arkts-apis/arkts-arkui-advanced-segmentbutton-commonsegmentbuttonoptions-i.md).

**Inheritance/Implementation:** TabSegmentButtonConstructionOptions extends [CommonSegmentButtonOptions](../../apis-default/arkts-apis/arkts-arkui-advanced-segmentbutton-commonsegmentbuttonoptions-i.md)

**Since:** 11

<!--Device-unnamed-interface TabSegmentButtonConstructionOptions--><!--Device-unnamed-interface TabSegmentButtonConstructionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SegmentButton, SegmentButtonOptions, SegmentButtonItemOptionsArray, TabSegmentButtonOptions, TabSegmentButtonConstructionOptions, CapsuleSegmentButtonOptions, CapsuleSegmentButtonConstructionOptions, SegmentButtonTextItem, SegmentButtonIconItem, SegmentButtonIconTextItem, DimensionNoPercentage, CommonSegmentButtonOptions, ItemRestriction, SegmentButtonItemTuple, SegmentButtonItemArray, SegmentButtonItemOptionsConstructorOptions, SegmentButtonItemOptions, BorderRadiusMode } from '@kit.ArkUI';
import { SegmentButtonV2ItemOptions, OnSelectedIndexChange, OnSelectedIndexesChange, SegmentButtonV2Item, SegmentButtonV2Items, TabSegmentButtonV2, CapsuleSegmentButtonV2, MultiCapsuleSegmentButtonV2 } from '@kit.ArkUI';
```

## buttons

```TypeScript
buttons: ItemRestriction<SegmentButtonTextItem>
```

Button information.

**Type:** [ItemRestriction](../../apis-default/arkts-apis/arkts-itemrestriction-t.md)&lt;[SegmentButtonTextItem](../../apis-default/arkts-apis/arkts-arkui-advanced-segmentbutton-segmentbuttontextitem-i.md)&gt;

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TabSegmentButtonConstructionOptions-buttons: ItemRestriction<SegmentButtonTextItem>--><!--Device-TabSegmentButtonConstructionOptions-buttons: ItemRestriction<SegmentButtonTextItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

