# SimpleNumberFormat

基于框架字符串提供数字格式化的能力。

**起始版本：** 23

<!--Device-i18n-export class SimpleNumberFormat--><!--Device-i18n-export class SimpleNumberFormat-End-->

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## format

```TypeScript
format(value: double): string
```

对数字进行格式化。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-SimpleNumberFormat-format(value: double): string--><!--Device-SimpleNumberFormat-format(value: double): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 数字对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的数字字符串。 |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let formatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
// formattedPhoneNumber = '158 **** 2312'
let formattedPhoneNumber: string = formatter.format('158****2312');

// 拨号中的电话号码格式化
let option: i18n.PhoneNumberFormatOptions = { type: 'TYPING' };
let typingFormatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN', option);
let phoneNumber: string = '130493';
let formatResult: string = '';
for (let i = 0; i < phoneNumber.length; i++) {
  formatResult += phoneNumber.charAt(i);
  formatResult = typingFormatter.format(formatResult); // formatResult = '130 493'
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale : Intl.Locale = new Intl.Locale("zh-Hans-CN");
  let date : Date = new Date(2024, 11, 13); // 时间日期为2024.12.13

  let formatterWithText: i18n.SimpleDateTimeFormat =
    i18n.getSimpleDateTimeFormatByPattern("'month('M')'", locale);
  let formattedDate: string = formatterWithText.format(date); // formattedDate = 'month(12)'

  let patternFormatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatByPattern('yMd', locale);
  formattedDate = patternFormatter.format(date); // formattedDate = '20241213'

  let skeletonFormatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatBySkeleton('yMd', locale);
  formattedDate = skeletonFormatter.format(date); // formattedDate = '2024/12/13'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call SimpleDateTimeFormat.format failed, error code: ${err.code}, message: ${err.message}.`);
}
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let locale = new Intl.Locale('zh-Hans-CN');
let formatter = new i18n.SymbolDateTimeFormat(locale, {
  timeStyle: 'short',
  amPMSymbol: ['早', '晚']
});
let result = formatter.format(new Date(2026, 3, 26, 14, 20, 0)); // result = '晚2:20'
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let yearTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let monthTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });
  let dayTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });

  // 通过Intl.DateTimeFormat创建StyledDateTimeFormat对象
  let dateFormat: Intl.DateTimeFormat = new Intl.DateTimeFormat('zh-Hans-CN', { dateStyle: 'full' });
  let styledDateFormat: i18n.StyledDateTimeFormat = new i18n.StyledDateTimeFormat(dateFormat, {
    year: yearTextStyle,
    month: monthTextStyle,
    day: dayTextStyle
  });
  let date: Date = new Date(2025, 11, 1);
  // formattedDate.getString() 为 '2025年12月1日星期一'。显示formattedDate时'2025'是红色，'12'是绿色，'1'是蓝色
  let formattedDate: StyledString = styledDateFormat.format(date);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call StyledNumberFormat.format failed, error code: ${err.code}, message: ${err.message}.`);
}
```

```TypeScript
let formatter = new i18n.ISO8601DateTimeFormat({
  dateFormat: 'calendar',
  timePrecision: 'minutes',
  separatorStyle: 'extended'
});
let result = formatter.format(new Date(2026, 2, 15, 12, 0, 0));
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale: Intl.Locale = new Intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('%', locale);
  let formattedNumber: string = formatter.format(10); // formattedNumber = '10%'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call SimpleNumberFormat.format failed, error code: ${err.code}, message: ${err.message}.`);
}
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let locale = new Intl.Locale('zh-Hans-CN');
let formatter = new i18n.SymbolNumberFormat(locale, {
  style: 'unit',
  unit: 'day',
  zero: '(0)'
});
let result = formatter.format(10); // result = '1(0)天'
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let integerTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let decimalTextStyle: TextStyle = new TextStyle({ fontColor: Color.Brown });
  let fractionTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });
  let unitTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });

  // 通过Intl.NumberFormat创建StyledNumberFormat对象
  let numFmt: Intl.NumberFormat = new Intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
  // formattedNumber.getString() 为 '1,234.568%'。显示formattedNumber时'1,234'是红色，'.'是棕色，'568'是蓝色，'%'是绿色
  let formattedNumber: StyledString = styledNumFmt.format(1234.5678);

  // 通过SimpleNumberFormat创建StyledNumberFormat对象
  let locale: Intl.Locale = new Intl.Locale('zh');
  let simpleNumFmt: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('percent', locale);
  let styledSimpleNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(simpleNumFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
  // formattedSimpleNumber.getString() 为 '1,234.5678%'。显示formattedSimpleNumber时'1,234'是红色，'.'是棕色，'5678'是蓝色，'%'是绿色
  let formattedSimpleNumber: StyledString = styledSimpleNumFmt.format(1234.5678);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call StyledNumberFormat.format failed, error code: ${err.code}, message: ${err.message}.`);
}
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let numFmt: Intl.NumberFormat = new Intl.NumberFormat('zh-Hans-CN', { style: 'unit', unit: 'fahrenheit' });
let advancedMeasureFormat: i18n.AdvancedMeasureFormat = new i18n.AdvancedMeasureFormat(numFmt, {
  unitUsage: i18n.UnitUsage.TEMPERATURE_PERSON
});
let result = advancedMeasureFormat.format(100); // result = '37.778°C'
```

