# DateTimeFormat

Date time format class for locale-sensitive date formatting.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class DateTimeFormat--><!--Device-Intl-export class DateTimeFormat-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: DateTimeFormatOptions)
```

Creates a new DateTimeFormat.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public constructor(locales?: string | string[], options?: DateTimeFormatOptions)--><!--Device-DateTimeFormat-public constructor(locales?: string | string[], options?: DateTimeFormatOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 否 | the locales. |
| options | [DateTimeFormatOptions](arkts-arkts-intl-datetimeformatoptions-i.md) | 否 | the options. |

## format

```TypeScript
public format(date?: Date | double): string
```

Formats a date.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public format(date?: Date | double): string--><!--Device-DateTimeFormat-public format(date?: Date | double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | Date \| double | 否 | the date to format. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | formatted date string. |

## formatRange

```TypeScript
public formatRange(startDate: Date | double, endDate: Date | double): string
```

Formats a date range.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public formatRange(startDate: Date | double, endDate: Date | double): string--><!--Device-DateTimeFormat-public formatRange(startDate: Date | double, endDate: Date | double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startDate | Date \| double | 是 | start date. |
| endDate | Date \| double | 是 | end date. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | formatted range string. |

## formatRangeToParts

```TypeScript
public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]
```

Formats a date range to parts.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]--><!--Device-DateTimeFormat-public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startDate | Date \| double | 是 | start date. |
| endDate | Date \| double | 是 | end date. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DateTimeRangeFormatPart](arkts-arkts-intl-datetimerangeformatpart-i.md)[] | formatted range parts. |

## formatToParts

```TypeScript
public formatToParts(date?: Date | double): DateTimeFormatPart[]
```

Formats a date to parts.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public formatToParts(date?: Date | double): DateTimeFormatPart[]--><!--Device-DateTimeFormat-public formatToParts(date?: Date | double): DateTimeFormatPart[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | Date \| double | 否 | the date to format. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DateTimeFormatPart](arkts-arkts-intl-datetimeformatpart-i.md)[] | formatted parts. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedDateTimeFormatOptions
```

Returns resolved options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public resolvedOptions(): ResolvedDateTimeFormatOptions--><!--Device-DateTimeFormat-public resolvedOptions(): ResolvedDateTimeFormatOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedDateTimeFormatOptions](arkts-arkts-intl-resolveddatetimeformatoptions-i.md) | the resolved options. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>, 
            options?: DateTimeFormatOptions): string[]
```

Returns supported locales.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>,             options?: DateTimeFormatOptions): string[]--><!--Device-DateTimeFormat-public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>,             options?: DateTimeFormatOptions): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| Locale \| ReadonlyArray&lt;string \| Locale&gt; | 是 | the locales. |
| options | [DateTimeFormatOptions](arkts-arkts-intl-datetimeformatoptions-i.md) | 否 | the options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | supported locales. |

