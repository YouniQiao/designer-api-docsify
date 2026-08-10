# stopPassiveRanging

## 导入模块

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## stopPassiveRanging

```TypeScript
function stopPassiveRanging(handle: int, capabilityType: RangingTypes): void
```

Stops passive ranging mode.

Stops the passive ranging broadcast and cleans up associated resources based on the specified handle and ranging capability type.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ranging-function stopPassiveRanging(handle: int, capabilityType: RangingTypes): void--><!--Device-ranging-function stopPassiveRanging(handle: int, capabilityType: RangingTypes): void-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the handle number of ranging monitoring. |
| capabilityType | [RangingTypes](arkts-connectivity-ranging-rangingtypes-e.md) | 是 | Indicates the capability type for ranging. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 34900052 | The specified type of ranging service is not supported. |
| 801 | Capability not supported. |
| 34900054 | The parameter value does not meet specifications. |
| 34900099 | Internal system error. For example, Internal object is invalid. |
| 201 | Permission denied. |

