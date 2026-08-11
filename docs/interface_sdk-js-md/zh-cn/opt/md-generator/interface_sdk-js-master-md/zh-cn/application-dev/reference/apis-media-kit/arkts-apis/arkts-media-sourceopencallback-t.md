# SourceOpenCallback

```TypeScript
type SourceOpenCallback = (request: MediaSourceLoadingRequest) => number
```

由应用实现此回调函数，应用需处理传入的资源打开请求，并返回所打开资源对应的唯一句柄。

> **注意：**
> 
> 客户端在处理完请求后应立刻返回。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-type SourceOpenCallback = (request: MediaSourceLoadingRequest) => long--><!--Device-unnamed-type SourceOpenCallback = (request: MediaSourceLoadingRequest) => long-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [MediaSourceLoadingRequest](arkts-media-multimedia-media-mediasourceloadingrequest-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |
