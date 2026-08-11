# getHotspotConfig (System API)

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getHotspotConfig

```TypeScript
function getHotspotConfig(): HotspotConfig
```

Obtain the Wi-Fi hotspot configuration.

**Since:** 9

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.GET_WIFI_CONFIG

<!--Device-wifiManager-function getHotspotConfig(): HotspotConfig--><!--Device-wifiManager-function getHotspotConfig(): HotspotConfig-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HotspotConfig](arkts-connectivity-wifi-hotspotconfig-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  let config = wifiManager.getHotspotConfig();
  console.info("result:" + JSON.stringify(config));    
} catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```
