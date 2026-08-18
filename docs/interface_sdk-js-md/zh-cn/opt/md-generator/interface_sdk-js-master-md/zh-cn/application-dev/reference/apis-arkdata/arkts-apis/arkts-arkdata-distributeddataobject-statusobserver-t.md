# StatusObserver

```TypeScript
type StatusObserver = (sessionId: string, networkId: string, status: string) => void
```

定义获取分布式对象状态变更的监听回调函数。

**起始版本：** 23

<!--Device-distributedDataObject-type StatusObserver = (sessionId: string, networkId: string, status: string) => void--><!--Device-distributedDataObject-type StatusObserver = (sessionId: string, networkId: string, status: string) => void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| networkId | string | 是 |
| status | string | 是 |
