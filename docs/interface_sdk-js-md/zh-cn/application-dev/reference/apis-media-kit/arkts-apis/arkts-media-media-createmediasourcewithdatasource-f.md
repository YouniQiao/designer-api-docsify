# createMediaSourceWithDataSource

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createMediaSourceWithDataSource

```TypeScript
function createMediaSourceWithDataSource(dataSrc: AVDataSrcDescriptor): MediaSource | undefined
```

通过自定义数据源创建媒体源。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataSrc | [AVDataSrcDescriptor](arkts-media-media-avdatasrcdescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [MediaSource](arkts-media-media-mediasource-i.md) \| undefined |
