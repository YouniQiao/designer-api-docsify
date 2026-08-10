# TextInputController

TextInput组件的控制器继承自[TextContentControllerBase](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md)，涉及的接口有  
[getTextContentRect](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#gettextcontentrect)、  
[getTextContentLineCount](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#gettextcontentlinecount)、  
[getCaretOffset](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#getcaretoffset)、[addText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#addtext)、  
[deleteText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#deletetext)、[getSelection](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#getselection)、[clearPreviewText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#clearpreviewtext)、  
[setStyledPlaceholder](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#setstyledplaceholder)、  
[deleteBackward](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#deletebackward)、  
[scrollToVisible](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#scrolltovisible)&lt;!--Del--&gt;以及系统接口  
[getText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c-sys.md/arkts-arkui-common-textcontentcontrollerbase-c-sys.md#gettext)&lt;!--DelEnd--&gt;。

## 导入对象

```ts controller: TextInputController = new TextInputController();```

**Inheritance/Implementation:** TextInputController extends [TextContentControllerBase](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class TextInputController extends TextContentControllerBase--><!--Device-unnamed-declare class TextInputController extends TextContentControllerBase-End-->

**System capability:** 
- API version 10 and later: SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: number): void
```

设置输入光标的位置。当取值小于0时，取0，大于文本长度时，显示在文本末尾。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-caretPosition(value: number): void--><!--Device-TextInputController-caretPosition(value: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | 从字符串开始到光标所在位置的字符长度。 |

## constructor

```TypeScript
constructor()
```

TextInputController的构造函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-constructor()--><!--Device-TextInputController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

设置文本选择区域并高亮显示。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-TextInputController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | number | Yes | 文本选择区域起始位置，文本框中文字的起始位置为0。当selectionStart<0时，按照0处理；当selectionStart大于文本长度时，按照文本长度处 理。 |
| selectionEnd | number | Yes | 文本选择区域结束位置。当selectionEnd<0时，按照0处理；当selectionEnd大于文本长度时，按照文本长度处理。 |
| options | [SelectionOptions](../arkts-apis/arkts-arkui-common-selectionoptions-i.md) | No | 选中文字时的配置，用于控制文本选择菜单的显示策略。 &lt;br&gt;配置项包括menuPolicy，用于指定菜单显示方式：MenuPolicy.DEFAULT表示按系统默认行为显示菜单；MenuPolicy.SHOW表示强制显示菜单；MenuPolicy.HIDE表示强制隐藏菜单。 &lt;br&gt;默认值MenuPolicy.DEFAULT &lt;br&gt;从API version 12开始，该接口中的options参数支持在原子化服务中使用。<br>**Since:** 12 |

## stopEditing

```TypeScript
stopEditing(): void
```

退出编辑态。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-stopEditing(): void--><!--Device-TextInputController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

