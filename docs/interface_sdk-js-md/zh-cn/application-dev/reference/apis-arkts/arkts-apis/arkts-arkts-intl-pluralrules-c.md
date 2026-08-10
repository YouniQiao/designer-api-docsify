# PluralRules

PluralRules class for locale-sensitive plural formatting.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class PluralRules--><!--Device-Intl-export class PluralRules-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(locales?: string | FixedArray<string>, options?: PluralRulesOptions)
```

Creates a new PluralRules.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PluralRules-public constructor(locales?: string | FixedArray<string>, options?: PluralRulesOptions)--><!--Device-PluralRules-public constructor(locales?: string | FixedArray<string>, options?: PluralRulesOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| FixedArray&lt;string&gt; | 否 | the locales. |
| options | [PluralRulesOptions](arkts-arkts-intl-pluralrulesoptions-i.md) | 否 | the options. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedPluralRulesOptions
```

Returns resolved options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PluralRules-public resolvedOptions(): ResolvedPluralRulesOptions--><!--Device-PluralRules-public resolvedOptions(): ResolvedPluralRulesOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedPluralRulesOptions](arkts-arkts-intl-resolvedpluralrulesoptions-i.md) | the resolved options. |

## select

```TypeScript
public select(value: double): LDMLPluralRule
```

Selects a plural rule category.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PluralRules-public select(value: double): LDMLPluralRule--><!--Device-PluralRules-public select(value: double): LDMLPluralRule-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | the value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LDMLPluralRule](arkts-arkts-intl-ldmlpluralrule-t.md) | the plural rule. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>, 
            options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]
```

Returns supported locales.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PluralRules-public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>,             options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]--><!--Device-PluralRules-public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>,             options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| FixedArray&lt;string&gt; \| Array&lt;string&gt; | 是 | the locales. |
| options | [SupportedLocalesOfOptions](arkts-arkts-intl-supportedlocalesofoptions-i.md) \| PluralRulesOptions | 否 | the options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | supported locales. |

