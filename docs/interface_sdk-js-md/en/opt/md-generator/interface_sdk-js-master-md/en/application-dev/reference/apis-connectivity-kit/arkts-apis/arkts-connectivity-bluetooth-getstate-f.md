# getState

## Modules to Import

```TypeScript
```

## getState

```TypeScript
function getState(): BluetoothState
```

Obtains the Bluetooth status of a device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getState](arkts-connectivity-bluetoothmanager-getstate-f.md#getstate)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getState(): BluetoothState--><!--Device-bluetooth-function getState(): BluetoothState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BluetoothState](arkts-connectivity-bluetoothmanager-bluetoothstate-e.md) |

**Examples**

```TypeScript
let state : bluetooth.BluetoothState = bluetooth.getState();
```
