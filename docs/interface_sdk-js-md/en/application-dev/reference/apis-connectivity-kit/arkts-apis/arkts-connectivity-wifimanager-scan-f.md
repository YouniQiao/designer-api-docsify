# scan

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## scan

```TypeScript
function scan(): void
```

Scan Wi-Fi hotspot.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [startScan](arkts-connectivity-wifimanager-startscan-f.md)

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**System capability:** SystemCapability.Communication.WiFi.STA

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
