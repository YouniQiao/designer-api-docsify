# DatePickerMode

设置日期展示模式。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare enum DatePickerMode--><!--Device-unnamed-declare enum DatePickerMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DATE

```TypeScript
DATE = 0
```

显示年、月、日三列。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DatePickerMode-DATE = 0--><!--Device-DatePickerMode-DATE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## YEAR_AND_MONTH

```TypeScript
YEAR_AND_MONTH = 1
```

显示年、月二列。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DatePickerMode-YEAR_AND_MONTH = 1--><!--Device-DatePickerMode-YEAR_AND_MONTH = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MONTH_AND_DAY

```TypeScript
MONTH_AND_DAY = 2
```

显示月、日二列。

在此模式下，年份始终保持不变，取值为selected参数指定的年份。若selected未指定则取当前系统年份。当月份滚动导致日期超出有效范围时，日期会自动调整至该月最后一天。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DatePickerMode-MONTH_AND_DAY = 2--><!--Device-DatePickerMode-MONTH_AND_DAY = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

