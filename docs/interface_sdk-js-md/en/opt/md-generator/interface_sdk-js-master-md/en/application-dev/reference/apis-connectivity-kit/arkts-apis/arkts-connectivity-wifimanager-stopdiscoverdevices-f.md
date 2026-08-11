# stopDiscoverDevices

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## stopDiscoverDevices

```TypeScript
function stopDiscoverDevices(): void
```

Stop discover Wi-Fi P2P devices.

**Since:** 9

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function stopDiscoverDevices(): void--><!--Device-wifiManager-function stopDiscoverDevices(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) |
| [2801001](../errorcode-wifi.md#2801001-p2p-module-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.stopDiscoverDevices();  
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
