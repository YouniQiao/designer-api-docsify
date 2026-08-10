# RelativeTimeFormat

RelativeTimeFormat class for locale-sensitive relative time formatting.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class RelativeTimeFormat--><!--Device-Intl-export class RelativeTimeFormat-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(locales?: string | string[], options?: RelativeTimeFormatOptions)
```

Creates a new RelativeTimeFormat.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RelativeTimeFormat-constructor(locales?: string | string[], options?: RelativeTimeFormatOptions)--><!--Device-RelativeTimeFormat-constructor(locales?: string | string[], options?: RelativeTimeFormatOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 否 | the locales. |
| options | [RelativeTimeFormatOptions](arkts-arkts-intl-relativetimeformatoptions-i.md) | 否 | the options. |

## format

```TypeScript
public format(value: double, unit: RelativeTimeFormatUnit): string
```

Formats a relative time.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RelativeTimeFormat-public format(value: double, unit: RelativeTimeFormatUnit): string--><!--Device-RelativeTimeFormat-public format(value: double, unit: RelativeTimeFormatUnit): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | the value. |
| unit | [RelativeTimeFormatUnit](../../apis-default/arkts-apis/arkts-intl-relativetimeformatunit-t.md) | 是 | the unit. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | formatted string. |

## formatToParts

```TypeScript
public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]
```

Formats a relative time to parts.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RelativeTimeFormat-public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]--><!--Device-RelativeTimeFormat-public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | the value. |
| unit | [RelativeTimeFormatUnit](../../apis-default/arkts-apis/arkts-intl-relativetimeformatunit-t.md) | 是 | the unit. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RelativeTimeFormatPart](../../apis-default/arkts-apis/arkts-intl-relativetimeformatpart-t.md)[] | formatted parts. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedRelativeTimeFormatOptions
```

Returns resolved options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RelativeTimeFormat-public resolvedOptions(): ResolvedRelativeTimeFormatOptions--><!--Device-RelativeTimeFormat-public resolvedOptions(): ResolvedRelativeTimeFormatOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedRelativeTimeFormatOptions](../../apis-default/arkts-apis/arkts-intl-resolvedrelativetimeformatoptions-i.md) | the resolved options. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]
```

Returns supported locales.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RelativeTimeFormat-public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]--><!--Device-RelativeTimeFormat-public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 是 | the locales. |
| options | [RelativeTimeFormatOptions](arkts-arkts-intl-relativetimeformatoptions-i.md) | 否 | the options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | supported locales. |

