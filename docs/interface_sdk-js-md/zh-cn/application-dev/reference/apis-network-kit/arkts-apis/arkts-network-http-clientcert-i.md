# ClientCert

The clientCert field of the client certificate, which includes 4 attributes:client certificate (cert), client certificate type (certType), certificate private key (key), and passphrase (keyPassword).

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-http-export interface ClientCert--><!--Device-http-export interface ClientCert-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## certPath

```TypeScript
certPath: string
```

The path to the client certificate file.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-ClientCert-certPath: string--><!--Device-ClientCert-certPath: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## certType

```TypeScript
certType?: CertType
```

The type of the client certificate.

**类型：** [CertType](arkts-network-http-certtype-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-ClientCert-certType?: CertType--><!--Device-ClientCert-certType?: CertType-End-->

**系统能力：** SystemCapability.Communication.NetStack

## keyPassword

```TypeScript
keyPassword?: string
```

Password required to use the client certificate private key.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-ClientCert-keyPassword?: string--><!--Device-ClientCert-keyPassword?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## keyPath

```TypeScript
keyPath: string
```

The path of the client certificate private key file.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-ClientCert-keyPath: string--><!--Device-ClientCert-keyPath: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

