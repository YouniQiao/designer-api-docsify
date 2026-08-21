# CommonSegmentButtonOptions

Defines the customizable attributes of a segment button component.

**Since:** 11

<!--Device-unnamed-interface CommonSegmentButtonOptions--><!--Device-unnamed-interface CommonSegmentButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SegmentButton, SegmentButtonOptions, SegmentButtonItemOptionsArray, TabSegmentButtonOptions, TabSegmentButtonConstructionOptions, CapsuleSegmentButtonOptions, CapsuleSegmentButtonConstructionOptions, SegmentButtonTextItem, SegmentButtonIconItem, SegmentButtonIconTextItem, DimensionNoPercentage, CommonSegmentButtonOptions, ItemRestriction, SegmentButtonItemTuple, SegmentButtonItemArray, SegmentButtonItemOptionsConstructorOptions, SegmentButtonItemOptions, BorderRadiusMode } from '@kit.ArkUI';
import { SegmentButtonV2ItemOptions, OnSelectedIndexChange, OnSelectedIndexesChange, SegmentButtonV2Item, SegmentButtonV2Items, TabSegmentButtonV2, CapsuleSegmentButtonV2, MultiCapsuleSegmentButtonV2 } from '@kit.ArkUI';
```

## backgroundSystemMaterial

```TypeScript
backgroundSystemMaterial?: uiMaterial.Material
```

Set system-styled materials for the component. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the component.

**Type:** uiMaterial.Material

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CommonSegmentButtonOptions-backgroundSystemMaterial?: uiMaterial.Material--><!--Device-CommonSegmentButtonOptions-backgroundSystemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

