# HolidayManager

Provides holiday data parsing capabilities, such as determining holidays and obtaining the holiday list of a specified year.

**Since:** 23

<!--Device-i18n-export class HolidayManager--><!--Device-i18n-export class HolidayManager-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(icsPath: String)
```

Creates a **HolidayManager** object for parsing holiday data.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HolidayManager-constructor(icsPath: String)--><!--Device-HolidayManager-constructor(icsPath: String)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icsPath | String | Yes | Path of the **.ics** file with the read permission granted for applications. iCalendar is a standard Internet calendar format for storing calendar data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

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

## getHolidayInfoItemArray

```TypeScript
getHolidayInfoItemArray(year?: int): Array<HolidayInfoItem>
```

Obtains the holiday information list of the specified year.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HolidayManager-getHolidayInfoItemArray(year?: int): Array<HolidayInfoItem>--><!--Device-HolidayManager-getHolidayInfoItemArray(year?: int): Array<HolidayInfoItem>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | int | No | Specified year, for example, 2023. The default value is the current year. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[HolidayInfoItem](arkts-localization-i18n-holidayinfoitem-i.md)&gt; | Holiday information list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // Replace /system/lib/US.ics with the actual ICS file path.
  let holidayManager: i18n.HolidayManager = new i18n.HolidayManager('/system/lib/US.ics');
  let holidayInfoItemArray: Array<i18n.HolidayInfoItem> = holidayManager.getHolidayInfoItemArray(2023);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call holidayManager.getHolidayInfoItemArray failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## isHoliday

```TypeScript
isHoliday(date?: Date): boolean
```

Determines whether the specified date is a holiday.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HolidayManager-isHoliday(date?: Date): boolean--><!--Device-HolidayManager-isHoliday(date?: Date): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | No | Date and time. Note: The month starts from **0**. For example, **0** indicates January. The default value is the current date. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the specified date is a holiday, and **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // Replace /system/lib/US.ics with the actual ICS file path.
  let holidayManager: i18n.HolidayManager = new i18n.HolidayManager('/system/lib/US.ics');
  let isHoliday: boolean = holidayManager.isHoliday();
  isHoliday = holidayManager.isHoliday(new Date(2023, 5, 25)); // The date is 2023.06.25.
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call holidayManager.isHoliday failed, error code: ${err.code}, message: ${err.message}.`);
}
```

