# enableHiLinkHandshake (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## enableHiLinkHandshake

```TypeScript
function enableHiLinkHandshake(isHiLinkEnable: boolean, bssid: string, config: WifiDeviceConfig): void
```

Enable hiLink handshake.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function enableHiLinkHandshake(isHiLinkEnable: boolean, bssid: string, config: WifiDeviceConfig): void--><!--Device-wifiManager-function enableHiLinkHandshake(isHiLinkEnable: boolean, bssid: string, config: WifiDeviceConfig): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isHiLinkEnable | boolean | Yes | Indicates the HiLink enable or not. |
| bssid | string | Yes | Indicates the Wi-Fi bssid. |
| config | WifiDeviceConfig | Yes | Indicates the Wi-Fi device config. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | System API is not allowed called by Non-system application. |
| [2501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501000-sta-internal-error) | Operation failed. |
| [2501001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501001-sta-disabled) | Wi-Fi STA disabled. |

## Examples

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

