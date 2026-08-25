# removeStickyCommonEvent（系统接口）

## 导入模块

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## removeStickyCommonEvent

```TypeScript
function removeStickyCommonEvent(event: string, callback: AsyncCallback<void>): void
```

移除粘性公共事件。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.COMMONEVENT_STICKY

**系统能力：** SystemCapability.Notification.CommonEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1500004](../errorcode-CommonEventService.md#1500004-无法发送系统公共事件) |
| [1500007](../errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500008](../errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |


## removeStickyCommonEvent

```TypeScript
function removeStickyCommonEvent(event: string): Promise<void>
```

移除已发布的粘性公共事件。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.COMMONEVENT_STICKY

**系统能力：** SystemCapability.Notification.CommonEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |

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
| [1500004](../errorcode-CommonEventService.md#1500004-无法发送系统公共事件) |
| [1500007](../errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500008](../errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |
