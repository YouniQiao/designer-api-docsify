# NumberFormat

NumberFormat class for locale-sensitive number formatting.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class NumberFormat--><!--Device-Intl-export class NumberFormat-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(locales?: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[], options?: NumberFormatOptions)
```

Creates a new NumberFormat.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public constructor(locales?: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[], options?: NumberFormatOptions)--><!--Device-NumberFormat-public constructor(locales?: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[], options?: NumberFormatOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.BCP47LanguageTag \| Intl.BCP47LanguageTag[] | 否 | the locales. |
| options | [NumberFormatOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-call-numberformatoptions-i.md) | 否 | the options. |

## format

```TypeScript
public format(value: long): string
```

Formats a number.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public format(value: long): string--><!--Device-NumberFormat-public format(value: long): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | the number to format. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | formatted string. |

## format

```TypeScript
public format(value: double): string
```

Formats a number.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public format(value: double): string--><!--Device-NumberFormat-public format(value: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | the number to format. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | formatted string. |

## format

```TypeScript
public format(value: double | bigint | long): string
```

Formats a number.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public format(value: double | bigint | long): string--><!--Device-NumberFormat-public format(value: double | bigint | long): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| bigint \| long | 是 | the number to format. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | formatted string. |

## formatRange

```TypeScript
public formatRange(start: double | bigint, end: double | bigint): string
```

Formats a range of numbers.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public formatRange(start: double | bigint, end: double | bigint): string--><!--Device-NumberFormat-public formatRange(start: double | bigint, end: double | bigint): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | double \| bigint | 是 | start of range. |
| end | double \| bigint | 是 | end of range. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | formatted range string. |

## formatRangeToParts

```TypeScript
public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]
```

Formats a range to parts.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]--><!--Device-NumberFormat-public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | double \| bigint | 是 | start of range. |
| end | double \| bigint | 是 | end of range. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NumberRangeFormatPart](arkts-arkts-intl-numberrangeformatpart-c.md)[] | formatted range parts. |

## formatToParts

```TypeScript
public formatToParts(value: double | bigint): NumberFormatPart[]
```

Formats a number to parts.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public formatToParts(value: double | bigint): NumberFormatPart[]--><!--Device-NumberFormat-public formatToParts(value: double | bigint): NumberFormatPart[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| bigint | 是 | the number to format. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NumberFormatPart](arkts-arkts-intl-numberformatpart-c.md)[] | formatted parts. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedNumberFormatOptions
```

Returns resolved options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public resolvedOptions(): ResolvedNumberFormatOptions--><!--Device-NumberFormat-public resolvedOptions(): ResolvedNumberFormatOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedNumberFormatOptions](arkts-arkts-intl-resolvednumberformatoptions-i.md) | the resolved options. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]
```

Returns supported locales.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]--><!--Device-NumberFormat-public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 是 | the locales. |
| options | [NumberFormatOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-call-numberformatoptions-i.md) | 否 | the options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | supported locales. |

