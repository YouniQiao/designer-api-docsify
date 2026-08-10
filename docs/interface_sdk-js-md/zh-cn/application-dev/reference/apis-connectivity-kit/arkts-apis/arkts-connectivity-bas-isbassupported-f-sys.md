# isBasSupported（系统接口）

## 导入模块

```TypeScript
import { bas } from 'kits/@kit.ConnectivityKit';
```

## isBasSupported

```TypeScript
function isBasSupported(): boolean
```

Determine whether the local device can obtain the battery level of the remote device.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bas-function isBasSupported(): boolean--><!--Device-bas-function isBasSupported(): boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the battery service is enabled; returns false otherwise. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Non-system applications are not allowed to use system APIs. |
| 2900099 | Operation failed. |

