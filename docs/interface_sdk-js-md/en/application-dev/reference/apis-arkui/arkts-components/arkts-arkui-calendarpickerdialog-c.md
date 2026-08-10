# CalendarPickerDialog

点击日期弹出日历选择器弹窗，可在弹窗内选择日期。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare class CalendarPickerDialog--><!--Device-unnamed-declare class CalendarPickerDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## show

```TypeScript
static show(options?: CalendarDialogOptions): void
```

显示日历选择器弹窗，供用户选择日期。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CalendarPickerDialog-static show(options?: CalendarDialogOptions): void--><!--Device-CalendarPickerDialog-static show(options?: CalendarDialogOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CalendarDialogOptions](../arkts-apis/arkts-arkui-calendarpicker-calendardialogoptions-i.md) | No | 配置日历选择器弹窗的参数，缺省时无法弹出弹窗。 |

