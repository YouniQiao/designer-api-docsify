# NetworkAccessPolicy（系统接口）

Network policies that limit the specified UID of application to access the network.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-policy-export interface NetworkAccessPolicy--><!--Device-policy-export interface NetworkAccessPolicy-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## allowCellular

```TypeScript
allowCellular?: boolean
```

Indicate whether the application can be allowed to access the network by cellular.

**类型：** boolean

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-NetworkAccessPolicy-allowCellular?: boolean--><!--Device-NetworkAccessPolicy-allowCellular?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## allowWiFi

```TypeScript
allowWiFi?: boolean
```

Indicate whether the application can be allowed to access the network by wifi.

**类型：** boolean

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-NetworkAccessPolicy-allowWiFi?: boolean--><!--Device-NetworkAccessPolicy-allowWiFi?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## alwaysAllowCellular

```TypeScript
alwaysAllowCellular?: boolean
```

Indicate whether the application can be always allowed to access the network by cellular and users cannot set it.

**类型：** boolean

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-NetworkAccessPolicy-alwaysAllowCellular?: boolean--><!--Device-NetworkAccessPolicy-alwaysAllowCellular?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## alwaysAllowWiFi

```TypeScript
alwaysAllowWiFi?: boolean
```

Indicate whether the application can be always allowed to access the network by wifi and users cannot set it.

**类型：** boolean

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-NetworkAccessPolicy-alwaysAllowWiFi?: boolean--><!--Device-NetworkAccessPolicy-alwaysAllowWiFi?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

