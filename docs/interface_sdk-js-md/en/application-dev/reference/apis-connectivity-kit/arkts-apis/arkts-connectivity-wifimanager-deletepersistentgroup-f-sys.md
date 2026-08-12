# deletePersistentGroup (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## deletePersistentGroup

```TypeScript
function deletePersistentGroup(netId: int): void
```

Delete the persistent P2P group with the specified network ID.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function deletePersistentGroup(netId: int): void--><!--Device-wifiManager-function deletePersistentGroup(netId: int): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| netId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the network ID of the group to be deleted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: 1.Incorrect parameter types. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [2801000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2801000-p2p-module-error) | Operation failed. |
| [2801001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2801001-p2p-module-error) | Wi-Fi STA disabled. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | System API is not allowed called by Non-system application. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  let netId = 0;
  wifiManager.deletePersistentGroup(netId);  
}catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```

