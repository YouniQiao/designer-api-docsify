# getMultiLinkedInfo

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## getMultiLinkedInfo

```TypeScript
function getMultiLinkedInfo(): Array<WifiLinkedInfo>
```

Obtain multiple Wi-Fi connection information when Wi-Fi linked in MLO(Muti-Link Operation) state. If does't have the permission of ohos.permission.GET_WIFI_PEERS_MAC, return random bssid.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function getMultiLinkedInfo(): Array<WifiLinkedInfo>--><!--Device-wifiManager-function getMultiLinkedInfo(): Array<WifiLinkedInfo>-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;WifiLinkedInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
| [2501001](../errorcode-wifi.md#2501001-sta-disabled) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let linkedInfo = wifiManager.getMultiLinkedInfo();
    console.info("linkedInfo:" + JSON.stringify(linkedInfo));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
