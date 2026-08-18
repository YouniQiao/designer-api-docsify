# PluralRules

PluralRules class for locale-sensitive plural formatting.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-Intl-export class PluralRules--><!--Device-Intl-export class PluralRules-End-->

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PluralRules-public constructor(locales?: string | FixedArray<string>, options?: PluralRulesOptions)--><!--Device-PluralRules-public constructor(locales?: string | FixedArray<string>, options?: PluralRulesOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| FixedArray&lt;string&gt; | No | the locales. |
| options | PluralRulesOptions | No | the options. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedPluralRulesOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PluralRules-public resolvedOptions(): ResolvedPluralRulesOptions--><!--Device-PluralRules-public resolvedOptions(): ResolvedPluralRulesOptions-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| ResolvedPluralRulesOptions | the resolved options. |

## select

```TypeScript
public select(value: double): LDMLPluralRule
```

Selects a plural rule category.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PluralRules-public select(value: double): LDMLPluralRule--><!--Device-PluralRules-public select(value: double): LDMLPluralRule-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | the value. |

**Return value:**

| Type | Description |
| --- | --- |
| LDMLPluralRule | the plural rule. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>, 
            options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PluralRules-public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>,             options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]--><!--Device-PluralRules-public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>,             options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| FixedArray&lt;string&gt; \| Array&lt;string&gt; | Yes | the locales. |
| options | [SupportedLocalesOfOptions](arkts-na-intl-supportedlocalesofoptions-i.md) \| PluralRulesOptions | No | the options. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | supported locales. |

