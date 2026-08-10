# PluralRules

提供获取单复数类型的能力。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules)

<!--Device-intl-export class PluralRules--><!--Device-intl-export class PluralRules-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

创建单复数对象来计算数字的单复数类别。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PluralRules-constructor()--><!--Device-PluralRules-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object using the current system locale ID.
let pluralRules = new intl.PluralRules();
```

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: PluralRulesOptions)
```

创建单复数对象来计算数字的单复数类别。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PluralRules-constructor(locale: string | Array<string>, options?: PluralRulesOptions)--><!--Device-PluralRules-constructor(locale: string | Array<string>, options?: PluralRulesOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | Yes | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | [PluralRulesOptions](../../apis-arkts/arkts-apis/arkts-arkts-intl-pluralrulesoptions-i.md) | No | 创建单复数对象时设置的配置项。 &lt;br&gt;默认值：所有属性都取默认值时的配置项。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object with the locale ID being zh-CN, localeMatcher being lookup, and type being cardinal.
let pluralRules: intl.PluralRules = new intl.PluralRules('zh-CN', { localeMatcher: 'lookup', type: 'cardinal' });
```

## select

```TypeScript
select(n: double): string
```

获取数字的单复数类别。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.PluralRules.select](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/select)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PluralRules-select(n: double): string--><!--Device-PluralRules-select(n: double): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | double | Yes | 待获取单复数类别的数字。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 单复数类别，取值包括："zero"，"one"，"two", "few", "many", "other"。 &lt;br&gt;不同取值的含义请参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object with the locale ID being zh-Hans.
let zhPluralRules = new intl.PluralRules('zh-Hans');
// Determine the singular-plural type corresponding to number 1 in locale zh-Hans.
let plural = zhPluralRules.select(1); // plural = 'other'

// Create a PluralRules object with the locale ID being en-US.
let enPluralRules = new intl.PluralRules('en-US');
// Determine the singular-plural type corresponding to number 1 in locale en-US.
plural = enPluralRules.select(1); // plural = 'one'
```

