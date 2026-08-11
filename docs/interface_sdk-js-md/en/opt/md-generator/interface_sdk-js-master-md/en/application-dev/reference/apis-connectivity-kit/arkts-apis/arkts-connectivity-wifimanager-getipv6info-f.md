# getIpv6Info

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getIpv6Info

```TypeScript
function getIpv6Info(): Ipv6Info
```

Obtain the IPv6 information of the Wi-Fi connection.The IPv6 information includes the host IP address, gateway address, and DNS information.

**Since:** 10

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function getIpv6Info(): Ipv6Info--><!--Device-wifiManager-function getIpv6Info(): Ipv6Info-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Ipv6Info](arkts-connectivity-wifimanager-ipv6info-i.md) |

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
    let info = wifiManager.getIpv6Info();
    console.info("info:" + JSON.stringify(info));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
