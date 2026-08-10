# NetAddress

Defines a network address.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-connection-export interface NetAddress--><!--Device-connection-export interface NetAddress-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address: string
```

Network address.

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-NetAddress-address: string--><!--Device-NetAddress-address: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## family

```TypeScript
family?: int
```

Address family identifier. The value is 1 for IPv4 and 2 for IPv6. The default value is 1.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-NetAddress-family?: int--><!--Device-NetAddress-family?: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## port

```TypeScript
port?: int
```

Port number. The value ranges from 0 to 65535.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-NetAddress-port?: int--><!--Device-NetAddress-port?: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

