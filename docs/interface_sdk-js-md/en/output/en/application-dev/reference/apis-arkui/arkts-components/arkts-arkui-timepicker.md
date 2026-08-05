# TimePicker

**TimePicker** is a component that allows users to select a time from the given range through scrolling. **NOTE** - Avoid changing component attributes during animation processes. - The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system configuration is set, the default is 3 rows. To check the specific system configuration value for landscape mode, use **$r('sys.float.ohos_id_picker_show_count_landscape')**. Child Components Not supported

## TimePicker

```TypeScript
TimePicker(options?: TimePickerOptions)
```

Creates a time picker, which uses the 24-hour time format by default.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TimePickerInterface-(options?: TimePickerOptions): TimePickerAttribute--><!--Device-TimePickerInterface-(options?: TimePickerOptions): TimePickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters of the time picker.  |

## Summary

