# CalendarPicker

The **CalendarPicker** component provides a drop-down calendar for users to select a date. > **NOTE** Child Components Not supported

## CalendarPicker

```TypeScript
CalendarPicker(options?: CalendarOptions)
```

Creates a calendar picker.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CalendarPickerInterface-(options?: CalendarOptions): CalendarPickerAttribute--><!--Device-CalendarPickerInterface-(options?: CalendarOptions): CalendarPickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CalendarOptions](arkts-arkui-calendaroptions-i.md) | No | Parameters of the calendar picker. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [CalendarDialogOptions](arkts-arkui-calendardialogoptions-i.md) | Defines the configuration options of the calendar picker dialog box. Inherits from [CalendarOptions](arkts-arkui-calendaroptions-i.md). &gt; **NOTE：**&gt; &gt; When the application window is resized, the width of the dialog box is continuously compressed. If the window width &gt; is reduced below a certain threshold, the content of the dialog box may not be fully visible. To ensure that the &gt; content of the **CalendarPickerDialog** component is fully displayed, the minimum window width required is 386 vp. |
| [CalendarOptions](arkts-arkui-calendaroptions-i.md) | Describes the parameters of the calendar picker. |

### Enums

| Name | Description |
| --- | --- |
| [CalendarAlign](arkts-arkui-calendaralign-e.md) | Enumerates alignment types. |

