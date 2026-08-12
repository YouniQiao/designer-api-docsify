# getDeviceConfig (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## getDeviceConfig

```TypeScript
function getDeviceConfig(networkId: int): WifiDeviceConfig
```

Obtain the single Wi-Fi configuration with Network ID.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.GET_WIFI_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-wifiManager-function getDeviceConfig(networkId: int): WifiDeviceConfig--><!--Device-wifiManager-function getDeviceConfig(networkId: int): WifiDeviceConfig-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | The network ID of the Wi-Fi configuration to retrieve. |

**Return value:**

| Type | Description |
| --- | --- |
| WifiDeviceConfig | Returns the Wi-Fi configuration corresponding to the network ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | System API is not allowed called by Non-system application. |
| [2501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501000-sta-internal-error) | Operation failed. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0;
    let config = wifiManager.getDeviceConfig(networkId);
    console.info(`config: ${JSON.stringify(config)}`);    
  }catch(error){
    console.error(`failed: ${JSON.stringify(error)}`);
  }
```

