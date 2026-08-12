# p2pCancelConnect

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## p2pCancelConnect

```TypeScript
function p2pCancelConnect(): void
```

Stop an ongoing p2p connection that is being established.

**Since:** 9

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function p2pCancelConnect(): void--><!--Device-wifiManager-function p2pCancelConnect(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [2801000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2801000-p2p-module-error) |
| [2801001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2801001-p2p-module-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.p2pCancelConnect();  
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
