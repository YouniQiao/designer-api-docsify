# PhoneNumberFormat

提供电话号码相关的能力，包括电话号码有效性判断、格式化和归属地获取。

**起始版本：** 23

<!--Device-i18n-export class PhoneNumberFormat--><!--Device-i18n-export class PhoneNumberFormat-End-->

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(country: string, options?: PhoneNumberFormatOptions)
```

创建电话号码格式化对象。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhoneNumberFormat-constructor(country: string, options?: PhoneNumberFormatOptions)--><!--Device-PhoneNumberFormat-constructor(country: string, options?: PhoneNumberFormatOptions)-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| country | string | 是 | 表示电话号码所属的国家地区代码，要求是 [合法的国家地区码](../../../internationalization/i18n-locale-culture.md#实现原理)。 |
| options | [PhoneNumberFormatOptions](../../apis-default/arkts-apis/arkts-i18n-phonenumberformatoptions-i.md) | 否 | 电话号码格式化时设置的配置项。默认值：NATIONAL。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let entityRecognizer: i18n.EntityRecognizer = new i18n.EntityRecognizer('zh-CN');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call new i18n.EntityRecognizer failed, error code: ${err.code}, message: ${err.message}.`);
}
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let option: i18n.PhoneNumberFormatOptions = { type: 'E164' };
let phoneNumberFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN', option);
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // 需要将'/system/lib/US.ics'替换为实际ics文件路径
  let holidayManager = new i18n.HolidayManager('/system/lib/US.ics');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.HolidayManager failed, error code: ${err.code}, message: ${err.message}.`);
}
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let locale = new Intl.Locale('zh-Hans-CN');
let formatter = new i18n.SymbolDateTimeFormat(locale, {
  timeStyle: 'short',
  amPMSymbol: ['早', '晚']
});
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

  let hourTextStyle: TextStyle = new TextStyle({ fontColor: Color.Yellow });
  let minuteTextStyle: TextStyle = new TextStyle({ fontColor: Color.Orange });
  let secondTextStyle: TextStyle = new TextStyle({ fontColor: Color.Pink });

  // 通过SimpleDateTimeFormat创建StyledDateTimeFormat对象
  let locale: Intl.Locale = new Intl.Locale('zh-Hans-CN');
  let simpleTimeFormat: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatBySkeleton('hhmmss', locale);
  let styledTimeFormat: i18n.StyledDateTimeFormat = new i18n.StyledDateTimeFormat(simpleTimeFormat, {
    hour: hourTextStyle,
    minute: minuteTextStyle,
    second: secondTextStyle
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.StyledDateTimeFormat failed, error code: ${err.code}, message: ${err.message}.`);
}
```

```TypeScript
let formatter = new i18n.ISO8601DateTimeFormat({
  dateFormat: 'calendar',
  timePrecision: 'minutes',
  separatorStyle: 'extended'
});
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let locale = new Intl.Locale('zh-Hans-CN');
let formatter = new i18n.SymbolNumberFormat(locale, {
  style: 'unit',
  unit: 'day',
  zero: '(0)'
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let integerTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let decimalTextStyle: TextStyle = new TextStyle({ fontColor: Color.Brown });
  let fractionTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });
  let unitTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });

  // 通过intl.NumberFormat创建StyledNumberFormat对象
  let numFmt: intl.NumberFormat = new intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });

  // 通过SimpleNumberFormat创建StyledNumberFormat对象
  let locale: intl.Locale = new intl.Locale('zh');
  let simpleNumFmt: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('percent', locale);
  let styledSimpleNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(simpleNumFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.StyledNumberFormat failed, error code: ${err.code}, message: ${err.message}.`);
}
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

  // 通过SimpleNumberFormat创建StyledNumberFormat对象
  let locale: Intl.Locale = new Intl.Locale('zh');
  let simpleNumFmt: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('percent', locale);
  let styledSimpleNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(simpleNumFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.StyledNumberFormat failed, error code: ${err.code}, message: ${err.message}.`);
}
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let numFmt: Intl.NumberFormat = new Intl.NumberFormat('zh-Hans-CN', { style: 'unit', unit: 'fahrenheit' });
let advancedMeasureFormat: i18n.AdvancedMeasureFormat = new i18n.AdvancedMeasureFormat(numFmt, {
  unitUsage: i18n.UnitUsage.TEMPERATURE_PERSON
});
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemLocaleManager: i18n.SystemLocaleManager = new i18n.SystemLocaleManager();
```

## format

```TypeScript
format(phoneNumber: string): string
```

对电话号码进行格式化。

> **说明：**&gt;
> 从API version 12开始，支持对拨号中的电话号码进行格式化。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhoneNumberFormat-format(phoneNumber: string): string--><!--Device-PhoneNumberFormat-format(phoneNumber: string): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 待格式化的电话号码。<br>**起始版本：** 12 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的电话号码。 |

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

## getLocationName

```TypeScript
getLocationName(phoneNumber: string, locale: string): string
```

获取电话号码归属地。

> **说明：**&gt;
> 从API version 23开始，支持对拨号中的电话号码实时获取归属地。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhoneNumberFormat-getLocationName(phoneNumber: string, locale: string): string--><!--Device-PhoneNumberFormat-getLocationName(phoneNumber: string, locale: string): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。获取其他地区电话号码的归属地时，需要在电话号码前加00+国际区号。<br>**起始版本：** 12 |
| locale | string | 是 | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组 成。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 电话号码归属地。无效号码时返回空字符串。 |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// 完整电话号码的归属地获取
let phonenumberFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
let locationName: string = phonenumberFormat.getLocationName('158****2345', 'zh-CN'); // locationName = '广东省湛江市'
let locName: string = phonenumberFormat.getLocationName('0039312****789', 'zh-CN'); // locName = '意大利'

// 拨号中的电话号码归属地获取
let option: i18n.PhoneNumberFormatOptions = { type: 'TYPING' };
let typingFormatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN', option);
let formatResult = typingFormatter.getLocationName('1', 'en'); // formatResult = ''
formatResult = typingFormatter.getLocationName('13', 'en'); // formatResult = 'China'
formatResult = typingFormatter.getLocationName('133', 'en'); // formatResult = 'China'
formatResult = typingFormatter.getLocationName('1334', 'en'); // formatResult = 'China'
formatResult = typingFormatter.getLocationName('13342', 'en'); // formatResult = 'China'
formatResult = typingFormatter.getLocationName('133426', 'en'); // formatResult = 'Dongguan, Guangdong'
```

## isValidNumber

```TypeScript
isValidNumber(phoneNumber: string): boolean
```

判断电话号码是否为当前电话号码格式化对象中国家的有效号码。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhoneNumberFormat-isValidNumber(phoneNumber: string): boolean--><!--Device-PhoneNumberFormat-isValidNumber(phoneNumber: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 待判断的电话号码。<br>**起始版本：** 12 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示电话号码有效，false表示电话号码无效。 |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let formatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
let isValidNumber: boolean = formatter.isValidNumber('158****2312'); // isValidNumber = true
```

