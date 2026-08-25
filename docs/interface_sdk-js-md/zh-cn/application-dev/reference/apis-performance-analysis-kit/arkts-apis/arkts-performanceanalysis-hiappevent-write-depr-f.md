# write

## 导入模块

```TypeScript
```

## write

```TypeScript
function write(eventName: string, eventType: EventType, keyValues: object): Promise<void>
```

应用事件打点方法，将事件写入到当天的事件文件中，使用Promise方式作为异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [write](arkts-performanceanalysis-hiappevent-write-f.md)

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventName | string | 是 |
| eventType | [EventType](../../apis-arkts/arkts-apis/arkts-arkts-xml-eventtype-e.md) | 是 |
| keyValues | object | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## write

```TypeScript
function write(eventName: string, eventType: EventType, keyValues: object, callback: AsyncCallback<void>): void
```

应用事件打点方法，将事件写入到当天的事件文件中，使用callback方式作为异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [write](arkts-performanceanalysis-hiappevent-write-f.md)

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventName | string | 是 |
| eventType | [EventType](../../apis-arkts/arkts-apis/arkts-arkts-xml-eventtype-e.md) | 是 |
| keyValues | object | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
