# SymbolDateTimeFormat

Provide a DateTime formatting interface that supports custom symbols. This interface formats date time values into strings with custom symbols, and can replace variable symbols in the formatted result with custom fixed symbols (e.g., replacing "2:23 PM" with "2:23 afternoon").

**Inheritance/Implementation:** SymbolDateTimeFormat extends Intl.DateTimeFormat

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-i18n-export class SymbolDateTimeFormat--><!--Device-i18n-export class SymbolDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
public constructor(locale?: Intl.Locale, options?: SymbolDateTimeFormatOptions)
```

A constructor used to create a SymbolDateTimeFormat object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public constructor(locale?: Intl.Locale, options?: SymbolDateTimeFormatOptions)--><!--Device-SymbolDateTimeFormat-public constructor(locale?: Intl.Locale, options?: SymbolDateTimeFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | Intl.Locale | No | Locale object used for formatting the date time value. The default value is the current system locale. |
| options | [SymbolDateTimeFormatOptions](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-symboldatetimeformatoptions-i.md) | No | Indicates the symbols used to replace. The symbols that support replacement are "AM" and "PM". |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../../apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## parse

```TypeScript
public parse(text: string, lenientMode: boolean): long
```

Parse a date time localized string to Unix timestamp. Unix timestamp, indicating the number of milliseconds elapsed since 00:00:00 on January 1, 1970 GMT.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public parse(text: string, lenientMode: boolean): long--><!--Device-SymbolDateTimeFormat-public parse(text: string, lenientMode: boolean): long-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Localized string to be parse. <br>Text to be parsed |
| lenientMode | boolean | Yes | Indicates whether parsing allows any non-compliant localized strings. For example, "2023/02-25" is a invalid separator date string, it will parse failure when lenientMode is false, and will parse success with value (2023, 02, 25) when lenientMode is true. it's better set to false, ensure the data is not polluted. <br>Whether to use loose parsing rules |

**Return value:**

| Type | Description |
| --- | --- |
| long | Unix timestamp, which indicates the number of milliseconds that have elapsed since the Unix epoch. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../../apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions
```

Obtains the options for creating a SymbolDateTimeFormat object. This will allow us to check the current config symbols.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions--><!--Device-SymbolDateTimeFormat-public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [ResolvedSymbolDateTimeFormatOptions](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-resolvedsymboldatetimeformatoptions-i.md) | Symbol options for SymbolDateTimeFormat. |

