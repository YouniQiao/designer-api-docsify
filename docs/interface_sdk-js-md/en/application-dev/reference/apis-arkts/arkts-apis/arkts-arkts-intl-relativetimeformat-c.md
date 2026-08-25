# RelativeTimeFormat

RelativeTimeFormat class for locale-sensitive relative time formatting.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(locales?: string | string[], options?: RelativeTimeFormatOptions)
```

Creates a new RelativeTimeFormat.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | string \| string[] | No |
| options | [RelativeTimeFormatOptions](arkts-arkts-intl-relativetimeformatoptions-i.md) | No |

## format

```TypeScript
public format(value: double, unit: RelativeTimeFormatUnit): string
```

Formats a relative time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |
| unit | [RelativeTimeFormatUnit](../../apis-default/arkts-apis/arkts-intl-relativetimeformatunit-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## formatToParts

```TypeScript
public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]
```

Formats a relative time to parts.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |
| unit | [RelativeTimeFormatUnit](../../apis-default/arkts-apis/arkts-intl-relativetimeformatunit-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [RelativeTimeFormatPart[]](../../apis-default/arkts-apis/arkts-intl-relativetimeformatpart-t.md) |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedRelativeTimeFormatOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ResolvedRelativeTimeFormatOptions](../../apis-default/arkts-apis/arkts-intl-resolvedrelativetimeformatoptions-i.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]
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
| options | [RelativeTimeFormatOptions](arkts-arkts-intl-relativetimeformatoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string[] |
