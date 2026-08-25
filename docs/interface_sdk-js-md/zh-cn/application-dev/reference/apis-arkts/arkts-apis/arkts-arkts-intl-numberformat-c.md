# NumberFormat

用于按区域设置格式化数字的NumberFormat类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | [Intl.BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [Intl.BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | 否 |
| options | [NumberFormatOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-call-numberformatoptions-i.md) | 否 |

## format

```TypeScript
public format(value: long): string
```

格式化数值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## format

```TypeScript
public format(value: double): string
```

格式化数值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## format

```TypeScript
public format(value: double | bigint | long): string
```

格式化数值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| bigint \| long | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## formatRange

```TypeScript
public formatRange(start: double | bigint, end: double | bigint): string
```

格式化数值区间。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | double \| bigint | 是 |
| end | double \| bigint | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## formatRangeToParts

```TypeScript
public formatRangeToParts(start: double | bigint, end: double | bigint): NumberRangeFormatPart[]
```

将区间格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | double \| bigint | 是 |
| end | double \| bigint | 是 |

**返回值：**

| 类型 |
| --- |
| [NumberRangeFormatPart](arkts-arkts-intl-numberrangeformatpart-c.md)[] |

## formatToParts

```TypeScript
public formatToParts(value: double | bigint): NumberFormatPart[]
```

将数值格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| bigint | 是 |

**返回值：**

| 类型 |
| --- |
| [NumberFormatPart](arkts-arkts-intl-numberformatpart-c.md)[] |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedNumberFormatOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ResolvedNumberFormatOptions](arkts-arkts-intl-resolvednumberformatoptions-i.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: NumberFormatOptions): string[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | string \| string[] | 是 |
| options | [NumberFormatOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-call-numberformatoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string[] |
