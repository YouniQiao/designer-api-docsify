# I18NUtil

Internationalization utility class, which provides the capabilities of unit conversion, date sequence retrieval,time segment name retrieval, region matching, and path localization.

**Since:** 9

<!--Device-i18n-export class I18NUtil--><!--Device-i18n-export class I18NUtil-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## convertCanonicalLocaleIdentifier

```TypeScript
static convertCanonicalLocaleIdentifier(locale: string): string
```

Adjusts a locale ID to a format that complies with the [BCP47](https://www.rfc-editor.org/info/bcp47) standard.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-I18NUtil-static convertCanonicalLocaleIdentifier(locale: string): string--><!--Device-I18NUtil-static convertCanonicalLocaleIdentifier(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getBestMatchLocale

```TypeScript
static getBestMatchLocale(locale: string, localeList: string[]): string
```

Obtains the locale that best matches a region from the specified locale list.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static getBestMatchLocale(locale: string, localeList: string[]): string--><!--Device-I18NUtil-static getBestMatchLocale(locale: string, localeList: string[]): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string | Yes |
| localeList | string[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## getDateOrder

```TypeScript
static getDateOrder(locale: string): string
```

Obtains the sequence of the year, month, and day in the specified locale.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static getDateOrder(locale: string): string--><!--Device-I18NUtil-static getDateOrder(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getThreeLetterLanguage

```TypeScript
static getThreeLetterLanguage(locale: string): string
```

Converts a language code from two letters to three letters.

For example, the two-letter language code of Chinese is **zh**, and the corresponding three-letter language code is **zho**. For details, see [ISO 639](https://www.iso.org/iso-639-language-code).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static getThreeLetterLanguage(locale: string): string--><!--Device-I18NUtil-static getThreeLetterLanguage(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## getThreeLetterRegion

```TypeScript
static getThreeLetterRegion(locale: string): string
```

Converts a region code from two letters to three letters.

For example, the two-letter region code of China is **CN**, and the corresponding three-letter region code is  
**CHN**. For details, see [ISO 3166](https://www.iso.org/iso-3166-country-codes.html).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static getThreeLetterRegion(locale: string): string--><!--Device-I18NUtil-static getThreeLetterRegion(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## getTimePeriodName

```TypeScript
static getTimePeriodName(hour:number, locale?: string): string
```

Obtains the localized expression of the specified time in the specified locale.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static getTimePeriodName(hour:int, locale?: string): string--><!--Device-I18NUtil-static getTimePeriodName(hour:int, locale?: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hour | number | Yes |
| locale | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## getUnicodeWrappedFilePath

```TypeScript
static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string
```

Localizes a file path for the specified locale.

For example, "/data/out/tmp" is changed to "tmp/out/data/" after localization.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-I18NUtil-static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string--><!--Device-I18NUtil-static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| delimiter | string | No |
| locale | Intl.Locale | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-parameter-verification-error) |

## getUnicodeWrappedFilePath

```TypeScript
static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string
```

Localizes a file path for the specified locale.

For example, "/data/out/tmp" is changed to "tmp/out/data/" after localization.

**Since:** 18

**Deprecated since:** 20

**Substitutes:** [i18n.I18NUtil.getUnicodeWrappedFilePath](arkts-localization-i18n-i18nutil-c.md#getunicodewrappedfilepath)(path:

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-I18NUtil-static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string--><!--Device-I18NUtil-static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| delimiter | string | No |
| locale | intl.Locale | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## setUnicodeWrappedBidiDirection

```TypeScript
static setUnicodeWrappedBidiDirection(text: string, direction: 'RTL' | 'LTR'): string
```

Sets the text direction for certain text within a paragraph, including RTL (right-to-left) and LTR (left-to-right). NOTE: The setting does not take effect within strong characters (characters  with an intrinsic, unambiguous writing direction).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-I18NUtil-static setUnicodeWrappedBidiDirection(text: string, direction: 'RTL' | 'LTR'): string--><!--Device-I18NUtil-static setUnicodeWrappedBidiDirection(text: string, direction: 'RTL' | 'LTR'): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| direction | 'RTL' \| 'LTR' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## unitConvert

```TypeScript
static unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string): string
```

Converts one measurement unit into another and formats the unit based on the specified locale and style.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-I18NUtil-static unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string--><!--Device-I18NUtil-static unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fromUnit | [UnitInfo](arkts-localization-i18n-unitinfo-i.md) | Yes |
| toUnit | [UnitInfo](arkts-localization-i18n-unitinfo-i.md) | Yes |
| value | number | Yes |
| locale | string | Yes |
| style | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
