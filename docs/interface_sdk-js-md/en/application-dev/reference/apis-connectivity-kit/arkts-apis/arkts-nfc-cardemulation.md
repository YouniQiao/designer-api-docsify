# @ohos.nfc.cardEmulation

The **cardEmulation** module implements Near-Field Communication (NFC) card emulation. You can use the APIs provided by this module to determine the card emulation type supported and implement Host Card Emulation (HCE).HCE provides card emulation that does not depend on a secure element. It allows an application to emulate a card and communicate with an NFC card reader through the NFC service.

**Since:** 23

<!--Device-unnamed-declare namespace cardEmulation--><!--Device-unnamed-declare namespace cardEmulation-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

## Modules to Import

```TypeScript
import { cardEmulation } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [hasHceCapability](arkts-connectivity-cardemulation-hashcecapability-f.md) | Checks whether the device supports HCE. |
| [isDefaultService](arkts-connectivity-cardemulation-isdefaultservice-f.md) | Checks whether an application is the default application of the specified service type. |
| [isSupported](arkts-connectivity-cardemulation-issupported-f.md) | Checks whether a certain type of card emulation is supported. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getPaymentServices](arkts-connectivity-cardemulation-getpaymentservices-f-sys.md) | Obtains all payment services. If an application declares the support for the HCE feature and **payment-aid**, the application is contained in the payment service list. For details, see HCE and AID Declaration. |
<!--DelEnd-->

### Classes

| Name | Description |
| --- | --- |
| [HceService](arkts-connectivity-cardemulation-hceservice-c.md) | Provides APIs for implementing HCE, including receiving Application Protocol Data Units (APDUs) from the peer card reader and sending a response. Before using HCE-related APIs, check whether the device supports HCE. |

### Enums

| Name | Description |
| --- | --- |
| [CardType](arkts-connectivity-cardemulation-cardtype-e.md) | Enumerates the types of services used by the card emulation application. |
| [FeatureType](arkts-connectivity-cardemulation-featuretype-e.md) | Enumerates the NFC card emulation types. |

