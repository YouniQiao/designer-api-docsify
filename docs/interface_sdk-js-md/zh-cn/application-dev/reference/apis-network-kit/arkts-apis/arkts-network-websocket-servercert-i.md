# ServerCert

The serverCert field of the server certificate, which includes two attributes:File paths of server certificate (certPath) and certificate private key (keyPath). Only support PEM format.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-webSocket-export interface ServerCert--><!--Device-webSocket-export interface ServerCert-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## certPath

```TypeScript
certPath: string
```

File path for the server cert.

**类型：** string

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-ServerCert-certPath: string--><!--Device-ServerCert-certPath: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## keyPath

```TypeScript
keyPath: string
```

The path of the server certificate private key file.

**类型：** string

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-ServerCert-keyPath: string--><!--Device-ServerCert-keyPath: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

