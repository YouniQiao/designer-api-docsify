# DateTimeOptions

时间日期格式化时可设置的配置项。从API version 9开始，DateTimeOptions的属性由必填改为可选。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-intl-export interface DateTimeOptions--><!--Device-intl-export interface DateTimeOptions-End-->

**System capability:** SystemCapability.Global.I18n

## dateStyle

```TypeScript
dateStyle?: string
```

日期显示格式，取值包括：

"long", "short", "medium", "full", "auto"。

不同取值的显示效果请参考[附录表1](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-dateStyle?: string--><!--Device-DateTimeOptions-dateStyle?: string-End-->

**System capability:** SystemCapability.Global.I18n

## day

```TypeScript
day?: string
```

日期的显示格式，取值包括：

"numeric", "2-digit"。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-day?: string--><!--Device-DateTimeOptions-day?: string-End-->

**System capability:** SystemCapability.Global.I18n

## dayPeriod

```TypeScript
dayPeriod?: string
```

时段的显示格式，取值包括：

"long", "short", "narrow", "auto"。

不同取值的显示效果请参考[附录表10](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-dayPeriod?: string--><!--Device-DateTimeOptions-dayPeriod?: string-End-->

**System capability:** SystemCapability.Global.I18n

## era

```TypeScript
era?: string
```

纪元的显示格式，取值包括：

"long", "short", "narrow", "auto"。

不同取值的显示效果请参考[附录表9](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-era?: string--><!--Device-DateTimeOptions-era?: string-End-->

**System capability:** SystemCapability.Global.I18n

## formatMatcher

```TypeScript
formatMatcher?: string
```

要使用的格式匹配算法，取值包括：

"basic"：精确匹配。

"best fit"：最佳匹配。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-formatMatcher?: string--><!--Device-DateTimeOptions-formatMatcher?: string-End-->

**System capability:** SystemCapability.Global.I18n

## hour

```TypeScript
hour?: string
```

小时的显示格式，取值包括：

"numeric", "2-digit"。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-hour?: string--><!--Device-DateTimeOptions-hour?: string-End-->

**System capability:** SystemCapability.Global.I18n

## hour12

```TypeScript
hour12?: boolean
```

true表示使用12小时制，false表示使用24小时制。

同时设置hour12和hourCycle时，hourCycle不生效。

若hour12和hourCycle未设置且系统24小时开关打开时，hour12属性的默认值为false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-hour12?: boolean--><!--Device-DateTimeOptions-hour12?: boolean-End-->

**System capability:** SystemCapability.Global.I18n

## hourCycle

```TypeScript
hourCycle?: string
```

时制格式，取值包括：

"h11", "h12", "h23", "h24"。

不设置dateStyle或timeStyle参数时的显示效果请参考[附录表5](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

设置dateStyle或timeStyle参数时的显示效果请参考[附录表6](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-hourCycle?: string--><!--Device-DateTimeOptions-hourCycle?: string-End-->

**System capability:** SystemCapability.Global.I18n

## locale

```TypeScript
locale?: string
```

合法的区域ID，如：zh-Hans-CN。

默认值：系统当前区域ID。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-locale?: string--><!--Device-DateTimeOptions-locale?: string-End-->

**System capability:** SystemCapability.Global.I18n

## localeMatcher

```TypeScript
localeMatcher?: string
```

要使用的区域匹配算法，取值包括：

"lookup"：精确匹配。

"best fit"：最佳匹配。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-localeMatcher?: string--><!--Device-DateTimeOptions-localeMatcher?: string-End-->

**System capability:** SystemCapability.Global.I18n

## minute

```TypeScript
minute?: string
```

分钟的显示格式，取值包括：

"numeric", "2-digit"。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-minute?: string--><!--Device-DateTimeOptions-minute?: string-End-->

**System capability:** SystemCapability.Global.I18n

## month

```TypeScript
month?: string
```

月份的显示格式，取值包括：

"numeric", "2-digit", "long", "short", "narrow", "auto"。

不同取值的显示效果请参考[附录表7](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-month?: string--><!--Device-DateTimeOptions-month?: string-End-->

**System capability:** SystemCapability.Global.I18n

## numberingSystem

```TypeScript
numberingSystem?: string
```

数字系统，取值包括：

"adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide","gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham","laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong","mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment","shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii","wara", "wcho"。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-numberingSystem?: string--><!--Device-DateTimeOptions-numberingSystem?: string-End-->

**System capability:** SystemCapability.Global.I18n

## second

```TypeScript
second?: string
```

秒钟的显示格式，取值包括：

"numeric", "2-digit"。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-second?: string--><!--Device-DateTimeOptions-second?: string-End-->

**System capability:** SystemCapability.Global.I18n

## timeStyle

```TypeScript
timeStyle?: string
```

时间显示格式，取值包括：

"long", "short", "medium", "full", "auto"。

不同取值的显示效果请参考[附录表2](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-timeStyle?: string--><!--Device-DateTimeOptions-timeStyle?: string-End-->

**System capability:** SystemCapability.Global.I18n

## timeZone

```TypeScript
timeZone?: string
```

使用的时区，取值为合法的IANA时区ID。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-timeZone?: string--><!--Device-DateTimeOptions-timeZone?: string-End-->

**System capability:** SystemCapability.Global.I18n

## timeZoneName

```TypeScript
timeZoneName?: string
```

时区名称的本地化表示，取值包括：

"long", "short", "auto"。

不同取值的显示效果请参考[附录表8](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-timeZoneName?: string--><!--Device-DateTimeOptions-timeZoneName?: string-End-->

**System capability:** SystemCapability.Global.I18n

## weekday

```TypeScript
weekday?: string
```

星期的显示格式，取值包括：

"long", "short", "narrow", "auto"。

不同取值的显示效果请参考[附录表4](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-weekday?: string--><!--Device-DateTimeOptions-weekday?: string-End-->

**System capability:** SystemCapability.Global.I18n

## year

```TypeScript
year?: string
```

年份的显示格式，取值包括：

"numeric", "2-digit"。

不同取值的显示效果请参考[附录表3](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeOptions-year?: string--><!--Device-DateTimeOptions-year?: string-End-->

**System capability:** SystemCapability.Global.I18n

