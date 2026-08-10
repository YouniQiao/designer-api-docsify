# cancelAll

## cancelAll

```TypeScript
function cancelAll(callback: AsyncCallback<void>): void
```

取消所有已发布的通知（callback形式）。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#cancelAll

<!--Device-notification-function cancelAll(callback: AsyncCallback<void>): void--><!--Device-notification-function cancelAll(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 表示被指定的回调方法。 |


## cancelAll

```TypeScript
function cancelAll(): Promise<void>
```

取消所有已发布的通知（Promise形式）。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#cancelAll

<!--Device-notification-function cancelAll(): Promise<void>--><!--Device-notification-function cancelAll(): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

