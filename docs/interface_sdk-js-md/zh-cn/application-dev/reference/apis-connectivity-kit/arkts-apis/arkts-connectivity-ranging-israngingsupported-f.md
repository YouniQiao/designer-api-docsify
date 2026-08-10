# isRangingSupported

## 导入模块

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## isRangingSupported

```TypeScript
function isRangingSupported(): boolean
```

Checks whether the current device supports the ranging feature.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ranging-function isRangingSupported(): boolean--><!--Device-ranging-function isRangingSupported(): boolean-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true indicates that the device supports the ranging capability, and false indicates that the device does not support the ranging capability. |

