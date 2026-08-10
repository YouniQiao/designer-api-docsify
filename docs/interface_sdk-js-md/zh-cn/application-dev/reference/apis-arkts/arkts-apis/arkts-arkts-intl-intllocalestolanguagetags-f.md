# intlLocalesToLanguageTags

## intlLocalesToLanguageTags

```TypeScript
export function intlLocalesToLanguageTags(locales: string | Intl.Locale | ReadonlyArray<string | Intl.Locale> | 
        undefined): string[]
```

Converts locales to language tags.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Intl-export function intlLocalesToLanguageTags(locales: string | Intl.Locale | ReadonlyArray<string | Intl.Locale> |         undefined): string[]--><!--Device-Intl-export function intlLocalesToLanguageTags(locales: string | Intl.Locale | ReadonlyArray<string | Intl.Locale> |         undefined): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| Intl.Locale \| ReadonlyArray&lt;string \| Intl.Locale&gt; \| undefined | 是 | the locales. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | the language tags. |

