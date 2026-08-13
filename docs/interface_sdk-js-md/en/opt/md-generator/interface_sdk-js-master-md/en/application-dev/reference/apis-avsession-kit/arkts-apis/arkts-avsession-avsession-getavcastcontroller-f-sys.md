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

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAVCastController(sessionId: string, callback: AsyncCallback<AVCastController>): void--><!--Device-avSession-function getAVCastController(sessionId: string, callback: AsyncCallback<AVCastController>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
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

          let avCastController: avSession.AVCastController;
          avSession.getAVCastController(sessionId, (avcontroller: avSession.AVCastController) => {
              avCastController = avcontroller;
              console.info('Succeeded in getting AV cast controller.');
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

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAVCastController(sessionId: string, callback: AsyncCallback<AVCastController | undefined>): void--><!--Device-avSession-function getAVCastController(sessionId: string, callback: AsyncCallback<AVCastController | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md) \| undefined & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## getAVCastController

```TypeScript
function getAVCastController(sessionId: string): Promise<AVCastController>
```

Get the current session's remote controller client. If the avsession is not under casting state, the controller will return null.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAVCastController(sessionId: string): Promise<AVCastController>--><!--Device-avSession-function getAVCastController(sessionId: string): Promise<AVCastController>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
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

          let avCastController: avSession.AVCastController;
          avSession.getAVCastController(sessionId).then((avcontroller: avSession.AVCastController) => {
            avCastController = avcontroller;
            console.info('Succeeded in getting AV cast controller.');
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

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getAVCastController(sessionId: string): Promise<AVCastController | undefined>--><!--Device-avSession-function getAVCastController(sessionId: string): Promise<AVCastController | undefined>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md) \| undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
