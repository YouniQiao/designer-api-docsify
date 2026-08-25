# DateTimeFormat

用于按区域设置格式化日期的日期时间格式化类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: DateTimeFormatOptions)
```

创建新的DateTimeFormat。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | string \| string[] | 否 |
| options | [DateTimeFormatOptions](arkts-arkts-intl-datetimeformatoptions-i.md) | 否 |

## format

```TypeScript
public format(date?: Date | double): string
```

格式化日期。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date \| double | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## formatRange

```TypeScript
public formatRange(startDate: Date | double, endDate: Date | double): string
```

格式化日期区间。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startDate | Date \| double | 是 |
| endDate | Date \| double | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## formatRangeToParts

```TypeScript
public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]
```

将日期区间格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startDate | Date \| double | 是 |
| endDate | Date \| double | 是 |

**返回值：**

| 类型 |
| --- |
| [DateTimeRangeFormatPart](arkts-arkts-intl-datetimerangeformatpart-i.md)[] |

## formatToParts

```TypeScript
public formatToParts(date?: Date | double): DateTimeFormatPart[]
```

将日期格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date \| double | 否 |

**返回值：**

| 类型 |
| --- |
| [DateTimeFormatPart](arkts-arkts-intl-datetimeformatpart-i.md)[] |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedDateTimeFormatOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ResolvedDateTimeFormatOptions](arkts-arkts-intl-resolveddatetimeformatoptions-i.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>, 
            options?: DateTimeFormatOptions): string[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | string \| Locale \| ReadonlyArray & lt;string \ | Locale & gt; | 是 |
| options | [DateTimeFormatOptions](arkts-arkts-intl-datetimeformatoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string[] |
