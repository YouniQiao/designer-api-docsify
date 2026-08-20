# Locale

用于区域相关操作的Locale类。

**继承/实现关系：** Locale implements [LocaleOptions](arkts-arkts-intl-localeoptions-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class Locale--><!--Device-Intl-export class Locale-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)
```

创建新的Locale。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)--><!--Device-Locale-public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tag | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| Locale | 是 | 标签。 |
| options | LocaleOptions | 否 | 选项。 |

## defaultTag

```TypeScript
public static defaultTag(): string
```

获取默认标签。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public static defaultTag(): string--><!--Device-Locale-public static defaultTag(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 默认标签。 |

## initLocale

```TypeScript
public initLocale(): void
```

初始化区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public initLocale(): void--><!--Device-Locale-public initLocale(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## isTagValid

```TypeScript
public isTagValid(tag: string): int
```

检查标签是否合法。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public isTagValid(tag: string): int--><!--Device-Locale-public isTagValid(tag: string): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tag | string | 是 | 标签。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 合法时返回1，否则返回0。 |

## langList

```TypeScript
public langList(): string
```

获取语言列表。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public langList(): string--><!--Device-Locale-public langList(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 语言列表。 |

## maximize

```TypeScript
public maximize(): Locale
```

获取语言、文字和地区最可能的取值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public maximize(): Locale--><!--Device-Locale-public maximize(): Locale-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Locale | 信息补全后的区域设置。 |

## maximizeInfo

```TypeScript
public maximizeInfo(lang: string): string
```

补全区域设置信息。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public maximizeInfo(lang: string): string--><!--Device-Locale-public maximizeInfo(lang: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lang | string | 是 | 语言。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 补全后的信息。 |

## minimize

```TypeScript
public minimize(): Locale
```

移除maximize()会补全的信息。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public minimize(): Locale--><!--Device-Locale-public minimize(): Locale-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Locale | 信息精简后的区域设置。 |

## numberingSystemList

```TypeScript
public numberingSystemList(): string
```

获取记数系统列表。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public numberingSystemList(): string--><!--Device-Locale-public numberingSystemList(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 记数系统列表。 |

## parseTagImpl

```TypeScript
public parseTagImpl(tag: string): string
```

解析标签。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public parseTagImpl(tag: string): string--><!--Device-Locale-public parseTagImpl(tag: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tag | string | 是 | 标签。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 解析得到的标签。 |

## regionList

```TypeScript
public regionList(): string
```

获取地区列表。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public regionList(): string--><!--Device-Locale-public regionList(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 地区列表。 |

## scriptList

```TypeScript
public scriptList(): string
```

获取文字列表。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public scriptList(): string--><!--Device-Locale-public scriptList(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 文字列表。 |

## toString

```TypeScript
public toString(): BCP47LanguageTag
```

返回完整的区域设置标识符字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public toString(): BCP47LanguageTag--><!--Device-Locale-public toString(): BCP47LanguageTag-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) | 区域设置标识符。 |

