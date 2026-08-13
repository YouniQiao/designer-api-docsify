# SymbolDateTimeFormat

Provide a DateTime formatting interface that supports custom symbols. This interface formats date time values into strings with custom symbols, and can replace variable symbols in the formatted result with custom fixed symbols (e.g., replacing "2:23 PM" with "2:23 afternoon").

**Inheritance/Implementation:** SymbolDateTimeFormat extends Intl.DateTimeFormat

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-i18n-export class SymbolDateTimeFormat--><!--Device-i18n-export class SymbolDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
public constructor(locale?: Intl.Locale, options?: SymbolDateTimeFormatOptions)
```

A constructor used to create a SymbolDateTimeFormat object.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public constructor(locale?: Intl.Locale, options?: SymbolDateTimeFormatOptions)--><!--Device-SymbolDateTimeFormat-public constructor(locale?: Intl.Locale, options?: SymbolDateTimeFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | Intl.Locale | No |
| options | [SymbolDateTimeFormatOptions](arkts-localization-i18n-symboldatetimeformatoptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-parameter-verification-error) |

## format

```TypeScript
public format(date?: Date | number): string
```

Formats the date and time.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public format(date?: Date | number): string--><!--Device-SymbolDateTimeFormat-public format(date?: Date | number): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | Date \| number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## formatRange

```TypeScript
public formatRange(startDate: Date | number | bigint, endDate: Date | number | bigint): string
```

Formats date and time ranges.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public formatRange(startDate: Date | number | bigint, endDate: Date | number | bigint): string--><!--Device-SymbolDateTimeFormat-public formatRange(startDate: Date | number | bigint, endDate: Date | number | bigint): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startDate | Date \| number \| bigint | Yes |
| endDate | Date \| number \| bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## formatRangeToParts

```TypeScript
public formatRangeToParts(startDate: Date | number | bigint, endDate: Date | number | bigint):
      Intl.DateTimeRangeFormatPart[]
```

Formats a date time range to Parts.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public formatRangeToParts(startDate: Date | number | bigint, endDate: Date | number | bigint):      Intl.DateTimeRangeFormatPart[]--><!--Device-SymbolDateTimeFormat-public formatRangeToParts(startDate: Date | number | bigint, endDate: Date | number | bigint):      Intl.DateTimeRangeFormatPart[]-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startDate | Date \| number \| bigint | Yes |
| endDate | Date \| number \| bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Intl.DateTimeRangeFormatPart[] |

## formatToParts

```TypeScript
public formatToParts(date?: Date | number): Intl.DateTimeFormatPart[]
```

Formats a date to parts.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public formatToParts(date?: Date | number): Intl.DateTimeFormatPart[]--><!--Device-SymbolDateTimeFormat-public formatToParts(date?: Date | number): Intl.DateTimeFormatPart[]-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | Date \| number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Intl.DateTimeFormatPart[] |

## parse

```TypeScript
public parse(text: string, lenientMode: boolean): number
```

Parse a date time localized string to Unix timestamp. Unix timestamp, indicating the number of milliseconds elapsed since 00:00:00 on January 1, 1970 GMT.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public parse(text: string, lenientMode: boolean): number--><!--Device-SymbolDateTimeFormat-public parse(text: string, lenientMode: boolean): number-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| lenientMode | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-parameter-verification-error) |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions
```

Obtains the options for creating a SymbolDateTimeFormat object. This will allow us to check the current config symbols.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions--><!--Device-SymbolDateTimeFormat-public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ResolvedSymbolDateTimeFormatOptions](arkts-localization-i18n-resolvedsymboldatetimeformatoptions-i.md) |
