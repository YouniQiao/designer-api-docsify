# DatePickerMode

Defines the mode of the date picker.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum DatePickerMode--><!--Device-unnamed-export declare enum DatePickerMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DATE

```TypeScript
DATE = 0
```

The date displays three columns: year, month, and day.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerMode-DATE = 0--><!--Device-DatePickerMode-DATE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## YEAR_AND_MONTH

```TypeScript
YEAR_AND_MONTH = 1
```

The date displays two columns: year and month.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerMode-YEAR_AND_MONTH = 1--><!--Device-DatePickerMode-YEAR_AND_MONTH = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MONTH_AND_DAY

```TypeScript
MONTH_AND_DAY = 2
```

Defines a mode that displays the date in months and days of the month. In this mode, if the month changes from December to January, the year does not increment by one; if the month changes from January to December, the year does not decrement by one. The year remains fixed at the currently set value.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerMode-MONTH_AND_DAY = 2--><!--Device-DatePickerMode-MONTH_AND_DAY = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

