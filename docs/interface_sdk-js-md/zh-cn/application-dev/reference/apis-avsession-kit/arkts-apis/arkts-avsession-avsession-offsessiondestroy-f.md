# offSessionDestroy

## 导入模块

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## offSessionDestroy

```TypeScript
function offSessionDestroy(callback?: Callback<AVSessionDescriptor>): void
```

Unregister session destroy callback

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC

<!--Device-avSession-function offSessionDestroy(callback?: Callback<AVSessionDescriptor>): void--><!--Device-avSession-function offSessionDestroy(callback?: Callback<AVSessionDescriptor>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVSessionDescriptor&gt; | 否 | 会话销毁回调函数 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 201 | permission denied. |

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
            avSession.onSessionDestroy((descriptor: avSession.AVSessionDescriptor) => {
            });
            avSession.offSessionDestroy();
          })
      }
    .width('100%')
    .height('100%')
  }
}
```

