# publish

## 导入模块

```TypeScript
```

## publish

```TypeScript
function publish(event: string, callback: AsyncCallback<void>): void
```

以回调形式发布公共事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [publish](arkts-basicservices-commoneventmanager-publish-f.md)(event: string, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## publish

```TypeScript
function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void
```

以回调形式发布公共事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [publish](arkts-basicservices-commoneventmanager-publish-f.md)(event: string, options: CommonEventPublishData, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
