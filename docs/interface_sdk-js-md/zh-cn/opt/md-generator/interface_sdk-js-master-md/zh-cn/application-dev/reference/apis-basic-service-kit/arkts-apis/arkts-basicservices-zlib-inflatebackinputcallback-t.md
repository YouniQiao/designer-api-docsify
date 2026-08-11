# InflateBackInputCallback

```TypeScript
type InflateBackInputCallback = (inDesc: object) => ArrayBuffer
```

一个用于读取用户提供的输入数据的回调函数。当解压缩过程需要更多输入数据时，zlib 将调用此函数。此函数应从数据源读取数据并将其写入缓冲区中。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-zlib-type InflateBackInputCallback = (inDesc: object) => ArrayBuffer--><!--Device-zlib-type InflateBackInputCallback = (inDesc: object) => ArrayBuffer-End-->

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inDesc | object | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |
