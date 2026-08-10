# SymbolDateTimeFormat

提供自定义时间日期符号的能力。继承自  
[Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)，支持  
[Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)的方法。

**Inheritance/Implementation:** SymbolDateTimeFormat extends [Intl.DateTimeFormat](../../apis-arkts/arkts-apis/arkts-arkts-intl-datetimeformat-c.md/arkts-arkts-intl-datetimeformat-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-i18n-export class SymbolDateTimeFormat extends Intl.DateTimeFormat--><!--Device-i18n-export class SymbolDateTimeFormat extends Intl.DateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
public constructor(locale?: Intl.Locale, options?: SymbolDateTimeFormatOptions)
```

创建使用自定义符号的时间日期格式化对象。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public constructor(locale?: Intl.Locale, options?: SymbolDateTimeFormatOptions)--><!--Device-SymbolDateTimeFormat-public constructor(locale?: Intl.Locale, options?: SymbolDateTimeFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | Intl.Locale | No | 区域对象。默认值：系统区域对象。 |
| options | [SymbolDateTimeFormatOptions](arkts-localization-i18n-symboldatetimeformatoptions-i.md) | No | 自定义符号时间日期格式化的配置项。默认值：区域对象默认的符号。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8900001 | Invalid parameter. Possible causes: Parameter verification failed. |

## parse

```TypeScript
public parse(text: string, lenientMode: boolean): long
```

解析本地化时间日期字符串，返回对应的时间戳。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public parse(text: string, lenientMode: boolean): long--><!--Device-SymbolDateTimeFormat-public parse(text: string, lenientMode: boolean): long-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 待解析的本地化时间日期字符串。 |
| lenientMode | boolean | Yes | 是否采用宽松模式，true表示采用宽松模式，false表示不采用宽松模式。 &lt;br&gt;宽松模式下，能够处理不符合常规逻辑的时间日期值，如"5月32日"会自动转换成"6月1日"进行解析。 |

**Return value:**

| Type | Description |
| --- | --- |
| long | 时间日期字符串解析后对应的时间戳，单位为毫秒（ms）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8900001 | Invalid parameter. Possible causes: Parameter verification failed. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions
```

解析自定义时间日期符号的配置项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormat-public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions--><!--Device-SymbolDateTimeFormat-public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [ResolvedSymbolDateTimeFormatOptions](arkts-localization-i18n-resolvedsymboldatetimeformatoptions-i.md) | 自定义符号时间日期格式化对象配置项的解析结果。 |

