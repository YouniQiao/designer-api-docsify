# DateTimeFormat

Date time format class for locale-sensitive date formatting.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: DateTimeFormatOptions)
```

Creates a new DateTimeFormat.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | string \| string[] | No |
| options | [DateTimeFormatOptions](arkts-arkts-intl-datetimeformatoptions-i.md) | No |

## format

```TypeScript
public format(date?: Date | double): string
```

Formats a date.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | Date \| double | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## formatRange

```TypeScript
public formatRange(startDate: Date | double, endDate: Date | double): string
```

Formats a date range.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startDate | Date \| double | Yes |
| endDate | Date \| double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## formatRangeToParts

```TypeScript
public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]
```

Formats a date range to parts.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startDate | Date \| double | Yes |
| endDate | Date \| double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [DateTimeRangeFormatPart[]](arkts-arkts-intl-datetimerangeformatpart-i.md) |

## formatToParts

```TypeScript
public formatToParts(date?: Date | double): DateTimeFormatPart[]
```

Formats a date to parts.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | Date \| double | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [DateTimeFormatPart[]](arkts-arkts-intl-datetimeformatpart-i.md) |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedDateTimeFormatOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ResolvedDateTimeFormatOptions](arkts-arkts-intl-resolveddatetimeformatoptions-i.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>, 
            options?: DateTimeFormatOptions): string[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | string \| Locale \| ReadonlyArray & lt;string \ | Locale & gt; | Yes |
| options | [DateTimeFormatOptions](arkts-arkts-intl-datetimeformatoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string[] |
