# getState

## getState

```TypeScript
function getState(): BluetoothState
```

Obtains the Bluetooth status of a device.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bluetoothManager/bluetoothManager.getState

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getState(): BluetoothState--><!--Device-bluetooth-function getState(): BluetoothState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Returns the Bluetooth status, which can be { |

**Example**

```TypeScript
let state : bluetooth.BluetoothState = bluetooth.getState();
```

