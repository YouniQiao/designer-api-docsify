# sendSystemAVKeyEvent (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## sendSystemAVKeyEvent

```TypeScript
function sendSystemAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void
```

Send system media key event.The system automatically selects the recipient.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function sendSystemAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void--><!--Device-avSession-function sendSystemAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md) | Yes | The key event to be sent |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | The asyncCallback triggered when the command is executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | permission denied |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [6600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |

## Examples

```TypeScript
import { KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyItem: KeyEvent.Key = {code:0x49, pressedTime:2, deviceId:0};
let event: KeyEvent.KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:[keyItem], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};

avSession.sendSystemAVKeyEvent(event, (err: BusinessError) => {
  if (err) {
    console.error(`SendSystemAVKeyEvent BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SendSystemAVKeyEvent : SUCCESS ');
  }
});
```


## sendSystemAVKeyEvent

```TypeScript
function sendSystemAVKeyEvent(event: KeyEvent): Promise<void>
```

Send system media key event.The system automatically selects the recipient.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function sendSystemAVKeyEvent(event: KeyEvent): Promise<void>--><!--Device-avSession-function sendSystemAVKeyEvent(event: KeyEvent): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md) | Yes | The key event to be sent |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | permission denied |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [6600105](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |

## Examples

```TypeScript
import { KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyItem: KeyEvent.Key = {code:0x49, pressedTime:2, deviceId:0};
let event: KeyEvent.KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:[keyItem], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};

avSession.sendSystemAVKeyEvent(event).then(() => {
  console.info('SendSystemAVKeyEvent Successfully');
}).catch((err: BusinessError) => {
  console.error(`SendSystemAVKeyEvent BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

