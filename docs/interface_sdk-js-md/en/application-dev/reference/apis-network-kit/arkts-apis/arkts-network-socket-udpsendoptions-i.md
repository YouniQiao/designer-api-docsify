# UDPSendOptions

Defines the parameters for sending data over a UDP socket connection.

**Since:** 7

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address: NetAddress
```

Destination address.

**Type:** NetAddress

**Since:** 7

**System capability:** SystemCapability.Communication.NetStack

## data

```TypeScript
data: string | ArrayBuffer
```

Data to send.

**Type:** string \| ArrayBuffer

**Since:** 7

**System capability:** SystemCapability.Communication.NetStack

## proxy

```TypeScript
proxy?: ProxyOptions
```

Proxy option. By default, no proxy is used.

**Type:** [ProxyOptions](arkts-network-socket-proxyoptions-i.md)

**Since:** 18

**System capability:** SystemCapability.Communication.NetStack
