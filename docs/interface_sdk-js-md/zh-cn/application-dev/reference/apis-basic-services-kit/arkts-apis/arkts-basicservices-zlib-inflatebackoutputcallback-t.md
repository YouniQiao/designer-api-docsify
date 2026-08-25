# InflateBackOutputCallback

```TypeScript
type InflateBackOutputCallback = (outDesc: object, buf: ArrayBuffer, length: int) => int
```

用户提供的输出数据会被写入回调函数中。每当解压后的数据准备好进行输出时，zlib 就会调用此函数将缓冲区中的数据写入目标位置。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| outDesc | object | 是 |
| buf | ArrayBuffer | 是 |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |
