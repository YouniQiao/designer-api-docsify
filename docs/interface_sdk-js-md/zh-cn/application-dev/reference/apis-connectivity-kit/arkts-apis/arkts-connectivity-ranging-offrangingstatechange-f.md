# offRangingStateChange

## 导入模块

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## offRangingStateChange

```TypeScript
function offRangingStateChange(callback?: Callback<RangingStateChangeInfo>): void
```

Unsubscribe from ranging state change events.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ranging-function offRangingStateChange(callback?: Callback<RangingStateChangeInfo>): void--><!--Device-ranging-function offRangingStateChange(callback?: Callback<RangingStateChangeInfo>): void-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RangingStateChangeInfo&gt; | 否 | Callback used to listen to the ranging state. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 34900099 | Internal system error. For example, Internal object is invalid. |
| 201 | Permission denied. |

