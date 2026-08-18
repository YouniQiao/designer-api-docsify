# createAVImageGenerator

## Modules to Import

```TypeScript
```

## createAVImageGenerator

```TypeScript
function createAVImageGenerator(): Promise<AVImageGenerator>
```

Creates an AVImageGenerator instance. This API uses a promise to return the result.

**Since:** 12

<!--Device-media-function createAVImageGenerator(): Promise<AVImageGenerator>--><!--Device-media-function createAVImageGenerator(): Promise<AVImageGenerator>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVImageGenerator](arkts-media-media-avimagegenerator-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avImageGenerator: media.AVImageGenerator;
media.createAVImageGenerator().then((generator: media.AVImageGenerator) => {
  if (generator) {
    avImageGenerator = generator;
    console.info('Succeeded in creating AVImageGenerator');
  } else {
    console.error('Failed to create AVImageGenerator');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVImageGenerator, error message:${error.message}`);
});
```


## createAVImageGenerator

```TypeScript
function createAVImageGenerator(): Promise<AVImageGenerator | undefined>
```

Creates an **AVImageGenerator** instance. This API uses a promise to return the result.

**Since:** 23

<!--Device-media-function createAVImageGenerator(): Promise<AVImageGenerator | undefined>--><!--Device-media-function createAVImageGenerator(): Promise<AVImageGenerator | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVImageGenerator](arkts-media-media-avimagegenerator-i.md) \| undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |


## createAVImageGenerator

```TypeScript
function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>): void
```

Creates an AVImageGenerator instance. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-media-function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>): void--><!--Device-media-function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVImageGenerator](arkts-media-media-avimagegenerator-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avImageGenerator: media.AVImageGenerator;
media.createAVImageGenerator((error: BusinessError, generator: media.AVImageGenerator) => {
  if (generator) {
    avImageGenerator = generator;
    console.info('Succeeded in creating AVImageGenerator');
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${error.message}`);
  }
});
```


## createAVImageGenerator

```TypeScript
function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator | undefined>): void
```

Creates an **AVImageGenerator** instance. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-media-function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator | undefined>): void--><!--Device-media-function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVImageGenerator](arkts-media-media-avimagegenerator-i.md) \| undefined & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
