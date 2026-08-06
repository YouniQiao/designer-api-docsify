# StyledNumberFormat

Provide a number formatting interface which could format number to StyleString.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class StyledNumberFormat--><!--Device-i18n-export class StyledNumberFormat-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)
```

A constructor used to create a StyledNumberFormat object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-StyledNumberFormat-constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)--><!--Device-StyledNumberFormat-constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| numberFormat | Intl.NumberFormat \| SimpleNumberFormat | Yes | Indicates the number format object that used to format number. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Indicates the options used to format the number. |

## format

```TypeScript
format(value: double): StyledString
```

Formats a number as a rich text object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-StyledNumberFormat-format(value: double): StyledString--><!--Device-StyledNumberFormat-format(value: double): StyledString-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | Number to be formatted. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Rich text object after formatting. |

