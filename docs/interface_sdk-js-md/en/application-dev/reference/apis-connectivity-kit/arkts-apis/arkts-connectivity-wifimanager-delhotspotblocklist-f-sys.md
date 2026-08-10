# delHotspotBlockList (System API)

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## delHotspotBlockList

```TypeScript
function delHotspotBlockList(stationInfo: StationInfo): void
```

Delete the station from block list, the station can access the hotspot.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifiManager-function delHotspotBlockList(stationInfo: StationInfo): void--><!--Device-wifiManager-function delHotspotBlockList(stationInfo: StationInfo): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| stationInfo | [StationInfo](arkts-connectivity-wifi-stationinfo-i-sys.md) | Yes | station which will be deleted in the block list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Invalid parameters. Possible causes: 1.Incorrect parameter types. 2.Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | System API is not allowed called by Non-system application. |
| 2601000 | Operation failed. |

## Examples

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

