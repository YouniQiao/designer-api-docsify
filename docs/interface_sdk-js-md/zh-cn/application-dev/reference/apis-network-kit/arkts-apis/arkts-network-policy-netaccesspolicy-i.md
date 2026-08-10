# NetAccessPolicy

Network policies that limit the specified UID of application to access the network.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-policy-export interface NetAccessPolicy--><!--Device-policy-export interface NetAccessPolicy-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## allowCellular

```TypeScript
allowCellular: boolean
```

Indicate whether the application can be allowed to access the network by cellular.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NetAccessPolicy-allowCellular: boolean--><!--Device-NetAccessPolicy-allowCellular: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## allowWiFi

```TypeScript
allowWiFi: boolean
```

Indicate whether the application can be allowed to access the network by wifi.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NetAccessPolicy-allowWiFi: boolean--><!--Device-NetAccessPolicy-allowWiFi: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

