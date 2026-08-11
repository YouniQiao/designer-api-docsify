# enableWifi

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## enableWifi

```TypeScript
function enableWifi(): void
```

Enable Wi-Fi.

**Since:** 15

**Required permissions:** ohos.permission.SET_WIFI_INFO and (ohos.permission.MANAGE_WIFI_CONNECTION or ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION)

<!--Device-wifiManager-function enableWifi(): void--><!--Device-wifiManager-function enableWifi(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2501003](../errorcode-wifi.md#2501003-failed-to-open-the-service) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
  
  try {
    wifiManager.enableWifi();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
