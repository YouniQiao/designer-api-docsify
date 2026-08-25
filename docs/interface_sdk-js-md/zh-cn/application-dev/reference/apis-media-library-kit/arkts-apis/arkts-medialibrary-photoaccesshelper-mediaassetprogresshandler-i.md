# MediaAssetProgressHandler

媒体资产进度处理器，应用于onProgress方法中获取媒体资产进度。

> **说明：**&gt;
> - 本Interface首批接口从API version 15开始支持。

**起始版本：** 15

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## onProgress

```TypeScript
onProgress(progress: number): void
```

当所请求的视频资源返回进度时系统会回调此方法。

**起始版本：** 15

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| progress | number | 是 |
