# TextContextInfo

Represents the text information about the recommended images.

**Since:** 26.0.0

<!--Device-photoAccessHelper-interface TextContextInfo--><!--Device-photoAccessHelper-interface TextContextInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## text

```TypeScript
text?: string
```

Text based on which images are recommended. The text cannot exceed 250 characters. The default value is an empty string.

**Type:** string

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextContextInfo-text?: string--><!--Device-TextContextInfo-text?: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let textInfo: photoAccessHelper.TextContextInfo = {
      text: 'Pandas at Shanghai Wild Zoo'
    }
    let recommendOptions: photoAccessHelper.RecommendationOptions = {
      textContextInfo: textInfo
    }
    let options: photoAccessHelper.PhotoSelectOptions = {
      MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
      maxSelectNumber: 1,
      recommendationOptions: recommendOptions
    }
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(options).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
    }).catch((err: BusinessError) => {
      console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```

