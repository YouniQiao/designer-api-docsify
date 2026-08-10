# TLSSecureOptions

Defines TLS security options. The CA certificate is mandatory, and other parameters are optional.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-socket-export interface TLSSecureOptions--><!--Device-socket-export interface TLSSecureOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## ca

```TypeScript
ca?: string | Array<string>
```

Certificate used to verify the identity of the server, if it is not set, use system ca.

**类型：** string \| Array&lt;string&gt;

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-TLSSecureOptions-ca?: string | Array<string>--><!--Device-TLSSecureOptions-ca?: string | Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetStack

## cert

```TypeScript
cert?: string | Array<string>
```

Certificate proving the identity of the client

**类型：** string \| Array&lt;string&gt;

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-TLSSecureOptions-cert?: string | Array<string>--><!--Device-TLSSecureOptions-cert?: string | Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetStack

## cipherSuite

```TypeScript
cipherSuite?: string
```

Crypto suite specification

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TLSSecureOptions-cipherSuite?: string--><!--Device-TLSSecureOptions-cipherSuite?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## isBidirectionalAuthentication

```TypeScript
isBidirectionalAuthentication?: boolean
```

Used to set up bidirectional authentication. The default value is false.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-TLSSecureOptions-isBidirectionalAuthentication?: boolean--><!--Device-TLSSecureOptions-isBidirectionalAuthentication?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## key

```TypeScript
key?: string
```

Private key of client certificate

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TLSSecureOptions-key?: string--><!--Device-TLSSecureOptions-key?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## password

```TypeScript
password?: string
```

Password of the private key

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TLSSecureOptions-password?: string--><!--Device-TLSSecureOptions-password?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## protocols

```TypeScript
protocols?: Protocol | Array<Protocol>
```

TLS protocol version

**类型：** [Protocol](arkts-network-socket-protocol-e.md) \| Array&lt;Protocol&gt;

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TLSSecureOptions-protocols?: Protocol | Array<Protocol>--><!--Device-TLSSecureOptions-protocols?: Protocol | Array<Protocol>-End-->

**系统能力：** SystemCapability.Communication.NetStack

## signatureAlgorithms

```TypeScript
signatureAlgorithms?: string
```

&lt;P&gt;Supported signature algorithms. This string can contain summary algorithms(SHA256,MD5,etc),Public key algorithm(RSA-PSS,ECDSA,etc),Combination of the two(For example 'RSA+SHA384') or TLS v1.3 Scheme name(For example rsa_pss_pss_sha512)&lt;/P&gt;

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TLSSecureOptions-signatureAlgorithms?: string--><!--Device-TLSSecureOptions-signatureAlgorithms?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## useRemoteCipherPrefer

```TypeScript
useRemoteCipherPrefer?: boolean
```

default is false, use local cipher.

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-TLSSecureOptions-useRemoteCipherPrefer?: boolean--><!--Device-TLSSecureOptions-useRemoteCipherPrefer?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

