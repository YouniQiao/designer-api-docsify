# intlBestFitLocales

## intlBestFitLocales

```TypeScript
export function intlBestFitLocales(locale: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[]): string[]
```

Gets the best fit locales from the given language tags.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Intl-export function intlBestFitLocales(locale: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[]): string[]--><!--Device-Intl-export function intlBestFitLocales(locale: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[]): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | Intl.BCP47LanguageTag \| Intl.BCP47LanguageTag[] | 是 | the locales. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | the best fit locales. |

