# AVImageGenerator

AVImageGenerator is a class for video thumbnail retrieval. It provides APIs to obtain a thumbnail from a video. Before calling any API in AVImageGenerator, you must use [createAVImageGenerator()](arkts-media-media-createavimagegenerator-f.md) to create an AVImageGenerator instance.For details about the demo for obtaining video thumbnails, see [Obtaining Video Thumbnails](../../../media/media/avimagegenerator.md).

**Since:** 23

<!--Device-media-interface AVImageGenerator--><!--Device-media-interface AVImageGenerator-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,
      callback: AsyncCallback<image.PixelMap>): void
```

Obtains a video thumbnail. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,      callback: AsyncCallback<image.PixelMap>): void--><!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,      callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | number | Yes | Time of the video for which a thumbnail is to be obtained, in μs. |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes | Relationship between the thumbnail timestamp in and the video frame. |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | Yes | Format parameters of the thumbnail to be obtained. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the PixelMap instance obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by callback. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by callback. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;
let pixel_map: image.PixelMap | undefined = undefined;

// Initialize input parameters.
let timeUs: number = 0;

let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;

let param: media.PixelMapParams = {
  width: 300,
  height: 300,
};

// Obtain the thumbnail.
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.fetchFrameByTime(timeUs, queryOption, param, (error: BusinessError, pixelMap) => {
      if (error) {
        console.error(`Failed to fetch FrameByTime, err = ${JSON.stringify(error)}`);
        return;
      }
      pixel_map = pixelMap;
    });
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;
let pixel_map: image.PixelMap | undefined = undefined;

// Initialize input parameters.
let timeUs: number = 0;

let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;

let param: media.PixelMapParams = {
  width: 300,
  height: 300,
};

// Obtain the thumbnail.
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.fetchFrameByTime(timeUs, queryOption, param).then((pixelMap: image.PixelMap) => {
      pixel_map = pixelMap;
    }).catch((error: BusinessError) => {
      console.error(`Failed to fetch FrameByTime, error message:${error.message}`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

let avMetadataExtractor: media.AVMetadataExtractor | undefined = undefined;
let pixelMap: image.PixelMap | undefined = undefined;

// Initialize input parameters.
let timeUs: number = 0;
let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_PREVIOUS_SYNC;
let param: media.PixelMapParams = {
  width: 300,
  height: 300
};
// Obtain the thumbnail.
media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
  if (extractor != null) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
    avMetadataExtractor.fetchFrameByTime(timeUs, queryOption, param).then((pixelMap: image.PixelMap) => {
      pixelMap = pixelMap;
    }).catch((error: BusinessError) => {
      console.error(`Failed to fetch FrameByTime, error message:${error.message}`);
    });
  } else {
    console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
  }
});
```

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams,
      callback: AsyncCallback<image.PixelMap | undefined>): void
```

Obtains a video thumbnail. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AVImageGenerator-fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams,      callback: AsyncCallback<image.PixelMap | undefined>): void--><!--Device-AVImageGenerator-fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams,      callback: AsyncCallback<image.PixelMap | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | long | Yes | Time of the video for which a thumbnail is to be obtained, in μs. |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes | Relationship between the time passed in and the video frame. |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | Yes | Format parameters of the thumbnail to be obtained. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap \| undefined&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **PixelMap** instance obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by callback. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by callback. |

**Examples**

See [fetchFrameByTime](#fetchframebytime)

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>
```

Obtains a video thumbnail. This API uses a promise to return the result.

**Since:** 12

<!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>--><!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | number | Yes | Time of the video for which a thumbnail is to be obtained, in μs. |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes | Relationship between the thumbnail timestamp in and the video frame. |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | Yes | Format parameters of the thumbnail to be obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | Promise used to return the video thumbnail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by promise. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by promise. |

**Examples**

See [fetchFrameByTime](#fetchframebytime)

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap | undefined>
```

Obtains a video thumbnail. This API uses a promise to return the result.

**Since:** 23

<!--Device-AVImageGenerator-fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap | undefined>--><!--Device-AVImageGenerator-fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | long | Yes | Time of the video for which a thumbnail is to be obtained, in μs. |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes | Relationship between the time passed in and the video frame. |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | Yes | Format parameters of the thumbnail to be obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap \| undefined&gt; | Promise used to return the video thumbnail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by promise. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by promise. |

**Examples**

See [fetchFrameByTime](#fetchframebytime)

## fetchScaledFrameByTime

```TypeScript
fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize):
      Promise<image.PixelMap>
```

Fetches a scaled thumbnail from the video at a particular timestamp. This API uses a promise to return the result.

**Since:** 20

<!--Device-AVImageGenerator-fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize):      Promise<image.PixelMap>--><!--Device-AVImageGenerator-fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize):      Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | number | Yes | Timestamp, in microseconds (μs), at which the thumbnail is to be fetched from the video. |
| queryMode | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes | Relationship between the thumbnail timestamp in and the video frame. |
| outputSize | [OutputSize](arkts-media-media-outputsize-i.md) | No | Output size of the thumbnail. By default, the original image size is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | Promise used to return the video thumbnail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |  |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |  |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;
let pixel_map: image.PixelMap | undefined = undefined;
// Initialize input parameters.
let timeUs: number = 0;
let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;
let outputSize: media.OutputSize = {
  width: 300,
  height: 300,
};
// Obtain the thumbnail.
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.fetchScaledFrameByTime(timeUs, queryOption, outputSize).then((pixelMap: image.PixelMap) => {
      pixel_map = pixelMap;
    }).catch((error: BusinessError) => {
      console.error(`Failed to fetch ScaledFrameByTime, error message:${error.message}`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
  }
});
```

## fetchScaledFrameByTime

```TypeScript
fetchScaledFrameByTime(timeUs: long, queryMode: AVImageQueryOptions, outputSize?: OutputSize):
      Promise<image.PixelMap | undefined>
```

Supports extracting video thumbnails by proportional scaling

**Since:** 23

<!--Device-AVImageGenerator-fetchScaledFrameByTime(timeUs: long, queryMode: AVImageQueryOptions, outputSize?: OutputSize):      Promise<image.PixelMap | undefined>--><!--Device-AVImageGenerator-fetchScaledFrameByTime(timeUs: long, queryMode: AVImageQueryOptions, outputSize?: OutputSize):      Promise<image.PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | long | Yes | The time expected to fetch picture from the video resource. The unit is microsecond(us). |
| queryMode | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes | Specify how to position the video frame |
| outputSize | [OutputSize](arkts-media-media-outputsize-i.md) | No | This field is used to define the output size of frame. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap \| undefined&gt; | Returns the output image object |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |  |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |  |

**Examples**

See [fetchScaledFrameByTime](#fetchscaledframebytime)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this AVImageGenerator instance. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AVImageGenerator-release(callback: AsyncCallback<void>): void--><!--Device-AVImageGenerator-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by callback. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.release((err: BusinessError) => {
  if (err == null) {
    console.info('release videorecorder success');
  } else {
    console.error('release videorecorder failed and error is ' + err.message);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.release().then(() => {
  console.info('release videorecorder success');
}).catch((err: BusinessError) => {
  console.error('release videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioPlayer.release();
audioPlayer = undefined;
```

```TypeScript
audioRecorder.on('release', () => {    // Set the 'release' event callback.
  console.info('audio recorder release called');
});
audioRecorder.release();
audioRecorder = undefined;
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;

// Release the resources.
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.release((error: BusinessError) => {
      if (error) {
        console.error(`Failed to release, err = ${JSON.stringify(error)}`);
        return;
      }
      console.info(`Succeeded in releasing`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;

// Release the resources.
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.release().then(() => {
      console.info(`Succeeded in releasing.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to release, error message:${error.message}`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release((error: BusinessError) => {
    if (error) {
      console.error(`Failed to release, err = ${JSON.stringify(error)}`);
      return;
    }
    console.info(`Succeeded in releasing.`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release().then(() => {
    console.info(`Succeeded in releasing.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to release, error message:${error.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach a state other than released before proceeding.
  avPlayer.release((err: BusinessError) => {
    if (err) {
      console.error('Failed to release,error message is :' + err.message);
    } else {
      console.info('Succeeded in releasing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach a state other than released before proceeding.
  avPlayer.release().then(() => {
    console.info('Succeeded in releasing');
  }, (err: BusinessError) => {
    console.error('Failed to release,error message is :' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release((err: BusinessError) => {
  if (err) {
    console.error(`Failed to release AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in releasing AVRecorder');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release().then(() => {
  console.info('Succeeded in releasing AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to release AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
});

// Other processes.

// Call the release method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.release().then(() => {
    console.info('Succeeded in releasing avScreenCaptureRecorder');
  }).catch((err: BusinessError) => {
    console.error(`Failed to release avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVTranscoder instance.
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.release().then(() => {
    console.info('release AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('release AVTranscoder failed and catch error is ' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release((err: BusinessError) => {
  if (err) {
    console.error('Failed to release!');
  } else {
    console.info('Succeeded in releasing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release().then(() => {
  console.info('Succeeded in releasing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## release

```TypeScript
release(): Promise<void>
```

Releases this AVImageGenerator instance. This API uses a promise to return the result.

**Since:** 23

<!--Device-AVImageGenerator-release(): Promise<void>--><!--Device-AVImageGenerator-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by promise. |

**Examples**

See [release](#release)

## fdSrc

```TypeScript
fdSrc ?: AVFileDescriptor
```

Media file descriptor, which specifies the data source.There is a media file that stores continuous assets, the address offset is 0, and the byte length is 100. Its file descriptor is **AVFileDescriptor { fd = resourceHandle; offset = 0; length = 100; }**.  
**NOTE：**After the resource handle (FD) is transferred to an AVImageGenerator instance, do not use the resource handle to perform other read and write operations, including but not limited to transferring this handle to other AVPlayer, AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. Competition occurs when multiple AVImageGenerator use the same resource handle to read and write files at the same time, resulting in errors in obtaining data.

**Type:** [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md)

**Since:** 23

<!--Device-AVImageGenerator-fdSrc ?: AVFileDescriptor--><!--Device-AVImageGenerator-fdSrc ?: AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

