# PhoneNumberFormat

Provides the API for formatting phone number strings

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-i18n-export class PhoneNumberFormat--><!--Device-i18n-export class PhoneNumberFormat-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(country: string, options?: PhoneNumberFormatOptions)
```

Creates a PhoneNumberFormat object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhoneNumberFormat-constructor(country: string, options?: PhoneNumberFormatOptions)--><!--Device-PhoneNumberFormat-constructor(country: string, options?: PhoneNumberFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| country | string | Yes | Country/region to which the phone number to be formatted belongs. |
| options | [PhoneNumberFormatOptions](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-phonenumberformatoptions-i.md) | No | Options for PhoneNumberFormat object initialization. The default value is "NATIONAL". |

## format

```TypeScript
format(phoneNumber: string): string
```

Formats a phone number.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhoneNumberFormat-format(phoneNumber: string): string--><!--Device-PhoneNumberFormat-format(phoneNumber: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| phoneNumber | string | Yes | Phone number to be formatted. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Formatted phone number. |

## getLocationName

```TypeScript
getLocationName(phoneNumber: string, locale: string): string
```

Obtains the home location of a phone number.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhoneNumberFormat-getLocationName(phoneNumber: string, locale: string): string--><!--Device-PhoneNumberFormat-getLocationName(phoneNumber: string, locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| phoneNumber | string | Yes | Phone number. To obtain the home location of a number in other countries/regions, you need to prefix the number with 00 and the country code. |
| locale | string | Yes | System locale, which consists of the language, script, and country/region. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Home location of the phone number. If the number is invalid, an empty string is returned. |

## isValidNumber

```TypeScript
isValidNumber(phoneNumber: string): boolean
```

Checks whether the phone number is valid for the country/region in the PhoneNumberFormat object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhoneNumberFormat-isValidNumber(phoneNumber: string): boolean--><!--Device-PhoneNumberFormat-isValidNumber(phoneNumber: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| phoneNumber | string | Yes | Phone number to be checked. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the phone number is valid. The value "true" indicates that the phone number is valid, and the value "false" indicates the opposite. |

