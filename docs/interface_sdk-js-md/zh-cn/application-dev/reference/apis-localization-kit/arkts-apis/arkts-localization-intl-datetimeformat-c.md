# DateTimeFormat

提供日期格式化的能力。

**起始版本：** 6

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)

<!--Device-intl-export class DateTimeFormat--><!--Device-intl-export class DateTimeFormat-End-->

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { intl } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

创建时间日期格式化对象。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-DateTimeFormat-constructor()--><!--Device-DateTimeFormat-constructor()-End-->

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
constructor(locale: string | Array<string>, options?: DateTimeOptions)
```

创建时间日期格式化对象。

**起始版本：** 6

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-DateTimeFormat-constructor(locale: string | Array<string>, options?: DateTimeOptions)--><!--Device-DateTimeFormat-constructor(locale: string | Array<string>, options?: DateTimeOptions)-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | 是 | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | DateTimeOptions | 否 | 创建时间日期格式化对象时可设置的配置项。 <br>若所有选项均未设置时，year、month、day三个属性的默认值为numeric。 <br>默认值：所有属性都取默认值时的配置项。 |

**示例**

参见 [constructor](#constructor)

## format

```TypeScript
format(date: Date): string
```

对时间日期进行格式化，返回格式化后的时间日期字符串。

**起始版本：** 6

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/format)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-DateTimeFormat-format(date: Date): string--><!--Device-DateTimeFormat-format(date: Date): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | Date | 是 | 时间日期。 <br>**说明：** <br>月份从0开始计数，0表示一月。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的时间日期字符串。 |

**示例**

```TypeScript
import { intl } from '@kit.LocalizationKit';

let date: Date = new Date(2021, 11, 17, 3, 24, 0); // 时间日期为2021.12.17 03:24:00
// 使用en-GB区域ID创建DateTimeFormat对象
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB');
let formattedDate: string = formatter.format(date); // formattedDate "17/12/2021"

// 使用en-GB区域ID创建DateTimeFormat对象，dateStyle设置为full，timeStyle设置为medium
formatter = new intl.DateTimeFormat('en-GB', { dateStyle: 'full', timeStyle: 'medium' });
formattedDate = formatter.format(date); // formattedDate "Friday, 17 December 2021, 03:24:00"
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用区域ID列表创建NumberFormat对象，因为en-GB为合法的区域ID，因此使用en-GB创建NumberFormat对象
let formatter: intl.NumberFormat = new intl.NumberFormat(['en-GB', 'zh'], { style: 'decimal', notation: 'scientific' });
let formattedNumber: string = formatter.format(1223); // formattedNumber = 1.223E3
let options: intl.NumberOptions = {
  roundingPriority: 'lessPrecision',
  maximumFractionDigits: 3,
  maximumSignificantDigits: 3
}
formatter = new intl.NumberFormat('en', options);
let result: string = formatter.format(1.23456); // result = 1.23
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建RelativeTimeFormat对象
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN');
// 计算zh-CN区域中数字3，单位quarter的本地化表示
let formatResult: string = formatter.format(3, 'quarter'); // formatResult = '3个季度后'
```

## formatRange

```TypeScript
formatRange(startDate: Date, endDate: Date): string
```

对时间日期段进行格式化，返回格式化后的时间日期段字符串。

**起始版本：** 6

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat.formatRange](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/formatRange)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-DateTimeFormat-formatRange(startDate: Date, endDate: Date): string--><!--Device-DateTimeFormat-formatRange(startDate: Date, endDate: Date): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startDate | Date | 是 | 时间日期的开始。 <br>**说明：** <br>月份从0开始计数，0表示一月。 |
| endDate | Date | 是 | 时间日期的结束。 <br>**说明：** <br>月份从0开始计数，0表示一月。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的时间日期段字符串。 |

**示例**

```TypeScript
import { intl } from '@kit.LocalizationKit';

let startDate: Date = new Date(2021, 11, 17, 3, 24, 0); // 时间日期为2021.12.17 03:24:00
let endDate: Date = new Date(2021, 11, 18, 3, 24, 0);
// 使用en-GB区域ID创建DateTimeFormat对象
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB');
let formattedDateRange: string = formatter.formatRange(startDate, endDate); // formattedDateRange = '17/12/2021 - 18/12/2021'
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

let formatter: intl.NumberFormat = new intl.NumberFormat('en-US', { style: 'unit', unit: 'meter' });
let formattedRange: string = formatter.formatRange(0, 3); // formattedRange: 0–3 m
```

## resolvedOptions

```TypeScript
resolvedOptions(): DateTimeOptions
```

获取创建时间日期格式化对象时设置的配置项。

**起始版本：** 6

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-DateTimeFormat-resolvedOptions(): DateTimeOptions--><!--Device-DateTimeFormat-resolvedOptions(): DateTimeOptions-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DateTimeOptions | 时间日期格式化对象设置的配置项。 |

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

