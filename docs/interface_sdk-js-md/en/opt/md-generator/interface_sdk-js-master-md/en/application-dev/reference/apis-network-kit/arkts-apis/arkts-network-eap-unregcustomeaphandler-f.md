# unregCustomEapHandler

## Modules to Import

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## unregCustomEapHandler

```TypeScript
function unregCustomEapHandler(netType:number, eapCode: number, eapType: number, callback: Callback<EapData>): void
```

unreg the callback of eap packet customization.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

<!--Device-eap-function unregCustomEapHandler(netType:number, eapCode: number, eapType: number, callback: Callback<EapData>): void--><!--Device-eap-function unregCustomEapHandler(netType:number, eapCode: number, eapType: number, callback: Callback<EapData>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netType | number | Yes |
| eapCode | number | Yes |
| eapType | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;EapData&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33200008](../errorcode-net-eap.md#33200008-invalid-eaptype-value) |
| [33200009](../errorcode-net-eap.md#33200009-netmanager-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [33200099](../errorcode-net-eap.md#33200099-internal-program-error) |
| [33200006](../errorcode-net-eap.md#33200006-invalid-network-type) |
| [33200007](../errorcode-net-eap.md#33200007-invalid-eapcode-value) |

## Examples

```TypeScript
import {eap} from '@kit.NetworkKit';
let netType = 1;
let eapCode = 1;
let eapType = 25;
let eapData = (eapData:eap.EapData):void => {
  console.info("rsp result", JSON.stringify(eapData));
};
    
eap.unregCustomEapHandler(netType, eapCode, eapType, eapData);
console.info('unregCustomEapHandler success');
```
