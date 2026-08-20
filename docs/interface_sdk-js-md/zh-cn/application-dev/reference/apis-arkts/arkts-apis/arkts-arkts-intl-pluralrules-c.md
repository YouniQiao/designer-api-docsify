# PluralRules

用于按区域设置处理复数形式的PluralRules类。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class PluralRules--><!--Device-Intl-export class PluralRules-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: string | FixedArray<string>, options?: PluralRulesOptions)
```

创建新的PluralRules。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PluralRules-public constructor(locales?: string | FixedArray<string>, options?: PluralRulesOptions)--><!--Device-PluralRules-public constructor(locales?: string | FixedArray<string>, options?: PluralRulesOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| FixedArray&lt;string&gt; | 否 | 区域设置。 |
| options | PluralRulesOptions | 否 | 选项。 |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedPluralRulesOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PluralRules-public resolvedOptions(): ResolvedPluralRulesOptions--><!--Device-PluralRules-public resolvedOptions(): ResolvedPluralRulesOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedPluralRulesOptions](arkts-arkts-intl-resolvedpluralrulesoptions-i.md) | 解析后的选项。 |

## select

```TypeScript
public select(value: double): LDMLPluralRule
```

选择复数规则类别。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PluralRules-public select(value: double): LDMLPluralRule--><!--Device-PluralRules-public select(value: double): LDMLPluralRule-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LDMLPluralRule](arkts-arkts-intl-ldmlpluralrule-t.md) | 复数规则类别。 |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>, 
            options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PluralRules-public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>,             options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]--><!--Device-PluralRules-public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>,             options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| FixedArray&lt;string&gt; \| Array&lt;string&gt; | 是 | 区域设置。 |
| options | [SupportedLocalesOfOptions](arkts-arkts-intl-supportedlocalesofoptions-i.md) \| PluralRulesOptions | 否 | 选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 支持的区域设置。 |

