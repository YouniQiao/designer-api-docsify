# startScan

## Modules to Import

```TypeScript
```

## startScan

```TypeScript
function startScan(): void
```

Scan Wi-Fi hotspot.

**Since:** 23

**Required permissions:** ohos.permission.SET_WIFI_INFO

<!--Device-wifiManager-function startScan(): void--><!--Device-wifiManager-function startScan(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |

**Examples**

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.startScan();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
