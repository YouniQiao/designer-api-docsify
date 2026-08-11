# p2pCancelConnect

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## p2pCancelConnect

```TypeScript
function p2pCancelConnect(): void
```

Stop an ongoing p2p connection that is being established.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function p2pCancelConnect(): void--><!--Device-wifiManager-function p2pCancelConnect(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) | Operation failed. |
| [2801001](../errorcode-wifi.md#2801001-p2p-module-error) | Wi-Fi STA disabled. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.p2pCancelConnect();  
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

