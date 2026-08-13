# getLocalAddress (System API)

## Modules to Import

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## getLocalAddress

```TypeScript
function getLocalAddress(): string
```

Obtaining the MAC address of the local device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_LOCAL_MAC

<!--Device-access-function getLocalAddress(): string--><!--Device-access-function getLocalAddress(): string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let localAddr = access.getLocalAddress();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
