# PhoneNumberFormatOptions

Options for PhoneNumberFormat object initialization.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-i18n-export interface PhoneNumberFormatOptions--><!--Device-i18n-export interface PhoneNumberFormatOptions-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
```

## type

```TypeScript
type?: string
```

Type of the phone number. The value can be "E164", "INTERNATIONAL", "NATIONAL", "RFC3966", or "TYPING". In API version 8, type is mandatory. In API version 9 or later, type is optional. In API version 12 or later, "TYPING" is supported, which indicates that the dialed number is formatted in real time.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhoneNumberFormatOptions-type?: string--><!--Device-PhoneNumberFormatOptions-type?: string-End-->

**System capability:** SystemCapability.Global.I18n

