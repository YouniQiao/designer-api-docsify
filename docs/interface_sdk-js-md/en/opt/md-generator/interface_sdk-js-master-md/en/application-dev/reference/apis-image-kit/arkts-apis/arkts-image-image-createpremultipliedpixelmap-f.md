# createPremultipliedPixelMap

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## createPremultipliedPixelMap

```TypeScript
function createPremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void
```

Transforms pixelmap from unpremultiplied alpha format to premultiplied alpha format.

**Since:** 12

<!--Device-image-function createPremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void--><!--Device-image-function createPremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [62980103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980103-unsupported-image-type) |
| [62980246](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980246-failure-in-reading-the-pixelmap) |
| [62980248](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980248-no-modification-to-the-pixelmap) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPremultipliedPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(16); // 16 indicates the size of the pixel buffer to create. The value is calculated as follows: width × height × 4.
  let bufferArr = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i += 4) {
    bufferArr[i] = 255;
    bufferArr[i + 1] = 255;
    bufferArr[i + 2] = 122;
    bufferArr[i + 3] = 122;
  }
  let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 }, alphaType: image.AlphaType.UNPREMUL};
  let srcPixelMap = image.createPixelMapSync(color, optsForUnpre);
  let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 }, alphaType: image.AlphaType.PREMUL};
  let dstPixelMap = image.createPixelMapSync(optsForPre);
  image.createPremultipliedPixelMap(srcPixelMap, dstPixelMap, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to convert the PixelMap. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in converting the PixelMap.');
  });
}
```


## createPremultipliedPixelMap

```TypeScript
function createPremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>
```

Transforms pixelmap from premultiplied alpha format to unpremultiplied alpha format.

**Since:** 12

<!--Device-image-function createPremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>--><!--Device-image-function createPremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [62980103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980103-unsupported-image-type) |
| [62980246](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980246-failure-in-reading-the-pixelmap) |
| [62980248](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-image-kit/errorcode-image.md#62980248-no-modification-to-the-pixelmap) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPremultipliedPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(16); // 16 indicates the size of the pixel buffer to create. The value is calculated as follows: width × height × 4.
  let bufferArr = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i += 4) {
    bufferArr[i] = 255;
    bufferArr[i + 1] = 255;
    bufferArr[i + 2] = 122;
    bufferArr[i + 3] = 122;
  }
  let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 }, alphaType: image.AlphaType.UNPREMUL};
  let srcPixelMap = image.createPixelMapSync(color, optsForUnpre);
  let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 }, alphaType: image.AlphaType.PREMUL};
  let dstPixelMap = image.createPixelMapSync(optsForPre);
  image.createPremultipliedPixelMap(srcPixelMap, dstPixelMap).then(() => {
    console.info('Succeeded in converting the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to convert the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```
