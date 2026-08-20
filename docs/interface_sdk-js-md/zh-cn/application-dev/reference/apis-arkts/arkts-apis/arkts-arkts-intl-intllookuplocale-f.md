# intlLookUpLocale

## 导入模块

```TypeScript
```

## intlLookUpLocale

```TypeScript
export function intlLookUpLocale(locale: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[]): string
```

从给定的语言标签中查找区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Intl-export function intlLookUpLocale(locale: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[]): string--><!--Device-Intl-export function intlLookUpLocale(locale: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[]): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | [Intl.BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [Intl.BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | 是 | 区域设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 解析得到的区域设置。 |

