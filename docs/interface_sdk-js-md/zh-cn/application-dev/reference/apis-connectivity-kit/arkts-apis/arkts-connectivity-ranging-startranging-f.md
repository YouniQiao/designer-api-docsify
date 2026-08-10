# startRanging

## 导入模块

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## startRanging

```TypeScript
function startRanging(params: RangingParams, callback: Callback<RangingResult>): void
```

Initiates ranging with a specified device.If the link to the target device is already established, ranging starts directly.If not connected, this interface will: 1. Attempt to establish connection and perform pairing/encryption. 2. Query service to verify the device supports ranging. Initiate ranging upon confirmation.Ranging state updates are notified via onRangingStateChange callback.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ranging-function startRanging(params: RangingParams, callback: Callback<RangingResult>): void--><!--Device-ranging-function startRanging(params: RangingParams, callback: Callback<RangingResult>): void-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [RangingParams](arkts-connectivity-ranging-rangingparams-i.md) | 是 | Parameters for ranging. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RangingResult&gt; | 是 | Indicates the callback for reporting the ranging result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 34900052 | The specified type of ranging service is not supported. |
| 801 | Capability not supported. |
| 34900053 | The ranging service is disabled. |
| 34900054 | The parameter value does not meet specifications. |
| 34900051 | The device has already initiated ranging. |
| 34900099 | Internal system error. For example, Internal object is invalid. |
| 201 | Permission denied. |

