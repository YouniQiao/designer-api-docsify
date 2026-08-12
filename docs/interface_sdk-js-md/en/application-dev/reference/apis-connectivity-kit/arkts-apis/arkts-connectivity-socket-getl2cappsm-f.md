# getL2capPsm

## Modules to Import

```TypeScript
import { socket } from '@kit.ConnectivityKit';
```

## getL2capPsm

```TypeScript
function getL2capPsm(serverSocket: int): int
```

Get l2cap socket psm.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

<!--Device-socket-function getL2capPsm(serverSocket: int): int--><!--Device-socket-function getL2capPsm(serverSocket: int): int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| serverSocket | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the server socket ID, returned by [sppListen](arkts-connectivity-socket-spplisten-f.md#sppListen). |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the l2cap socket psm |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// The server obtains the address of the client.
let serverNumber = 1; // Set serverNumber to the value of serverNumber returned by the sppListen callback.
try {
    let l2capPsm: number = socket.getL2capPsm(serverNumber);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

