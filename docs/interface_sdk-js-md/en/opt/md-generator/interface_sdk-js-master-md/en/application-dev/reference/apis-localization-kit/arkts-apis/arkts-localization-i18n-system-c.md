# System

Provides system attribute configuration functions, including translating language and country/region names, obtaining the list of supported languages and countries/regions, and obtaining the system language and region.

**Since:** 23

**Deprecated since:** -1

<!--Device-i18n-export class System--><!--Device-i18n-export class System-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getAppPreferredLanguage

```TypeScript
static getAppPreferredLanguage(): string
```

Obtains the preferred language of an application.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-System-static getAppPreferredLanguage(): string--><!--Device-System-static getAppPreferredLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let appPreferredLanguage: string = i18n.System.getAppPreferredLanguage();
```

## getDisplayCountry

```TypeScript
static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string
```

Obtains the country/region display name in the specified language.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-System-static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string--><!--Device-System-static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| country | string | Yes |
| locale | string | Yes |
| sentenceCase | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let displayCountry: string = i18n.System.getDisplayCountry('CN', 'en-GB'); // displayCountry = 'China'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getDisplayCountry failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getDisplayLanguage

```TypeScript
static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string
```

Obtains the language display name in the specified language.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-System-static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string--><!--Device-System-static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| language | string | Yes |
| locale | string | Yes |
| sentenceCase | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // Obtain the display name of Chinese in English.
  let displayLanguage: string = i18n.System.getDisplayLanguage('zh', 'en-GB'); // displayLanguage = 'Chinese'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getDisplayLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getFirstDayOfWeek

```TypeScript
static getFirstDayOfWeek(): WeekDay
```

Obtains the first day of a week in the system settings.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getFirstDayOfWeek(): WeekDay--><!--Device-System-static getFirstDayOfWeek(): WeekDay-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WeekDay](arkts-localization-i18n-weekday-e.md) |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let firstDayOfWeek: i18n.WeekDay = i18n.System.getFirstDayOfWeek();
```

## getFirstPreferredLanguage

```TypeScript
static getFirstPreferredLanguage(): string
```

Obtains the first language in the preferred language list.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-System-static getFirstPreferredLanguage(): string--><!--Device-System-static getFirstPreferredLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let firstPreferredLanguage: string = i18n.System.getFirstPreferredLanguage();
```

## getPreferredLanguageList

```TypeScript
static getPreferredLanguageList(): Array<string>
```

Obtains the list of preferred languages.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-System-static getPreferredLanguageList(): Array<string>--><!--Device-System-static getPreferredLanguageList(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let preferredLanguageList: Array<string> = i18n.System.getPreferredLanguageList();
```

## getSimplifiedLanguage

```TypeScript
static getSimplifiedLanguage(language?: string): string
```

Obtains the simplified representation of a language. For example, the simplified representation of **en-Latn-US** is **en**, and that of **en-Latn-GB** is **en-GB**.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSimplifiedLanguage(language?: string): string--><!--Device-System-static getSimplifiedLanguage(language?: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| language | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // simplifiedLanguage = 'zh'
  let simplifiedLanguage: string = i18n.System.getSimplifiedLanguage('zh-Hans-CN');
  // Obtain the simplified representation of the current system language.
  let simplifiedSystemLanguage: string = i18n.System.getSimplifiedLanguage();
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getSimplifiedLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getSystemCountries

```TypeScript
static getSystemCountries(language: string): Array<string>
```

Obtains the list of countries/regions supported for the specified language.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-System-static getSystemCountries(language: string): Array<string>--><!--Device-System-static getSystemCountries(language: string): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| language | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // systemCountries = [ 'ZW', 'YT', 'YE', ..., 'ER', 'CN', 'DE' ]
  let systemCountries: Array<string> = i18n.System.getSystemCountries('zh');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getSystemCountries failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getSystemLanguage

```TypeScript
static getSystemLanguage(): string
```

Obtains the current system language. To listen for system language changes, enable listening for [COMMON_EVENT_LOCALE_CHANGED](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed) . For details, see [System Language and Region](../../../internationalization/i18n-system-language-region.md#how-to-develop).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-System-static getSystemLanguage(): string--><!--Device-System-static getSystemLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemLanguage: string = i18n.System.getSystemLanguage(); // If the system language is simplified Chinese, then systemLanguage is 'zh-Hans'.
```

## getSystemLanguages

```TypeScript
static getSystemLanguages(): Array<string>
```

Obtains the list of system languages. Since API version 11, this API is supported in ArkTS widgets.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-System-static getSystemLanguages(): Array<string>--><!--Device-System-static getSystemLanguages(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// systemLanguages = [ 'ug', 'bo', 'zh-Hant', 'en-Latn-US', 'zh-Hans' ]
let systemLanguages: Array<string> = i18n.System.getSystemLanguages();
```

## getSystemLocale

```TypeScript
static getSystemLocale(): string
```

Obtains the current system locale.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getSystemLocaleInstance](#getSystemLocaleInstance)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-System-static getSystemLocale(): string--><!--Device-System-static getSystemLocale(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemLocale: string = i18n.System.getSystemLocale(); // If the system language is simplified Chinese and the system region is China, then systemLocale is zh-Hans-CN.
```

## getSystemLocaleInstance

```TypeScript
static getSystemLocaleInstance(): Intl.Locale
```

Obtains the current system locale. To listen for system locale changes, enable listening for [COMMON_EVENT_LOCALE_CHANGED](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed) . For details, see [System Language and Region](../../../internationalization/i18n-system-language-region.md#how-to-develop).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSystemLocaleInstance(): Intl.Locale--><!--Device-System-static getSystemLocaleInstance(): Intl.Locale-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Intl.Locale |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemLocale: Intl.Locale = i18n.System.getSystemLocaleInstance();
```

## getSystemRegion

```TypeScript
static getSystemRegion(): string
```

Obtains the current system country/region. To listen for system region changes, enable listening for [COMMON_EVENT_LOCALE_CHANGED](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed) . For details, see [System Language and Region](../../../internationalization/i18n-system-language-region.md#how-to-develop).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-System-static getSystemRegion(): string--><!--Device-System-static getSystemRegion(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemRegion: string = i18n.System.getSystemRegion(); // If the system region is China, then systemRegion is CN.
```

## getTemperatureName

```TypeScript
static getTemperatureName(type: TemperatureType): string
```

Obtains the name of a temperature unit.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getTemperatureName(type: TemperatureType): string--><!--Device-System-static getTemperatureName(type: TemperatureType): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [TemperatureType](arkts-localization-i18n-temperaturetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // temperatureName = 'celsius'
  let temperatureName: string = i18n.System.getTemperatureName(i18n.TemperatureType.CELSIUS);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getTemperatureName failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getTemperatureType

```TypeScript
static getTemperatureType(): TemperatureType
```

Obtains the temperature unit of the system.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getTemperatureType(): TemperatureType--><!--Device-System-static getTemperatureType(): TemperatureType-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TemperatureType](arkts-localization-i18n-temperaturetype-e.md) |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let temperatureType: i18n.TemperatureType = i18n.System.getTemperatureType();
```

## getUsingLocalDigit

```TypeScript
static getUsingLocalDigit(): boolean
```

Checks whether use of local digits is enabled.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-System-static getUsingLocalDigit(): boolean--><!--Device-System-static getUsingLocalDigit(): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let usingLocalDigit: boolean = i18n.System.getUsingLocalDigit();
```

## is24HourClock

```TypeScript
static is24HourClock(): boolean
```

Checks whether the 24-hour clock is used. To listen for system time format changes, enable listening for [COMMON_EVENT_TIME_CHANGED](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_time_changed) . For details, see [User Preference](../../../internationalization/i18n-user-preferences.md#how-to-develop).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-System-static is24HourClock(): boolean--><!--Device-System-static is24HourClock(): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let is24HourClock: boolean = i18n.System.is24HourClock(); // If the 24-hour clock is used, then is24HourClock is true.
```

## isSuggested

```TypeScript
static isSuggested(language: string, region?: string): boolean
```

Checks whether a language is a suggested language in the specified region. It can be used for region-based language recommendation or language-based region recommendation.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-System-static isSuggested(language: string, region?: string): boolean--><!--Device-System-static isSuggested(language: string, region?: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| language | string | Yes |
| region | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let isSuggestedCountry: boolean = i18n.System.isSuggested('zh', 'CN'); // isSuggestedCountry = true
  isSuggestedCountry = i18n.System.isSuggested('en'); // Check whether a language is a suggested language for the current system region.
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.isSuggested failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## setAppPreferredLanguage

```TypeScript
static setAppPreferredLanguage(language: string): void
```

Sets the preferred language of the application. Resources are loaded in the preferred language when the application is launched. If the preferred language is set to **default**, the application's language will be the same as the system language, and the setting will take effect upon cold starting of the application.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-System-static setAppPreferredLanguage(language: string): void--><!--Device-System-static setAppPreferredLanguage(language: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| language | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setAppPreferredLanguage('zh');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```
