# regCustomEapHandler

## Modules to Import

```TypeScript
import { eap } from '@kit.NetworkKit';
```

## regCustomEapHandler

```TypeScript
function regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void
```

Registers a custom handler of Extensible Authentication Protocol (EAP) packets for extensible authentication. This API returns the result asynchronously through a callback.The system will encapsulate the eligible EAP packets into the callback function for enterprise applications to retrieve.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [netType](arkts-network-policy-networkmatchrule-i-sys.md) | number | Yes |
| eapCode | number | Yes |
| eapType | number | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[EapData](arkts-network-eap-eapdata-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [33200006](../errorcode-net-eap.md#33200006-invalid-network-type) |
| [33200007](../errorcode-net-eap.md#33200007-invalid-eapcode-value) |
| [33200008](../errorcode-net-eap.md#33200008-invalid-eaptype-value) |
| [33200009](../errorcode-net-eap.md#33200009-netmanager-not-exist) |
| [33200099](../errorcode-net-eap.md#33200099-internal-program-error) |

**Examples**

```TypeScript
import {eap} from '@kit.NetworkKit';
let netType = 1;
let eapCode = 1;
let eapType = 25;
let  eapData = (eapData:eap.EapData):void => {
  console.info("rsp result",JSON.stringify(eapData))
}
    
try {
  eap.regCustomEapHandler(netType, eapCode, eapType, eapData);
  console.info('regCustomEapHandler success');
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```
