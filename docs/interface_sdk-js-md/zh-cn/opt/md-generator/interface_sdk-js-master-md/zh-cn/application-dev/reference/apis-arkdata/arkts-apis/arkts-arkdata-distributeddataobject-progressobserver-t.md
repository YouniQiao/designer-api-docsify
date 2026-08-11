# ProgressObserver

```TypeScript
type ProgressObserver = (sessionId: string, progress: number) => void
```

定义传输进度的监听回调函数。

**起始版本：** 20

<!--Device-distributedDataObject-type ProgressObserver = (sessionId: string, progress: int) => void--><!--Device-distributedDataObject-type ProgressObserver = (sessionId: string, progress: int) => void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| progress | number | 是 |
