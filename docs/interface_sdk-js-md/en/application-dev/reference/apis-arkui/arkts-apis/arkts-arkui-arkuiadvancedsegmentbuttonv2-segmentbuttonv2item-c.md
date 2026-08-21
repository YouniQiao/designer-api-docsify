# SegmentButtonV2Item

Defines segmented button item.

**Since:** 18

<!--Device-unnamed-export declare class SegmentButtonV2Item--><!--Device-unnamed-export declare class SegmentButtonV2Item-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SegmentButtonV2ItemOptions, OnSelectedIndexChange, OnSelectedIndexesChange, SegmentButtonV2Item, SegmentButtonV2Items, TabSegmentButtonV2, CapsuleSegmentButtonV2, MultiCapsuleSegmentButtonV2 } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options: SegmentButtonV2ItemOptions)
```

Constructs a **SegmentButtonV2ItemOptions** instance.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-constructor(options: SegmentButtonV2ItemOptions)--><!--Device-SegmentButtonV2Item-constructor(options: SegmentButtonV2ItemOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SegmentButtonV2ItemOptions](arkts-arkui-arkuiadvancedsegmentbuttonv2-segmentbuttonv2itemoptions-i.md) | Yes | Options of the item of the **SegmentButtonV2** component. |

## accessibilityDescription

```TypeScript
@Trace
    accessibilityDescription?: ResourceStr
```

Accessibility description of the segmented button item.

Default value: **""**

If the value is **undefined**, the default value is used.

Decorator type: @Trace

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-@Trace    accessibilityDescription?: ResourceStr--><!--Device-SegmentButtonV2Item-@Trace    accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
    accessibilityLevel?: string
```

Accessibility level of the segmented button item.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

Decorator type: @Trace

**Type:** string

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-@Trace    accessibilityLevel?: string--><!--Device-SegmentButtonV2Item-@Trace    accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
    accessibilityText?: ResourceStr
```

Accessibility text of the segmented button item.

Default value: **""**

If the value is **undefined**, the default value is used.

Decorator type: @Trace

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-@Trace    accessibilityText?: ResourceStr--><!--Device-SegmentButtonV2Item-@Trace    accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
@Trace
    enabled: boolean
```

Whether the segmented button item is enabled.

Default value: **true**

**true**: enabled. **false**: disabled.

If the value is **undefined**, the default value is used.

Decorator type: @Trace

**Type:** boolean

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-@Trace    enabled: boolean--><!--Device-SegmentButtonV2Item-@Trace    enabled: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
@Trace
    icon?: ResourceStr
```

Image icon of the segmented button item.

Default value: **undefined**

Decorator type: @Trace

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-@Trace    icon?: ResourceStr--><!--Device-SegmentButtonV2Item-@Trace    icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconModifier

```TypeScript
@Trace
    iconModifier?: ImageModifier
```

Image icon modifier for the segmented button item.

Default value: **undefined**

Decorator type: @Trace

**Type:** ImageModifier

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-@Trace    iconModifier?: ImageModifier--><!--Device-SegmentButtonV2Item-@Trace    iconModifier?: ImageModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbol

```TypeScript
@Trace
    symbol?: Resource
```

HM Symbol icon of the segmented button item.

Default value: **undefined**

Decorator type: @Trace

**Type:** Resource

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-@Trace    symbol?: Resource--><!--Device-SegmentButtonV2Item-@Trace    symbol?: Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolModifier

```TypeScript
@Trace
    symbolModifier?: SymbolGlyphModifier
```

HM Symbol icon modifier for the segmented button item.

Default value: **undefined**

Decorator type: @Trace

**Type:** SymbolGlyphModifier

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-@Trace    symbolModifier?: SymbolGlyphModifier--><!--Device-SegmentButtonV2Item-@Trace    symbolModifier?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
@Trace
    text?: ResourceStr
```

Text of the segmented button item.

Default value: **undefined**

Decorator type: @Trace

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-@Trace    text?: ResourceStr--><!--Device-SegmentButtonV2Item-@Trace    text?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textModifier

```TypeScript
@Trace
    textModifier?: TextModifier
```

Text modifier for the segmented button item.

Default value: **undefined**

Decorator type: @Trace

**Type:** [TextModifier](arkts-arkui-textmodifier-c.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SegmentButtonV2Item-@Trace    textModifier?: TextModifier--><!--Device-SegmentButtonV2Item-@Trace    textModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

