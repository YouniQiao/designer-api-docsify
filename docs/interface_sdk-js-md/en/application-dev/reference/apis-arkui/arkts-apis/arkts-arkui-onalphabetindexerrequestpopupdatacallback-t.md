# OnAlphabetIndexerRequestPopupDataCallback

```TypeScript
export type OnAlphabetIndexerRequestPopupDataCallback = (index: int) => Array<string>
```

[usingPopup](arkts-arkui-alphabetindexer-alphabetindexerattribute-i.md#usingpopup)设置值为true，索引项被选中时触发的事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnAlphabetIndexerRequestPopupDataCallback = (index: int) => Array<string>--><!--Device-unnamed-export type OnAlphabetIndexerRequestPopupDataCallback = (index: int) => Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | selected index |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | string array corresponding to the index |

