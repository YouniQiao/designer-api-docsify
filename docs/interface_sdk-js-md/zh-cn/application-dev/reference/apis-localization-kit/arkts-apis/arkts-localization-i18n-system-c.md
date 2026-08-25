# System

提供系统属性相关的能力，包括语言地区名称翻译、支持的语言地区列表获取和系统语言地区获取等。

**起始版本：** 9

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getAppPreferredLanguage

```TypeScript
static getAppPreferredLanguage(): string
```

获取应用偏好语言。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

## getDisplayCountry

```TypeScript
static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string
```

获取国家地区名称在指定语言下的翻译。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| country | string | 是 |
| locale | string | 是 |
| sentenceCase | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## getDisplayLanguage

```TypeScript
static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string
```

获取语言名称在指定语言下的翻译。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| language | string | 是 |
| locale | string | 是 |
| sentenceCase | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## getFirstDayOfWeek

```TypeScript
static getFirstDayOfWeek(): WeekDay
```

获取系统设置的周起始日。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [WeekDay](arkts-localization-i18n-weekday-e.md) |

## getFirstPreferredLanguage

```TypeScript
static getFirstPreferredLanguage(): string
```

获取系统偏好语言列表中的第一个语言。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

## getPreferredLanguageList

```TypeScript
static getPreferredLanguageList(): Array<string>
```

获取系统偏好语言列表。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## getSimplifiedLanguage

```TypeScript
static getSimplifiedLanguage(language?: string): string
```

获取语言的简化表示。例如：'en-Latn-US'的简化表示为'en'，'en-Latn-GB'的简化表示为'en-GB'。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| language | string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## getSystemCountries

```TypeScript
static getSystemCountries(language: string): Array<string>
```

获取输入语言下系统支持的国家地区列表。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| language | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## getSystemLanguage

```TypeScript
static getSystemLanguage(): string
```

获取系统当前设置的语言。若要监听系统语言变化，可以监听 [公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed) OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考 [系统语言与区域](../../../internationalization/i18n-system-language-region.md#开发步骤)。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

## getSystemLanguages

```TypeScript
static getSystemLanguages(): Array<string>
```

获取系统支持的语言列表。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## getSystemLocale

```TypeScript
static getSystemLocale(): string
```


> [System.getSystemLocaleInstance](#getsystemlocaleinstance)代替。
> 获取系统当前设置的区域。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [getSystemLocaleInstance](#getsystemlocaleinstance)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

## getSystemLocaleInstance

```TypeScript
static getSystemLocaleInstance(): Intl.Locale
```

获取系统当前设置的区域对象。若要监听系统区域变化，可以监听 [公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed) OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考 [系统语言与区域](../../../internationalization/i18n-system-language-region.md#开发步骤)。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| Intl.Locale |

## getSystemRegion

```TypeScript
static getSystemRegion(): string
```

获取系统当前设置的国家地区。若要监听系统地区变化，可以监听 [公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed) OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考 [系统语言与区域](../../../internationalization/i18n-system-language-region.md#开发步骤)。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

## getTemperatureName

```TypeScript
static getTemperatureName(type: TemperatureType): string
```

获取温度单位的名称。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [TemperatureType](arkts-localization-i18n-temperaturetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## getTemperatureType

```TypeScript
static getTemperatureType(): TemperatureType
```

获取系统设置的温度单位。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [TemperatureType](arkts-localization-i18n-temperaturetype-e.md) |

## getUsingLocalDigit

```TypeScript
static getUsingLocalDigit(): boolean
```

判断系统是否使用本地数字。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| boolean |

## is24HourClock

```TypeScript
static is24HourClock(): boolean
```

判断系统时制是否为24小时制。若要监听系统时制变化，可以监听 [公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_time_changed) OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_TIME_CHANGED，具体可参考 [用户偏好](../../../internationalization/i18n-user-preferences.md#开发步骤)。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| boolean |

## isSuggested

```TypeScript
static isSuggested(language: string, region?: string): boolean
```

判断语言是否是地区的推荐语言。用于根据地区推荐语言或根据语言推荐地区。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| language | string | 是 |
| region | string | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## setAppPreferredLanguage

```TypeScript
static setAppPreferredLanguage(language: string): void
```

设置应用偏好语言。设置后，应用将优先加载应用偏好语言对应的资源。设置偏好语言为'default'后，应用语言将跟随系统语言，应用冷启动生效。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| language | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |
