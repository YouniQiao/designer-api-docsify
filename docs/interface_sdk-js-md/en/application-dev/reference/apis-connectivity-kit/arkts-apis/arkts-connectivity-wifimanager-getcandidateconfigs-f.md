# getCandidateConfigs

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getCandidateConfigs

```TypeScript
function getCandidateConfigs(): Array<WifiDeviceConfig>
```

Obtain the list of all existed candidate Wi-Fi configurations which added by ourself. You can obtain only the Wi-Fi configurations you created on your own application.

**Since:** 12

**Required permissions:** ohos.permission.GET_WIFI_INFO

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.WiFi.STA

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;WifiDeviceConfig & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
