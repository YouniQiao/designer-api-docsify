# getAVCastController (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## getAVCastController

```TypeScript
function getAVCastController(sessionId: string, callback: AsyncCallback<AVCastController>): void
```

Register a callback to retrieve an avsession cast controller. This function can be used at both side to get the same controller to do the playback control.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAVCastController(sessionId: string, callback: AsyncCallback<AVCastController>): void--><!--Device-avSession-function getAVCastController(sessionId: string, callback: AsyncCallback<AVCastController>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | Specifies the sessionId to get controller. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md)&gt; | Yes | async callback for the AVCastController. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | session does not exist |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .onClick(() => {
          let currentAVSession: avSession.AVSession | undefined = undefined;
          let tag = "createNewSession";
          let context = this.getUIContext().getHostContext() as Context;
          let sessionId: string = ""; // Used as an input parameter of subsequent functions.

          let aVCastController: avSession.AVCastController;
          avSession.getAVCastController(sessionId, (err: BusinessError, avcontroller: avSession.AVCastController) => {
            if (err) {
              console.error(`getAVCastController BusinessError: code: ${err.code}, message: ${err.message}`);
            } else {
              aVCastController = avcontroller;
              console.info('getAVCastController : SUCCESS ');
            }
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```


## getAVCastController

```TypeScript
function getAVCastController(sessionId: string, callback: AsyncCallback<AVCastController | undefined>): void
```

Register a callback to retrieve an avsession cast controller. This function can be used at both side to get the same controller to do the playback control.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAVCastController(sessionId: string, callback: AsyncCallback<AVCastController | undefined>): void--><!--Device-avSession-function getAVCastController(sessionId: string, callback: AsyncCallback<AVCastController | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | Specifies the sessionId to get controller. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md) \| undefined&gt; | Yes | async callback for the AVCastController. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | session does not exist |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |


## getAVCastController

```TypeScript
function getAVCastController(sessionId: string): Promise<AVCastController>
```

Get the current session's remote controller client. If the avsession is not under casting state, the controller will return null.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAVCastController(sessionId: string): Promise<AVCastController>--><!--Device-avSession-function getAVCastController(sessionId: string): Promise<AVCastController>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | Specifies the sessionId to get controller. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md)&gt; | Promise for the AVCastController |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | server exception |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | session does not exist |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .onClick(() => {
          let currentAVSession: avSession.AVSession | undefined = undefined;
          let tag = "createNewSession";
          let context = this.getUIContext().getHostContext() as Context;
          let sessionId: string = ""; // Used as an input parameter of subsequent functions.

          let aVCastController: avSession.AVCastController;
          avSession.getAVCastController(sessionId).then((avcontroller: avSession.AVCastController) => {
            aVCastController = avcontroller;
            console.info('getAVCastController : SUCCESS');
          }).catch((err: BusinessError) => {
            console.error(`getAVCastController BusinessError: code: ${err.code}, message: ${err.message}`);
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```


## getAVCastController

```TypeScript
function getAVCastController(sessionId: string): Promise<AVCastController | undefined>
```

Get the current session's remote controller client. If the avsession is not under casting state, the controller will return undefined.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAVCastController(sessionId: string): Promise<AVCastController | undefined>--><!--Device-avSession-function getAVCastController(sessionId: string): Promise<AVCastController | undefined>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | Specifies the sessionId to get controller. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md) \| undefined&gt; | Promise for the AVCastController |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | server exception |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | session does not exist |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

