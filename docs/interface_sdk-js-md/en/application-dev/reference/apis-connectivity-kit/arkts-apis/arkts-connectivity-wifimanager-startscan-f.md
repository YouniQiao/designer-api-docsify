# startScan

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## startScan

```TypeScript
function startScan(): void
```

Scan Wi-Fi hotspot.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_WIFI_INFO

<!--Device-wifiManager-function startScan(): void--><!--Device-wifiManager-function startScan(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501000-sta-internal-error) | Operation failed. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.startScan();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

