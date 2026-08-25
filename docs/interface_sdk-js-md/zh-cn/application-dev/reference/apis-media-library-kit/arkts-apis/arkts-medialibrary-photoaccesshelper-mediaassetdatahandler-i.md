# MediaAssetDataHandler

媒体资源处理器，应用在onDataPrepared方法中可自定义媒体资源处理逻辑。

> **说明：**&gt;
> - 本Interface首批接口从API version 11开始支持。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## onDataPrepared

```TypeScript
onDataPrepared(data: T, map?: Map<string, string>): void
```

媒体资源就绪通知，系统在资源准备就绪时回调此方法。若资源准备出错，回调的data为undefined。资源请求与回调一一对应。T支持ArrayBuffer，[ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md)， [MovingPhoto](arkts-medialibrary-photoaccesshelper-movingphoto-i.md)和boolean四种数据类型。其中，ArrayBuffer表示图片/视频资源数据， [ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md)表示图片源， [MovingPhoto](arkts-medialibrary-photoaccesshelper-movingphoto-i.md)表示动态照片对象，boolean表示图片/视频资源是否成功写入应用沙箱，true表示成功，false表示失败。map支持返回的信息：  
| map键名 | 值说明 | |----------|-------| | 'quality' |

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | T | 是 |
| map | Map & lt;string, string & gt; | 否 |
