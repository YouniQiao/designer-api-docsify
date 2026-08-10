# MovingPhotoViewAttribute

Defines the moving photo view attribute functions.

**继承/实现关系：** MovingPhotoViewAttribute extends [CommonMethod<MovingPhotoViewAttribute>](CommonMethod<MovingPhotoViewAttribute>)

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-unnamed-declare class MovingPhotoViewAttribute extends CommonMethod<MovingPhotoViewAttribute>--><!--Device-unnamed-declare class MovingPhotoViewAttribute extends CommonMethod<MovingPhotoViewAttribute>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { PixelMapFormat, MovingPhotoViewAttribute, MovingPhotoView, MovingPhotoViewController, DynamicRangeMode } from 'kits/@kit.MediaLibraryKit';
```

## setPlaybackStrategy

```TypeScript
setPlaybackStrategy(strategy: media.PlaybackStrategy): MovingPhotoViewAttribute
```

Sets playback strategy.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhotoViewAttribute-setPlaybackStrategy(strategy: media.PlaybackStrategy): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-setPlaybackStrategy(strategy: media.PlaybackStrategy): MovingPhotoViewAttribute-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | media.PlaybackStrategy | 是 | playback strategy |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-medialibrary-multimedia-movingphotoview-movingphotoviewattribute-i-sys.md) |  |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Non-system applications are not allowed to use system APIs. |

## 示例

系统应用可以同时设置动态照片解码格式、HDR效果格式和边播边处理策略。

```TypeScript
// 该示例只展示参数用法，具体可以执行用例参考动态照片公开接口文档。
// API version 21及之前版本导入方式：import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
// API version 22及之后版本导入方式如下：
import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController, PixelMapFormat, DynamicRangeMode } from '@kit.MediaLibraryKit';
import { media } from '@kit.MediaKit';

let data: photoAccessHelper.MovingPhoto
async function loading(context: Context) {
  try {
    // 需要确保imageFileUri和videoFileUri对应的资源在应用沙箱存在。
    let imageFileUri = 'file://{bundleName}/data/storage/el2/base/haps/entry/files/xxx.jpg';
    let videoFileUri = 'file://{bundleName}/data/storage/el2/base/haps/entry/files/xxx.mp4';
    data = await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
    console.info('load moving photo successfully');
  } catch (err) {
    console.error(`load moving photo failed with error: ${err.code}, ${err.message}`);
  }
}
@Entry
@Component
struct Index {
  controller: MovingPhotoViewController = new MovingPhotoViewController();
  format: undefined | PixelMapFormat = PixelMapFormat.YCBCR_P010;
  mode: undefined | DynamicRangeMode = DynamicRangeMode.HIGH;
  playbackstrategy: media.PlaybackStrategy = {enableCameraPostprocessing: true};
  private uiContext: UIContext = this.getUIContext()
  aboutToAppear(): void {
    loading(this.uiContext.getHostContext()!)
  }

  build() {
    NavDestination() {
      Column() {
        Stack({ alignContent: Alignment.BottomStart }) {
          MovingPhotoView({
            movingPhoto: data,
            controller: this.controller,
            movingPhotoFormat: this.format,
            dynamicRangeMode: this.mode,
            playWithMask: false
          })
          .setPlaybackStrategy(this.playbackstrategy)
        }
      }
    }
  }
}
```

