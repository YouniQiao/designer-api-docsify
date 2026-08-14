# constructTLSSocketInstance

## Modules to Import

```TypeScript
import { socket } from 'socket';
```

## constructTLSSocketInstance

```TypeScript
function constructTLSSocketInstance(): TLSSocket
```

Creates a TLSSocket object.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-socket-function constructTLSSocketInstance(): TLSSocket--><!--Device-socket-function constructTLSSocketInstance(): TLSSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| [TLSSocket](arkts-network-socket-tlssocket-i.md) | the TLSSocket of the constructTLSSocketInstance. |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
```


## constructTLSSocketInstance

```TypeScript
function constructTLSSocketInstance(tcpSocket: TCPSocket): TLSSocket
```

Creates a TLSSocket object with a TCPSocket object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-socket-function constructTLSSocketInstance(tcpSocket: TCPSocket): TLSSocket--><!--Device-socket-function constructTLSSocketInstance(tcpSocket: TCPSocket): TLSSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tcpSocket | TCPSocket | Yes | Parameter for creating a TLSSocket object. |

**Return value:**

| Type | Description |
| --- | --- |
| [TLSSocket](arkts-network-socket-tlssocket-i.md) | the TLSSocket of the constructTLSSocketInstance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) | System internal error. |
| 2303602 | Socket is not connected. |
| 2303601 | Invalid socket FD. |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}

tcp.connect(tcpconnectoptions, (err: BusinessError) => {
  if (err) {
    console.error('connect fail');
    return;
  }
  console.info('connect success');

  // Ensure that a TCPSocket connection has been established before upgrading it to a TLSSocket connection.
  let tls: socket.TLSSocket = socket.constructTLSSocketInstance(tcp);
})
```

