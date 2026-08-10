# RelativeTimeFormatInputOptions

创建相对时间格式化对象时可设置的配置项。

从API version 9开始，RelativeTimeFormatInputOptions中的属性改为可选。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormatOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#options)

<!--Device-intl-export interface RelativeTimeFormatInputOptions--><!--Device-intl-export interface RelativeTimeFormatInputOptions-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## localeMatcher

```TypeScript
localeMatcher?: string
```

区域匹配算法，取值包括："best fit", "lookup"。

默认值：best fit。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormatOptions.localeMatcher](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#localematcher)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormatInputOptions-localeMatcher?: string--><!--Device-RelativeTimeFormatInputOptions-localeMatcher?: string-End-->

**System capability:** SystemCapability.Global.I18n

## numeric

```TypeScript
numeric?: string
```

输出消息的格式，表示格式化结果中是否使用数字表示相对日期或时间。取值包括："always", "auto"。

默认值：always。

不同取值的显示效果请参考[附录表23](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormatOptions.numeric](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#numeric)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormatInputOptions-numeric?: string--><!--Device-RelativeTimeFormatInputOptions-numeric?: string-End-->

**System capability:** SystemCapability.Global.I18n

## style

```TypeScript
style?: string
```

国际化消息的长度，取值包括："long", "short", "narrow"。

默认值：long。

不同取值的显示效果请参考[附录表24](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormatOptions.style](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#style)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormatInputOptions-style?: string--><!--Device-RelativeTimeFormatInputOptions-style?: string-End-->

**System capability:** SystemCapability.Global.I18n

