# getState

## 导入模块

```TypeScript
import { manager } from 'kits/@kit.ConnectivityKit';
```

## getState

```TypeScript
function getState(): NearlinkState
```

获取星闪状态。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-manager-function getState(): NearlinkState--><!--Device-manager-function getState(): NearlinkState-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NearlinkState](arkts-connectivity-manager-nearlinkstate-e.md) | 返回NearLink状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |

