# ServerAuthentication

HTTP server authentication.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-http-export interface ServerAuthentication--><!--Device-http-export interface ServerAuthentication-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## authenticationType

```TypeScript
authenticationType?: AuthenticationType
```

Authentication type of server. If not set, negotiate with the server.

**类型：** [AuthenticationType](arkts-network-http-authenticationtype-t.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ServerAuthentication-authenticationType?: AuthenticationType--><!--Device-ServerAuthentication-authenticationType?: AuthenticationType-End-->

**系统能力：** SystemCapability.Communication.NetStack

## credential

```TypeScript
credential: Credential
```

Credential of server.

**类型：** [Credential](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-credential-i.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ServerAuthentication-credential: Credential--><!--Device-ServerAuthentication-credential: Credential-End-->

**系统能力：** SystemCapability.Communication.NetStack

