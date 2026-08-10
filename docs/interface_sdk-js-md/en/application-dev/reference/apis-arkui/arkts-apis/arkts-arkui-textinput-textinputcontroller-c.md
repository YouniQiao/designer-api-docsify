# TextInputController

TextInput组件的控制器继承自  
[TextContentControllerBase](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#textcontentcontrollerbase)，涉及的接口有  
[getTextContentRect](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#gettextcontentrect)、  
[getTextContentLineCount](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#gettextcontentlinecount)、[getCaretOffset](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#getcaretoffset11)、  
[addText](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#addtext15)、  
[deleteText](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#deletetext15)、  
[getSelection](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#getselection15)、  
[clearPreviewText](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#clearpreviewtext17)、  
[setStyledPlaceholder](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#setstyledplaceholder22)、[deleteBackward](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#deletebackward23)、  
[scrollToVisible](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#scrolltovisible23)&lt;!-  
-Del--&gt;以及系统接口[getText](../../../reference/apis-arkui/arkui-ts/ts-text-common-sys.md#gettext19)&lt;!--DelEnd--&gt;。

**Inheritance/Implementation:** TextInputController extends [TextContentControllerBase](arkts-arkui-common-textcontentcontrollerbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TextInputController extends TextContentControllerBase--><!--Device-unnamed-export declare class TextInputController extends TextContentControllerBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: int): void
```

设置输入光标的位置。当取值小于0时，取0，大于文本长度时，显示在文本末尾。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputController-caretPosition(value: int): void--><!--Device-TextInputController-caretPosition(value: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes |  |

## constructor

```TypeScript
constructor()
```

TextInputController的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputController-constructor()--><!--Device-TextInputController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void
```

设置文本选择区域并高亮显示。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void--><!--Device-TextInputController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int | Yes | 文本选择区域起始位置，文本框中文字的起始位置为0。 |
| selectionEnd | int | Yes | 文本选择区域结束位置。当selectionEnd<0时，按照0处理；当selectionEnd大于文本长度时，按照文本长度处理。 |
| options | [SelectionOptions](../arkts-components/arkts-arkui-selectionoptions-i.md) | No | 选中文字时的配置。&lt;br /&gt;默认值：MenuPolicy.DEFAULT |

## stopEditing

```TypeScript
stopEditing(): void
```

退出编辑态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputController-stopEditing(): void--><!--Device-TextInputController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

