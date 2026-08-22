# intlLocalesToLanguageTags

## 导入模块

```TypeScript
```

## intlLocalesToLanguageTags

```TypeScript
export function intlLocalesToLanguageTags(locales: string | Intl.Locale | ReadonlyArray<string | Intl.Locale> | 
        undefined): string[]
```

将区域设置转换为语言标签。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Intl-export function intlLocalesToLanguageTags(locales: string | Intl.Locale | ReadonlyArray<string | Intl.Locale> |         undefined): string[]--><!--Device-Intl-export function intlLocalesToLanguageTags(locales: string | Intl.Locale | ReadonlyArray<string | Intl.Locale> |         undefined): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| [Intl.Locale](arkts-arkts-intl-locale-c.md) \| [ReadonlyArray](arkts-arkts-readonlyarray-i.md)&lt;string \| [Intl.Locale](arkts-arkts-intl-locale-c.md)&gt; \| undefined | 是 | 区域设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 语言标签。 |

