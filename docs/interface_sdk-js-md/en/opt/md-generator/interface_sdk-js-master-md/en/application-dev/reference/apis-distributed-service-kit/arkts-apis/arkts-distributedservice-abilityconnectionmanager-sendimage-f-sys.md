# sendImage (System API)

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## sendImage

```TypeScript
function sendImage(sessionId: number, image: image.PixelMap, quality?: number): Promise<void>
```

Send image data.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function sendImage(sessionId: int, image: image.PixelMap, quality?: int): Promise<void>--><!--Device-abilityConnectionManager-function sendImage(sessionId: int, image: image.PixelMap, quality?: int): Promise<void>-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |
| [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) | image.PixelMap | Yes |
| quality | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';

try {
  let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
  photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
  photoSelectOptions.maxSelectNumber = 5;
  let photoPicker = new photoAccessHelper.PhotoViewPicker();
  photoPicker.select(photoSelectOptions).then((photoSelectResult) => {
    if (!photoSelectResult) {
      hilog.error(0x0000, 'testTag', 'photoSelectResult = null');
    return;
    }

    let file = fileIo.openSync(photoSelectResult.photoUris[0], fileIo.OpenMode.READ_ONLY);
    hilog.info(0x0000, 'testTag', 'file.fd:' + file.fd);

    let sessionId = 100;
    let imageSourceApi: image.ImageSource = image.createImageSource(file.fd);
    if (imageSourceApi) {
      imageSourceApi.createPixelMap().then((pixelMap) => {
        abilityConnectionManager.sendImage(sessionId, pixelMap)
      });
    } else {
      hilog.info(0x0000, 'testTag', 'imageSourceApi is undefined');
    }
  })
} catch (error) {
  hilog.error(0x0000, 'testTag', 'photoPicker failed with error: ' + JSON.stringify(error));
}
```
