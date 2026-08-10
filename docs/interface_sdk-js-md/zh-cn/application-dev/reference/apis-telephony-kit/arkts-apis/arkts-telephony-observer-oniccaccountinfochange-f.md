# onIccAccountInfoChange

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## onIccAccountInfoChange

```TypeScript
function onIccAccountInfoChange(callback: Callback<void>): void
```

Receives an ICC account change. This callback is invoked when the ICC account updates and the observer is added to monitor the updates.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-observer-function onIccAccountInfoChange(callback: Callback<void>): void--><!--Device-observer-function onIccAccountInfoChange(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | including state Indicates the ICC account information, and reason Indicates the cause of the change. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

