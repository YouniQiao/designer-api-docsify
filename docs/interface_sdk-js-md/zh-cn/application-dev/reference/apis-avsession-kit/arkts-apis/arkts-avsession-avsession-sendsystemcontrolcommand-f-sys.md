# sendSystemControlCommand（系统接口）

## 导入模块

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## sendSystemControlCommand

```TypeScript
function sendSystemControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void
```

发送控制命令给置顶会话。结果通过callback异步回调方式返回。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |
| [6600107](../errorcode-avsession.md#6600107-命令消息过载) |


## sendSystemControlCommand

```TypeScript
function sendSystemControlCommand(command: AVControlCommand): Promise<void>
```

发送控制命令给置顶会话。结果通过Promise异步回调方式返回。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |
| [6600107](../errorcode-avsession.md#6600107-命令消息过载) |
