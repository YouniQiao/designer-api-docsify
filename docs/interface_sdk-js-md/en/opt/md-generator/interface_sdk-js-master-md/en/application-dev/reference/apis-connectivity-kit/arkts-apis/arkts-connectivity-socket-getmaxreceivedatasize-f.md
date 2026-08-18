# getMaxReceiveDataSize

## Modules to Import

```TypeScript
```

## getMaxReceiveDataSize

```TypeScript
function getMaxReceiveDataSize(clientSocket: number): number
```

Obtain the maximum data size that can be received through this socket channel.

**Since:** 26.0.0

<!--Device-socket-function getMaxReceiveDataSize(clientSocket: int): int--><!--Device-socket-function getMaxReceiveDataSize(clientSocket: int): int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clientSocket | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// clientNumber is obtained via sppAccept or sppConnect.
let clientSocket = 1; 
try {
    let result: number = socket.getMaxReceiveDataSize(clientSocket);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
