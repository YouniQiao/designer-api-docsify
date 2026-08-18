# logOffEthEap

## Modules to Import

```TypeScript
```

## logOffEthEap

```TypeScript
function logOffEthEap(netId: number): void
```

Check whether the specified network is active.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

<!--Device-eap-function logOffEthEap(netId: number): void--><!--Device-eap-function logOffEthEap(netId: number): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33200010](../errorcode-net-eap.md#33200010-invalid-eap-status) |
| [33200009](../errorcode-net-eap.md#33200009-netmanager-not-exist) |
| [33200002](../errorcode-net-eap.md#33200002-failed-to-exit-extended-authentication-of-the-specified-nic) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [33200099](../errorcode-net-eap.md#33200099-internal-program-error) |
| [33200001](../errorcode-net-eap.md#33200001-invalid-netid) |

**Examples**

```TypeScript
import {eap} from '@kit.NetworkKit';
let netId = 100;    
try{
  eap.logOffEthEap(netId);
  console.info("logOffEthEap success");
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```
