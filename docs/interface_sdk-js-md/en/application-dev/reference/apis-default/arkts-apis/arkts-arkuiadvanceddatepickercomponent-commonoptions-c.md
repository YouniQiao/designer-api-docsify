# CommonOptions

CommonOptions defines common options for the date time picker.

> **Description:**
> 
> - For Date usage, refer to
> [TimePickerOptions](../../../reference/apis-arkui/arkui-ts/ts-basic-components-timepicker.md#timepickeroptions对象说明)。
> 
> - The text size of DatePickerComponent adapts between 14vp and 16vp. When the component width is too narrow,
> text may be truncated.
> 
> - When parameters are omitted or set to undefined, default values are used.
> 
> - In [DateOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvanceddatepickercomponent-dateoptions-c.md), setting start, end, and selected only takes effect for the date part
> (year, month, day). In [TimeOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvanceddatepickercomponent-timeoptions-c.md), setting start, end, and selected only takes effect for the
> time part (hour, minute, second).

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare class CommonOptions--><!--Device-unnamed-export declare class CommonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## enableHapticFeedback

```TypeScript
enableHapticFeedback?: boolean
```

Enables or disables haptic feedback.

Default value: true

- true: Enable haptic feedback. - false: Disable haptic feedback.

**Description**:

1. When set to true, its effectiveness depends on whether the system's hardware supports it. 2. To enable haptic feedback, you need to configure the requestPermissions field in the project's [module.json5](../../../quick-start/module-configuration-file.md) to enable vibration permission, as follows:

"requestPermissions": [{"name": "ohos.permission.VIBRATE"}]

**Type:** boolean

**Default:** true

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonOptions-enableHapticFeedback?: boolean--><!--Device-CommonOptions-enableHapticFeedback?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end?: Date
```

End date or time of the picker.

Default value: Date(2100, 12, 31, 23, 59, 59)

Value range: [Date(0, 0, 1, 0, 0, 0), Date(10000, 11, 31,23, 59, 59)]

**Type:** Date

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonOptions-end?: Date--><!--Device-CommonOptions-end?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## loop

```TypeScript
loop?: boolean
```

Sets whether to enable loop mode.

- true: Enable loop mode. - false: Disable loop mode.

Default value: true

**Type:** boolean

**Default:** true

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonOptions-loop?: boolean--><!--Device-CommonOptions-loop?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: Callback<DatePickerComponentResult>
```

Callback triggered after date or time is selected.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DatePickerComponentResult](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvanceddatepickercomponent-datepickercomponentresult-c.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonOptions-onChange?: Callback<DatePickerComponentResult>--><!--Device-CommonOptions-onChange?: Callback<DatePickerComponentResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onScrollStop

```TypeScript
onScrollStop?: Callback<DatePickerComponentResult>
```

Callback triggered when a picker item is selected and scrolling stops.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DatePickerComponentResult](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvanceddatepickercomponent-datepickercomponentresult-c.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonOptions-onScrollStop?: Callback<DatePickerComponentResult>--><!--Device-CommonOptions-onScrollStop?: Callback<DatePickerComponentResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected?: Date
```

Selected date. Default value is the current system date or time.

**Type:** Date

**Default:** current system date or time

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonOptions-selected?: Date--><!--Device-CommonOptions-selected?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: Date
```

Start date or time of the picker.

Default value: Date(1970, 0, 1, 0, 0, 0)

Value range: [Date(0, 0, 1, 0, 0, 0), Date(10000, 11, 31,23, 59, 59)]

**Type:** Date

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonOptions-start?: Date--><!--Device-CommonOptions-start?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

