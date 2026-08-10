# SymbolDateTimeFormatOptions

创建自定义符号时间日期格式化对象时的可选配置项。继承自Intl.DateTimeFormatOptions，支持Intl.DateTimeFormatOptions的所有配置项，并且功能与其一致。

**Inheritance/Implementation:** SymbolDateTimeFormatOptions extends [Intl.DateTimeFormatOptions](../../apis-arkts/arkts-apis/arkts-arkts-intl-datetimeformatoptions-i.md/arkts-arkts-intl-datetimeformatoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-i18n-export interface SymbolDateTimeFormatOptions extends Intl.DateTimeFormatOptions--><!--Device-i18n-export interface SymbolDateTimeFormatOptions extends Intl.DateTimeFormatOptions-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## amPMSymbol

```TypeScript
amPMSymbol?: string[] | undefined
```

指定的上午和下午符号，要求数组长度不小于2，其中第一个元素为上午符号，第二个元素为下午符号。默认值：区域默认的符号。

**Type:** string[] \| undefined

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolDateTimeFormatOptions-amPMSymbol?: string[] | undefined--><!--Device-SymbolDateTimeFormatOptions-amPMSymbol?: string[] | undefined-End-->

**System capability:** SystemCapability.Global.I18n

