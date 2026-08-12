# SymbolNumberFormat

提供自定义数字符号的能力。继承自  
[Intl.NumberFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)，支持  
[Intl.NumberFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)的方法。

**继承/实现关系：** SymbolNumberFormat implements [Intl.NumberFormat](arkts-localization-intl-numberformat-c.md#NumberFormat)

**起始版本：** 26.0.0

<!--Device-i18n-export class SymbolNumberFormat implements Intl.NumberFormat--><!--Device-i18n-export class SymbolNumberFormat implements Intl.NumberFormat-End-->

**系统能力：** SystemCapability.Global.I18n

## constructor

```TypeScript
public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)
```

创建使用自定义符号的数字格式化对象。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-SymbolNumberFormat-public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)--><!--Device-SymbolNumberFormat-public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | Intl.Locale | 否 |
| options | [SymbolNumberFormatOptions](arkts-localization-i18n-symbolnumberformatoptions-i.md) | 否 |

## format

```TypeScript
public format(value: number | bigint): string
```

对数字进行格式化，返回使用自定义符号的数字字符串。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-SymbolNumberFormat-public format(value: number | bigint): string--><!--Device-SymbolNumberFormat-public format(value: number | bigint): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| bigint | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## formatRange

```TypeScript
public formatRange(startRange: number, endRange: number): string
```

对数字范围进行格式化，返回使用自定义符号的数字范围字符串。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-SymbolNumberFormat-public formatRange(startRange: number, endRange: number): string--><!--Device-SymbolNumberFormat-public formatRange(startRange: number, endRange: number): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startRange | number | 是 |
| endRange | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## formatRangeToParts

```TypeScript
public formatRangeToParts(startRange: number, endRange: number): Intl.NumberFormatPart[]
```

对数字范围进行格式化，返回使用自定义符号的数字元素数组。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-SymbolNumberFormat-public formatRangeToParts(startRange: number, endRange: number): Intl.NumberFormatPart[]--><!--Device-SymbolNumberFormat-public formatRangeToParts(startRange: number, endRange: number): Intl.NumberFormatPart[]-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startRange | number | 是 |
| endRange | number | 是 |

**返回值：**

| 类型 |
| --- |
| Intl.NumberFormatPart[] |

## formatToParts

```TypeScript
public formatToParts(value?: number | bigint): Intl.NumberFormatPart[]
```

对数字进行格式化，返回使用自定义符号的数字元素数组。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-SymbolNumberFormat-public formatToParts(value?: number | bigint): Intl.NumberFormatPart[]--><!--Device-SymbolNumberFormat-public formatToParts(value?: number | bigint): Intl.NumberFormatPart[]-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| bigint | 否 |

**返回值：**

| 类型 |
| --- |
| Intl.NumberFormatPart[] |

## parse

```TypeScript
public parse(text: string, lenientMode: boolean): number
```

解析本地化数字字符串，返回对应的数字。无法正确解析使用自定义符号的本地化数字字符串。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-SymbolNumberFormat-public parse(text: string, lenientMode: boolean): number--><!--Device-SymbolNumberFormat-public parse(text: string, lenientMode: boolean): number-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| lenientMode | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [8900001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-localization-kit/errorcode-i18n.md#8900001-参数校验错误) |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSymbolNumberFormatOptions
```

解析自定义数字符号的配置项。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-SymbolNumberFormat-public resolvedOptions(): ResolvedSymbolNumberFormatOptions--><!--Device-SymbolNumberFormat-public resolvedOptions(): ResolvedSymbolNumberFormatOptions-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [ResolvedSymbolNumberFormatOptions](arkts-localization-i18n-resolvedsymbolnumberformatoptions-i.md) |
