# TCPConnectOptions

Defines TCPSocket connection parameters.

**Since:** 10

<!--Device-socket-export interface TCPConnectOptions--><!--Device-socket-export interface TCPConnectOptions-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address: NetAddress
```

Bound IP address and port number.

**Type:** [NetAddress](arkts-network-connection-netaddress-i.md)

**Since:** 10

<!--Device-TCPConnectOptions-address: NetAddress--><!--Device-TCPConnectOptions-address: NetAddress-End-->

**System capability:** SystemCapability.Communication.NetStack

## proxy

```TypeScript
proxy?: ProxyOptions
```

Set this option for the proxy feature.

**Type:** [ProxyOptions](arkts-network-socket-proxyoptions-i.md)

**Since:** 18

<!--Device-TCPConnectOptions-proxy?: ProxyOptions--><!--Device-TCPConnectOptions-proxy?: ProxyOptions-End-->

**System capability:** SystemCapability.Communication.NetStack

## timeout

```TypeScript
timeout?: number
```

Timeout duration of the TCPSocket connection, in milliseconds.

**Type:** number

**Since:** 10

<!--Device-TCPConnectOptions-timeout?: number--><!--Device-TCPConnectOptions-timeout?: number-End-->

**System capability:** SystemCapability.Communication.NetStack
