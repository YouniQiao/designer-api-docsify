# createController (System API)

## Modules to Import

```TypeScript
import { avSession } from 'avSession';
```

## createController

```TypeScript
function createController(sessionId: string, callback: AsyncCallback<AVSessionController>): void
```

Create an avsession controller

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function createController(sessionId: string, callback: AsyncCallback<AVSessionController>): void--><!--Device-avSession-function createController(sessionId: string, callback: AsyncCallback<AVSessionController>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | Specifies the sessionId to create the controller. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt; | Yes | async callback for AVSessionController. If provided 'default', the system will create a default controller, Used to control the system default session |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let currentAVcontroller: avSession.AVSessionController | undefined = undefined;
currentAvSession.createController(sessionId, (err: BusinessError, avcontroller: avSession.AVSessionController) => {
  if (err) {
    console.error(`CreateController BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    currentAVcontroller = avcontroller;
    console.info('CreateController : SUCCESS ');
  }
});
```


## createController

```TypeScript
function createController(sessionId: string): Promise<AVSessionController>
```

Create an avsession controller

**Since:** 23

**Required permissions:** 
- API version 23+: ohos.permission.MANAGE_MEDIA_RESOURCES or ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
- API version 9 - 22: ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function createController(sessionId: string): Promise<AVSessionController>--><!--Device-avSession-function createController(sessionId: string): Promise<AVSessionController>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | Specifies the sessionId to create the controller. If provided 'default', the system will create a default controller, Used to control the system default session |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt; | Promise for AVSessionController |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App.<br>**Applicable version:** 9 - 22 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let currentAVcontroller: avSession.AVSessionController | undefined = undefined;
currentAvSession.createController(sessionId).then((avcontroller: avSession.AVSessionController) => {
  currentAVcontroller = avcontroller;
  console.info('CreateController : SUCCESS ');
}).catch((err: BusinessError) => {
  console.error(`CreateController BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

