# NumberFormat

NumberFormat class for locale-sensitive number formatting.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[], options?: NumberFormatOptions)
```

Creates a new NumberFormat.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | [Intl.BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [Intl.BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | No |
| options | [NumberFormatOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-call-numberformatoptions-i.md) | No |

## format

```TypeScript
public format(value: long): string
```

Formats a number.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | long | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## format

```TypeScript
public format(value: double): string
```

Formats a number.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## format

```TypeScript
public format(value: double | bigint | long): string
```

Formats a number.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| bigint \| long | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## formatRange

```TypeScript
public formatRange(start: double | bigint, end: double | bigint): string
```

Formats a range of numbers.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | double \| bigint | Yes |
| end | double \| bigint | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## formatRangeToParts

```TypeScript
public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]
```

Formats a range to parts.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | double \| bigint | Yes |
| end | double \| bigint | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [NumberRangeFormatPart](arkts-arkts-intl-numberrangeformatpart-c.md)[] |

## formatToParts

```TypeScript
public formatToParts(value: double | bigint): NumberFormatPart[]
```

Formats a number to parts.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| bigint | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [NumberFormatPart[]](arkts-arkts-intl-numberformatpart-c.md) |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedNumberFormatOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ResolvedNumberFormatOptions](arkts-arkts-intl-resolvednumberformatoptions-i.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | string \| string[] | Yes |
| options | [NumberFormatOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-call-numberformatoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string[] |
