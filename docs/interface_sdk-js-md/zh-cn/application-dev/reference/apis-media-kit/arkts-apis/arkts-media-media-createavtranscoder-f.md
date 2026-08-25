# createAVTranscoder

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAVTranscoder

```TypeScript
function createAVTranscoder(): Promise<AVTranscoder>
```

创建视频转码实例。使用Promise异步回调。

> **说明：**&gt;
> 可创建的视频转码实例不能超过2个。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AVTranscoder](arkts-media-media-avtranscoder-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
