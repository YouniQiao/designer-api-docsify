# DataProgressListener

```TypeScript
type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void
```

定义获取进度信息和数据的监听回调函数。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| progressInfo | [ProgressInfo](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-progressinfo-i.md) | 是 |
| data | UnifiedData \| null | 是 |
