# disableNetwork (System API)

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## disableNetwork

```TypeScript
function disableNetwork(netId: number): void
```

Disable the specified DeviceConfig by networkId.The disabled DeviceConfig will not be associated with again.

**Since:** 9

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function disableNetwork(netId: int): void--><!--Device-wifiManager-function disableNetwork(netId: int): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
| [2501001](../errorcode-wifi.md#2501001-sta-disabled) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
  let netId = 0;
  wifiManager.disableNetwork(netId);  
} catch (error) {
  console.error(`failed: ${JSON.stringify(error)}`);
}
```


## disableNetwork

```TypeScript
function disableNetwork(netId: number, blockDuration: number): void
```

Disable the specified DeviceConfig by networkId for a period of time.The disabled DeviceConfig will not be associated with again.

**Since:** 23

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function disableNetwork(netId: int, blockDuration: int): void--><!--Device-wifiManager-function disableNetwork(netId: int, blockDuration: int): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netId | number | Yes |
| blockDuration | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
| [2501001](../errorcode-wifi.md#2501001-sta-disabled) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let netId = 0;
    let blockDuration = 300;
    wifiManager.disableNetwork(netId, blockDuration);
  } catch (error) {
    console.error(`failed: ${JSON.stringify(error)}`);
  }
```
