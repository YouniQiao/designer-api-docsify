# getDistributedSessionController（系统接口）

## getDistributedSessionController

```TypeScript
function getDistributedSessionController(distributedSessionType: DistributedSessionType): Promise<Array<AVSessionController>>
```

根据远端会话类型，获取远端分布式会话控制器。结果通过Promise异步回调方式返回。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getDistributedSessionController(distributedSessionType: DistributedSessionType): Promise<Array<AVSessionController>>--><!--Device-avSession-function getDistributedSessionController(distributedSessionType: DistributedSessionType): Promise<Array<AVSessionController>>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| distributedSessionType | [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { avSession } from '@kit.AVSessionKit';

avSession.getDistributedSessionController(avSession.DistributedSessionType.TYPE_SESSION_REMOTE).then((sessionControllers: Array<avSession.AVSessionController>) => {
  console.info(`Succeeded in getting distributed session controller, length: ${sessionControllers.length}`);
});
```
