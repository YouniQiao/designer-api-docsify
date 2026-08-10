# Collator

Collator class for locale-sensitive string comparison.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class Collator--><!--Device-Intl-export class Collator-End-->

**系统能力：** SystemCapability.Utils.Lang

## compare

```TypeScript
public compare(x: string, y: string): double
```

Compares two strings.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Collator-public compare(x: string, y: string): double--><!--Device-Collator-public compare(x: string, y: string): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | string | 是 | first string to compare. |
| y | string | 是 | second string to compare. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | comparison result. |

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: CollatorOptions)
```

Creates a new Collator.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Collator-public constructor(locales?: string | string[], options?: CollatorOptions)--><!--Device-Collator-public constructor(locales?: string | string[], options?: CollatorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 否 | the locales. |
| options | [CollatorOptions](arkts-arkts-intl-collatoroptions-i.md) | 否 | the options. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedCollatorOptions
```

Returns resolved options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Collator-public resolvedOptions(): ResolvedCollatorOptions--><!--Device-Collator-public resolvedOptions(): ResolvedCollatorOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedCollatorOptions](arkts-arkts-intl-resolvedcollatoroptions-i.md) | the resolved options. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: CollatorOptions): string[]
```

Returns supported locales.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Collator-public static supportedLocalesOf(locales: string | string[], options?: CollatorOptions): string[]--><!--Device-Collator-public static supportedLocalesOf(locales: string | string[], options?: CollatorOptions): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 是 | the locales. |
| options | [CollatorOptions](arkts-arkts-intl-collatoroptions-i.md) | 否 | the options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | supported locales. |

