# Collator

提供字符串排序的能力。

**起始版本：** 8

<!--Device-intl-export class Collator--><!--Device-intl-export class Collator-End-->

**系统能力：** SystemCapability.Global.I18n

## compare

```TypeScript
compare(first: string, second: string): number
```

根据配置项的排序规则，比较两个字符串。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Collator-compare(first: string, second: string): int--><!--Device-Collator-compare(first: string, second: string): int-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| first | string | 是 |
| second | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用en-GB区域ID创建Collator对象
let collator = new intl.Collator('en-GB');
// 比较first和second的先后顺序
let compareResult = collator.compare('first', 'second'); // compareResult = -1
```

## constructor

```TypeScript
constructor()
```

使用当前系统区域创建排序对象。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Collator-constructor()--><!--Device-Collator-constructor()-End-->

**系统能力：** SystemCapability.Global.I18n

## 示例

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用系统区域创建Collator对象
let collator = new intl.Collator();
```

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: CollatorOptions)
```

根据指定的区域和配置项创建排序对象。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Collator-constructor(locale: string | Array<string>, options?: CollatorOptions)--><!--Device-Collator-constructor(locale: string | Array<string>, options?: CollatorOptions)-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | 是 |
| options | [CollatorOptions](arkts-localization-intl-collatoroptions-i.md) | 否 |

## 示例

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建Collator对象，localeMatcher设置为lookup，usage设置为sort
let collator = new intl.Collator('zh-CN', {localeMatcher: 'lookup', usage: 'sort'});
```

## resolvedOptions

```TypeScript
resolvedOptions(): CollatorOptions
```

获取创建排序对象时设置的配置项。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Collator-resolvedOptions(): CollatorOptions--><!--Device-Collator-resolvedOptions(): CollatorOptions-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [CollatorOptions](arkts-localization-intl-collatoroptions-i.md) |

## 示例

```TypeScript
import { intl } from '@kit.LocalizationKit';

let collator = new intl.Collator('zh-Hans', { usage: 'sort', ignorePunctuation: true });
// 获取Collator对象的配置项
let options = collator.resolvedOptions();
let usage = options.usage; // usage = 'sort'
let ignorePunctuation = options.ignorePunctuation; // ignorePunctuation = true
```
