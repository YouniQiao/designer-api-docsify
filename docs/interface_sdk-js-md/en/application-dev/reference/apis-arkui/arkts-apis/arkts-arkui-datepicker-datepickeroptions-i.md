# DatePickerOptions

Parameters of the date picker.@interface DatePickerOptions

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end?: Date
```

End date of the picker.

**Type:** Date

**Default:** Date('2100-12-31')

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: DatePickerMode
```

Date columns to be displayed.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>In DatePickerDialog, with showTime=true, this parameter has no effect and the default three columns for year, <br>month, and day are displayed. </p>

**Type:** [DatePickerMode](arkts-arkui-datepicker-datepickermode-e.md)

**Default:** DatePickerMode.DATE - which means to display three columns: year, month, and day. <br>Decimal values are rounded off.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected?: Date | Bindable<Date>
```

Specifies the date selector check date or time selector check time.

**Type:** Date \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;Date&gt;

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: Date
```

Start date of the picker.

**Type:** Date

**Default:** Date('1970-1-1')

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
