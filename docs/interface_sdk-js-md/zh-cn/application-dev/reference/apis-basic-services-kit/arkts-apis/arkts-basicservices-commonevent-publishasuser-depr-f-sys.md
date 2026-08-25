# publishAsUser（系统接口）

## 导入模块

```TypeScript
```

## publishAsUser

```TypeScript
function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void
```

以回调的形式向指定用户发布公共事件。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [publishAsUser](arkts-basicservices-commoneventmanager-publishasuser-f-sys.md)(event: string, userId: int, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Notification.CommonEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| userId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## publishAsUser

```TypeScript
function publishAsUser(
    event: string,
    userId: number,
    options: CommonEventPublishData,
    callback: AsyncCallback<void>
  ): void
```

以回调形式向指定用户发布公共事件并指定发布信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [publishAsUser](arkts-basicservices-commoneventmanager-publishasuser-f-sys.md)( event: string, userId: int, options: CommonEventPublishData, callback: AsyncCallback&lt;void&gt; )

**系统能力：** SystemCapability.Notification.CommonEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| userId | number | 是 |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
