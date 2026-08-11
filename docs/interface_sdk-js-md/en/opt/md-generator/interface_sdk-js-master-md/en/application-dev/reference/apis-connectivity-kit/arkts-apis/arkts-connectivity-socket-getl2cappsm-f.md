# getL2capPsm

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.ConnectivityKit';
```

## getL2capPsm

```TypeScript
function getL2capPsm(serverSocket: number): number
```

Get l2cap socket psm.

**Since:** 20

<!--Device-socket-function getL2capPsm(serverSocket: int): int--><!--Device-socket-function getL2capPsm(serverSocket: int): int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serverSocket | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

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
