# cancelSession (System API)

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## cancelSession

```TypeScript
function cancelSession(slotId: number, transactionId: string, cancelReason: CancelReason): Promise<ResultCode>
```

Cancel session can be used in the1.after the response to "ES9+.AuthenticateClient"2.after the response to "ES9+.GetBoundProfilePackage"

**Since:** 18

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function cancelSession(slotId: int, transactionId: string, cancelReason: CancelReason): Promise<ResultCode>--><!--Device-eSIM-function cancelSession(slotId: int, transactionId: string, cancelReason: CancelReason): Promise<ResultCode>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| transactionId | string | Yes |
| cancelReason | [CancelReason](arkts-telephony-esim-cancelreason-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ResultCode & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3120002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#3120002-system-internal-error) |
| [3120001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#3120001-service-connection-error) |

## Examples

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
