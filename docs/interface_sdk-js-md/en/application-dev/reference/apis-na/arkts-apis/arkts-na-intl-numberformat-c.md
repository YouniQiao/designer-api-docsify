# NumberFormat

NumberFormat class for locale-sensitive number formatting.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-Intl-export class NumberFormat--><!--Device-Intl-export class NumberFormat-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(locales?: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[], options?: NumberFormatOptions)
```

Creates a new NumberFormat.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumberFormat-public constructor(locales?: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[], options?: NumberFormatOptions)--><!--Device-NumberFormat-public constructor(locales?: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[], options?: NumberFormatOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | [Intl.BCP47LanguageTag](arkts-na-intl-bcp47languagetag-t.md) \| [Intl.BCP47LanguageTag](arkts-na-intl-bcp47languagetag-t.md)[] | No | the locales. |
| options | NumberFormatOptions | No | the options. |

## format

```TypeScript
public format(value: long): string
```

Formats a number.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumberFormat-public format(value: long): string--><!--Device-NumberFormat-public format(value: long): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | the number to format. |

**Return value:**

| Type | Description |
| --- | --- |
| string | formatted string. |

## format

```TypeScript
public format(value: double): string
```

Formats a number.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumberFormat-public format(value: double): string--><!--Device-NumberFormat-public format(value: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | the number to format. |

**Return value:**

| Type | Description |
| --- | --- |
| string | formatted string. |

## format

```TypeScript
public format(value: double | bigint | long): string
```

Formats a number.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumberFormat-public format(value: double | bigint | long): string--><!--Device-NumberFormat-public format(value: double | bigint | long): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| bigint \| long | Yes | the number to format. |

**Return value:**

| Type | Description |
| --- | --- |
| string | formatted string. |

## formatRange

```TypeScript
public formatRange(start: double | bigint, end: double | bigint): string
```

Formats a range of numbers.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumberFormat-public formatRange(start: double | bigint, end: double | bigint): string--><!--Device-NumberFormat-public formatRange(start: double | bigint, end: double | bigint): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | double \| bigint | Yes | start of range. |
| end | double \| bigint | Yes | end of range. |

**Return value:**

| Type | Description |
| --- | --- |
| string | formatted range string. |

## formatRangeToParts

```TypeScript
public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]
```

Formats a range to parts.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumberFormat-public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]--><!--Device-NumberFormat-public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | double \| bigint | Yes | start of range. |
| end | double \| bigint | Yes | end of range. |

**Return value:**

| Type | Description |
| --- | --- |
| [NumberRangeFormatPart](arkts-na-intl-numberrangeformatpart-c.md)[] | formatted range parts. |

## formatToParts

```TypeScript
public formatToParts(value: double | bigint): NumberFormatPart[]
```

Formats a number to parts.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumberFormat-public formatToParts(value: double | bigint): NumberFormatPart[]--><!--Device-NumberFormat-public formatToParts(value: double | bigint): NumberFormatPart[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| bigint | Yes | the number to format. |

**Return value:**

| Type | Description |
| --- | --- |
| NumberFormatPart[] | formatted parts. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedNumberFormatOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumberFormat-public resolvedOptions(): ResolvedNumberFormatOptions--><!--Device-NumberFormat-public resolvedOptions(): ResolvedNumberFormatOptions-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| ResolvedNumberFormatOptions | the resolved options. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumberFormat-public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]--><!--Device-NumberFormat-public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| string[] | Yes | the locales. |
| options | NumberFormatOptions | No | the options. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | supported locales. |

