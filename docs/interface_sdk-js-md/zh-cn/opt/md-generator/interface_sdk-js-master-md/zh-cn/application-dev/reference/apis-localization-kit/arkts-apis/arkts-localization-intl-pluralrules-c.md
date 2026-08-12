# PluralRules

提供获取单复数类型的能力。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [PluralRules]]([Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules))

<!--Device-intl-export class PluralRules--><!--Device-intl-export class PluralRules-End-->

**系统能力：** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor()
```

创建单复数对象来计算数字的单复数类别。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [constructor]]([Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules))

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PluralRules-constructor()--><!--Device-PluralRules-constructor()-End-->

**系统能力：** SystemCapability.Global.I18n

## 示例

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用系统区域创建PluralRules对象
let pluralRules = new intl.PluralRules();
```

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: PluralRulesOptions)
```

创建单复数对象来计算数字的单复数类别。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [constructor]]([Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules))

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PluralRules-constructor(locale: string | Array<string>, options?: PluralRulesOptions)--><!--Device-PluralRules-constructor(locale: string | Array<string>, options?: PluralRulesOptions)-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | 是 |
| options | [PluralRulesOptions](arkts-localization-intl-pluralrulesoptions-i.md) | 否 |

## 示例

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建PluralRules对象，localeMatcher设置为lookup，type设置为cardinal
let pluralRules: intl.PluralRules = new intl.PluralRules('zh-CN', { localeMatcher: 'lookup', type: 'cardinal' });
```

## select

```TypeScript
select(n: number): string
```

获取数字的单复数类别。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [select]]([Intl.PluralRules.select](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/select))

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PluralRules-select(n: double): string--><!--Device-PluralRules-select(n: double): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| n | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用zh-Hans区域ID创建PluralRules对象
let zhPluralRules = new intl.PluralRules('zh-Hans');
// 计算zh-Hans区域中数字1对应的单复数类别
let plural = zhPluralRules.select(1); // plural = 'other'

// 使用en-US区域ID创建PluralRules对象
let enPluralRules = new intl.PluralRules('en-US');
// 计算en-US区域中数字1对应的单复数类别
plural = enPluralRules.select(1); // plural = 'one'
```
