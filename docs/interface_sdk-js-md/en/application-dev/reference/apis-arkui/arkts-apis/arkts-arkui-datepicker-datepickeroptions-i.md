# DatePickerOptions

日期选择器组件的参数说明。

**说明：**

- Date的使用请参考[TimePickerOptions](arkts-arkui-timepicker-timepickeroptions-i.md)。

- 在DatePicker组件滑动过程中修改DatePickerOptions中的属性，会导致这些属性无法生效。

**说明：**

- 先处理起始日期与结束日期的异常情形，再处理选中日期的异常情形。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DatePickerOptions--><!--Device-unnamed-export declare interface DatePickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end?: Date
```

指定选择器的结束日期。

默认值：Date('2100-12-31')

取值范围：[Date('1900-01-31'), Date('2100-12-31')]

**Type:** Date

**Default:** Date('2100-12-31')

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-end?: Date--><!--Device-DatePickerOptions-end?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: DatePickerMode
```

设置日期展示模式。

默认值：DatePickerMode.DATE，显示年、月、日三列。

在[DatePickerDialog](./datePicker.static)中，当[DatePickerDialogOptions](../../../reference/apis-arkui/arkui-ts/ts-methods-datepicker-dialog.md#datepickerdialogoptions)的showTime设置为true时，此参数不生效，默认显示年、月、日三列。

**Type:** [DatePickerMode](arkts-arkui-datepicker-datepickermode-e.md)

**Default:** DatePickerMode.DATE - which means to display three columns: year, month, and day. <br>Decimal values are rounded off.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-mode?: DatePickerMode--><!--Device-DatePickerOptions-mode?: DatePickerMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected?: Date | Bindable<Date>
```

设置选中项的日期。

默认值：当前系统日期。

取值范围：[Date('1900-01-31'), Date('2100-12-31')]

从API version 23开始，该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync-static.md)双向绑定变量。

**Type:** Date \| Bindable&lt;Date&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-selected?: Date | Bindable<Date>--><!--Device-DatePickerOptions-selected?: Date | Bindable<Date>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: Date
```

指定选择器的起始日期。

默认值：Date('1970-1-1')

取值范围：[Date('1900-01-31'), Date('2100-12-31')]

**Type:** Date

**Default:** Date('1970-1-1')

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-start?: Date--><!--Device-DatePickerOptions-start?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

