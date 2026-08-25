# createMediaSourceWithDirectory

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createMediaSourceWithDirectory

```TypeScript
function createMediaSourceWithDirectory(path: string): Promise< MediaSource | undefined>
```

根据指定目录路径创建一个媒体源对象。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MediaSource](arkts-media-media-mediasource-i.md) \| undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5411007](../errorcode-media.md#5411007-无可用资源) |
