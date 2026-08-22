# Collator

提供字符串排序的能力。

**起始版本：** 23

<!--Device-intl-export class Collator--><!--Device-intl-export class Collator-End-->

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { intl } from '@kit.LocalizationKit';
```

## compare

```TypeScript
compare(first: string, second: string): int
```

根据配置项的排序规则，比较两个字符串。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Collator-compare(first: string, second: string): int--><!--Device-Collator-compare(first: string, second: string): int-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | string | 是 | 进行比较的第一个字符串。 |
| second | string | 是 | 进行比较的第二个字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 比较结果。 <br>- number为负数时，表示first排序在second之前。 <br>- number为0时，表示first与second排序相同。 <br>- number为正数，表示first排序在second之后。 |

**示例**

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

**示例**

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 默认构造函数使用系统当前区域ID创建
let locale = new intl.Locale();
// 返回系统当前区域ID
let localeID = locale.toString();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 创建zh-CN区域对象
let locale = new intl.Locale('zh-CN');
let localeID = locale.toString(); // localeID = 'zh-CN'
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用系统当前区域ID创建DateTimeFormat对象
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建DateTimeFormat对象，日期风格为full，时间风格为medium
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('zh-CN', { dateStyle: 'full', timeStyle: 'medium' });

// 使用区域ID列表创建DateTimeFormat对象，因为ban为非法区域ID，因此使用zh区域ID创建DateTimeFormat对象
formatter = new intl.DateTimeFormat(['ban', 'zh'], { dateStyle: 'full', timeStyle: 'medium' });
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用系统当前区域ID创建NumberFormat对象
let formatter: intl.NumberFormat = new intl.NumberFormat();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用en-GB区域ID创建NumberFormat对象，style设置为decimal，notation设置为scientific
let formatter: intl.NumberFormat = new intl.NumberFormat('en-GB', { style: 'decimal', notation: 'scientific' });
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用系统区域创建Collator对象
let collator = new intl.Collator();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建Collator对象，localeMatcher设置为lookup，usage设置为sort
let collator = new intl.Collator('zh-CN', {localeMatcher: 'lookup', usage: 'sort'});
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用系统区域创建PluralRules对象
let pluralRules = new intl.PluralRules();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建PluralRules对象，localeMatcher设置为lookup，type设置为cardinal
let pluralRules: intl.PluralRules = new intl.PluralRules('zh-CN', { localeMatcher: 'lookup', type: 'cardinal' });
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用系统区域创建RelativeTimeFormat对象
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建RelativeTimeFormat对象，localeMatcher设置为lookup，numeric设置为always，style设置为long
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN', {
  localeMatcher: 'lookup',
  numeric: 'always',
  style: 'long'
});
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

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | 是 | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | CollatorOptions | 否 | 创建排序对象时可设置的配置项。 <br>默认值：所有属性都取默认值时的配置项。 |

**示例**

参见 [constructor](#constructor)

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

| 类型 | 说明 |
| --- | --- |
| CollatorOptions | 返回排序对象的属性。 |

**示例**

```TypeScript
import { intl } from '@kit.LocalizationKit';

let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB', { dateStyle: 'full', timeStyle: 'medium' });
// 返回DateTimeFormat对象的配置项
let options: intl.DateTimeOptions = formatter.resolvedOptions();
let dateStyle: string | undefined = options.dateStyle; // dateStyle = 'full'
let timeStyle: string | undefined = options.timeStyle; // timeStyle = 'medium'
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

let formatter: intl.NumberFormat = new intl.NumberFormat(['en-GB', 'zh'], { style: 'decimal', notation: 'scientific' });
// 获取NumberFormat对象配置项
let options: intl.NumberOptions = formatter.resolvedOptions();
let style: string | undefined = options.style; // style = 'decimal'
let notation: string | undefined = options.notation; // notation = 'scientific'
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

let collator = new intl.Collator('zh-Hans', { usage: 'sort', ignorePunctuation: true });
// 获取Collator对象的配置项
let options = collator.resolvedOptions();
let usage = options.usage; // usage = 'sort'
let ignorePunctuation = options.ignorePunctuation; // ignorePunctuation = true
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用en-GB区域ID创建RelativeTimeFormat对象
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('en-GB', { style: 'short' });
// 获取RelativeTimeFormat对象配置项
let options: intl.RelativeTimeFormatResolvedOptions = formatter.resolvedOptions();
let style: string = options.style; // style = 'short'
```

