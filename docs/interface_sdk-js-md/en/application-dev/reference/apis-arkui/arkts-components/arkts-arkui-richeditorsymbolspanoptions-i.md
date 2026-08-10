# RichEditorSymbolSpanOptions

设置SymbolSpan组件的偏移位置和样式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface RichEditorSymbolSpanOptions--><!--Device-unnamed-declare interface RichEditorSymbolSpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: number
```

添加SymbolSpan的位置。省略时，添加到所有内容的最后。

如果值小于0，添加到所有内容的最前面；如果值大于所有内容的长度，添加到所有内容的最后面。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorSymbolSpanOptions-offset?: number--><!--Device-RichEditorSymbolSpanOptions-offset?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: RichEditorSymbolSpanStyle
```

SymbolSpan样式信息。当需要自定义SymbolSpan的颜色、大小、粗细、渲染策略等样式时传入此参数；省略时，使用系统默认样式信息。

**Type:** [RichEditorSymbolSpanStyle](../arkts-apis/arkts-arkui-richeditor-richeditorsymbolspanstyle-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorSymbolSpanOptions-style?: RichEditorSymbolSpanStyle--><!--Device-RichEditorSymbolSpanOptions-style?: RichEditorSymbolSpanStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

