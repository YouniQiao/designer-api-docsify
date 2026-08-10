# DatePickerResult

日期选择器返回的时间格式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DatePickerResult--><!--Device-unnamed-export declare interface DatePickerResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## day

```TypeScript
day?: int
```

选中日期的日。

取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[1, 31]。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerResult-day?: int--><!--Device-DatePickerResult-day?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## month

```TypeScript
month?: int
```

选中日期的月的索引值，索引从0开始，0表示1月，11表示12月。

取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[0, 11]。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerResult-month?: int--><!--Device-DatePickerResult-month?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## year

```TypeScript
year?: int
```

选中日期的年。

取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[1970, 2100]。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerResult-year?: int--><!--Device-DatePickerResult-year?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

