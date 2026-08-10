# createServer

## 导入模块

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
```

## createServer

```TypeScript
function createServer(): Server
```

创建SSAP服务端实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ssap-function createServer(): Server--><!--Device-ssap-function createServer(): Server-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Server](arkts-connectivity-ssap-server-i.md) | 返回一个SSAP服务端实例{ |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |

