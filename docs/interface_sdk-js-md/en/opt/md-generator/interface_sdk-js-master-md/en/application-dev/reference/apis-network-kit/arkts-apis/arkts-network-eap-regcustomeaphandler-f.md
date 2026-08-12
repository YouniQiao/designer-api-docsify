# regCustomEapHandler

## Modules to Import

```TypeScript
import { eap } from '@kit.NetworkKit';
```

## regCustomEapHandler

```TypeScript
function regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void
```

Customize eap packets by callback

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

<!--Device-eap-function regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void--><!--Device-eap-function regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [netType](arkts-network-policy-networkmatchrule-i-sys.md) | number | Yes |
| eapCode | number | Yes |
| eapType | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[EapData](arkts-network-eap-eapdata-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33200008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200008-invalid-eaptype-value) |
| [33200009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200009-netmanager-not-exist) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [33200099](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200099-internal-program-error) |
| [33200006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200006-invalid-network-type) |
| [33200007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200007-invalid-eapcode-value) |

## Examples

```TypeScript
import {eap} from '@kit.NetworkKit';
let netType = 1;
let eapCode = 1;
let eapType = 25;
let eapData = (eapData:eap.EapData):void => {
  console.info("rsp result", JSON.stringify(eapData));
};
    
eap.regCustomEapHandler(netType, eapCode, eapType, eapData);
console.info('regCustomEapHandler success');
```
