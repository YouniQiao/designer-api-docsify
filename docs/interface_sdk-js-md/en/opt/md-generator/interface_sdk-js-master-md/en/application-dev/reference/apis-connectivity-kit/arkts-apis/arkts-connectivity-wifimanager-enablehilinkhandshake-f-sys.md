# enableHiLinkHandshake (System API)

## Modules to Import

```TypeScript
```

## enableHiLinkHandshake

```TypeScript
function enableHiLinkHandshake(isHiLinkEnable: boolean, bssid: string, config: WifiDeviceConfig): void
```

Enable hiLink handshake.

**Since:** 23

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function enableHiLinkHandshake(isHiLinkEnable: boolean, bssid: string, config: WifiDeviceConfig): void--><!--Device-wifiManager-function enableHiLinkHandshake(isHiLinkEnable: boolean, bssid: string, config: WifiDeviceConfig): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isHiLinkEnable | boolean | Yes |
| bssid | string | Yes |
| config | [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
| [2501001](../errorcode-wifi.md#2501001-sta-disabled) |

**Examples**

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
// You can obtain config data by using getScanInfoList, which can be used only when WifiScanInfo.isHiLinkNetwork is true.
let config:wifiManager.WifiDeviceConfig = {
  ssid : "****",
  preSharedKey : "****",
  securityType : 0,
  bssid : "38:37:8b:80:bf:cc",
  bssidType : 1,
  isHiddenSsid : false
}  
try {
  wifiManager.enableHiLinkHandshake(true, config.bssid, config);
} catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```
