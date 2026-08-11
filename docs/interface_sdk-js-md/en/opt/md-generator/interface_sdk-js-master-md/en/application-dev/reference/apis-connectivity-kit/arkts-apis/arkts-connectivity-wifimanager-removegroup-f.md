# removeGroup

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## removeGroup

```TypeScript
function removeGroup(): void
```

Remove a P2P group.

**Since:** 9

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function removeGroup(): void--><!--Device-wifiManager-function removeGroup(): void-End-->

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
    wifiManager.removeGroup();  
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
