# cancelSession（系统接口）

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## cancelSession

```TypeScript
function cancelSession(slotId: int, transactionId: string, cancelReason: CancelReason): Promise<ResultCode>
```

Cancel session can be used in the1.after the response to "ES9+.AuthenticateClient"2.after the response to "ES9+.GetBoundProfilePackage"

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function cancelSession(slotId: int, transactionId: string, cancelReason: CancelReason): Promise<ResultCode>--><!--Device-eSIM-function cancelSession(slotId: int, transactionId: string, cancelReason: CancelReason): Promise<ResultCode>-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number. |
| transactionId | string | 是 | The transaction ID returned by SM-DP+ server. |
| cancelReason | [CancelReason](arkts-telephony-esim-cancelreason-e-sys.md) | 是 | The cancel reason. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ResultCode&gt; | Returns the result code. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 3120002 | System internal error. |
| 3120001 | Service connection failed. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

let transactionId = '';
eSIM.cancelSession(1, transactionId, eSIM.CancelReason.CANCEL_REASON_END_USER_REJECTION)
  .then((data: eSIM.ResultCode) => {
    console.info(`cancelSession, result: data->${JSON.stringify(data)}`);
  })
  .catch((err: BusinessError<void>) => {
    console.error(`cancelSession execution failed: err->${JSON.stringify(err)}`);
  });
```

