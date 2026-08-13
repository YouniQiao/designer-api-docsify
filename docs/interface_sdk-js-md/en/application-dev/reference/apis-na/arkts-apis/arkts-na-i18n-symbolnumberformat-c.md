# SymbolNumberFormat

Provide a Number formatting interface that supports custom symbols. This interface formats number values into strings with custom symbols, and can replace variable symbols in the formatted result with custom fixed symbols (e.g., replacing "null" to "NA").

**Inheritance/Implementation:** SymbolNumberFormat extends Intl.NumberFormat

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-i18n-export class SymbolNumberFormat--><!--Device-i18n-export class SymbolNumberFormat-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)
```

A constructor used to create a SymbolNumberFormat object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)--><!--Device-SymbolNumberFormat-public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | Intl.Locale | No | Locale object used for formatting the date time value. The default value is the current system locale. |
| options | [SymbolNumberFormatOptions](arkts-na-i18n-symbolnumberformatoptions-i.md) | No | Indicates the symbols used to replace. Such as zero, nan, positiveInfinity, etc. |

## parse

```TypeScript
public parse(text: string, lenientMode: boolean): double
```

Parse a localized string to number object. For example, "123,456" will parse to 123456.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public parse(text: string, lenientMode: boolean): double--><!--Device-SymbolNumberFormat-public parse(text: string, lenientMode: boolean): double-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Localized string to be parse. &lt;br&gt;Text to be parsed |
| lenientMode | boolean | Yes | Indicates whether parsing allows any non-compliant localized strings. For example, "1,23,456" is a invalid thousand separator number string, it will parse failure when lenientMode is false, and will parse success with value 123456 when lenientMode is true.it's better set to false, ensure the data is not polluted. &lt;br&gt;Whether to use loose rules |

**Return value:**

| Type | Description |
| --- | --- |
| double | The result parse with localization rules. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../../apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSymbolNumberFormatOptions
```

Represents optional element for the ResolvedSymbolDateTimeFormatOptions object. Define the resolved symbol element and value that need to get.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public resolvedOptions(): ResolvedSymbolNumberFormatOptions--><!--Device-SymbolNumberFormat-public resolvedOptions(): ResolvedSymbolNumberFormatOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [ResolvedSymbolNumberFormatOptions](arkts-na-i18n-resolvedsymbolnumberformatoptions-i.md) | Symbol options for SymbolNumberFormat. |

