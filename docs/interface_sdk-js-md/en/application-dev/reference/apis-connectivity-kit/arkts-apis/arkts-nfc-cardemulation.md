# @ohos.nfc.cardEmulation(Standard NFC Card Emulation)

###### HCE and AID Declaration
 Before developing an application related to HCE, you must declare NFC-related attributes in the **module.json5**
 file.
 ```json5
 // Applicable to devices other than lite wearables
 {
 "module": {
 // Other declared attributes
 "abilities": [
 {
 // Other declared attributes
 "skills": [
 {
 "actions": [
 "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
 ]
 }
 ],
 "metadata": [
 {
 "name": "payment-aid",
 "value": "your payment aid"
 },
 {
 "name": "other-aid",
 "value": "your other aid"
 }
 ]
 }
 ],
 "requestPermissions": [
 {
 "name": "ohos.permission.NFC_CARD_EMULATION",
 // Set reason to card_emulation_reason.
 "reason": "$string:card_emulation_reason"
 }
 ]
 }
 }
 ```
 ```json5
 // Applicable to lite wearables
 {
 "module": {
 // Other declared attributes
 "abilities": [
 {
 // Other declared attributes
 "metaData": {
 "customizeData": [
 {
 "name": "paymentAid",
 "value": "A0000000041012"
 },
 {
 "name": "otherAid",
 "value": "A0000000041010"
 }
 ]
 },
 "skills": [
 {
 "entities": [
 "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
 ],
 "actions": [
 "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
 ]
 }
 ]
 }
 ],
 "reqPermissions": [
 {
 "name": "ohos.permission.NFC_CARD_EMULATION",
 // Set reason to card_emulation_reason.
 "reason": "$string:card_emulation_reason",
 "usedScene":{
 "ability":[
 "FormAbility"
 ],
 "when":"always"
 }
 },
 {
 "name": "ohos.permission.NFC_TAG",
 // Set reason to card_emulation_reason.
 "reason": "$string:card_emulation_reason",
 "usedScene":{
 "ability":[
 "FormAbility"
 ],
 "when":"always"
 }
 }
 ]
 }
 }
 ```
 > **NOTE**
 >
 > 1. The **actions** field must contain **ohos.nfc.cardemulation.action.HOST_APDU_SERVICE** and cannot be changed.
 >
 > 2. When declaring an AID (in compliance with ISO/IEC 7816-4), ensure that **name** is set to **payment-aid** or
 > **other-aid**. Incorrect setting will cause a parsing failure.
 >
 > 3. The **name** field of **requestPermissions** must be **ohos.permission.NFC_CARD_EMULATION** and cannot be
 > changed.
 >
 > 4. Lite wearables support only the [FA Model](../../../application-models/ability-terminology.md#fa-model), with
 > attribute configurations and API invocation methods differing from those of other device types. Refer to the
 > example code for detailed implementations.


**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NFC.CardEmulation

## Modules to Import

```TypeScript
import { cardEmulation } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [hasHceCapability(Standard NFC Card Emulation)](arkts-connectivity-cardemulation-hashcecapability-f.md) |
| [isDefaultService(Standard NFC Card Emulation)](arkts-connectivity-cardemulation-isdefaultservice-f.md) |
| [isSupported(Standard NFC Card Emulation)](arkts-connectivity-cardemulation-issupported-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getPaymentServices(Standard NFC Card Emulation)](arkts-connectivity-cardemulation-getpaymentservices-f-sys.md) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [HceService(Standard NFC Card Emulation)](arkts-connectivity-cardemulation-hceservice-c.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CardType(Standard NFC Card Emulation)](arkts-connectivity-cardemulation-cardtype-e.md) |
| [FeatureType(Standard NFC Card Emulation)](arkts-connectivity-cardemulation-featuretype-e.md) |
