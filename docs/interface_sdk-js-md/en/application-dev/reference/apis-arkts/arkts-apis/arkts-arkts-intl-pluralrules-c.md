# PluralRules

PluralRules class for locale-sensitive plural formatting.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: string | FixedArray<string>, options?: PluralRulesOptions)
```

Creates a new PluralRules.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | string \| FixedArray & lt;string & gt; | No |
| options | [PluralRulesOptions](arkts-arkts-intl-pluralrulesoptions-i.md) | No |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedPluralRulesOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ResolvedPluralRulesOptions](arkts-arkts-intl-resolvedpluralrulesoptions-i.md) |

## select

```TypeScript
public select(value: double): LDMLPluralRule
```

Selects a plural rule category.

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
| [LDMLPluralRule](arkts-arkts-intl-ldmlpluralrule-t.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>, 
            options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | string \| FixedArray & lt;string & gt; \ | Array & lt;string & gt; | Yes |
| options | [SupportedLocalesOfOptions](arkts-arkts-intl-supportedlocalesofoptions-i.md) \| [PluralRulesOptions](arkts-arkts-intl-pluralrulesoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string[] |
