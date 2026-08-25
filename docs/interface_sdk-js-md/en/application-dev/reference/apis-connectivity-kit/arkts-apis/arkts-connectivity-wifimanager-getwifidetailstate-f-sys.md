# getWifiDetailState (System API)

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getWifiDetailState

```TypeScript
function getWifiDetailState(): WifiDetailState
```

Obtains information about a Wi-Fi detail state.

**Since:** 12

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WifiDetailState](arkts-connectivity-wifimanager-wifidetailstate-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
