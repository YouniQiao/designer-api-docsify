# NumberOptions

创建数字格式化对象时可设置的配置项。从API version 9开始，NumberOptions的属性由必填改为可选。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-intl-export interface NumberOptions--><!--Device-intl-export interface NumberOptions-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## compactDisplay

```TypeScript
compactDisplay?: string
```

紧凑显示格式，取值包括："long", "short"。

默认值：short。

不同取值的显示效果请参考[附录表18](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-compactDisplay?: string--><!--Device-NumberOptions-compactDisplay?: string-End-->

**System capability:** SystemCapability.Global.I18n

## currency

```TypeScript
currency?: string
```

货币单位（需设置style为currency）， 取值符合[ISO-4217标准](https://www.iso.org/iso-4217-currency-codes.html)，如："EUR"，"CNY"，"USD"等。

从API version 12开始支持三位数字代码，如："978"，"156"，"840"等。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-currency?: string--><!--Device-NumberOptions-currency?: string-End-->

**System capability:** SystemCapability.Global.I18n

## currencyDisplay

```TypeScript
currencyDisplay?: string
```

货币的显示方式（需设置style为currency），取值包括："symbol", "narrowSymbol", "code", "name"。

默认值：symbol。

不同取值的显示效果请参考[附录表20](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-currencyDisplay?: string--><!--Device-NumberOptions-currencyDisplay?: string-End-->

**System capability:** SystemCapability.Global.I18n

## currencySign

```TypeScript
currencySign?: string
```

货币单位的符号显示（需设置style为currency），取值包括： "standard"，"accounting"。

默认值：standard。

不同取值的显示效果请参考[附录表19](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-currencySign?: string--><!--Device-NumberOptions-currencySign?: string-End-->

**System capability:** SystemCapability.Global.I18n

## locale

```TypeScript
locale?: string
```

合法的区域ID， 如："zh-Hans-CN"。

默认值：系统当前区域ID。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-locale?: string--><!--Device-NumberOptions-locale?: string-End-->

**System capability:** SystemCapability.Global.I18n

## localeMatcher

```TypeScript
localeMatcher?: string
```

要使用的区域匹配算法，取值包括："lookup", "best fit"。

默认值：best fit。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-localeMatcher?: string--><!--Device-NumberOptions-localeMatcher?: string-End-->

**System capability:** SystemCapability.Global.I18n

## maximumFractionDigits

```TypeScript
maximumFractionDigits?: int
```

表示要使用的最大分数位数，取值范围：[1, 21]。

默认值：3。

不同取值的显示效果请参考[附录表13](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** int

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-maximumFractionDigits?: int--><!--Device-NumberOptions-maximumFractionDigits?: int-End-->

**System capability:** SystemCapability.Global.I18n

## maximumSignificantDigits

```TypeScript
maximumSignificantDigits?: int
```

表示要使用的最大有效位数，取值范围：[1, 21]。

默认值：21。

不同取值的显示效果请参考[附录表15](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** int

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-maximumSignificantDigits?: int--><!--Device-NumberOptions-maximumSignificantDigits?: int-End-->

**System capability:** SystemCapability.Global.I18n

## minimumFractionDigits

```TypeScript
minimumFractionDigits?: int
```

表示要使用的最小分数位数，取值范围：[0, 20]。

默认值：0。

不同取值的显示效果请参考[附录表12](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** int

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-minimumFractionDigits?: int--><!--Device-NumberOptions-minimumFractionDigits?: int-End-->

**System capability:** SystemCapability.Global.I18n

## minimumIntegerDigits

```TypeScript
minimumIntegerDigits?: int
```

表示要使用的最小整数位数，取值范围：[1, 21]。

默认值：1。

不同取值的显示效果请参考[附录表11](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** int

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-minimumIntegerDigits?: int--><!--Device-NumberOptions-minimumIntegerDigits?: int-End-->

**System capability:** SystemCapability.Global.I18n

## minimumSignificantDigits

```TypeScript
minimumSignificantDigits?: int
```

表示要使用的最小有效位数，取值范围：[1, 21]。

默认值：1。

不同取值的显示效果请参考[附录表14](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** int

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-minimumSignificantDigits?: int--><!--Device-NumberOptions-minimumSignificantDigits?: int-End-->

**System capability:** SystemCapability.Global.I18n

## notation

```TypeScript
notation?: string
```

数字的表示方法，取值包括："standard", "scientific", "engineering", "compact"。

默认值：standard。

不同取值的显示效果请参考[附录表17](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-notation?: string--><!--Device-NumberOptions-notation?: string-End-->

**System capability:** SystemCapability.Global.I18n

## numberingSystem

```TypeScript
numberingSystem?: string
```

数字系统，取值包括：

"adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide","gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham","laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong","mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment","shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii","wara", "wcho"。

默认值：区域的默认数字系统。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-numberingSystem?: string--><!--Device-NumberOptions-numberingSystem?: string-End-->

**System capability:** SystemCapability.Global.I18n

## roundingIncrement

```TypeScript
roundingIncrement?: int
```

表示舍入增量，取值范围：1，2，5，10，20，25，50，100，200，250，500，1000，2000，2500，5000。

默认值：1。

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NumberOptions-roundingIncrement?: int--><!--Device-NumberOptions-roundingIncrement?: int-End-->

**System capability:** SystemCapability.Global.I18n

## roundingMode

```TypeScript
roundingMode?: string
```

表示舍入模式，取值包括：

"ceil"：向上取整。

"floor"：向下取整。

"expand"：远离零取整。

"trunc"：向零取整。

"halfCeil"：半向上取整，大于等于增量的一半时向上取整，小于增量的一半时向下取整。

"halfFloor"：半向下取整，大于增量的一半时向上取整，小于等于增量的一半时向下取整。

"halfExpand"：半远离零取整，大于等于增量的一半时远离零取整，小于增量的一半时向零取整。

"halfTrunc"：半向零取整，大于增量的一半时远离零取整，小于等于增量的一半时向零取整。

"halfEven"：半向偶数取整，大于增量的一半时 远离零取整，小于增量的一半时向零取整，等于增量的一半时向最近的偶数位舍入。

默认值：halfExpand。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NumberOptions-roundingMode?: string--><!--Device-NumberOptions-roundingMode?: string-End-->

**System capability:** SystemCapability.Global.I18n

## roundingPriority

```TypeScript
roundingPriority?: string
```

最大分数位数和最大有效位数同时设置时的舍入优先级，取值包括："auto" 选择区域默认的最大分数位数或最大有效位数，"morePrecision" 取最大分数位数，"lessPrecision" 取最大有效位数。

默认值：auto。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NumberOptions-roundingPriority?: string--><!--Device-NumberOptions-roundingPriority?: string-End-->

**System capability:** SystemCapability.Global.I18n

## signDisplay

```TypeScript
signDisplay?: string
```

数字符号的显示格式，取值包括：

"auto"：自动判断是否显示正负符号。

"never"：不显示正负号。

"always"：总是显示正负号。

"exceptZero"：除了0都显示正负号。

默认值："auto"。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-signDisplay?: string--><!--Device-NumberOptions-signDisplay?: string-End-->

**System capability:** SystemCapability.Global.I18n

## style

```TypeScript
style?: string
```

数字的显示格式，取值包括："decimal", "currency", "percent", "unit"。

默认值：decimal。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-style?: string--><!--Device-NumberOptions-style?: string-End-->

**System capability:** SystemCapability.Global.I18n

## unit

```TypeScript
unit?: string
```

单位名称（需设置style为unit），如："meter"，"inch"，“hectare”等。

从API version 18开始新增支持的组合单位有： "beat-per-minute", "body-weight-per-second", "breath-per-minute", "foot-per-hour","jump-rope-per-minute", "meter-per-hour", "milliliter-per-minute-per-kilogram", "rotation-per-minute", "step-per-minute","stroke-per-minute"。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-unit?: string--><!--Device-NumberOptions-unit?: string-End-->

**System capability:** SystemCapability.Global.I18n

## unitDisplay

```TypeScript
unitDisplay?: string
```

单位的显示格式（需设置style为unit），取值包括："long", "short", "narrow"。

默认值：short。

不同取值的显示效果请参考[附录表21](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-unitDisplay?: string--><!--Device-NumberOptions-unitDisplay?: string-End-->

**System capability:** SystemCapability.Global.I18n

## unitUsage

```TypeScript
unitUsage?: string
```

单位的使用场景（需设置style为unit），取值包括："default", "area-land-agricult", "area-land-commercl", "area-land-residntl","length-person", "length-person-small", "length-rainfall", "length-road", "length-road-small", "length-snowfall","length-vehicle", "length-visiblty", "length-visiblty-small", "length-person-informal", "length-person-small-informal","length-road-informal", "speed-road-travel", "speed-wind", "temperature-person", "temperature-weather","volume-vehicle-fuel", "elapsed-time-second", "size-file-byte", "size-shortfile-byte"。

默认值：default。

不同取值的显示效果请参考[附录表22](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-unitUsage?: string--><!--Device-NumberOptions-unitUsage?: string-End-->

**System capability:** SystemCapability.Global.I18n

## useGrouping

```TypeScript
useGrouping?: boolean
```

true表示分组显示，false表示不分组显示。

默认值：true。

不同取值的显示效果请参考[附录表16](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** boolean

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberOptions-useGrouping?: boolean--><!--Device-NumberOptions-useGrouping?: boolean-End-->

**System capability:** SystemCapability.Global.I18n

