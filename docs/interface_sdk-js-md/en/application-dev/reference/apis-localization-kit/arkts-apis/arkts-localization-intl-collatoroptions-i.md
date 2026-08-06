# CollatorOptions

Defines the options for creating a Collator object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-intl-export interface CollatorOptions--><!--Device-intl-export interface CollatorOptions-End-->

**System capability:** SystemCapability.Global.I18n

## caseFirst

```TypeScript
caseFirst?: string
```

Whether upper case or lower case is sorted first. The value can be "upper", "lower", or "false".The default value is "false".

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CollatorOptions-caseFirst?: string--><!--Device-CollatorOptions-caseFirst?: string-End-->

**System capability:** SystemCapability.Global.I18n

## collation

```TypeScript
collation?: string
```

Collation rule. The value can be any of the following: "big5han", "compat", "dict", "direct", "ducet", "eor","gb2312", "phonebk", "phonetic", "pinyin", "reformed", "searchjl", "stroke", "trad", "unihan", or "zhuyin".The default value is "default".

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CollatorOptions-collation?: string--><!--Device-CollatorOptions-collation?: string-End-->

**System capability:** SystemCapability.Global.I18n

## ignorePunctuation

```TypeScript
ignorePunctuation?: boolean
```

Whether to ignore punctuation. The value "true" means to ignore punctuation, and the value "false" means the opposite. The default value is "false".

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CollatorOptions-ignorePunctuation?: boolean--><!--Device-CollatorOptions-ignorePunctuation?: boolean-End-->

**System capability:** SystemCapability.Global.I18n

## localeMatcher

```TypeScript
localeMatcher?: string
```

Locale matching algorithm. The value can be "lookup" or "best fit". The default value is "best fit".

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CollatorOptions-localeMatcher?: string--><!--Device-CollatorOptions-localeMatcher?: string-End-->

**System capability:** SystemCapability.Global.I18n

## numeric

```TypeScript
numeric?: boolean
```

Whether to use numeric collation. The value "true" means to use numeric collation, and the value "false" means the opposite. The default value is "false".

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CollatorOptions-numeric?: boolean--><!--Device-CollatorOptions-numeric?: boolean-End-->

**System capability:** SystemCapability.Global.I18n

## sensitivity

```TypeScript
sensitivity?: string
```

Differences in the strings that lead to non-zero return values. The value can be "base", "accent", "case", or"letiant". The default value is "variant".

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CollatorOptions-sensitivity?: string--><!--Device-CollatorOptions-sensitivity?: string-End-->

**System capability:** SystemCapability.Global.I18n

## usage

```TypeScript
usage?: string
```

Whether the comparison is for sorting or for searching. The value can be "sort" or "search".The default value is "sort".

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CollatorOptions-usage?: string--><!--Device-CollatorOptions-usage?: string-End-->

**System capability:** SystemCapability.Global.I18n

