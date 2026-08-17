# DatePickerOptions

Parameters of the date picker.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface DatePickerOptions--><!--Device-unnamed-export declare interface DatePickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end?: Date
```

End date of the picker.

**Type:** Date

**Default:** Date('2100-12-31')

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-end?: Date--><!--Device-DatePickerOptions-end?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: DatePickerMode
```

Date columns to be displayed. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>In DatePickerDialog, with showTime=true, this parameter has no effect and the default three columns for year, <br>month, and day are displayed. &lt;/p&gt;

**Type:** [DatePickerMode](arkts-na-datepicker-datepickermode-e.md)

**Default:** DatePickerMode.DATE - which means to display three columns: year, month, and day. <br>Decimal values are rounded off.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-mode?: DatePickerMode--><!--Device-DatePickerOptions-mode?: DatePickerMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected?: Date | Bindable<Date>
```

Specifies the date selector check date or time selector check time.

**Type:** Date \| [Bindable](arkts-na-common-bindable-i.md)&lt;Date&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-selected?: Date | Bindable<Date>--><!--Device-DatePickerOptions-selected?: Date | Bindable<Date>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: Date
```

Start date of the picker.

**Type:** Date

**Default:** Date('1970-1-1')

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-start?: Date--><!--Device-DatePickerOptions-start?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

