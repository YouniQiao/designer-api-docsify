# System

提供系统属性相关的能力，包括语言地区名称翻译、支持的语言地区列表获取和系统语言地区获取等。

**起始版本：** 9

<!--Device-i18n-export class System--><!--Device-i18n-export class System-End-->

**系统能力：** SystemCapability.Global.I18n

## addPreferredLanguage

```TypeScript
static addPreferredLanguage(language: string, index?: number): void
```

在系统偏好语言列表的指定位置添加偏好语言。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static addPreferredLanguage(language: string, index?: int): void--><!--Device-System-static addPreferredLanguage(language: string, index?: int): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| language | string | 是 |
| index | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

// 将语言zh-CN添加到系统偏好语言列表中
let language = 'zh-CN';
let index = 0;
try {
  i18n.System.addPreferredLanguage(language, index); // 将zh-CN添加到系统偏好语言列表的第1位
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.addPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getSystemCollations

```TypeScript
static getSystemCollations(): Map<string, string>
```

获取系统支持的排序方式及名称。如系统语言为英文时，可以支持大写在前或小写在前的排序方式。

**起始版本：** 20

<!--Device-System-static getSystemCollations(): Map<string, string>--><!--Device-System-static getSystemCollations(): Map<string, string>-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Map&lt;string, string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let systemCollations: Map<string, string> = i18n.System.getSystemCollations();
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getSystemCollations failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getSystemMeasurements

```TypeScript
static getSystemMeasurements(): Map<string, string>
```

获取系统支持的度量衡及其名称。

**起始版本：** 20

<!--Device-System-static getSystemMeasurements(): Map<string, string>--><!--Device-System-static getSystemMeasurements(): Map<string, string>-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Map&lt;string, string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let systemMeasurements: Map<string, string> = i18n.System.getSystemMeasurements();
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getSystemMeasurements failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getSystemNumberPatterns

```TypeScript
static getSystemNumberPatterns(): Map<string, string>
```

获取系统支持的数字格式及示例。数字格式指数字中的千分符和小数分隔符的格式。

**起始版本：** 20

<!--Device-System-static getSystemNumberPatterns(): Map<string, string>--><!--Device-System-static getSystemNumberPatterns(): Map<string, string>-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Map&lt;string, string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let systemNumberPatterns: Map<string, string> = i18n.System.getSystemNumberPatterns();
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getSystemNumberPatterns failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getSystemNumberingSystems

```TypeScript
static getSystemNumberingSystems(): Map<string, string>
```

获取系统支持的数字系统及示例。示例为数字0~9在对应数字系统下的显示。

**起始版本：** 20

<!--Device-System-static getSystemNumberingSystems(): Map<string, string>--><!--Device-System-static getSystemNumberingSystems(): Map<string, string>-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Map&lt;string, string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let systemNumberingSystems: Map<string, string> = i18n.System.getSystemNumberingSystems();
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getSystemNumberingSystems failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getSystemNumericalDatePatterns

```TypeScript
static getSystemNumericalDatePatterns(): Map<string, string>
```

获取系统支持的数字日期格式及其示例。

**起始版本：** 20

<!--Device-System-static getSystemNumericalDatePatterns(): Map<string, string>--><!--Device-System-static getSystemNumericalDatePatterns(): Map<string, string>-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Map&lt;string, string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let datePatterns: Map<string, string> = i18n.System.getSystemNumericalDatePatterns();
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getSystemNumericalDatePatterns failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getUsingCollation

```TypeScript
static getUsingCollation(): string
```

获取系统当前使用的排序方式。

**起始版本：** 20

<!--Device-System-static getUsingCollation(): string--><!--Device-System-static getUsingCollation(): string-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let usingCollation: string = i18n.System.getUsingCollation();
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getUsingCollation failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getUsingMeasurement

```TypeScript
static getUsingMeasurement(): string
```

获取系统当前使用的度量衡。

**起始版本：** 20

<!--Device-System-static getUsingMeasurement(): string--><!--Device-System-static getUsingMeasurement(): string-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let usingMeasurement: string = i18n.System.getUsingMeasurement();
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getUsingMeasurement failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getUsingNumberPattern

```TypeScript
static getUsingNumberPattern(): string
```

获取系统当前使用的数字格式。

**起始版本：** 20

<!--Device-System-static getUsingNumberPattern(): string--><!--Device-System-static getUsingNumberPattern(): string-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let usingNumberPattern: string = i18n.System.getUsingNumberPattern();
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getUsingNumberPattern failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getUsingNumberingSystem

```TypeScript
static getUsingNumberingSystem(): string
```

获取系统当前使用的数字系统。

**起始版本：** 20

<!--Device-System-static getUsingNumberingSystem(): string--><!--Device-System-static getUsingNumberingSystem(): string-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getUsingNumericalDatePattern

```TypeScript
static getUsingNumericalDatePattern(): string
```

获取系统当前使用的数字日期格式。

**起始版本：** 20

<!--Device-System-static getUsingNumericalDatePattern(): string--><!--Device-System-static getUsingNumericalDatePattern(): string-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let datePattern: string = i18n.System.getUsingNumericalDatePattern();
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getUsingNumericalDatePattern failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## removePreferredLanguage

```TypeScript
static removePreferredLanguage(index: number): void
```

从系统偏好语言列表中移除指定位置的偏好语言。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static removePreferredLanguage(index: int): void--><!--Device-System-static removePreferredLanguage(index: int): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

// 删除系统偏好语言列表中的第一个偏好语言
let index: number = 0;
try {
  i18n.System.removePreferredLanguage(index);
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.removePreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## set24HourClock

```TypeScript
static set24HourClock(option: boolean): void
```

设置系统时制是否为24小时制。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static set24HourClock(option: boolean): void--><!--Device-System-static set24HourClock(option: boolean): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

// 将系统时制设置为24小时制
try {
  i18n.System.set24HourClock(true);
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.set24HourClock failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setFirstDayOfWeek

```TypeScript
static setFirstDayOfWeek(type: WeekDay): void
```

设置系统的周起始日。

**起始版本：** 18

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setFirstDayOfWeek(type: WeekDay): void--><!--Device-System-static setFirstDayOfWeek(type: WeekDay): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [WeekDay](arkts-localization-i18n-weekday-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setFirstDayOfWeek(i18n.WeekDay.MON); // 设置用户偏好的周起始日为周一
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setFirstDayOfWeek failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setSystemCollation

```TypeScript
static setSystemCollation(identifier: string): void
```

设置系统的排序方式。

**起始版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemCollation(identifier: string): void--><!--Device-System-static setSystemCollation(identifier: string): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identifier | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setSystemCollation("zhuyin"); // 如果设置当前系统不支持的排序方式会报错
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setSystemCollation failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setSystemLanguage

```TypeScript
static setSystemLanguage(language: string): void
```

设置系统语言。若要监听系统语言变化，可以监听  
[公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed)OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考  
[系统语言与区域](../../../internationalization/i18n-system-language-region.md#开发步骤)。 &lt;br&gt;**说明：**  &lt;br&gt;可以通过[i18n.System.getSystemLanguage()](../../../reference/apis-localization-kit/js-apis-i18n.md#getsystemlanguage9)接口获取系统语言。 &lt;br&gt;从API version 21开始，也可以使用[param工具](../../../tools/param-tool.md#获取系统参数的值)的“param get persist.global.language”命令获取系统语言。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemLanguage(language: string): void--><!--Device-System-static setSystemLanguage(language: string): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| language | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

// 设置系统语言
try {
  i18n.System.setSystemLanguage('zh'); // 设置系统当前语言为 "zh"
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setSystemLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setSystemLocale

```TypeScript
static setSystemLocale(locale: string): void
```

设置系统区域。

**起始版本：** 9

**废弃版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemLocale(locale: string): void--><!--Device-System-static setSystemLocale(locale: string): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setSystemLocale('zh-CN');  // 设置系统当前区域ID为 "zh-CN"
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setSystemLocale failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setSystemMeasurement

```TypeScript
static setSystemMeasurement(identifier: string): void
```

设置系统的度量衡。

**起始版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemMeasurement(identifier: string): void--><!--Device-System-static setSystemMeasurement(identifier: string): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identifier | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setSystemMeasurement("uksystem"); // 如果设置当前系统不支持的度量衡会抛8900001错误码
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setSystemMeasurement failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setSystemNumberPattern

```TypeScript
static setSystemNumberPattern(pattern: string): void
```

设置系统的数字格式。

**起始版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemNumberPattern(pattern: string): void--><!--Device-System-static setSystemNumberPattern(pattern: string): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pattern | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setSystemNumberPattern("002e002c"); // 如果设置当前系统不支持的数字格式会报错
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setSystemNumberPattern failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setSystemNumberingSystem

```TypeScript
static setSystemNumberingSystem(identifier: string): void
```

设置系统的数字系统。

**起始版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemNumberingSystem(identifier: string): void--><!--Device-System-static setSystemNumberingSystem(identifier: string): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identifier | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setSystemNumberingSystem("arab"); // 如果设置当前系统不支持的数字系统会报错
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setSystemNumberingSystem failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setSystemNumericalDatePattern

```TypeScript
static setSystemNumericalDatePattern(identifier : string): void
```

设置系统的数字日期格式。

**起始版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemNumericalDatePattern(identifier : string): void--><!--Device-System-static setSystemNumericalDatePattern(identifier : string): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identifier | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setSystemNumericalDatePattern("dd/MM/y"); // 如果设置当前系统不支持的数字日期格式，系统会抛出8900001错误码
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setSystemNumericalDatePattern failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setSystemRegion

```TypeScript
static setSystemRegion(region: string): void
```

设置系统地区。若要监听系统地区变化，可以监听  
[公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed)OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考  
[系统语言与区域](../../../internationalization/i18n-system-language-region.md#开发步骤)。 &lt;br&gt;**说明：**  &lt;br&gt;可以通过[i18n.System.getSystemRegion()](../../../reference/apis-localization-kit/js-apis-i18n.md#getsystemregion9)接口获取系统地区。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemRegion(region: string): void--><!--Device-System-static setSystemRegion(region: string): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setSystemRegion('CN');  // 设置系统当前地区为 "CN"
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setSystemRegion failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setTemperatureType

```TypeScript
static setTemperatureType(type: TemperatureType): void
```

设置系统的温度单位。

**起始版本：** 18

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setTemperatureType(type: TemperatureType): void--><!--Device-System-static setTemperatureType(type: TemperatureType): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [TemperatureType](arkts-localization-i18n-temperaturetype-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setTemperatureType(i18n.TemperatureType.CELSIUS); // 设置温度单位为摄氏度
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setTemperatureType failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setUsingLocalDigit

```TypeScript
static setUsingLocalDigit(flag: boolean): void
```

设置系统是否使用本地数字。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setUsingLocalDigit(flag: boolean): void--><!--Device-System-static setUsingLocalDigit(flag: boolean): void-End-->

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setUsingLocalDigit(true); // 打开本地化数字开关
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setUsingLocalDigit failed, error code: ${err.code}, message: ${err.message}.`);
}
```
