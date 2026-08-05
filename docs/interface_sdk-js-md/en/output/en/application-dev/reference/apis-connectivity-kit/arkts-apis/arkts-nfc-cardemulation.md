# @ohos.nfc.cardEmulation

Provides methods to operate or manage NFC card emulation.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace cardEmulation--><!--Device-unnamed-declare namespace cardEmulation-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

## Summary

### Functions

| Name | Description |
| --- | --- |
| [hasHceCapability](arkts-connectivity-cardemulation-hashcecapability-f.md#hashcecapability) | Checks whether Host Card Emulation(HCE) capability is supported. |
| [isDefaultService](arkts-connectivity-cardemulation-isdefaultservice-f.md#isdefaultservice) | Checks whether a service is default for given type. |
| [isSupported](arkts-connectivity-cardemulation-issupported-f.md#issupported) | Checks whether a specified type of card emulation is supported. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_This method is used to check Whether the host or secure element supports card emulation. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getPaymentServices](arkts-connectivity-cardemulation-getpaymentservices-f-sys.md#getpaymentservices) | Gets all payment services. |
<!--DelEnd-->

### Classes

| Name | Description |
| --- | --- |
| [HceService](arkts-connectivity-cardemulation-hceservice-c.md) | A class for NFC host application. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The NFC host application use this class, then Nfc service can access the application installation information and connect to services of the application. |

### Enums

| Name | Description |
| --- | --- |
| [CardType](arkts-connectivity-cardemulation-cardtype-e.md) | Define the card emulation type, payment or other. |
| [FeatureType](arkts-connectivity-cardemulation-featuretype-e.md) | Defines the capability type. |

