# RichEditorSymbolSpanOptions

设置SymbolSpan组件的偏移位置和样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RichEditorSymbolSpanOptions--><!--Device-unnamed-export declare interface RichEditorSymbolSpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: int
```

添加组件的位置。省略时，添加到所有内容的最后。

如果值小于0，添加到所有内容的最前面；如果值大于所有内容的长度，添加到所有内容的最后面。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorSymbolSpanOptions-offset?: int--><!--Device-RichEditorSymbolSpanOptions-offset?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: RichEditorSymbolSpanStyle
```

组件样式信息。省略时，使用系统默认样式信息。

**Type:** [RichEditorSymbolSpanStyle](arkts-arkui-richeditor-richeditorsymbolspanstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorSymbolSpanOptions-style?: RichEditorSymbolSpanStyle--><!--Device-RichEditorSymbolSpanOptions-style?: RichEditorSymbolSpanStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

