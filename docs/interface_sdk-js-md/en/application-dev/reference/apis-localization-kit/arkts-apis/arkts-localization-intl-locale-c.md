# Locale

区域信息

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)

<!--Device-intl-export class Locale--><!--Device-intl-export class Locale-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

创建区域对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.Locale.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-constructor()--><!--Device-Locale-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// The current locale ID is used by the default constructor.
let locale = new intl.Locale();
// Return the current system locale ID.
let localeID = locale.toString();
```

## constructor

```TypeScript
constructor(locale: string, options?: LocaleOptions)
```

创建区域对象。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.Locale.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-constructor(locale: string, options?: LocaleOptions)--><!--Device-Locale-constructor(locale: string, options?: LocaleOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | 表示区域ID的字符串，由语言、脚本、国家地区组成。 |
| options | [LocaleOptions](../../apis-arkts/arkts-apis/arkts-arkts-intl-localeoptions-i.md) | No | 创建区域对象的配置项。 &lt;br&gt;默认值：所有属性都取默认值时的配置项。<br>**Since:** 12 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a zh-CN locale object.
let locale = new intl.Locale('zh-CN');
let localeID = locale.toString(); // localeID = 'zh-CN'
```

## maximize

```TypeScript
maximize(): Locale
```

最大化区域信息，补齐区域对象中缺少的脚本、国家地区信息。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.Locale.maximize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/maximize)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-maximize(): Locale--><!--Device-Locale-maximize(): Locale-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [Locale](arkts-localization-intl-locale-c.md) | 补齐完脚本、国家地区信息后的区域对象。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a zh locale object.
let locale = new intl.Locale('zh');
// Supplement the locale object's script and region.
let maximizedLocale = locale.maximize();
let localeID = maximizedLocale.toString(); // localeID = 'zh-Hans-CN'

// Create an en-US locale object.
locale = new intl.Locale('en-US');
// Supplement the locale object's script.
maximizedLocale = locale.maximize();
localeID = maximizedLocale.toString(); // localeID = 'en-Latn-US'
```

## minimize

```TypeScript
minimize(): Locale
```

最小化区域信息，移除区域对象中的脚本、国家地区信息。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.Locale.minimize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/minimize)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-minimize(): Locale--><!--Device-Locale-minimize(): Locale-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [Locale](arkts-localization-intl-locale-c.md) | 移除完脚本、国家地区信息后的区域对象。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a zh-Hans-CN locale object.
let locale = new intl.Locale('zh-Hans-CN');
// Remove the locale object's script and region.
let minimizedLocale = locale.minimize();
let localeID = minimizedLocale.toString(); // localeID = 'zh'

// Create an en-US locale object.
locale = new intl.Locale('en-US');
// Remove locale object's region.
minimizedLocale = locale.minimize();
localeID = minimizedLocale.toString(); // localeID = 'en'
```

## toString

```TypeScript
toString(): string
```

获取区域对象的字符串。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.Locale.toString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/toString)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-toString(): string--><!--Device-Locale-toString(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | 区域对象的字符串。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create an en-GB locale object.
let locale = new intl.Locale('en-GB');
let localeID = locale.toString(); // localeID = 'en-GB'
```

## baseName

```TypeScript
baseName: string
```

区域对象的基本信息，由语言、脚本、国家地区组成，如：zh-Hans-CN。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.baseName](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/baseName)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-baseName: string--><!--Device-Locale-baseName: string-End-->

**System capability:** SystemCapability.Global.I18n

## calendar

```TypeScript
calendar: string
```

区域的日历信息，取值包括：

"buddhist", "chinese", "coptic","dangi", "ethioaa", "ethiopic", "gregory", "hebrew", "indian", "islamic","islamic-umalqura", "islamic-tbla", "islamic-civil", "islamic-rgsa", "iso8601", "japanese", "persian", "roc","islamicc"。

不同取值表示的含义请参考[设置日历和历法表1](../../../internationalization/i18n-calendar.md)。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/calendar)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-calendar: string--><!--Device-Locale-calendar: string-End-->

**System capability:** SystemCapability.Global.I18n

## caseFirst

```TypeScript
caseFirst: string
```

区域的排序规则是否考虑大小写，取值包括：

"upper"：大写排前面。

"lower"：小写排前面。

"false"：使用区域默认的大小写排序规则。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.caseFirst](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-caseFirst: string--><!--Device-Locale-caseFirst: string-End-->

**System capability:** SystemCapability.Global.I18n

## collation

```TypeScript
collation: string
```

区域的排序规则，取值包括：

"big5han"：拉丁字母使用的拼音排序。

"compat"：兼容性排序，仅用于阿拉伯语。

"dict"：词典风格排序，仅用于僧伽罗语。

"direct"：二进制码点排序。

"ducet"：按Unicode排序元素表排序。

"eor"：按欧洲排序规则排序。

"gb2312"：拼音排序，仅用于中文排序。

"phonebk"：电话本风格排序。

"phonetic"：发音排序。

"pinyin"：拼音排序。

"reformed"：瑞典语排序。

"searchjl"：韩语初始辅音搜索的特殊排序。

"stroke"：汉语的笔画排序。

"trad"：传统风格排序，如西班牙语。

"unihan"：统一汉字排序，用于日语、韩语、中文等汉字排序。

"zhuyin"：注音排序，仅用于中文排序。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.collation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/collation)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-collation: string--><!--Device-Locale-collation: string-End-->

**System capability:** SystemCapability.Global.I18n

## hourCycle

```TypeScript
hourCycle: string
```

区域的时制信息，取值包括：

"h11"、"h12"、"h23"、"h24"。

不同取值的显示效果可参考[附录表5](../../../reference/apis-localization-kit/js-apis-intl.md#附录)。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.hourCycle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/hourCycle)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-hourCycle: string--><!--Device-Locale-hourCycle: string-End-->

**System capability:** SystemCapability.Global.I18n

## language

```TypeScript
language: string
```

与区域设置相关的语言，如：zh。取值遵循ISO 639标准。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.language](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-language: string--><!--Device-Locale-language: string-End-->

**System capability:** SystemCapability.Global.I18n

## numberingSystem

```TypeScript
numberingSystem: string
```

区域使用的数字系统，取值包括：

"adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide","gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham","laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong","mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment","shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii","wara", "wcho"。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.numberingSystem](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/numberingSystem)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-numberingSystem: string--><!--Device-Locale-numberingSystem: string-End-->

**System capability:** SystemCapability.Global.I18n

## numeric

```TypeScript
numeric: boolean
```

true表示对数字字符进行特殊的排序规则处理（把数字字符作为数值进行排序），false表示不对数字字符进行特殊的排序规则处理。

默认值：false。

**Type:** boolean

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.numeric](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/numeric)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-numeric: boolean--><!--Device-Locale-numeric: boolean-End-->

**System capability:** SystemCapability.Global.I18n

## region

```TypeScript
region: string
```

与区域设置相关的国家地区，如：CN。取值遵循ISO 3166标准。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.region](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/region)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-region: string--><!--Device-Locale-region: string-End-->

**System capability:** SystemCapability.Global.I18n

## script

```TypeScript
script: string
```

区域语言的书写方式（脚本），如：Hans。取值遵循ISO 15924标准。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.script](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-Locale-script: string--><!--Device-Locale-script: string-End-->

**System capability:** SystemCapability.Global.I18n

