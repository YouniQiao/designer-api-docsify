# offCallStateChangeEx

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## offCallStateChangeEx

```TypeScript
function offCallStateChangeEx(callback?: Callback<TelCallState>): void
```

Cancel callback when the telCall state is updated.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-observer-function offCallStateChangeEx(callback?: Callback<TelCallState>): void--><!--Device-observer-function offCallStateChangeEx(callback?: Callback<TelCallState>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | 否 | Indicates the callback to unsubscribe from the callStateChangeEx event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8800999 | Unknown error. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800001 | Invalid parameter value. |

