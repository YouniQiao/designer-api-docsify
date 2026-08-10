# Socks5Proxy

Socks5 Proxy Configuration Information.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-connection-export interface Socks5Proxy--><!--Device-connection-export interface Socks5Proxy-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## dnsStrategy

```TypeScript
dnsStrategy?: Socks5DnsStrategy
```

DNS resolution strategy.Determines whether the client or the proxy server resolves the domain name.

**类型：** [Socks5DnsStrategy](arkts-network-connection-socks5dnsstrategy-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Socks5Proxy-dnsStrategy?: Socks5DnsStrategy--><!--Device-Socks5Proxy-dnsStrategy?: Socks5DnsStrategy-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## exclusionList

```TypeScript
exclusionList?: Array<string>
```

Exclusion list for proxy servers.

**类型：** Array&lt;string&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Socks5Proxy-exclusionList?: Array<string>--><!--Device-Socks5Proxy-exclusionList?: Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## host

```TypeScript
host: string
```

Proxy server host name.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Socks5Proxy-host: string--><!--Device-Socks5Proxy-host: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## password

```TypeScript
password?: string
```

Proxy password.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Socks5Proxy-password?: string--><!--Device-Socks5Proxy-password?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## port

```TypeScript
port: int
```

Host port.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Socks5Proxy-port: int--><!--Device-Socks5Proxy-port: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## username

```TypeScript
username?: string
```

Proxy username.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Socks5Proxy-username?: string--><!--Device-Socks5Proxy-username?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

