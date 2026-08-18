# delHotspotBlockList (System API)

## Modules to Import

```TypeScript
```

## delHotspotBlockList

```TypeScript
function delHotspotBlockList(stationInfo: StationInfo): void
```

Delete the station from block list, the station can access the hotspot.

**Since:** 23

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifiManager-function delHotspotBlockList(stationInfo: StationInfo): void--><!--Device-wifiManager-function delHotspotBlockList(stationInfo: StationInfo): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| stationInfo | [StationInfo](arkts-connectivity-wifi-stationinfo-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) |

**Examples**

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  let config:wifiManager.StationInfo = {
    name : "testSsid",
    macAddress : "11:22:33:44:55:66",
    ipAddress : "192.168.1.111"
  }
  wifiManager.delHotspotBlockList(config);
} catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```
