# createAVSession

## createAVSession

```TypeScript
function createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void
```

创建会话对象，一个应用程序仅允许存在一个会话，重复创建会失败，结果通过callback异步回调方式返回。

> **说明：**
> 
> - 在业务执行阶段需要保持avsession对象存活，避免后台管控静音、设备选择异常、通知/锁屏/胶囊播控卡片显示异常等情况。

**起始版本：** 10

<!--Device-avSession-function createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void--><!--Device-avSession-function createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| tag | string | 是 |
| type | [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVSession&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## 示例

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
          let sessionId: string;  // 供后续函数入参使用。

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

创建会话对象，一个应用进程仅允许存在一个会话，重复创建会失败，结果通过Promise异步回调方式返回。

> **说明：**
> 
> - 在业务执行阶段需要保持avsession对象存活，避免后台管控静音、设备选择异常、通知/锁屏/胶囊播控卡片显示异常等情况。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-avSession-function createAVSession(context: Context, tag: string, type: AVSessionType): Promise<AVSession>--><!--Device-avSession-function createAVSession(context: Context, tag: string, type: AVSessionType): Promise<AVSession>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| tag | string | 是 |
| type | [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;AVSession&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## 示例

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
            let sessionId: string;  // 供后续函数入参使用。

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
