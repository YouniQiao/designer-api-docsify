# InflateBackInputCallback

```TypeScript
type InflateBackInputCallback = (inDesc: RecordData) => ArrayBuffer
```

一个用于读取用户提供的输入数据的回调函数。当解压缩过程需要更多输入数据时，zlib 将调用此函数。此函数应从数据源读取数据并将其写入缓冲区中。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-zlib-type InflateBackInputCallback = (inDesc: RecordData) => ArrayBuffer--><!--Device-zlib-type InflateBackInputCallback = (inDesc: RecordData) => ArrayBuffer-End-->

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inDesc | [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |
