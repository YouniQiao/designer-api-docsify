# TLSConnectOptions

Defines TLS connection options.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-socket-export interface TLSConnectOptions--><!--Device-socket-export interface TLSConnectOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## ALPNProtocols

```TypeScript
ALPNProtocols?: Array<string>
```

Application layer protocol negotiation extension, such as "spdy/1", "http/1.1", "h2"

**类型：** Array&lt;string&gt;

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TLSConnectOptions-ALPNProtocols?: Array<string>--><!--Device-TLSConnectOptions-ALPNProtocols?: Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetStack

## address

```TypeScript
address: NetAddress
```

Gateway address.

**类型：** [NetAddress](arkts-network-connection-netaddress-i.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TLSConnectOptions-address: NetAddress--><!--Device-TLSConnectOptions-address: NetAddress-End-->

**系统能力：** SystemCapability.Communication.NetStack

## proxy

```TypeScript
proxy?: ProxyOptions
```

Set this option for the proxy feature.

**类型：** [ProxyOptions](arkts-network-socket-proxyoptions-i.md)

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-TLSConnectOptions-proxy?: ProxyOptions--><!--Device-TLSConnectOptions-proxy?: ProxyOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## secureOptions

```TypeScript
secureOptions: TLSSecureOptions
```

Protocol http2TLS security related operations.

**类型：** [TLSSecureOptions](arkts-network-socket-tlssecureoptions-i.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TLSConnectOptions-secureOptions: TLSSecureOptions--><!--Device-TLSConnectOptions-secureOptions: TLSSecureOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## skipRemoteValidation

```TypeScript
skipRemoteValidation?: boolean
```

Skip identity verification for remote servers. The default value is false.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-TLSConnectOptions-skipRemoteValidation?: boolean--><!--Device-TLSConnectOptions-skipRemoteValidation?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## timeout

```TypeScript
timeout?: int
```

Timeout duration of the TLSSocket connection, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为24。

<!--Device-TLSConnectOptions-timeout?: int--><!--Device-TLSConnectOptions-timeout?: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

