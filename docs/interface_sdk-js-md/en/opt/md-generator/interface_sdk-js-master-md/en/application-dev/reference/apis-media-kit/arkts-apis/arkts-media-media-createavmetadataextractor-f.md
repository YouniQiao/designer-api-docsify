# createAVMetadataExtractor

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## createAVMetadataExtractor

```TypeScript
function createAVMetadataExtractor(): Promise<AVMetadataExtractor>
```

Creates an AVMetadataExtractor instance. This API uses a promise to return the result.

**Since:** 11

<!--Device-media-function createAVMetadataExtractor(): Promise<AVMetadataExtractor>--><!--Device-media-function createAVMetadataExtractor(): Promise<AVMetadataExtractor>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVMetadataExtractor](arkts-media-media-avmetadataextractor-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avMetadataExtractor: media.AVMetadataExtractor;
media.createAVMetadataExtractor().then((extractor: media.AVMetadataExtractor) => {
  if (extractor) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
  } else {
    console.error(`Failed to create AVMetadataExtractor`);
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
});
```


## createAVMetadataExtractor

```TypeScript
function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void
```

Creates an AVMetadataExtractor instance. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-media-function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void--><!--Device-media-function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVMetadataExtractor](arkts-media-media-avmetadataextractor-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avMetadataExtractor: media.AVMetadataExtractor;
media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
  if (extractor) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
  } else {
    console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
  }
});
```
