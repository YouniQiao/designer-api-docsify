# logOffEthEap

## Modules to Import

```TypeScript
import { eap } from '@kit.NetworkKit';
```

## logOffEthEap

```TypeScript
function logOffEthEap(netId: number): void
```

Check whether the specified network is active.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

<!--Device-eap-function logOffEthEap(netId: number): void--><!--Device-eap-function logOffEthEap(netId: number): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| netId | number | Yes | Indicates the eth network id to log off EAP authentication. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33200010](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200010-invalid-eap-status) | invalid eth state |
| [33200009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200009-netmanager-not-exist) | netmanager stop |
| [33200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200002-failed-to-exit-extended-authentication-of-the-specified-nic) | Log off fail |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [33200099](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200099-internal-program-error) | internal error |
| [33200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200001-invalid-netid) | Invalid netId |

## Examples

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

