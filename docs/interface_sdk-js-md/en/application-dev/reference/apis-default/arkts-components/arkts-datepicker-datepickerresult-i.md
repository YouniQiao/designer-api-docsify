# DatePickerResult

Defines the struct of DatePickerResult.

@interface DatePickerResult

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface DatePickerResult--><!--Device-unnamed-export declare interface DatePickerResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## day

```TypeScript
day?: int
```

Day of the selected date.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Value range: depends on start and end. If start and end are not set, the default range is [1, 31]. &lt;/p&gt;

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerResult-day?: int--><!--Device-DatePickerResult-day?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## month

```TypeScript
month?: int
```

Month index of the selected date. The index is zero-based. 0 indicates January, and 11 indicates December.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Value range: depends on start and end. If start and end are not set, the default range is [0, 11]. &lt;/p&gt;

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerResult-month?: int--><!--Device-DatePickerResult-month?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## year

```TypeScript
year?: int
```

Year of the selected date.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Value range: depends on start and end. If start and end are not set, the default range is [1970, 2100]. &lt;/p&gt;

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerResult-year?: int--><!--Device-DatePickerResult-year?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

