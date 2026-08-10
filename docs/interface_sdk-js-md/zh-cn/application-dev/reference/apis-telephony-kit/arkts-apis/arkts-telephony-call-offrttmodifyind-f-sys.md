# offRttModifyInd（系统接口）

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## offRttModifyInd

```TypeScript
function offRttModifyInd(callback?: Callback<RttEventInfo>): void
```

Unsubscribe from the rtt modify indication.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function offRttModifyInd(callback?: Callback<RttEventInfo>): void--><!--Device-call-function offRttModifyInd(callback?: Callback<RttEventInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RttEventInfo&gt; | 否 | Indicates the callback for getting the rtt event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8400001 | Invalid parameter value. |
| 8400002 | Operation failed. Cannot connect to service. |
| 8400003 | System internal error. |
| 8400999 | Unknown error code. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

