# DateTimeFormat

Date time format class for locale-sensitive date formatting.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-Intl-export class DateTimeFormat--><!--Device-Intl-export class DateTimeFormat-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: DateTimeFormatOptions)
```

Creates a new DateTimeFormat.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateTimeFormat-public constructor(locales?: string | string[], options?: DateTimeFormatOptions)--><!--Device-DateTimeFormat-public constructor(locales?: string | string[], options?: DateTimeFormatOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| string[] | No | the locales. |
| options | DateTimeFormatOptions | No | the options. |

## format

```TypeScript
public format(date?: Date | double): string
```

Formats a date.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateTimeFormat-public format(date?: Date | double): string--><!--Device-DateTimeFormat-public format(date?: Date | double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date \| double | No | the date to format. |

**Return value:**

| Type | Description |
| --- | --- |
| string | formatted date string. |

## formatRange

```TypeScript
public formatRange(startDate: Date | double, endDate: Date | double): string
```

Formats a date range.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateTimeFormat-public formatRange(startDate: Date | double, endDate: Date | double): string--><!--Device-DateTimeFormat-public formatRange(startDate: Date | double, endDate: Date | double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startDate | Date \| double | Yes | start date. |
| endDate | Date \| double | Yes | end date. |

**Return value:**

| Type | Description |
| --- | --- |
| string | formatted range string. |

## formatRangeToParts

```TypeScript
public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]
```

Formats a date range to parts.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateTimeFormat-public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]--><!--Device-DateTimeFormat-public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startDate | Date \| double | Yes | start date. |
| endDate | Date \| double | Yes | end date. |

**Return value:**

| Type | Description |
| --- | --- |
| DateTimeRangeFormatPart[] | formatted range parts. |

## formatToParts

```TypeScript
public formatToParts(date?: Date | double): DateTimeFormatPart[]
```

Formats a date to parts.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateTimeFormat-public formatToParts(date?: Date | double): DateTimeFormatPart[]--><!--Device-DateTimeFormat-public formatToParts(date?: Date | double): DateTimeFormatPart[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date \| double | No | the date to format. |

**Return value:**

| Type | Description |
| --- | --- |
| DateTimeFormatPart[] | formatted parts. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedDateTimeFormatOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateTimeFormat-public resolvedOptions(): ResolvedDateTimeFormatOptions--><!--Device-DateTimeFormat-public resolvedOptions(): ResolvedDateTimeFormatOptions-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| ResolvedDateTimeFormatOptions | the resolved options. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>, 
            options?: DateTimeFormatOptions): string[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateTimeFormat-public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>,             options?: DateTimeFormatOptions): string[]--><!--Device-DateTimeFormat-public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>,             options?: DateTimeFormatOptions): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| Locale \| ReadonlyArray&lt;string \| Locale&gt; | Yes | the locales. |
| options | DateTimeFormatOptions | No | the options. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | supported locales. |

