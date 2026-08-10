# DatePickerDialog

根据指定的日期范围创建日期滑动选择器并展示在弹窗上。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class DatePickerDialog--><!--Device-unnamed-declare class DatePickerDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## show

```TypeScript
static show(options?: DatePickerDialogOptions)
```

定义日期滑动选择器弹窗并弹出。

> **说明：**
> 
> 从API version 10开始，可以通过使用[UIContext](../arkts-apis/arkts-arkui-uicontext.md/arkts-arkui-uicontext.md)中的
> [showDatePickerDialog](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md/arkts-arkui-arkui-uicontext-uicontext-c.md#showdatepickerdialog)来明确UI的执行上下文。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.UIContext#showDatePickerDialog

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DatePickerDialog-static show(options?: DatePickerDialogOptions)--><!--Device-DatePickerDialog-static show(options?: DatePickerDialogOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DatePickerDialogOptions](../arkts-apis/arkts-arkui-datepicker-datepickerdialogoptions-i.md) | No | 配置日期选择器弹窗的参数，缺省时不弹出弹窗。 |

