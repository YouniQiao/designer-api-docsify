# I18NUtil

Internationalization utility class, which provides the capabilities of unit conversion, date sequence retrieval, time segment name retrieval, region matching, and path localization.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-i18n-export class I18NUtil--><!--Device-i18n-export class I18NUtil-End-->

**System capability:** SystemCapability.Global.I18n

## convertCanonicalLocaleIdentifier

```TypeScript
static convertCanonicalLocaleIdentifier(locale: string): string
```

Adjusts a locale ID to a format that complies with the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ standard.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-I18NUtil-static convertCanonicalLocaleIdentifier(locale: string): string--><!--Device-I18NUtil-static convertCanonicalLocaleIdentifier(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | Locale string to be converted, which consists of the language, script,and country/region. |

**Return value:**

| Type | Description |
| --- | --- |
| string | If the input locale ID is valid, a locale ID that complies with the \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ standard will be returned. |

## getBestMatchLocale

```TypeScript
static getBestMatchLocale(locale: string, localeList: string[]): string
```

Obtains the locale that best matches a region from the specified locale list.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static getBestMatchLocale(locale: string, localeList: string[]): string--><!--Device-I18NUtil-static getBestMatchLocale(locale: string, localeList: string[]): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, for example, **zh-Hans-CN**. |
| localeList | string[] | Yes | List of locale IDs. |

**Return value:**

| Type | Description |
| --- | --- |
| string | ID of the locale that best matches a region. If no matching locale is found, an empty string |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| [890001](../errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getDateOrder

```TypeScript
static getDateOrder(locale: string): string
```

Obtains the sequence of the year, month, and day in the specified locale.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static getDateOrder(locale: string): string--><!--Device-I18NUtil-static getDateOrder(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, which consists of the language, script, and country/region, for example, **zh-Hans-CN**. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Sequence of the year, month, and day in the locale. **y** indicates the year, **L** indicates |

## getThreeLetterLanguage

```TypeScript
static getThreeLetterLanguage(locale: string): string
```

Converts a language code from two letters to three letters. For example, the two-letter language code of Chinese is **zh**, and the corresponding three-letter language code is **zho**. For details, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static getThreeLetterLanguage(locale: string): string--><!--Device-I18NUtil-static getThreeLetterLanguage(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | Two-letter code of the language to be converted, for example, **zh**. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Language code after conversion. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| [890001](../errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getThreeLetterRegion

```TypeScript
static getThreeLetterRegion(locale: string): string
```

Converts a region code from two letters to three letters. For example, the two-letter region code of China is **CN**, and the corresponding three-letter region code is **CHN**. For details, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static getThreeLetterRegion(locale: string): string--><!--Device-I18NUtil-static getThreeLetterRegion(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | Two-letter country/region code to be converted, for example, **CN**. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Region code after conversion . |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| [890001](../errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getTimePeriodName

ArkTS-Dyn:
```TypeScript
static getTimePeriodName(hour:number, locale?: string): string
```

ArkTS-Sta:
```TypeScript
static getTimePeriodName(hour:int, locale?: string): string
```

Obtains the localized expression of the specified time in the specified locale.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static getTimePeriodName(hour:int, locale?: string): string--><!--Device-I18NUtil-static getTimePeriodName(hour:int, locale?: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hour | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Specified time, for example, **16**. |
| locale | string | No | \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_,which consists of the language, script, and country/region. for example, **zh-Hans-CN**.The default value is the current system locale. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Localized expression of the specified time in the specified locale. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| [890001](../errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getUnicodeWrappedFilePath

```TypeScript
static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string
```

Localizes a file path for the specified locale. For example, "/data/out/tmp" is changed to "tmp/out/data/" after localization.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-I18NUtil-static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string--><!--Device-I18NUtil-static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path to mirror, for example, "/data/out/tmp". |
| delimiter | string | No | Path delimiter. The default value is "/". |
| locale | Intl.Locale | No | **Locale** object. The default value is the current system locale. |

**Return value:**

| Type | Description |
| --- | --- |
| string | File path after localization. If the specified locale object corresponds to an RTL language, |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getUnicodeWrappedFilePath

```TypeScript
static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string
```

Localizes a file path for the specified locale. For example, "/data/out/tmp" is changed to "tmp/out/data/" after localization.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** 20

**Substitutes:** [i18n.I18NUtil.getUnicodeWrappedFilePath](arkts-localization-i18n-i18nutil-c.md#getunicodewrappedfilepath)(path:

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-I18NUtil-static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string--><!--Device-I18NUtil-static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path to mirror, for example, "/data/out/tmp". |
| delimiter | string | No | Path delimiter. The default value is "/". |
| locale | intl.Locale | No | **Locale** object. The default value is the current system locale. |

**Return value:**

| Type | Description |
| --- | --- |
| string | File path after localization. If the specified locale object corresponds to an RTL language, |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [890001](../errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## setUnicodeWrappedBidiDirection

```TypeScript
static setUnicodeWrappedBidiDirection(text: string, direction: 'RTL' | 'LTR'): string
```

Sets the text direction for certain text within a paragraph, including RTL (right-to-left) and LTR (left-to-right). NOTE: The setting does not take effect within strong characters (characters with an intrinsic, unambiguous writing direction).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-I18NUtil-static setUnicodeWrappedBidiDirection(text: string, direction: 'RTL' | 'LTR'): string--><!--Device-I18NUtil-static setUnicodeWrappedBidiDirection(text: string, direction: 'RTL' | 'LTR'): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Text for which the direction needs to be set. |
| direction | 'RTL' \| 'LTR' | Yes | The value can be "RTL" or "LTR"."RTL" indicates setting the input text direction from right to left."LTR" indicates setting the input text direction from left to right. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Processed Text. |

## unitConvert

ArkTS-Dyn:
```TypeScript
static unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string): string
```

ArkTS-Sta:
```TypeScript
static unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string
```

Converts one measurement unit into another and formats the unit based on the specified locale and style.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string--><!--Device-I18NUtil-static unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fromUnit | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Measurement unit to be converted. |
| toUnit | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Measurement unit to be converted to. |
| value | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Value of the measurement unit to be converted. |
| locale | string | Yes | \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, which consists of the language, script, and country/region, for example, **zh-Hans-CN**. |
| style | string | No | Style used for formatting. The value can be **long**, **short**, or **narrow**. The default value is **short**.For details about the meaning or display effect of different values, see \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

**Return value:**

| Type | Description |
| --- | --- |
| string | String converted to the measurement unit after formatting. |

