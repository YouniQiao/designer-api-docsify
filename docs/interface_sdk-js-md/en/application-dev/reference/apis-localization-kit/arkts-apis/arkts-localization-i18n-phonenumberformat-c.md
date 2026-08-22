# PhoneNumberFormat

Provides phone number management capabilities, such as phone number validity verification, formatting, and home location retrieval.

**Since:** 23

<!--Device-i18n-export class PhoneNumberFormat--><!--Device-i18n-export class PhoneNumberFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(country: string, options?: PhoneNumberFormatOptions)
```

Creates a **PhoneNumberFormat** object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhoneNumberFormat-constructor(country: string, options?: PhoneNumberFormatOptions)--><!--Device-PhoneNumberFormat-constructor(country: string, options?: PhoneNumberFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| country | string | Yes | Country/region to which the phone number to be formatted belongs. |
| options | [PhoneNumberFormatOptions](arkts-localization-i18n-phonenumberformatoptions-i.md) | No | Options for **PhoneNumberFormat** object initialization. The default value is **NATIONAL**. |

**Examples**

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
  // Replace /system/lib/US.ics with the actual ICS file path.
  let holidayManager = new i18n.HolidayManager('/system/lib/US.ics');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.HolidayManager failed, error code: ${err.code}, message: ${err.message}.`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let yearTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let monthTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });
  let dayTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });

  // Create a StyledDateTimeFormat object through Intl.DateTimeFormat.
  let dateFormat: Intl.DateTimeFormat = new Intl.DateTimeFormat('zh-Hans-CN', { dateStyle: 'full' });
  let styledDateFormat: i18n.StyledDateTimeFormat = new i18n.StyledDateTimeFormat(dateFormat, {
    year: yearTextStyle,
    month: monthTextStyle,
    day: dayTextStyle
  });

  let hourTextStyle: TextStyle = new TextStyle({ fontColor: Color.Yellow });
  let minuteTextStyle: TextStyle = new TextStyle({ fontColor: Color.Orange });
  let secondTextStyle: TextStyle = new TextStyle({ fontColor: Color.Pink });

  // Create a StyledDateTimeFormat object through SimpleDateTimeFormat.
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
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let integerTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let decimalTextStyle: TextStyle = new TextStyle({ fontColor: Color.Brown });
  let fractionTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });
  let unitTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });

  // Create a StyledNumberFormat object through intl.NumberFormat.
  let numFmt: intl.NumberFormat = new intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });

  // Create a StyledNumberFormat object through SimpleNumberFormat.
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

  // Create a StyledNumberFormat object through Intl.NumberFormat.
  let numFmt: Intl.NumberFormat = new Intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });

  // Create a StyledNumberFormat object through SimpleNumberFormat.
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

Formats a phone number.

> **Description**
> 
> Formatting dialed phone numbers is supported since API version 12.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhoneNumberFormat-format(phoneNumber: string): string--><!--Device-PhoneNumberFormat-format(phoneNumber: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| phoneNumber | string | Yes | Phone number to be formatted.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| string | Formatted phone number. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let formatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
// formattedPhoneNumber = '158 **** 2312'
let formattedPhoneNumber: string = formatter.format('158****2312');

// Format the phone number being dialed.
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
  let date: Date = new Date(2024, 11, 13); // Set the date to 2024.12.13.

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
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let yearTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let monthTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });
  let dayTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });

  // Create a StyledDateTimeFormat object through Intl.DateTimeFormat.
  let dateFormat: Intl.DateTimeFormat = new Intl.DateTimeFormat('zh-Hans-CN', { dateStyle: 'full' });
  let styledDateFormat: i18n.StyledDateTimeFormat = new i18n.StyledDateTimeFormat(dateFormat, {
    year: yearTextStyle,
    month: monthTextStyle,
    day: dayTextStyle
  });
  let date: Date = new Date(2025, 11, 1);
  // formattedDate.getString() is 'Monday, December 1, 2025'. When formattedDate is displayed, 2025 is in red, 12 is in green, and 1 is in blue.
  let formattedDate: StyledString = styledDateFormat.format(date);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call StyledNumberFormat.format failed, error code: ${err.code}, message: ${err.message}.`);
}
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
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let integerTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let decimalTextStyle: TextStyle = new TextStyle({ fontColor: Color.Brown });
  let fractionTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });
  let unitTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });

  // Create a StyledNumberFormat object through Intl.NumberFormat.
  let numFmt: Intl.NumberFormat = new Intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
  // formattedNumber.getString () is 1,234.568%. In the formatted number, 1,234 is in red, . in brown, 568 in blue, and % in green.
  let formattedNumber: StyledString = styledNumFmt.format(1234.5678);

  // Create a StyledNumberFormat object through SimpleNumberFormat.
  let locale: Intl.Locale = new Intl.Locale('zh');
  let simpleNumFmt: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('percent', locale);
  let styledSimpleNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(simpleNumFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
  // formattedSimpleNumber.getString () is 1,234.5678%. In the formatted number, '1,234' is in red, . in brown, 5678 in blue, and % in green.
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

Obtains the home location of a phone number.

> **Description**
> 
> This API can be used to obtain the home location of a dialed number in real time since API version 23.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhoneNumberFormat-getLocationName(phoneNumber: string, locale: string): string--><!--Device-PhoneNumberFormat-getLocationName(phoneNumber: string, locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| phoneNumber | string | Yes | Phone number. To obtain the home location of a number in other countries/regions, you need to prefix the number with **00** and the country code.<br>**Since:** 12 |
| locale | string | Yes | [System locale](../../../internationalization/i18n-locale-culture.md#how-it-works), which consists of the language, script, and country/region. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Home location of the phone number. If the number is invalid, an empty string is returned. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// Obtain the home location of the complete phone number.
let phonenumberFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
let locationName: string = phonenumberFormat.getLocationName('158****2345', 'zh-CN'); // locationName = 'Zhanjiang, Guangdong Province'
let locName: string = phonenumberFormat.getLocationName('0039312****789', 'zh-CN'); // locName = 'Italy'

// Obtain the home area of the phone number being dialed.
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

Checks whether the phone number is valid for the country/region in the **PhoneNumberFormat** object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhoneNumberFormat-isValidNumber(phoneNumber: string): boolean--><!--Device-PhoneNumberFormat-isValidNumber(phoneNumber: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| phoneNumber | string | Yes | Phone number to be checked.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the phone number is valid. The value **true** indicates that the phone number is valid, and the value **false** indicates the opposite. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let formatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
let isValidNumber: boolean = formatter.isValidNumber('158****2312'); // isValidNumber = true
```

