# TimePicker

**TimePicker** is a component that allows users to select a time from the given range through scrolling. **NOTE** - Avoid changing component attributes during animation processes. - The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system configuration is set, the default is 3 rows. To check the specific system configuration value for landscape mode, use **$r('sys.float.ohos_id_picker_show_count_landscape')**. Child Components Not supported

## TimePicker

```TypeScript
TimePicker(options?: TimePickerOptions)
```

Creates a time picker, which uses the 24-hour time format by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TimePickerInterface-(options?: TimePickerOptions): TimePickerAttribute--><!--Device-TimePickerInterface-(options?: TimePickerOptions): TimePickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TimePickerOptions](arkts-arkui-timepickeroptions-i.md) | No | Parameters of the time picker. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [TimePickerDialogOptions](arkts-arkui-timepickerdialogoptions-i.md) | Defines the configuration options of the time picker dialog box. Inherited from [TimePickerOptions](arkts-arkui-timepickeroptions-i.md). |
| [TimePickerOptions](arkts-arkui-timepickeroptions-i.md) | Describes the parameters of the time picker. Property modifications made to **TimePickerOptions** during the **TimePicker** scrolling process may not take effect. The **Date** object is used to handle dates and time. It can be used in the following ways: **Method 1**: new Date() Obtains the current system date and time. **Method 2**: new Date(value: number | string) **Method 3**: new Date(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number) |
| [TimePickerResult](arkts-arkui-timepickerresult-i.md) | Describes a time in 24-hour format. |

### Types

| Name | Description |
| --- | --- |
| [DateTimeOptions](arkts-arkui-datetimeoptions-t.md) | Defines the options for a **DateTimeOptions** object. |
| [OnTimePickerChangeCallback](arkts-arkui-ontimepickerchangecallback-t.md) | Triggered when a time is selected. |

### Enums

| Name | Description |
| --- | --- |
| [TimePickerFormat](arkts-arkui-timepickerformat-e.md) | Enumerates time display formats of the time picker. |

