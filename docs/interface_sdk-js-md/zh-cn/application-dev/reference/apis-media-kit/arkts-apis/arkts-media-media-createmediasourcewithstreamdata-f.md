# createMediaSourceWithStreamData

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createMediaSourceWithStreamData

```TypeScript
function createMediaSourceWithStreamData(streams: Array<MediaStream>): MediaSource
```

创建流媒体多码率媒体来源实例方法，当前仅支持HTTP-FLV协议格式多码率。

**起始版本：** 19

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streams | Array&lt;[MediaStream](arkts-media-media-mediastream-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [MediaSource](arkts-media-media-mediasource-i.md) |
