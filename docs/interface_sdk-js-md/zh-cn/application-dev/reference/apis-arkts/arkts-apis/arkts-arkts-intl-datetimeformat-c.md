# DateTimeFormat

用于按区域设置格式化日期的日期时间格式化类。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-Intl-export class DateTimeFormat--><!--Device-Intl-export class DateTimeFormat-End-->

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

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public constructor(locales?: string | string[], options?: DateTimeFormatOptions)--><!--Device-DateTimeFormat-public constructor(locales?: string | string[], options?: DateTimeFormatOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 否 | 区域设置。 |
| options | [DateTimeFormatOptions](arkts-arkts-intl-datetimeformatoptions-i.md) | 否 | 选项。 |

## format

```TypeScript
public format(date?: Date | double): string
```

格式化日期。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public format(date?: Date | double): string--><!--Device-DateTimeFormat-public format(date?: Date | double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | Date \| double | 否 | 待格式化的日期。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的日期字符串。 |

## formatRange

```TypeScript
public formatRange(startDate: Date | double, endDate: Date | double): string
```

格式化日期区间。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public formatRange(startDate: Date | double, endDate: Date | double): string--><!--Device-DateTimeFormat-public formatRange(startDate: Date | double, endDate: Date | double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startDate | Date \| double | 是 | 起始日期。 |
| endDate | Date \| double | 是 | 结束日期。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的区间字符串。 |

## formatRangeToParts

```TypeScript
public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]
```

将日期区间格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]--><!--Device-DateTimeFormat-public formatRangeToParts(startDate: Date | double, endDate: Date | double): DateTimeRangeFormatPart[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startDate | Date \| double | 是 | 起始日期。 |
| endDate | Date \| double | 是 | 结束日期。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DateTimeRangeFormatPart](arkts-arkts-intl-datetimerangeformatpart-i.md)[] | 格式化后的区间各片段。 |

## formatToParts

```TypeScript
public formatToParts(date?: Date | double): DateTimeFormatPart[]
```

将日期格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public formatToParts(date?: Date | double): DateTimeFormatPart[]--><!--Device-DateTimeFormat-public formatToParts(date?: Date | double): DateTimeFormatPart[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | Date \| double | 否 | 待格式化的日期。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DateTimeFormatPart](arkts-arkts-intl-datetimeformatpart-i.md)[] | 格式化后的各个片段。 |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedDateTimeFormatOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public resolvedOptions(): ResolvedDateTimeFormatOptions--><!--Device-DateTimeFormat-public resolvedOptions(): ResolvedDateTimeFormatOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedDateTimeFormatOptions](arkts-arkts-intl-resolveddatetimeformatoptions-i.md) | 解析后的选项。 |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>, 
            options?: DateTimeFormatOptions): string[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateTimeFormat-public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>,             options?: DateTimeFormatOptions): string[]--><!--Device-DateTimeFormat-public static supportedLocalesOf(locales: string | Locale | ReadonlyArray<string | Locale>,             options?: DateTimeFormatOptions): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| Locale \| ReadonlyArray&lt;string \| Locale&gt; | 是 | 区域设置。 |
| options | [DateTimeFormatOptions](arkts-arkts-intl-datetimeformatoptions-i.md) | 否 | 选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 支持的区域设置。 |

