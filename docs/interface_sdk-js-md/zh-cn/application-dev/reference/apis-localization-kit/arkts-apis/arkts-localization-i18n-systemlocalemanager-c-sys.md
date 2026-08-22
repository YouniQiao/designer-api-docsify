# SystemLocaleManager（系统接口）

提供语言、地区和时区信息排序的能力。

**起始版本：** 23

<!--Device-i18n-export class SystemLocaleManager--><!--Device-i18n-export class SystemLocaleManager-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

创建SystemLocaleManager对象。

**起始版本：** 23

<!--Device-SystemLocaleManager-constructor()--><!--Device-SystemLocaleManager-constructor()-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed. A non-system application calls a system API.<br>**适用版本：** 26.0.0+ |

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

## getLanguageInfoArray

```TypeScript
getLanguageInfoArray(languages: Array<string>, options?: SortOptions): Array<LocaleItem>
```

获取排序后的语言信息列表。

**起始版本：** 23

<!--Device-SystemLocaleManager-getLanguageInfoArray(languages: Array<string>, options?: SortOptions): Array<LocaleItem>--><!--Device-SystemLocaleManager-getLanguageInfoArray(languages: Array<string>, options?: SortOptions): Array<LocaleItem>-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| languages | Array&lt;string&gt; | 是 | 待排序的语言列表，要求是合法的语言ID。 |
| options | [SortOptions](../../apis-default/arkts-apis/arkts-i18n-sortoptions-i-sys.md) | 否 | 语言排序选项。默认值：所有属性都取默认值时的配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[LocaleItem](../../apis-default/arkts-apis/arkts-i18n-localeitem-i-sys.md)&gt; | 排序后的语言信息列表。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../errorcode-i18n.md#890001-参数校验错误) | Invalid parameter. Possible causes: Parameter verification failed. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed. A non-system application calls a system API.<br>**适用版本：** 12+ |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

// 当系统语言为zh-Hans，系统地区为CN，系统区域为zh-Hans-CN时
let systemLocaleManager: i18n.SystemLocaleManager = new i18n.SystemLocaleManager();
let languages: string[] = ["zh-Hans", "en-US", "pt", "ar"];
let sortOptions: i18n.SortOptions = {locale: "zh-Hans-CN", isUseLocalName: true, isSuggestedFirst: true};
try {
    // 排序后的语言顺序为: [zh-Hans, en-US, pt, ar]
    let sortedLanguages: Array<i18n.LocaleItem> = systemLocaleManager.getLanguageInfoArray(languages, sortOptions);
} catch(error) {
    let err: BusinessError = error as BusinessError;
    console.error(`call systemLocaleManager.getLanguageInfoArray failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getRegionInfoArray

```TypeScript
getRegionInfoArray(regions: Array<string>, options?: SortOptions): Array<LocaleItem>
```

获取排序后的国家或地区信息列表。

**起始版本：** 23

<!--Device-SystemLocaleManager-getRegionInfoArray(regions: Array<string>, options?: SortOptions): Array<LocaleItem>--><!--Device-SystemLocaleManager-getRegionInfoArray(regions: Array<string>, options?: SortOptions): Array<LocaleItem>-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| regions | Array&lt;string&gt; | 是 | 待排序的国家或地区列表，要求是合法的国家或地区ID。 |
| options | [SortOptions](../../apis-default/arkts-apis/arkts-i18n-sortoptions-i-sys.md) | 否 | 国家或地区排序选项。 区域ID的默认值为系统当前区域ID，isUseLocalName的默认值为false，isSuggestedFirst的默认值为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[LocaleItem](../../apis-default/arkts-apis/arkts-i18n-localeitem-i-sys.md)&gt; | 排序后的国家或地区信息列表。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../errorcode-i18n.md#890001-参数校验错误) | Invalid parameter. Possible causes: Parameter verification failed. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed. A non-system application calls a system API.<br>**适用版本：** 12+ |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

// 当系统语言为zh-Hans，系统地区为CN，系统区域为zh-Hans-CN时
let systemLocaleManager: i18n.SystemLocaleManager = new i18n.SystemLocaleManager();
let regions: string[] = ["CN", "US", "PT", "EG"];
let sortOptions: i18n.SortOptions = {locale: "zh-Hans-CN", isUseLocalName: false, isSuggestedFirst: true};
try {
    // 排序后的地区顺序为: [CN, EG, US, PT]
    let sortedRegions: Array<i18n.LocaleItem> = systemLocaleManager.getRegionInfoArray(regions, sortOptions);
} catch(error) {
    let err: BusinessError = error as BusinessError;
    console.error(`call systemLocaleManager.getRegionInfoArray failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getTimeZoneCityItemArray

```TypeScript
static getTimeZoneCityItemArray(): Array<TimeZoneCityItem>
```

获取排序后的时区城市组合信息列表。

**起始版本：** 23

<!--Device-SystemLocaleManager-static getTimeZoneCityItemArray(): Array<TimeZoneCityItem>--><!--Device-SystemLocaleManager-static getTimeZoneCityItemArray(): Array<TimeZoneCityItem>-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[TimeZoneCityItem](../../apis-default/arkts-apis/arkts-i18n-timezonecityitem-i-sys.md)&gt; | 排序后的时区城市组合信息列表。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed. A non-system application calls a systemAPI.<br>**适用版本：** 12+ |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let timeZoneCityItemArray: Array<i18n.TimeZoneCityItem> = i18n.SystemLocaleManager.getTimeZoneCityItemArray();
  for (let i = 0; i < timeZoneCityItemArray.length; i++) {
      console.info(timeZoneCityItemArray[i].zoneId + ", " + timeZoneCityItemArray[i].cityId + ", " + timeZoneCityItemArray[i].cityDisplayName +
          ", " + timeZoneCityItemArray[i].offset + "\r\n");
  }
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call SystemLocaleManager.getTimeZoneCityItemArray failed, error code: ${err.code}, message: ${err.message}.`);
}
```

