# ValidationContext

The validation context of {@link ValidationCallback}

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-http-export interface ValidationContext--><!--Device-http-export interface ValidationContext-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## host

```TypeScript
host: string
```

The host of this request.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ValidationContext-host: string--><!--Device-ValidationContext-host: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## ip

```TypeScript
ip: string
```

The real IP which this request connect to.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ValidationContext-ip: string--><!--Device-ValidationContext-ip: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## pemCerts

```TypeScript
pemCerts: string[]
```

The raw data which in PEM format of certificate.

**类型：** string[]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ValidationContext-pemCerts: string[]--><!--Device-ValidationContext-pemCerts: string[]-End-->

**系统能力：** SystemCapability.Communication.NetStack

## x509Certs

```TypeScript
x509Certs: X509Cert[]
```

X509 certificate chain.

**类型：** [X509Cert](arkts-network-http-x509cert-t.md)[]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ValidationContext-x509Certs: X509Cert[]--><!--Device-ValidationContext-x509Certs: X509Cert[]-End-->

**系统能力：** SystemCapability.Communication.NetStack

