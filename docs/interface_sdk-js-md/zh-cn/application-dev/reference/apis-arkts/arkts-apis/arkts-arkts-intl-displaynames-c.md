# DisplayNames

DisplayNames class for locale-sensitive name display.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class DisplayNames--><!--Device-Intl-export class DisplayNames-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: DisplayNamesOptions)
```

Creates a new DisplayNames.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DisplayNames-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: DisplayNamesOptions)--><!--Device-DisplayNames-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: DisplayNamesOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| BCP47LanguageTag[] | 否 | the locales. |
| options | [DisplayNamesOptions](arkts-arkts-intl-displaynamesoptions-i.md) | 否 | the options. |

## of

```TypeScript
public of(code: string): string | undefined
```

Returns the localized display name for the provided code.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DisplayNames-public of(code: string): string | undefined--><!--Device-DisplayNames-public of(code: string): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | string | 是 | the code to get display name for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the display name. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedDisplayNamesOptions
```

Returns the resolved options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DisplayNames-public resolvedOptions(): ResolvedDisplayNamesOptions--><!--Device-DisplayNames-public resolvedOptions(): ResolvedDisplayNamesOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedDisplayNamesOptions](arkts-arkts-intl-resolveddisplaynamesoptions-i.md) | the resolved options. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | Locale | FixedArray<string | Locale>): string[]
```

Returns an array of supported locales.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DisplayNames-public static supportedLocalesOf(locales: string | Locale | FixedArray<string | Locale>): string[]--><!--Device-DisplayNames-public static supportedLocalesOf(locales: string | Locale | FixedArray<string | Locale>): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| Locale \| FixedArray&lt;string \| Locale&gt; | 是 | the locales. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | supported locales. |

