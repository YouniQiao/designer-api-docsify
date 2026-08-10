# ConnectionExtraInfo

Information details of the HTTP request

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-http-export interface ConnectionExtraInfo--><!--Device-http-export interface ConnectionExtraInfo-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## cipherSuite

```TypeScript
cipherSuite?: CipherSuite
```

The cipher suite used to fetch the resource.

**类型：** [CipherSuite](arkts-network-http-ciphersuite-t.md)

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-cipherSuite?: CipherSuite--><!--Device-ConnectionExtraInfo-cipherSuite?: CipherSuite-End-->

**系统能力：** SystemCapability.Communication.NetStack

## isCacheHit

```TypeScript
isCacheHit: boolean
```

A Boolean value that indicates whether the http request hit cache.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-isCacheHit: boolean--><!--Device-ConnectionExtraInfo-isCacheHit: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## isProxyConnection

```TypeScript
isProxyConnection: boolean
```

A Boolean value that indicastes whether the task used a proxy connection to fetch the resource.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-isProxyConnection: boolean--><!--Device-ConnectionExtraInfo-isProxyConnection: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## isReusedConnection

```TypeScript
isReusedConnection: boolean
```

The HTTP request is a reused connection or not.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-isReusedConnection: boolean--><!--Device-ConnectionExtraInfo-isReusedConnection: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## localAddress

```TypeScript
localAddress: string
```

localAddress of the HTTP request.

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-localAddress: string--><!--Device-ConnectionExtraInfo-localAddress: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## localPort

```TypeScript
localPort: int
```

localPort of the HTTP request. -1 for unknown.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-localPort: int--><!--Device-ConnectionExtraInfo-localPort: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## networkProtocolName

```TypeScript
networkProtocolName: string
```

The network protocol used to fetch the resource.

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-networkProtocolName: string--><!--Device-ConnectionExtraInfo-networkProtocolName: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## redirectCount

```TypeScript
redirectCount: int
```

The HTTP request redirect count.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-redirectCount: int--><!--Device-ConnectionExtraInfo-redirectCount: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## remoteAddress

```TypeScript
remoteAddress: string
```

remoteAddress of the HTTP request.

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-remoteAddress: string--><!--Device-ConnectionExtraInfo-remoteAddress: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## remotePort

```TypeScript
remotePort: int
```

remotePort of the HTTP request. -1 for unknown.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-remotePort: int--><!--Device-ConnectionExtraInfo-remotePort: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## tlsVersion

```TypeScript
tlsVersion?: TlsVersion
```

The tls version used to fetch the resource.

**类型：** [TlsVersion](arkts-network-http-tlsversion-e.md)

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionExtraInfo-tlsVersion?: TlsVersion--><!--Device-ConnectionExtraInfo-tlsVersion?: TlsVersion-End-->

**系统能力：** SystemCapability.Communication.NetStack

