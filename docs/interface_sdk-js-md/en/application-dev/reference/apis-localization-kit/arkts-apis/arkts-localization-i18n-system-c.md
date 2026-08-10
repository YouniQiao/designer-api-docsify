# System

提供系统属性相关的能力，包括语言地区名称翻译、支持的语言地区列表获取和系统语言地区获取等。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class System--><!--Device-i18n-export class System-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getAppPreferredLanguage

```TypeScript
static getAppPreferredLanguage(): string
```

获取应用偏好语言。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getAppPreferredLanguage(): string--><!--Device-System-static getAppPreferredLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | 应用偏好语言。 |

## getDisplayCountry

```TypeScript
static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string
```

获取国家地区名称在指定语言下的翻译。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string--><!--Device-System-static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| country | string | Yes | 国家地区，要求是[合法的国家地区码](../../../internationalization/i18n-locale-culture.md#实现原理)。 |
| locale | string | Yes | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组 成。 |
| sentenceCase | boolean | No | true表示按照首字母大写的格式显示文本，false表示按照区域默认的大小写格式显示文本。默认值：true。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 国家地区名称在指定语言下的翻译。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

## getDisplayLanguage

```TypeScript
static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string
```

获取语言名称在指定语言下的翻译。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string--><!--Device-System-static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | 语言，要求是[合法的语言ID](../../../internationalization/i18n-locale-culture.md#实现原理)。 |
| locale | string | Yes | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组 成。 |
| sentenceCase | boolean | No | true表示按照首字母大写的格式显示文本，false表示按照区域默认的大小写格式显示文本。默认值：true。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 语言名称在指定语言下的翻译。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

## getFirstDayOfWeek

```TypeScript
static getFirstDayOfWeek(): WeekDay
```

获取系统设置的周起始日。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getFirstDayOfWeek(): WeekDay--><!--Device-System-static getFirstDayOfWeek(): WeekDay-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [WeekDay](arkts-localization-i18n-weekday-e.md) | 周起始日。 |

## getFirstPreferredLanguage

```TypeScript
static getFirstPreferredLanguage(): string
```

获取系统偏好语言列表中的第一个语言。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getFirstPreferredLanguage(): string--><!--Device-System-static getFirstPreferredLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | 系统偏好语言列表中的第一个语言。 |

## getPreferredLanguageList

```TypeScript
static getPreferredLanguageList(): Array<string>
```

获取系统偏好语言列表。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getPreferredLanguageList(): Array<string>--><!--Device-System-static getPreferredLanguageList(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 系统偏好语言列表。 |

## getSimplifiedLanguage

```TypeScript
static getSimplifiedLanguage(language?: string): string
```

获取语言的简化表示。例如：'en-Latn-US'的简化表示为'en'，'en-Latn-GB'的简化表示为'en-GB'。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSimplifiedLanguage(language?: string): string--><!--Device-System-static getSimplifiedLanguage(language?: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | No | [合法的语言ID](../../../internationalization/i18n-locale-culture.md#实现原理)。默认值：系统语言。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 不传入language时，会根据系统语言和地区判断是否存在系统支持的方言，若存在则返回方言的简化表示；若不存在，则返回系统语言的简化表示。 &lt;br&gt;传入language时，返回language的简化表示。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

## getSystemCountries

```TypeScript
static getSystemCountries(language: string): Array<string>
```

获取输入语言下系统支持的国家地区列表。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSystemCountries(language: string): Array<string>--><!--Device-System-static getSystemCountries(language: string): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | [合法的语言ID](../../../internationalization/i18n-locale-culture.md#实现原理)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | language参数指定的语言下，系统支持的国家/地区列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

## getSystemLanguage

```TypeScript
static getSystemLanguage(): string
```

获取系统当前设置的语言。若要监听系统语言变化，可以监听  
[公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed)OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考  
[系统语言与区域](../../../internationalization/i18n-system-language-region.md#开发步骤)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-System-static getSystemLanguage(): string--><!--Device-System-static getSystemLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示语言ID的字符串。 |

## getSystemLanguages

```TypeScript
static getSystemLanguages(): Array<string>
```

获取系统支持的语言列表。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSystemLanguages(): Array<string>--><!--Device-System-static getSystemLanguages(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 系统支持的语言列表。 |

## getSystemLocaleInstance

```TypeScript
static getSystemLocaleInstance(): Intl.Locale
```

获取系统当前设置的区域对象。若要监听系统区域变化，可以监听  
[公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed)OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考  
[系统语言与区域](../../../internationalization/i18n-system-language-region.md#开发步骤)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSystemLocaleInstance(): Intl.Locale--><!--Device-System-static getSystemLocaleInstance(): Intl.Locale-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Intl.Locale | the locale object currently used by the system. |

## getSystemRegion

```TypeScript
static getSystemRegion(): string
```

获取系统当前设置的国家地区。若要监听系统地区变化，可以监听  
[公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed)OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考  
[系统语言与区域](../../../internationalization/i18n-system-language-region.md#开发步骤)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSystemRegion(): string--><!--Device-System-static getSystemRegion(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示国家地区ID的字符串。 |

## getTemperatureName

```TypeScript
static getTemperatureName(type: TemperatureType): string
```

获取温度单位的名称。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getTemperatureName(type: TemperatureType): string--><!--Device-System-static getTemperatureName(type: TemperatureType): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [TemperatureType](arkts-localization-i18n-temperaturetype-e.md) | Yes | 温度单位。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回温度单位的名称，包括celsius，fahrenheit，kelvin。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

## getTemperatureType

```TypeScript
static getTemperatureType(): TemperatureType
```

获取系统设置的温度单位。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getTemperatureType(): TemperatureType--><!--Device-System-static getTemperatureType(): TemperatureType-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [TemperatureType](arkts-localization-i18n-temperaturetype-e.md) | 温度单位。 |

## getUsingLocalDigit

```TypeScript
static getUsingLocalDigit(): boolean
```

判断系统是否使用本地数字。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getUsingLocalDigit(): boolean--><!--Device-System-static getUsingLocalDigit(): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示系统当前使用本地数字，false表示系统当前不使用本地数字。 |

## is24HourClock

```TypeScript
static is24HourClock(): boolean
```

判断系统时制是否为24小时制。若要监听系统时制变化，可以监听  
[公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_time_changed)OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_TIME_CHANGED，具体可参考  
[用户偏好](../../../internationalization/i18n-user-preferences.md#开发步骤)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-System-static is24HourClock(): boolean--><!--Device-System-static is24HourClock(): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示系统时制为24小时制，false表示系统时制为12小时制。 |

## isSuggested

```TypeScript
static isSuggested(language: string, region?: string): boolean
```

判断语言是否是地区的推荐语言。用于根据地区推荐语言或根据语言推荐地区。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static isSuggested(language: string, region?: string): boolean--><!--Device-System-static isSuggested(language: string, region?: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | [合法的语言ID](../../../internationalization/i18n-locale-culture.md#实现原理)，例如zh。 |
| region | string | No | [合法的国家地区码](../../../internationalization/i18n-locale-culture.md#实现原理)，例如CN。 &lt;br&gt;默认值：SIM卡国家地区。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示语言是地区的推荐语言，false表示语言不是地区的推荐语言。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

## setAppPreferredLanguage

```TypeScript
static setAppPreferredLanguage(language: string): void
```

设置应用偏好语言。设置后，应用将优先加载应用偏好语言对应的资源。设置偏好语言为'default'后，应用语言将跟随系统语言，应用冷启动生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static setAppPreferredLanguage(language: string): void--><!--Device-System-static setAppPreferredLanguage(language: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | [合法的语言ID](../../../internationalization/i18n-locale-culture.md#实现原理)或'default'。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

