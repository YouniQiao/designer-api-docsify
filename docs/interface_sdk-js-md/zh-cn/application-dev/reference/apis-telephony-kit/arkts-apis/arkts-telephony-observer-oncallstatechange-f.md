# onCallStateChange

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## onCallStateChange

```TypeScript
function onCallStateChange(callback: Callback<CallStateInfo>): void
```

Callback when the call state corresponding to the default sim card is updated.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-observer-function onCallStateChange(callback: Callback<CallStateInfo>): void--><!--Device-observer-function onCallStateChange(callback: Callback<CallStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CallStateInfo&gt; | 是 | Indicates the callback for getting the call state and the called number. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |


## onCallStateChange

```TypeScript
function onCallStateChange(options: ObserverOptions, callback: Callback<CallStateInfo>): void
```

Callback when the call state corresponding to the monitored {@code slotId} is updated.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-observer-function onCallStateChange(options: ObserverOptions, callback: Callback<CallStateInfo>): void--><!--Device-observer-function onCallStateChange(options: ObserverOptions, callback: Callback<CallStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CallStateInfo&gt; | 是 | Indicates the callback for getting the call state and the called number. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

