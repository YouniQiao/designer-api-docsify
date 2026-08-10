# TextPickerDialog

Defines TextPickerDialog which uses show method to show TextPicker dialog.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class TextPickerDialog--><!--Device-unnamed-declare class TextPickerDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## show

```TypeScript
static show(options?: TextPickerDialogOptions)
```

定义文本滑动选择器弹窗并弹出。

> **说明：**
> 
> 从API version 10开始，可以通过使用[UIContext](../arkts-apis/arkts-arkui-uicontext.md/arkts-arkui-uicontext.md)中的
> [showTextPickerDialog](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md/arkts-arkui-arkui-uicontext-uicontext-c.md#showtextpickerdialog)来明确UI的执行上下文。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.UIContext#showTextPickerDialog

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialog-static show(options?: TextPickerDialogOptions)--><!--Device-TextPickerDialog-static show(options?: TextPickerDialogOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TextPickerDialogOptions](../arkts-apis/arkts-arkui-textpicker-textpickerdialogoptions-i.md) | No | 配置文本选择器弹窗的参数，缺省时无法弹出弹窗。至少需要提供range参数才能正常弹出弹窗， 其他参数均为可选配置。 |

