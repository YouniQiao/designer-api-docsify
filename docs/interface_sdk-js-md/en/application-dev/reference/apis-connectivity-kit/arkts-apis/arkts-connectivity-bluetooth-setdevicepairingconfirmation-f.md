# setDevicePairingConfirmation

## Modules to Import

```TypeScript
import { bluetooth } from 'bluetooth';
```

## setDevicePairingConfirmation

```TypeScript
function setDevicePairingConfirmation(device: string, accept: boolean): boolean
```

Sets the confirmation of pairing with a certain device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setDevicePairingConfirmation](arkts-connectivity-bluetoothmanager-setdevicepairingconfirmation-f.md#setdevicepairingconfirmation)

**Required permissions:** ohos.permission.MANAGE_BLUETOOTH

<!--Device-bluetooth-function setDevicePairingConfirmation(device: string, accept: boolean): boolean--><!--Device-bluetooth-function setDevicePairingConfirmation(device: string, accept: boolean): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | string | Yes | The address of the remote device. |
| accept | boolean | Yes | Indicates whether to accept the pairing request, {@code true} indicates accept or {@code false} otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
// Subscribe to the pinRequired event and configure the pairing confirmation after receiving a pairing request from the remote device.
function onReceivePinRequiredEvent(data : bluetooth.PinRequiredParam) { // data is the input parameter for the pairing request.
    console.info('pin required  = '+ JSON.stringify(data));
    bluetooth.setDevicePairingConfirmation(data.deviceId, true);
}
bluetooth.on("pinRequired", onReceivePinRequiredEvent);
```

