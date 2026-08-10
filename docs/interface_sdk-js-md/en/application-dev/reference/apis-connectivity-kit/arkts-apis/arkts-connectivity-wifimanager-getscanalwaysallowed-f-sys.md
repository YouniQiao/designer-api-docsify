# getScanAlwaysAllowed (System API)

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getScanAlwaysAllowed

```TypeScript
function getScanAlwaysAllowed(): boolean
```

Get scan always allowed flag.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.GET_WIFI_CONFIG

<!--Device-wifiManager-function getScanAlwaysAllowed(): boolean--><!--Device-wifiManager-function getScanAlwaysAllowed(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | System API is not allowed called by Non-system application. |
| 2501000 | Operation failed. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let isScanAlwaysAllowed = wifiManager.getScanAlwaysAllowed();
    console.info("isScanAlwaysAllowed:" + isScanAlwaysAllowed);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

