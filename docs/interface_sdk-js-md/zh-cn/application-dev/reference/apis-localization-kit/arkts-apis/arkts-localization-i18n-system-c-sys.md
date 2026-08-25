# System

提供系统属性相关的能力，包括语言地区名称翻译、支持的语言地区列表获取和系统语言地区获取等。

**起始版本：** 9

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## addPreferredLanguage

```TypeScript
static addPreferredLanguage(language: string, index?: number): void
```

在系统偏好语言列表的指定位置添加偏好语言。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSystemCollations

```TypeScript
static getSystemCollations(): Map<string, string>
```

获取系统支持的排序方式及名称。如系统语言为英文时，可以支持大写在前或小写在前的排序方式。

**起始版本：** 20

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Map & lt;string, string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSystemMeasurements

```TypeScript
static getSystemMeasurements(): Map<string, string>
```

获取系统支持的度量衡及其名称。

**起始版本：** 20

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Map & lt;string, string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSystemNumberingSystems

```TypeScript
static getSystemNumberingSystems(): Map<string, string>
```

获取系统支持的数字系统及示例。示例为数字0~9在对应数字系统下的显示。

**起始版本：** 20

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Map & lt;string, string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSystemNumberPatterns

```TypeScript
static getSystemNumberPatterns(): Map<string, string>
```

获取系统支持的数字格式及示例。数字格式指数字中的千分符和小数分隔符的格式。

**起始版本：** 20

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Map & lt;string, string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSystemNumericalDatePatterns

```TypeScript
static getSystemNumericalDatePatterns(): Map<string, string>
```

获取系统支持的数字日期格式及其示例。

**起始版本：** 20

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Map & lt;string, string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getUsingCollation

```TypeScript
static getUsingCollation(): string
```

获取系统当前使用的排序方式。

**起始版本：** 20

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

## getUsingMeasurement

```TypeScript
static getUsingMeasurement(): string
```

获取系统当前使用的度量衡。

**起始版本：** 20

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

## getUsingNumberingSystem

```TypeScript
static getUsingNumberingSystem(): string
```

获取系统当前使用的数字系统。

**起始版本：** 20

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

## getUsingNumberPattern

```TypeScript
static getUsingNumberPattern(): string
```

获取系统当前使用的数字格式。

**起始版本：** 20

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

## removePreferredLanguage

```TypeScript
static removePreferredLanguage(index: number): void
```

从系统偏好语言列表中移除指定位置的偏好语言。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## set24HourClock

```TypeScript
static set24HourClock(option: boolean): void
```

设置系统时制是否为24小时制。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setFirstDayOfWeek

```TypeScript
static setFirstDayOfWeek(type: WeekDay): void
```

设置系统的周起始日。

**起始版本：** 18

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

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

## setSystemCollation

```TypeScript
static setSystemCollation(identifier: string): void
```

设置系统的排序方式。

**起始版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identifier | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |

## setSystemLanguage

```TypeScript
static setSystemLanguage(language: string): void
```

设置系统语言。若要监听系统语言变化，可以监听 [公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed) OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考 [系统语言与区域](../../../internationalization/i18n-system-language-region.md#开发步骤)。   
**说明：** 可以通过[i18n.System.getSystemLanguage()](../../../reference/apis-localization-kit/js-apis-i18n.md#getsystemlanguage9)接口获取系统语言。 从API version 21开始，也可以使用[param工具](../../../tools/param-tool.md#获取系统参数的值)的“param get persist.global.language”命令获取系统语言。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| language | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setSystemLocale

```TypeScript
static setSystemLocale(locale: string): void
```

设置系统区域。

**起始版本：** 9

**废弃版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## setSystemMeasurement

```TypeScript
static setSystemMeasurement(identifier: string): void
```

设置系统的度量衡。

**起始版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identifier | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |

## setSystemNumberingSystem

```TypeScript
static setSystemNumberingSystem(identifier: string): void
```

设置系统的数字系统。

**起始版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identifier | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |

## setSystemNumberPattern

```TypeScript
static setSystemNumberPattern(pattern: string): void
```

设置系统的数字格式。

**起始版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |

## setSystemNumericalDatePattern

```TypeScript
static setSystemNumericalDatePattern(identifier : string): void
```

设置系统的数字日期格式。

**起始版本：** 20

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identifier | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |

## setSystemRegion

```TypeScript
static setSystemRegion(region: string): void
```

设置系统地区。若要监听系统地区变化，可以监听 [公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed) OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考 [系统语言与区域](../../../internationalization/i18n-system-language-region.md#开发步骤)。   
**说明：** 可以通过[i18n.System.getSystemRegion()](../../../reference/apis-localization-kit/js-apis-i18n.md#getsystemregion9)接口获取系统地区。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setTemperatureType

```TypeScript
static setTemperatureType(type: TemperatureType): void
```

设置系统的温度单位。

**起始版本：** 18

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

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

## setUsingLocalDigit

```TypeScript
static setUsingLocalDigit(flag: boolean): void
```

设置系统是否使用本地数字。

**起始版本：** 9

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
