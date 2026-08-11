# removeStickyCommonEvent（系统接口）

## removeStickyCommonEvent

```TypeScript
function removeStickyCommonEvent(event: string, callback: AsyncCallback<void>): void
```

移除粘性公共事件。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.COMMONEVENT_STICKY

<!--Device-commonEventManager-function removeStickyCommonEvent(event: string, callback: AsyncCallback<void>): void--><!--Device-commonEventManager-function removeStickyCommonEvent(event: string, callback: AsyncCallback<void>): void-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500004](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500004-无法发送系统公共事件) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

commonEventManager.removeStickyCommonEvent('sticky_event', (err: BusinessError) => {
  if (err) {
    console.error(`removeStickyCommonEvent failed, errCode: ${err.code}, errMsg: ${err.message}`);
    return;
  }
  console.info(`removeStickyCommonEvent success`);
});
```


## removeStickyCommonEvent

```TypeScript
function removeStickyCommonEvent(event: string): Promise<void>
```

移除已发布的粘性公共事件。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.COMMONEVENT_STICKY

<!--Device-commonEventManager-function removeStickyCommonEvent(event: string): Promise<void>--><!--Device-commonEventManager-function removeStickyCommonEvent(event: string): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500004](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500004-无法发送系统公共事件) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

commonEventManager.removeStickyCommonEvent('sticky_event').then(() => {
  console.info(`removeStickyCommonEvent success`);
}).catch((err: BusinessError) => {
  console.error(`removeStickyCommonEvent failed, errCode: ${err.code}, errMsg: ${err.message}`);
});
```
