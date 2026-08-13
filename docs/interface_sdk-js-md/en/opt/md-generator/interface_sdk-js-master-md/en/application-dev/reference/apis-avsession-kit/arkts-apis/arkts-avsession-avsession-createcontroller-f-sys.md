# createController (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## createController

```TypeScript
function createController(sessionId: string, callback: AsyncCallback<AVSessionController>): void
```

Create an avsession controller

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function createController(sessionId: string, callback: AsyncCallback<AVSessionController>): void--><!--Device-avSession-function createController(sessionId: string, callback: AsyncCallback<AVSessionController>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt; | Yes |

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
          .onClick(()=>{
            avSession.getAllSessionDescriptors().then((descriptors: avSession.AVSessionDescriptor[]) => {
              console.info(`Succeeded in getting all session descriptors, length: ${descriptors.length}`);
              if (descriptors.length > 0 ) {
avSession.createController(descriptors[0]?.sessionId, (avcontroller: avSession.AVSessionController) => { 
                    console.info('Succeeded in creating controller.'); 
                });
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```


## createController

```TypeScript
function createController(sessionId: string): Promise<AVSessionController>
```

Create an avsession controller

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 23+: ohos.permission.MANAGE_MEDIA_RESOURCES or ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
- API version 9 - 22: ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function createController(sessionId: string): Promise<AVSessionController>--><!--Device-avSession-function createController(sessionId: string): Promise<AVSessionController>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
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
          .onClick(()=>{
            avSession.getAllSessionDescriptors().then((descriptors: avSession.AVSessionDescriptor[]) => {
              console.info(`Succeeded in getting all session descriptors, length: ${descriptors.length}`);
              if (descriptors.length > 0 ) {
                avSession.createController(descriptors[0]?.sessionId).then((avcontroller: avSession.AVSessionController) => {
                  console.info('Succeeded in creating controller.');
                });
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```
