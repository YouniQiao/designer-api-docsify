# ResolvedSymbolDateTimeFormatOptions

自定义符号时间日期格式化对象配置项的解析结果。继承自Intl.ResolvedDateTimeFormatOptions，支持Intl.ResolvedDateTimeFormatOptions的所有配置项，并且功能与其一致。

**Inheritance/Implementation:** ResolvedSymbolDateTimeFormatOptions extends [Intl.ResolvedDateTimeFormatOptions](../../apis-arkts/arkts-apis/arkts-arkts-intl-resolveddatetimeformatoptions-i.md/arkts-arkts-intl-resolveddatetimeformatoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-i18n-export interface ResolvedSymbolDateTimeFormatOptions extends Intl.ResolvedDateTimeFormatOptions--><!--Device-i18n-export interface ResolvedSymbolDateTimeFormatOptions extends Intl.ResolvedDateTimeFormatOptions-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## amPMSymbol

```TypeScript
amPMSymbol?: string[]
```

指定的上午和下午符号，其中第一个元素为上午符号，第二个元素为下午符号。默认值：区域默认的符号。

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ResolvedSymbolDateTimeFormatOptions-amPMSymbol?: string[]--><!--Device-ResolvedSymbolDateTimeFormatOptions-amPMSymbol?: string[]-End-->

**System capability:** SystemCapability.Global.I18n

