# SymbolNumberFormat

提供自定义数字符号的能力。继承自  
[Intl.NumberFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)，支持  
[Intl.NumberFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)的方法。

**Inheritance/Implementation:** SymbolNumberFormat extends [Intl.NumberFormat](../../apis-arkts/arkts-apis/arkts-arkts-intl-numberformat-c.md/arkts-arkts-intl-numberformat-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-i18n-export class SymbolNumberFormat extends Intl.NumberFormat--><!--Device-i18n-export class SymbolNumberFormat extends Intl.NumberFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)
```

创建使用自定义符号的数字格式化对象。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)--><!--Device-SymbolNumberFormat-public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | Intl.Locale | No | 区域对象。默认值：系统区域对象。 |
| options | [SymbolNumberFormatOptions](arkts-localization-i18n-symbolnumberformatoptions-i.md) | No | 自定义数字格式化符号的配置项。默认值：区域默认的符号。 |

## parse

```TypeScript
public parse(text: string, lenientMode: boolean): double
```

解析本地化数字字符串，返回对应的数字。无法正确解析使用自定义符号的本地化数字字符串。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public parse(text: string, lenientMode: boolean): double--><!--Device-SymbolNumberFormat-public parse(text: string, lenientMode: boolean): double-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 待解析的本地化数字字符串。 |
| lenientMode | boolean | Yes | 是否采用宽松模式，true表示采用宽松模式，false表示不采用宽松模式。 &lt;br&gt;宽松模式下，能够识别错误的千分符，如"1,23,456"可以正确解析为"123456"。 |

**Return value:**

| Type | Description |
| --- | --- |
| double | 本地化数字字符串解析后的数字。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8900001 | Invalid parameter. Possible causes: Parameter verification failed. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSymbolNumberFormatOptions
```

解析自定义数字符号的配置项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public resolvedOptions(): ResolvedSymbolNumberFormatOptions--><!--Device-SymbolNumberFormat-public resolvedOptions(): ResolvedSymbolNumberFormatOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [ResolvedSymbolNumberFormatOptions](arkts-localization-i18n-resolvedsymbolnumberformatoptions-i.md) | 自定义符号数字格式化对象配置项的解析结果。 |

