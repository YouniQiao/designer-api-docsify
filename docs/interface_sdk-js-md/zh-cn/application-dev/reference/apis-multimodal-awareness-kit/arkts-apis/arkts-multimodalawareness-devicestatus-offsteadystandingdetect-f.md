# offSteadyStandingDetect

## 导入模块

```TypeScript
import { deviceStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## offSteadyStandingDetect

```TypeScript
function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void
```

Unsubscribes from steady standing status detection events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-deviceStatus-function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void--><!--Device-deviceStatus-function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DeviceStatus

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;SteadyStandingStatus&gt; | 否 | Indicates the callback for getting the event data. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| 32500003 | Unsubscription failed. |
| 32500001 | Service exception. |

