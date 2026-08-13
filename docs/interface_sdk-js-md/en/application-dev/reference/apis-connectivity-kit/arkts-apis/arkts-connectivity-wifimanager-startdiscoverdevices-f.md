# startDiscoverDevices

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## startDiscoverDevices

```TypeScript
function startDiscoverDevices(): void
```

Start discover Wi-Fi P2P devices.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function startDiscoverDevices(): void--><!--Device-wifiManager-function startDiscoverDevices(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) | Operation failed. |
| [2801001](../errorcode-wifi.md#2801001-p2p-module-error) | Wi-Fi STA disabled. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.startDiscoverDevices();  
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

