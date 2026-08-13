# AdvancedMeasureFormat

Provides the number formatting capability, supporting automatic unit conversion based on specific application scenarios.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-i18n-export class AdvancedMeasureFormat--><!--Device-i18n-export class AdvancedMeasureFormat-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(numberFormat: Intl.NumberFormat, options?: AdvancedMeasureFormatOptions)
```

A constructor used to create an AdvancedMeasureFormat object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AdvancedMeasureFormat-constructor(numberFormat: Intl.NumberFormat, options?: AdvancedMeasureFormatOptions)--><!--Device-AdvancedMeasureFormat-constructor(numberFormat: Intl.NumberFormat, options?: AdvancedMeasureFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| numberFormat | Intl.NumberFormat | Yes | Indicates the number format object that used to format number. |
| options | [AdvancedMeasureFormatOptions](arkts-na-i18n-advancedmeasureformatoptions-i.md) | No |  |

## format

```TypeScript
format(num: double): string
```

Formats a number by appropriate measure for usage scenarios. For instance, when formatting the value 12.3 for rainfall in the English locale, the output is "12.3 mm".

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AdvancedMeasureFormat-format(num: double): string--><!--Device-AdvancedMeasureFormat-format(num: double): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| num | double | Yes | number to be formatted. |

**Return value:**

| Type | Description |
| --- | --- |
| string | measure formatting result. |

