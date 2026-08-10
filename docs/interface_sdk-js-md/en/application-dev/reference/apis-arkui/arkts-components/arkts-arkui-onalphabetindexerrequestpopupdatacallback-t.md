# OnAlphabetIndexerRequestPopupDataCallback

```TypeScript
declare type OnAlphabetIndexerRequestPopupDataCallback  = (index: number) => Array<string>
```

[usingPopup](AlphabetIndexerAttribute#usingPopup)设置值为true，索引项被选中时触发的事件。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnAlphabetIndexerRequestPopupDataCallback  = (index: number) => Array<string>--><!--Device-unnamed-declare type OnAlphabetIndexerRequestPopupDataCallback  = (index: number) => Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | selected index |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | string array corresponding to the index |

