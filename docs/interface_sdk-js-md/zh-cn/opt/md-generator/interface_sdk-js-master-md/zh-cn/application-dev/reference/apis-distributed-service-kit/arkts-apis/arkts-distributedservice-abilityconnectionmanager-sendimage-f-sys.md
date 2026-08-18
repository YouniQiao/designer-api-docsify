# sendImage（系统接口）

## 导入模块

```TypeScript
```

## sendImage

```TypeScript
function sendImage(sessionId: number, image: image.PixelMap, quality?: number): Promise<void>
```

Send image data.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-abilityConnectionManager-function sendImage(sessionId: int, image: image.PixelMap, quality?: int): Promise<void>--><!--Device-abilityConnectionManager-function sendImage(sessionId: int, image: image.PixelMap, quality?: int): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | number | 是 |
| [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) | image.PixelMap | 是 |
| quality | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';

try {
  let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
  photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
  photoSelectOptions.maxSelectNumber = 5;
  let photoPicker = new photoAccessHelper.PhotoViewPicker();
  // 打开图片选择器，让用户选择图片
  photoPicker.select(photoSelectOptions).then((photoSelectResult) => {
    if (!photoSelectResult) {
      hilog.error(0x0000, 'testTag', 'photoSelectResult = null');
      return;
    }

    // 以只读方式打开图片文件
    let file = fileIo.openSync(photoSelectResult.photoUris[0], fileIo.OpenMode.READ_ONLY);
    hilog.info(0x0000, 'testTag', 'file.fd:' + file.fd);

    // 示例中sessionId为模拟值，实际需通过abilityConnectionManager.connectAbility等接口创建协同会话后获取
    let sessionId = 100;
    // 根据文件描述符创建图片源对象
    let imageSourceApi: image.ImageSource = image.createImageSource(file.fd);
    if (imageSourceApi) {
      // 将图片源转换为像素映射对象
      imageSourceApi.createPixelMap().then((pixelMap) => {
        // 发送图片到对端设备
        abilityConnectionManager.sendImage(sessionId, pixelMap).then(() => {
          hilog.info(0x0000, 'testTag', 'sendImage success');
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'testTag', `sendImage failed with error. Code: ${err.code}, message: ${err.message}`);
        });
      });
    } else {
      hilog.info(0x0000, 'testTag', 'imageSourceApi is undefined');
    }
  })
} catch (error) {
  const err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `photoPicker failed with error. Code: ${err.code}, message: ${err.message}`);
}
```
