# MediaAssetDataHandler

媒体资源处理器，应用在onDataPrepared方法中可自定义媒体资源处理逻辑。

> **说明：**&gt;
> - 本Interface首批接口从API version 11开始支持。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## onDataPrepared

```TypeScript
onDataPrepared(data: T, map?: Map<string, string>): void
```

媒体资源就绪通知，系统在资源准备就绪时回调此方法。若资源准备出错，回调的data为undefined。资源请求与回调一一对应。T支持ArrayBuffer，[ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md)， [MovingPhoto](arkts-medialibrary-photoaccesshelper-movingphoto-i.md)和boolean四种数据类型。其中，ArrayBuffer表示图片/视频资源数据， [ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md)表示图片源， [MovingPhoto](arkts-medialibrary-photoaccesshelper-movingphoto-i.md)表示动态照片对象，boolean表示图片/视频资源是否成功写入应用沙箱，true表示成功，false表示失败。map支持返回的信息：  
| map键名 | 值说明 | |----------|-------| | 'quality' |

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | T | 是 |
| map | Map & lt;string, string & gt; | 否 |

**示例**

```TypeScript
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.MediaAssetDataHandler<image.ImageSource> {
  onDataPrepared = (data: image.ImageSource, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 自定义对ImageSource的处理逻辑。
    console.info('on image data prepared, photo quality is ' + map['quality']);
  }
}

class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
  onDataPrepared = (data: ArrayBuffer, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 自定义对ArrayBuffer的处理逻辑。
    console.info('on image data prepared, photo quality is ' + map['quality']);
  }
}

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  onDataPrepared = (data: photoAccessHelper.MovingPhoto, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 自定义对MovingPhoto的处理逻辑。
    console.info('on image data prepared, photo quality is ' + map['quality']);
  }
}
```

```TypeScript
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.QuickImageDataHandler<image.Picture> {
  onDataPrepared(data: image.Picture, imageSource: image.ImageSource, map: Map<string, string>) {
    console.info('on image data prepared');
  }
}
```

## onDataPrepared

```TypeScript
onDataPrepared(data: T | undefined, map?: Map<string, string>): void
```

所需的媒体资产数据已准备就绪。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | T \| undefined | 是 |
| map | Map & lt;string, string & gt; | 否 |

**示例**

参见 [onDataPrepared](#ondataprepared)
