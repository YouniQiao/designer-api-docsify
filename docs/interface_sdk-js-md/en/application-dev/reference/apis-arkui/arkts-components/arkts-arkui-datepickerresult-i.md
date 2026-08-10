# DatePickerResult

日期选择器返回的时间格式。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface DatePickerResult--><!--Device-unnamed-declare interface DatePickerResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## day

```TypeScript
day?: number
```

选中日期的日。

取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[1, 31]。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DatePickerResult-day?: number--><!--Device-DatePickerResult-day?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## month

```TypeScript
month?: number
```

选中日期的月的索引值，索引从0开始，0表示1月，11表示12月。

取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[0, 11]。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DatePickerResult-month?: number--><!--Device-DatePickerResult-month?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## year

```TypeScript
year?: number
```

选中日期的年。

取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[1970, 2100]。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DatePickerResult-year?: number--><!--Device-DatePickerResult-year?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

