# DateMode

DateMode枚举用于定义日期选择器的模式。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare enum DateMode--><!--Device-unnamed-export declare enum DateMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DATE

```TypeScript
DATE = 0
```

日期显示三列：年、月、日。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateMode-DATE = 0--><!--Device-DateMode-DATE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## YEAR_AND_MONTH

```TypeScript
YEAR_AND_MONTH = 1
```

日期显示两列：年、月。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateMode-YEAR_AND_MONTH = 1--><!--Device-DateMode-YEAR_AND_MONTH = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MONTH_AND_DAY

```TypeScript
MONTH_AND_DAY = 2
```

定义以月和日显示日期的模式。在此模式下，当月份从12月变为1月时，年份不会增加；当月份从1月变为12月时，年份不会减少。年份保持当前设置的值不变。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateMode-MONTH_AND_DAY = 2--><!--Device-DateMode-MONTH_AND_DAY = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

