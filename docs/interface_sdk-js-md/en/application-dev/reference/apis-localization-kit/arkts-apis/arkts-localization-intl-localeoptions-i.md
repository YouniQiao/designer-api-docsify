# LocaleOptions

> 从API version 6开始支持，从API version 20开始废弃，以calendar为例，
> 区域初始化配置项。从API version 9开始，LocaleOptions属性由必填改为可选。

> **说明：**
> 
> - calendar：不同取值的含义请参考[设置日历和历法表1](../../../internationalization/i18n-calendar.md)。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#options)

<!--Device-intl-export interface LocaleOptions--><!--Device-intl-export interface LocaleOptions-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## calendar

```TypeScript
calendar?: string
```

历法参数，取值包括：

"buddhist", "chinese", "coptic", "dangi", "ethioaa", "ethiopic", "gregory", "hebrew", "indian", "islamic", "islamic-umalqura", "islamic-tbla", "islamic-civil", "islamic-rgsa", "iso8601", "japanese", "persian", "roc", "islamicc"。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#calendar)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-LocaleOptions-calendar?: string--><!--Device-LocaleOptions-calendar?: string-End-->

**System capability:** SystemCapability.Global.I18n

## caseFirst

```TypeScript
caseFirst?: string
```

区域的排序规则是否考虑大小写，取值包括：

"upper"：大写排前面。

"lower"：小写排前面。

"false"：使用区域默认的大小写排序规则。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.caseFirst](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#casefirst)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-LocaleOptions-caseFirst?: string--><!--Device-LocaleOptions-caseFirst?: string-End-->

**System capability:** SystemCapability.Global.I18n

## collation

```TypeScript
collation?: string
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

**Substitutes:** [Intl.LocaleOptions.collation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#collation)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-LocaleOptions-collation?: string--><!--Device-LocaleOptions-collation?: string-End-->

**System capability:** SystemCapability.Global.I18n

## hourCycle

```TypeScript
hourCycle?: string
```

时制格式，取值包括：

"h11", "h12", "h23", "h24"。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.hourCycle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#hourcycle)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-LocaleOptions-hourCycle?: string--><!--Device-LocaleOptions-hourCycle?: string-End-->

**System capability:** SystemCapability.Global.I18n

## numberingSystem

```TypeScript
numberingSystem?: string
```

数字系统，取值包括：

"adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.numberingSystem](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#numberingsystem)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-LocaleOptions-numberingSystem?: string--><!--Device-LocaleOptions-numberingSystem?: string-End-->

**System capability:** SystemCapability.Global.I18n

## numeric

```TypeScript
numeric?: boolean
```

true表示将数字字符视为数字进行排序处理，false表示将数字字符视为普通字符进行排序处理。例如设置为true时，字符串“21”和字符串“123”比较，相当于数字21和123比较。默认值：false。

**Type:** boolean

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 20

**Substitutes:** [Intl.LocaleOptions.numeric](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#numeric)

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-LocaleOptions-numeric?: boolean--><!--Device-LocaleOptions-numeric?: boolean-End-->

**System capability:** SystemCapability.Global.I18n

