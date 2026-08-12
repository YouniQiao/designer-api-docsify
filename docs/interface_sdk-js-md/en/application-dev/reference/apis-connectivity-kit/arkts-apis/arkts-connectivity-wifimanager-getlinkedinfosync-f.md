# getLinkedInfoSync

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## getLinkedInfoSync

```TypeScript
function getLinkedInfoSync(): WifiLinkedInfo
```

Obtain connection information about the Wi-Fi connection.this apireturns the result syncchronously.If does't have the permission of ohos.permission.GET_WIFI_PEERS_MAC, return random bssid.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function getLinkedInfoSync(): WifiLinkedInfo--><!--Device-wifiManager-function getLinkedInfoSync(): WifiLinkedInfo-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Return value:**

| Type | Description |
| --- | --- |
| WifiLinkedInfo | Returns Wi-Fi linked information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501000-sta-internal-error) | Operation failed. |
| [2501001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501001-sta-disabled) | Wi-Fi STA disabled. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
  try {
    let linkInfo = wifiManager.getLinkedInfoSync();
    console.info("get linked info:" + JSON.stringify(linkInfo));
  } catch(error) {
    console.error("get linked info failed:" + JSON.stringify(error));
  }
```

