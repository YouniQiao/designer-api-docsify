# createAVDownloaderManager

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## createAVDownloaderManager

```TypeScript
function createAVDownloaderManager(): Promise<AVDownloaderManager>
```

创建一个离线下载任务管理器实例。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-function createAVDownloaderManager(): Promise<AVDownloaderManager>--><!--Device-unnamed-function createAVDownloaderManager(): Promise<AVDownloaderManager>-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AVDownloaderManager](arkts-media-multimediamedia-avdownloadermanager-i.md)&gt; | Promise对象。返回离线下载任务管理器实例。 |

