# ClientCert

The clientCert field of the client certificate, which includes three attributes:client certificate (certPath) and only support PEM format, certificate private key (keyPath), and passphrase (keyPassword).

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-webSocket-export interface ClientCert--><!--Device-webSocket-export interface ClientCert-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
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

## keyPassword

```TypeScript
keyPassword?: string
```

Client certificate password.

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

