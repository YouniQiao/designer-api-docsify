# removeAllNetwork (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## removeAllNetwork

```TypeScript
function removeAllNetwork(): void
```

Remove all the saved Wi-Fi configurations.

**Since:** 9

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function removeAllNetwork(): void--><!--Device-wifiManager-function removeAllNetwork(): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501000-sta-internal-error) |
| [2501001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-wifi.md#2501001-sta-disabled) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  wifiManager.removeAllNetwork();    
} catch (error) {
  console.error("failed:" + JSON.stringify(error));
}
```
