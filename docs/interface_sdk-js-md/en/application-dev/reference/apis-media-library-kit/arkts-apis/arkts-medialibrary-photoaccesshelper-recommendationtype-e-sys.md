# RecommendationType

Enumerates the types of recommended images.

**Since:** 26.0.0

<!--Device-photoAccessHelper-enum RecommendationType--><!--Device-photoAccessHelper-enum RecommendationType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## COLOR_STYLE_PHOTO

```TypeScript
COLOR_STYLE_PHOTO = 12
```

Recommended style.

**Since:** 26.0.0

<!--Device-RecommendationType-COLOR_STYLE_PHOTO = 12--><!--Device-RecommendationType-COLOR_STYLE_PHOTO = 12-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## CAT

```TypeScript
CAT = 13
```

Cat images will be recommended.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RecommendationType-CAT = 13--><!--Device-RecommendationType-CAT = 13-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## DOG

```TypeScript
DOG = 14
```

Dog images will be recommended.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RecommendationType-DOG = 14--><!--Device-RecommendationType-DOG = 14-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## ARCHITECTURE

```TypeScript
ARCHITECTURE = 15
```

Architecture images will be recommended.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RecommendationType-ARCHITECTURE = 15--><!--Device-RecommendationType-ARCHITECTURE = 15-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## LANDSCAPE

```TypeScript
LANDSCAPE = 16
```

Landscape images will be recommended.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RecommendationType-LANDSCAPE = 16--><!--Device-RecommendationType-LANDSCAPE = 16-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## GAUSSIAN_SPLAT_3D

```TypeScript
GAUSSIAN_SPLAT_3D = 17
```

Images generated using the 3D Gaussian technology will be recommended.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RecommendationType-GAUSSIAN_SPLAT_3D = 17--><!--Device-RecommendationType-GAUSSIAN_SPLAT_3D = 17-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let recommendOptions: photoAccessHelper.RecommendationOptions = {
      recommendationType: photoAccessHelper.RecommendationType.ID_CARD
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

