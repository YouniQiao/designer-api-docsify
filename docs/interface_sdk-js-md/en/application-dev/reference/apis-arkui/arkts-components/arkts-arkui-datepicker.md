# DatePicker

**DatePicker** is a component for selecting a date through scrolling interaction. > **NOTE** > - Avoid changing component attributes during animation processes. > > - The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default > number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system > configuration is set, the default is 3 rows. To check the specific system configuration value for landscape mode, > use **$r('sys.float.ohos_id_picker_show_count_landscape')**. Child Components Not supported

## DatePicker

```TypeScript
DatePicker(options?: DatePickerOptions)
```

Creates a date picker in the given date range.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DatePickerInterface-(options?: DatePickerOptions): DatePickerAttribute--><!--Device-DatePickerInterface-(options?: DatePickerOptions): DatePickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DatePickerOptions](arkts-arkui-datepickeroptions-i.md) | No | Parameters of the date picker. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [DatePickerDialogOptions](arkts-arkui-datepickerdialogoptions-i.md) | Defines the configuration options of the date picker dialog box. Inherited from [DatePickerOptions](arkts-arkui-datepickeroptions-i.md). |
| [DatePickerOptions](arkts-arkui-datepickeroptions-i.md) | Describes the parameters of the date picker. > **NOTE：**> > - For details about how to use **Date**, see TimePickerOptions. > > - Property modifications made to **DatePickerOptions** during the **DatePicker** scrolling process may not take > effect. > **NOTE：**> > Handle exceptions for the start and end dates first, followed by exceptions for the selected date. |
| [DatePickerResult](arkts-arkui-datepickerresult-i.md) | Defines the time format returned by the date picker. |
| [LunarSwitchStyle](arkts-arkui-lunarswitchstyle-i.md) | Defines the style of the lunar calendar switch in the **DatePickerDialog** component. |

### Enums

| Name | Description |
| --- | --- |
| [DatePickerMode](arkts-arkui-datepickermode-e.md) | Enumerates date display modes. |

