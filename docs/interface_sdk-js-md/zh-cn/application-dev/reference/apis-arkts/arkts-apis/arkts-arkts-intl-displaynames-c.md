# DisplayNames

用于按区域设置展示名称的DisplayNames类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: DisplayNamesOptions)
```

创建新的DisplayNames。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | 否 |
| options | [DisplayNamesOptions](arkts-arkts-intl-displaynamesoptions-i.md) | 否 |

## of

```TypeScript
public of(code: string): string | undefined
```

返回给定代码的本地化展示名称。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | string | 是 |

**返回值：**

| 类型 |
| --- |
| string \| undefined |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedDisplayNamesOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ResolvedDisplayNamesOptions](arkts-arkts-intl-resolveddisplaynamesoptions-i.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | Locale | FixedArray<string | Locale>): string[]
```

返回支持的区域设置数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | string \| Locale \| FixedArray & lt;string \ | Locale & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string[] |
