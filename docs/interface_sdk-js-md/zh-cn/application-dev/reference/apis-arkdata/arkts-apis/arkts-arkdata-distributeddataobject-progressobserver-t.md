# ProgressObserver

```TypeScript
type ProgressObserver = (sessionId: string, progress: int) => void
```

定义传输进度的监听回调函数。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| progress | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
