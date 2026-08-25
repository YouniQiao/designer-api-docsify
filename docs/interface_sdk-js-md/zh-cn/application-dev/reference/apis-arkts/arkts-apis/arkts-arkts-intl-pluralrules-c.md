# PluralRules

用于按区域设置处理复数形式的PluralRules类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | string \| FixedArray & lt;string & gt; | 否 |
| options | [PluralRulesOptions](arkts-arkts-intl-pluralrulesoptions-i.md) | 否 |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedPluralRulesOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ResolvedPluralRulesOptions](arkts-arkts-intl-resolvedpluralrulesoptions-i.md) |

## select

```TypeScript
public select(value: double): LDMLPluralRule
```

选择复数规则类别。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double | 是 |

**返回值：**

| 类型 |
| --- |
| [LDMLPluralRule](arkts-arkts-intl-ldmlpluralrule-t.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | FixedArray<string> | Array<string>, 
            options?: SupportedLocalesOfOptions | PluralRulesOptions): string[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | string \| FixedArray & lt;string & gt; \ | Array & lt;string & gt; | 是 |
| options | [SupportedLocalesOfOptions](arkts-arkts-intl-supportedlocalesofoptions-i.md) \| [PluralRulesOptions](arkts-arkts-intl-pluralrulesoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string[] |
