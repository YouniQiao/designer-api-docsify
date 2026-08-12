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

**Required permissions:** ohos.permission.SET_WIFI_INFO

<!--Device-wifiManager-function startScan(): void--><!--Device-wifiManager-function startScan(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [2501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501000-sta-internal-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.startScan();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
