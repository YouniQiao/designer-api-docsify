# DisplayNames

用于按区域设置展示名称的DisplayNames类。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class DisplayNames--><!--Device-Intl-export class DisplayNames-End-->

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DisplayNames-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: DisplayNamesOptions)--><!--Device-DisplayNames-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: DisplayNamesOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | 否 | 区域设置。 |
| options | [DisplayNamesOptions](arkts-arkts-intl-displaynamesoptions-i.md) | 否 | 选项。 |

## of

```TypeScript
public of(code: string): string | undefined
```

返回给定代码的本地化展示名称。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DisplayNames-public of(code: string): string | undefined--><!--Device-DisplayNames-public of(code: string): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | string | 是 | 待获取展示名称的代码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string \| undefined | 展示名称。 |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedDisplayNamesOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DisplayNames-public resolvedOptions(): ResolvedDisplayNamesOptions--><!--Device-DisplayNames-public resolvedOptions(): ResolvedDisplayNamesOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedDisplayNamesOptions](arkts-arkts-intl-resolveddisplaynamesoptions-i.md) | 解析后的选项。 |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | Locale | FixedArray<string | Locale>): string[]
```

返回支持的区域设置数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DisplayNames-public static supportedLocalesOf(locales: string | Locale | FixedArray<string | Locale>): string[]--><!--Device-DisplayNames-public static supportedLocalesOf(locales: string | Locale | FixedArray<string | Locale>): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| Locale \| FixedArray&lt;string \| Locale&gt; | 是 | 区域设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 支持的区域设置。 |

