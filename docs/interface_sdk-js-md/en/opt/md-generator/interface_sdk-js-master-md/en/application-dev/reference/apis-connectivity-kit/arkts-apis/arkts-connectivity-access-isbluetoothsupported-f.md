# isBluetoothSupported

## Modules to Import

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## isBluetoothSupported

```TypeScript
function isBluetoothSupported(): boolean
```

Check whether Bluetooth is available.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-access-function isBluetoothSupported(): boolean--><!--Device-access-function isBluetoothSupported(): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 2900099 |

## Examples

```TypeScript
try {
    let isSupported: boolean = access.isBluetoothSupported();
    console.info("isSupported: " + isSupported);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
