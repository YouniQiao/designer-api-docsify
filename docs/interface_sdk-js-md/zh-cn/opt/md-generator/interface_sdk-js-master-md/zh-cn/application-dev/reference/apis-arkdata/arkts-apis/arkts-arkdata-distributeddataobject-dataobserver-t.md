# DataObserver

```TypeScript
type DataObserver = (sessionId: string, fields: Array<string>) => void
```

定义获取分布式对象数据变更的监听回调函数。

**起始版本：** 20

<!--Device-distributedDataObject-type DataObserver = (sessionId: string, fields: Array<string>) => void--><!--Device-distributedDataObject-type DataObserver = (sessionId: string, fields: Array<string>) => void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| fields | Array&lt;string&gt; | 是 |
