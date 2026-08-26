# SegmentButtonItemTuple

```TypeScript
declare type SegmentButtonItemTuple = ItemRestriction<SegmentButtonTextItem> | ItemRestriction<SegmentButtonIconItem> | ItemRestriction<SegmentButtonIconTextItem>
```

Represents the tuple union type used to store button information.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| [ItemRestriction](arkts-arkui-itemrestriction-t.md) & lt;SegmentButtonTextItem & gt; | A tuple of text-only button information. |
| [ItemRestriction](arkts-arkui-itemrestriction-t.md) & lt;SegmentButtonIconItem & gt; | A tuple of icon-only button information. |
| [ItemRestriction](arkts-arkui-itemrestriction-t.md) & lt;SegmentButtonIconTextItem & gt; | A tuple of icon and text button information. |
