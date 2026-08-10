# logOffEthEap

## Modules to Import

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
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
| 33200010 | invalid eth state |
| 33200009 | netmanager stop |
| 33200002 | Log off fail |
| 201 | Permission denied. |
| 33200099 | internal error |
| 33200001 | Invalid netId |

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

