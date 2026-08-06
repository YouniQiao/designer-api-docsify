# OnDidChangeCallback

```TypeScript
declare type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) => void
```

Represents the callback invoked after text changes.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) => void--><!--Device-unnamed-declare type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rangeBefore | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Range of the text to be changed.  |
| rangeAfter | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Range of the text added.  |

