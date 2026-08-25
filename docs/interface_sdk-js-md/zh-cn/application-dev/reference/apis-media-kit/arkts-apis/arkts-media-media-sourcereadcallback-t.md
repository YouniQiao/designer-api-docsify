# SourceReadCallback

```TypeScript
type SourceReadCallback = (uuid: number, requestedOffset: number, requestedLength: number) => void
```

由应用实现此回调函数，应用需记录读取请求，并在数据充足时通过对应的MediaSourceLoadingRequest对象的 [respondData](arkts-media-media-mediasourceloadingrequest-i.md#responddata) 方法推送数据。

> **注意：**&gt;
> 客户端在处理完请求后应立刻返回。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | number | 是 |
| requestedOffset | number | 是 |
| requestedLength | number | 是 |
