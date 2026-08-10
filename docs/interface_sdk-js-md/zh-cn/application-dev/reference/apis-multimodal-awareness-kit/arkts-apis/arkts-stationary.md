# @ohos.stationary

The **stationary** module provides APIs to report the device status, including absolute still and relative still.

> **NOTE：**
> 
> This module does not support x86 emulators.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-unnamed-declare namespace stationary--><!--Device-unnamed-declare namespace stationary-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Stationary

## 导入模块

```TypeScript
import { stationary } from 'kits/@kit.MultimodalAwarenessKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [off](arkts-multimodalawareness-stationary-off-f.md#off) | Unsubscribes from the device status. |
| [on](arkts-multimodalawareness-stationary-on-f.md#on) | Subscribes to the device status. |
| [once](arkts-multimodalawareness-stationary-once-f.md#once) | Obtains the device status. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ActivityResponse](arkts-multimodalawareness-stationary-activityresponse-i.md) | Defines the response interface to receive the device status. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ActivityEvent](arkts-multimodalawareness-stationary-activityevent-e.md) | Enumerates the device status events. |
| [ActivityState](arkts-multimodalawareness-stationary-activitystate-e.md) | Enumerates the device statuses. |

### 类型

| 名称 | 说明 |
| --- | --- |
| [ActivityType](arkts-multimodalawareness-stationary-activitytype-t.md) | Enumerates the device status types. |

