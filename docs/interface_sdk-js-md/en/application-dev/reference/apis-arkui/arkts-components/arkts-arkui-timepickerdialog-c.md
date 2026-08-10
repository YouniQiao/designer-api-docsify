# TimePickerDialog

以24小时的时间区间创建时间滑动选择器，展示在弹窗上。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class TimePickerDialog--><!--Device-unnamed-declare class TimePickerDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## show

```TypeScript
static show(options?: TimePickerDialogOptions)
```

定义时间滑动选择器弹窗并弹出。

> **说明：**
> 
> 从API version 10开始，可以通过使用[UIContext](../arkts-apis/arkts-arkui-uicontext.md/arkts-arkui-uicontext.md)中的
> [showTimePickerDialog](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md/arkts-arkui-arkui-uicontext-uicontext-c.md#showtimepickerdialog)来明确UI的执行上下文。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.UIContext#showTimePickerDialog

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TimePickerDialog-static show(options?: TimePickerDialogOptions)--><!--Device-TimePickerDialog-static show(options?: TimePickerDialogOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TimePickerDialogOptions](arkts-arkui-timepickerdialogoptions-i.md) | No | 配置时间选择器弹窗的参数。参数缺省时不弹出弹窗。 |

