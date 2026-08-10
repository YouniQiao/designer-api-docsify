# setRttCapability（系统接口）

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## setRttCapability

```TypeScript
function setRttCapability(accountId: int, isEnable: boolean): Promise<void>
```

Set rtt capability.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.PLACE_CALL

<!--Device-call-function setRttCapability(accountId: int, isEnable: boolean): Promise<void>--><!--Device-call-function setRttCapability(accountId: int, isEnable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the identifier of the account to set rtt capability. |
| isEnable | boolean | 是 | Indicates whether Rtt capability is enabled. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setRttCapability. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8400001 | Invalid parameter value. |
| 8400002 | Operation failed. Cannot connect to service. |
| 8400003 | System internal error. |
| 8400999 | Unknown error code. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

