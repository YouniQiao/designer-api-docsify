# ProxyOptions

Define parameters for the proxy connection.

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-socket-export interface ProxyOptions--><!--Device-socket-export interface ProxyOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address: NetAddress
```

Proxy server address.

**类型：** [NetAddress](arkts-network-connection-netaddress-i.md)

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-ProxyOptions-address: NetAddress--><!--Device-ProxyOptions-address: NetAddress-End-->

**系统能力：** SystemCapability.Communication.NetStack

## password

```TypeScript
password?: string
```

Specify password, if the proxy server supports user-password authentication.

**类型：** string

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-ProxyOptions-password?: string--><!--Device-ProxyOptions-password?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## type

```TypeScript
type: ProxyTypes
```

Proxy types.

**类型：** [ProxyTypes](arkts-network-socket-proxytypes-e.md)

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-ProxyOptions-type: ProxyTypes--><!--Device-ProxyOptions-type: ProxyTypes-End-->

**系统能力：** SystemCapability.Communication.NetStack

## username

```TypeScript
username?: string
```

Specify username, if the proxy server supports user-password authentication.

**类型：** string

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-ProxyOptions-username?: string--><!--Device-ProxyOptions-username?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

