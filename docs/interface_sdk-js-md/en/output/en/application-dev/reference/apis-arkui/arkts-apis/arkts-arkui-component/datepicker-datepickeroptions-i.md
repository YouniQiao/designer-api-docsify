# DatePickerOptions

Parameters of the date picker.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-end?: Date--><!--Device-DatePickerOptions-end?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: DatePickerMode
```

Date columns to be displayed. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_In DatePickerDialog, with showTime=true, this parameter has no effect and the default three columns for year, \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_month, and day are displayed. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_

**Type:** DatePickerMode

**Default:** DatePickerMode.DATE - which means to display three columns: year, month, and day.
<br>Decimal values are rounded off.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-mode?: DatePickerMode--><!--Device-DatePickerOptions-mode?: DatePickerMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected?: Date | Bindable<Date>
```

Specifies the date selector check date or time selector check time.

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

Start date of the picker.

**Type:** Date

**Default:** Date('1970-1-1')

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerOptions-start?: Date--><!--Device-DatePickerOptions-start?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

