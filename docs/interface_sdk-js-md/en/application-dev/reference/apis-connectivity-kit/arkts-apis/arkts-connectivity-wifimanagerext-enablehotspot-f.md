# enableHotspot

## Modules to Import

```TypeScript
import { wifiManagerExt } from 'kits/@kit.ConnectivityKit';
```

## enableHotspot

```TypeScript
function enableHotspot(): void
```

Enable Wi-Fi hotspot function. This method is asynchronous. After the Wi-Fi hotspot is enabled, Wi-Fi may be disabled.

**Since:** 9

**Deprecated since:** 10

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

**System capability:** SystemCapability.Communication.WiFi.AP.Extension

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2701000](../errorcode-wifi.md#2701000-ap-extension-module-error) |
