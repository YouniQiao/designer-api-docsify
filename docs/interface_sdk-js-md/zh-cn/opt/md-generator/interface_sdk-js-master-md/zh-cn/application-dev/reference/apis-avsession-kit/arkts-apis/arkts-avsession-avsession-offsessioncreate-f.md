# offSessionCreate

## offSessionCreate

```TypeScript
function offSessionCreate(callback?: Callback<AVSessionDescriptor>): void
```

Unregister session create callback

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC

<!--Device-avSession-function offSessionCreate(callback?: Callback<AVSessionDescriptor>): void--><!--Device-avSession-function offSessionCreate(callback?: Callback<AVSessionDescriptor>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-会话服务端异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

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
            avSession.onSessionCreate((descriptor: avSession.AVSessionDescriptor) => {
            });
            avSession.offSessionCreate();
          })
      }
    .width('100%')
    .height('100%')
  }
}
```
