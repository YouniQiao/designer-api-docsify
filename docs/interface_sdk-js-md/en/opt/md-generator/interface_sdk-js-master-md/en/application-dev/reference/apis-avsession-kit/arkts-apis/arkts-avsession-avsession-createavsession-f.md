# createAVSession

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## createAVSession

```TypeScript
function createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void
```

Create an AVSession instance. An ability can only create one AVSession

**Since:** 10

<!--Device-avSession-function createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void--><!--Device-avSession-function createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| tag | string | Yes |
| type | [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVSession](arkts-avsession-avsession-avsession-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6600101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-session-service-exception) |

## Examples

```TypeScript
import { avSession } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .onClick(()=>{
          let currentAVSession: avSession.AVSession;
          let tag = "createNewSession";
          let context: Context = this.getUIContext().getHostContext() as Context;
          let sessionId: string;  // Used as an input parameter of subsequent functions.

          avSession.createAVSession(context, tag, "audio", async (err:BusinessError, data: avSession.AVSession) => {
              currentAVSession = data;
              sessionId = currentAVSession.sessionId;
              console.info(`Succeeded in creating AV session, sessionId: ${sessionId}`);
            });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```


## createAVSession

```TypeScript
function createAVSession(context: Context, tag: string, type: AVSessionType): Promise<AVSession>
```

Create an AVSession instance. An ability can only create one AVSession

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-avSession-function createAVSession(context: Context, tag: string, type: AVSessionType): Promise<AVSession>--><!--Device-avSession-function createAVSession(context: Context, tag: string, type: AVSessionType): Promise<AVSession>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| tag | string | Yes |
| type | [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVSession](arkts-avsession-avsession-avsession-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6600101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-session-service-exception) |

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
            let currentAVSession: avSession.AVSession;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;
            let sessionId: string;  // Used as an input parameter of subsequent functions.

            avSession.createAVSession(context, tag, "audio").then(async (data: avSession.AVSession) => {
            currentAVSession = data;
            sessionId = currentAVSession.sessionId;
            console.info(`Succeeded in creating AV session, sessionId: ${sessionId}`);
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```
