# getDoNotDisturbDate（系统接口）

## 导入模块

```TypeScript
```

## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(callback: AsyncCallback<DoNotDisturbDate>): void
```

查询免打扰时间（Callback形式）。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(callback: AsyncCallback<DoNotDisturbDate>): void--><!--Device-notification-function getDoNotDisturbDate(callback: AsyncCallback<DoNotDisturbDate>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DoNotDisturbDate&gt; | 是 |


## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(): Promise<DoNotDisturbDate>
```

查询免打扰时间（Promise形式）。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(): Promise<DoNotDisturbDate>--><!--Device-notification-function getDoNotDisturbDate(): Promise<DoNotDisturbDate>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;DoNotDisturbDate & gt; |


## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(userId: number, callback: AsyncCallback<DoNotDisturbDate>): void
```

查询指定用户的免打扰时间（Callback形式）。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(userId: number, callback: AsyncCallback<DoNotDisturbDate>): void--><!--Device-notification-function getDoNotDisturbDate(userId: number, callback: AsyncCallback<DoNotDisturbDate>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DoNotDisturbDate&gt; | 是 |


## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(userId: number): Promise<DoNotDisturbDate>
```

查询指定用户的免打扰时间（Promise形式）。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(userId: number): Promise<DoNotDisturbDate>--><!--Device-notification-function getDoNotDisturbDate(userId: number): Promise<DoNotDisturbDate>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;DoNotDisturbDate & gt; |
