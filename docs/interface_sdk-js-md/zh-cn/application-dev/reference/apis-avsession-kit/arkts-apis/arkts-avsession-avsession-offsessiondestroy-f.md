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

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
