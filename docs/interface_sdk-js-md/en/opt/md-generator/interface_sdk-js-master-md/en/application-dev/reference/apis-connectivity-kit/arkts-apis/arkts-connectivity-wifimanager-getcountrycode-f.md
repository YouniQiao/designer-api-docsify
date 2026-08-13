# getCountryCode

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## getCountryCode

```TypeScript
function getCountryCode(): string
```

Obtain the country code of the device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function getCountryCode(): string--><!--Device-wifiManager-function getCountryCode(): string-End-->

**System capability:** SystemCapability.Communication.WiFi.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2401000](../errorcode-wifi.md#2401000-sta-internal-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let code = wifiManager.getCountryCode();
    console.info("code:" + code);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
