# HttpProxy

Network Global Proxy Configuration Information.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-connection-export interface HttpProxy--><!--Device-connection-export interface HttpProxy-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## exclusionList

```TypeScript
exclusionList: Array<string>
```

Do not use a blocking list for proxy servers.

**类型：** Array&lt;string&gt;

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpProxy-exclusionList: Array<string>--><!--Device-HttpProxy-exclusionList: Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## host

```TypeScript
host: string
```

Proxy server host name.

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-HttpProxy-host: string--><!--Device-HttpProxy-host: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## password

```TypeScript
password?: string
```

Http proxy password.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-HttpProxy-password?: string--><!--Device-HttpProxy-password?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## port

```TypeScript
port: int
```

Host port.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-HttpProxy-port: int--><!--Device-HttpProxy-port: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## username

```TypeScript
username?: string
```

Http proxy username.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-HttpProxy-username?: string--><!--Device-HttpProxy-username?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

