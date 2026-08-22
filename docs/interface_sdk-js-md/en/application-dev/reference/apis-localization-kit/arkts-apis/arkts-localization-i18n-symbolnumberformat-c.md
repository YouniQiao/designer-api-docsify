# SymbolNumberFormat

Provide a Number formatting interface that supports custom symbols. This interface formats number values into strings with custom symbols, and can replace variable symbols in the formatted result with custom fixed symbols (e.g., replacing "null" to "NA").

**Inheritance/Implementation:** SymbolNumberFormat implements Intl.NumberFormat

**Since:** 26.0.0

<!--Device-i18n-export class SymbolNumberFormat--><!--Device-i18n-export class SymbolNumberFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)
```

A constructor used to create a SymbolNumberFormat object.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)--><!--Device-SymbolNumberFormat-public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | Intl.Locale | No | Locale object used for formatting the date time value. The default value is the current system locale. <br>Default value:The default is the current system locale. <br>Default Value: System Locale. <br>Region object. |
| options | [SymbolNumberFormatOptions](arkts-localization-i18n-symbolnumberformatoptions-i.md) | No | Indicates the symbols used to replace. Such as zero, nan, positiveInfinity, etc. <br>Symbol Number Formatting Options. |

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
public format(value: number | bigint): string
```

Formats a number with give locale and SymbolNumberFormatOptions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public format(value: number | bigint): string--><!--Device-SymbolNumberFormat-public format(value: number | bigint): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| bigint | Yes | Number to be formatted. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Formatted number. |

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

## formatRange

```TypeScript
public formatRange(startRange: number, endRange: number): string
```

Formats a number range.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public formatRange(startRange: number, endRange: number): string--><!--Device-SymbolNumberFormat-public formatRange(startRange: number, endRange: number): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startRange | number | Yes | Start number of the range. |
| endRange | number | Yes | End number of the range. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Formatted number range. |

## formatRangeToParts

```TypeScript
public formatRangeToParts(startRange: number, endRange: number): Intl.NumberFormatPart[]
```

Formats a number range into parts.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public formatRangeToParts(startRange: number, endRange: number): Intl.NumberFormatPart[]--><!--Device-SymbolNumberFormat-public formatRangeToParts(startRange: number, endRange: number): Intl.NumberFormatPart[]-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startRange | number | Yes | Start number of the range. |
| endRange | number | Yes | End number of the range. |

**Return value:**

| Type | Description |
| --- | --- |
| Intl.NumberFormatPart[] | Locale formatted NumberFormatPart array. |

## formatToParts

```TypeScript
public formatToParts(value?: number | bigint): Intl.NumberFormatPart[]
```

Formats a number into parts.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public formatToParts(value?: number | bigint): Intl.NumberFormatPart[]--><!--Device-SymbolNumberFormat-public formatToParts(value?: number | bigint): Intl.NumberFormatPart[]-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| bigint | No | Number to be formatted. |

**Return value:**

| Type | Description |
| --- | --- |
| Intl.NumberFormatPart[] | Locale formatted NumberFormatPart array. |

## parse

```TypeScript
public parse(text: string, lenientMode: boolean): number
```

Parse a localized string to number object. For example, "123,456" will parse to 123456.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public parse(text: string, lenientMode: boolean): number--><!--Device-SymbolNumberFormat-public parse(text: string, lenientMode: boolean): number-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Localized string to be parse. <br>Text to be parsed |
| lenientMode | boolean | Yes | Indicates whether parsing allows any non-compliant localized strings. For example, "1,23,456" is a invalid thousand separator number string, it will parse failure when lenientMode is false, and will parse success with value 123456 when lenientMode is true.it's better set to false, ensure the data is not polluted. <br>Whether to use loose rules |

**Return value:**

| Type | Description |
| --- | --- |
| number | The result parse with localization rules. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSymbolNumberFormatOptions
```

Represents optional element for the ResolvedSymbolDateTimeFormatOptions object. Define the resolved symbol element and value that need to get.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SymbolNumberFormat-public resolvedOptions(): ResolvedSymbolNumberFormatOptions--><!--Device-SymbolNumberFormat-public resolvedOptions(): ResolvedSymbolNumberFormatOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [ResolvedSymbolNumberFormatOptions](arkts-localization-i18n-resolvedsymbolnumberformatoptions-i.md) | Symbol options for SymbolNumberFormat. |

