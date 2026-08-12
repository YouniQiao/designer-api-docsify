# getMultiLinkedInfo

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## getMultiLinkedInfo

```TypeScript
function getMultiLinkedInfo(): Array<WifiLinkedInfo>
```

Obtain multiple Wi-Fi connection information when Wi-Fi linked in MLO(Muti-Link Operation) state.If does't have the permission of ohos.permission.GET_WIFI_PEERS_MAC, return random bssid.

**Since:** 18

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
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [2501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501000-sta-internal-error) |
| [2501001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501001-sta-disabled) |

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
