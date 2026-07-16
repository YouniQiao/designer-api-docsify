# ProxyOptions

Define parameters for the proxy connection.

**Since:** 18

<!--Device-socket-export interface ProxyOptions--><!--Device-socket-export interface ProxyOptions-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## address

```TypeScript
address: NetAddress
```

Proxy server address.

**Type:** NetAddress

**Since:** 18

<!--Device-ProxyOptions-address: NetAddress--><!--Device-ProxyOptions-address: NetAddress-End-->

**System capability:** SystemCapability.Communication.NetStack

## password

```TypeScript
password?: string
```

Specify password, if the proxy server supports user-password authentication.

**Type:** string

**Since:** 18

<!--Device-ProxyOptions-password?: string--><!--Device-ProxyOptions-password?: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## type

```TypeScript
type: ProxyTypes
```

Proxy types.

**Type:** ProxyTypes

**Since:** 18

<!--Device-ProxyOptions-type: ProxyTypes--><!--Device-ProxyOptions-type: ProxyTypes-End-->

**System capability:** SystemCapability.Communication.NetStack

## username

```TypeScript
username?: string
```

Specify username, if the proxy server supports user-password authentication.

**Type:** string

**Since:** 18

<!--Device-ProxyOptions-username?: string--><!--Device-ProxyOptions-username?: string-End-->

**System capability:** SystemCapability.Communication.NetStack

