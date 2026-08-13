# OnDidChangeCallback

```TypeScript
declare type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) => void
```

Represents the callback invoked after text changes.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) => void--><!--Device-unnamed-declare type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rangeBefore | [TextRange](arkts-arkui-textrange-i.md) | Yes |
| rangeAfter | [TextRange](arkts-arkui-textrange-i.md) | Yes |
