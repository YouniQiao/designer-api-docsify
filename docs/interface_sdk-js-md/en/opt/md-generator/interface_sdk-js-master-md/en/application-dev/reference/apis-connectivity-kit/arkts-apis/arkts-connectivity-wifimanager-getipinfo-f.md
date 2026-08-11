# getIpInfo

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getIpInfo

```TypeScript
function getIpInfo(): IpInfo
```

Obtain the IPv4 information of the Wi-Fi connection.The IP information includes the host IP address, gateway address, and DNS information.

**Since:** 9

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function getIpInfo(): IpInfo--><!--Device-wifiManager-function getIpInfo(): IpInfo-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IpInfo](arkts-connectivity-wifi-ipinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let info = wifiManager.getIpInfo();
    console.info("info:" + JSON.stringify(info));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
