# NumberFormat

用于按区域设置格式化数字的NumberFormat类。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class NumberFormat--><!--Device-Intl-export class NumberFormat-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[], options?: NumberFormatOptions)
```

创建新的NumberFormat。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public constructor(locales?: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[], options?: NumberFormatOptions)--><!--Device-NumberFormat-public constructor(locales?: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[], options?: NumberFormatOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | [Intl.BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [Intl.BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | 否 | 区域设置。 |
| options | NumberFormatOptions | 否 | 选项。 |

## format

```TypeScript
public format(value: long): string
```

格式化数值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public format(value: long): string--><!--Device-NumberFormat-public format(value: long): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 待格式化的数值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的字符串。 |

## format

```TypeScript
public format(value: double): string
```

格式化数值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public format(value: double): string--><!--Device-NumberFormat-public format(value: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 待格式化的数值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的字符串。 |

## format

```TypeScript
public format(value: double | bigint | long): string
```

格式化数值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public format(value: double | bigint | long): string--><!--Device-NumberFormat-public format(value: double | bigint | long): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| bigint \| long | 是 | 待格式化的数值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的字符串。 |

## formatRange

```TypeScript
public formatRange(start: double | bigint, end: double | bigint): string
```

格式化数值区间。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public formatRange(start: double | bigint, end: double | bigint): string--><!--Device-NumberFormat-public formatRange(start: double | bigint, end: double | bigint): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | double \| bigint | 是 | 区间起始值。 |
| end | double \| bigint | 是 | 区间结束值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的区间字符串。 |

## formatRangeToParts

```TypeScript
public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]
```

将区间格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]--><!--Device-NumberFormat-public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | double \| bigint | 是 | 区间起始值。 |
| end | double \| bigint | 是 | 区间结束值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NumberRangeFormatPart](arkts-arkts-intl-numberrangeformatpart-c.md)[] | 格式化后的区间各片段。 |

## formatToParts

```TypeScript
public formatToParts(value: double | bigint): NumberFormatPart[]
```

将数值格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public formatToParts(value: double | bigint): NumberFormatPart[]--><!--Device-NumberFormat-public formatToParts(value: double | bigint): NumberFormatPart[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| bigint | 是 | 待格式化的数值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NumberFormatPart](arkts-arkts-intl-numberformatpart-c.md)[] | 格式化后的各个片段。 |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedNumberFormatOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public resolvedOptions(): ResolvedNumberFormatOptions--><!--Device-NumberFormat-public resolvedOptions(): ResolvedNumberFormatOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedNumberFormatOptions](arkts-arkts-intl-resolvednumberformatoptions-i.md) | 解析后的选项。 |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NumberFormat-public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]--><!--Device-NumberFormat-public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 是 | 区域设置。 |
| options | NumberFormatOptions | 否 | 选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 支持的区域设置。 |

