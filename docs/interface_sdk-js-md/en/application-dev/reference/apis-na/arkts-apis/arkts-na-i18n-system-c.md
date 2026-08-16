# System

Provides system functions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-i18n-export class System--><!--Device-i18n-export class System-End-->

**System capability:** SystemCapability.Global.I18n

## getAppPreferredLanguage

```TypeScript
static getAppPreferredLanguage(): string
```

Obtains the preferred language of an application.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getAppPreferredLanguage(): string--><!--Device-System-static getAppPreferredLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | Preferred language of the application. |

## getDisplayCountry

```TypeScript
static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string
```

Obtains the country/region display name in the specified language.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string--><!--Device-System-static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| country | string | Yes | Valid country/region code. |
| locale | string | Yes | System locale, which consists of the language, script, and country/region. |
| sentenceCase | boolean | No | Whether to use sentence case to display the text. The value "true" means to display the text in title case format, and the value "false" means to display the text in the default case format of the locale. The default value is true. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Country/region display name in the specified language. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getDisplayLanguage

```TypeScript
static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string
```

Obtains the language display name in the specified language.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string--><!--Device-System-static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | Valid language ID. |
| locale | string | Yes | System locale, which consists of the language, script, and country/region. |
| sentenceCase | boolean | No | Whether to use sentence case to display the text. The value "true" means to display the text in title case format, and the value "false" means to display the text in the default case format of the locale. The default value is true. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Language display name in the specified language. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getFirstDayOfWeek

```TypeScript
static getFirstDayOfWeek(): WeekDay
```

Obtains the first day of a week in the system settings.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getFirstDayOfWeek(): WeekDay--><!--Device-System-static getFirstDayOfWeek(): WeekDay-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [WeekDay](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-weekday-e.md) | Start day of a week. |

## getFirstPreferredLanguage

```TypeScript
static getFirstPreferredLanguage(): string
```

Obtains the first language in the preferred language list.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getFirstPreferredLanguage(): string--><!--Device-System-static getFirstPreferredLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | First language in the preferred language list. |

## getPreferredLanguageList

```TypeScript
static getPreferredLanguageList(): Array<string>
```

Obtains the list of preferred languages.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getPreferredLanguageList(): Array<string>--><!--Device-System-static getPreferredLanguageList(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | List of preferred languages. |

## getSimplifiedLanguage

```TypeScript
static getSimplifiedLanguage(language?: string): string
```

Obtains the simplified representation of a language. For example, the simplified representation of "en-Latn-US" is "en", and that of "en-Latn-GB" is "en-GB".

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSimplifiedLanguage(language?: string): string--><!--Device-System-static getSimplifiedLanguage(language?: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | No | Valid language ID. The default value is the system language. |

**Return value:**

| Type | Description |
| --- | --- |
| string | If language is not passed, the application checks for dialects supported by the system based on the system language and locale. If such a dialect is found, the simplified representation of the dialect is returned. Otherwise, the simplified representation of the system language is returned. If language is passed, the simplified representation of the specified language is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getSystemCountries

```TypeScript
static getSystemCountries(language: string): Array<string>
```

Obtains the list of countries/regions supported for the specified language.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSystemCountries(language: string): Array<string>--><!--Device-System-static getSystemCountries(language: string): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | Valid language ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | List of countries/regions supported for the specified language. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getSystemLanguage

```TypeScript
static getSystemLanguage(): string
```

Obtains the current system language.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-System-static getSystemLanguage(): string--><!--Device-System-static getSystemLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | Language ID. |

## getSystemLanguages

```TypeScript
static getSystemLanguages(): Array<string>
```

Obtains the list of system languages.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSystemLanguages(): Array<string>--><!--Device-System-static getSystemLanguages(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | List of system languages. |

## getSystemLocaleInstance

```TypeScript
static getSystemLocaleInstance(): Intl.Locale
```

Obtains the locale object currently used by the system.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

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

Obtains the current system country/region.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getSystemRegion(): string--><!--Device-System-static getSystemRegion(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | Country/region ID. |

## getTemperatureName

```TypeScript
static getTemperatureName(type: TemperatureType): string
```

Obtains the name of a temperature unit.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getTemperatureName(type: TemperatureType): string--><!--Device-System-static getTemperatureName(type: TemperatureType): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [TemperatureType](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-temperaturetype-e.md) | Yes | Temperature unit. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Name of the temperature unit, which can be "celsius", "fahrenheit", and "kelvin". |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getTemperatureType

```TypeScript
static getTemperatureType(): TemperatureType
```

Obtains the temperature unit of the system.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getTemperatureType(): TemperatureType--><!--Device-System-static getTemperatureType(): TemperatureType-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [TemperatureType](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-temperaturetype-e.md) | Temperature unit. |

## getUsingLocalDigit

```TypeScript
static getUsingLocalDigit(): boolean
```

Checks whether use of local digits is enabled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static getUsingLocalDigit(): boolean--><!--Device-System-static getUsingLocalDigit(): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether use of local digits is enabled. The value "true" indicates that use of local digits is enabled, and the value "false" indicates the opposite. |

## is24HourClock

```TypeScript
static is24HourClock(): boolean
```

Checks whether the 24-hour clock is used.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-System-static is24HourClock(): boolean--><!--Device-System-static is24HourClock(): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the 24-hour clock is used. The value "true" indicates that the 24-hour clock is used, the the value "false" means the opposite. |

## isSuggested

```TypeScript
static isSuggested(language: string, region?: string): boolean
```

Checks whether a language is a suggested language in the specified region. It can be used for region-based language recommendation or language-based region recommendation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static isSuggested(language: string, region?: string): boolean--><!--Device-System-static isSuggested(language: string, region?: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | Valid language ID, for example, "zh". |
| region | string | No | Valid region ID, for example, "CN". The default value is the country/region of the SIM card. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether a language is a suggested language. The value "true" indicates that the language is a suggested language of the region, the the value "false" indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## setAppPreferredLanguage

```TypeScript
static setAppPreferredLanguage(language: string): void
```

Sets the preferred language of the application. Resources are loaded in the preferred language when the application is launched. If the preferred language is set to default, the application's language will be the same as the system language, and the setting will take effect upon cold starting of the application.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-System-static setAppPreferredLanguage(language: string): void--><!--Device-System-static setAppPreferredLanguage(language: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | Valid language ID or default. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

