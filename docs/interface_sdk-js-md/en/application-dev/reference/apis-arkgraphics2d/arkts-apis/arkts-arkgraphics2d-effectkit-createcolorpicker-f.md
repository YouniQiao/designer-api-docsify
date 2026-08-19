# createColorPicker

## Modules to Import

```TypeScript
import { effectKit } from '@kit.ArkGraphics2D';
```

## createColorPicker

```TypeScript
function createColorPicker(source: image.PixelMap): Promise<ColorPicker>
```

Creates a ColorPicker instance based on a pixel map. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-effectKit-function createColorPicker(source: image.PixelMap): Promise<ColorPicker>--><!--Device-effectKit-function createColorPicker(source: image.PixelMap): Promise<ColorPicker>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | image.PixelMap | Yes | PixelMap instance created by the image module. An instance can be obtained by decoding an image or directly created. For details, see Introduction to Image Kit. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md)&gt; | Promise used to return the ColorPicker instance created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Input parameter error. |

**Examples**

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";
import { BusinessError } from "@kit.BasicServicesKit";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}

image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap).then(colorPicker => {
    console.info("color picker=" + colorPicker);
  }).catch( (reason : BusinessError) => {
    console.error("error=" + reason.message);
  })
})
```


## createColorPicker

```TypeScript
function createColorPicker(source: image.PixelMap, region: Array<double>): Promise<ColorPicker>
```

Creates a ColorPicker instance for the selected region based on a pixel map. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-effectKit-function createColorPicker(source: image.PixelMap, region: Array<double>): Promise<ColorPicker>--><!--Device-effectKit-function createColorPicker(source: image.PixelMap, region: Array<double>): Promise<ColorPicker>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | image.PixelMap | Yes | PixelMap instance created by the image module. An instance can be obtained by decoding an image or directly created. For details, see Introduction to Image Kit. |
| region | Array&lt;double&gt; | Yes | Color picking region of the image. The array contains four elements, with a value range of [0, 1]. Values outside this range are automatically truncated during implementation. The four elements represent the left, top, right, and bottom positions of the image region, respectively. The leftmost and topmost edges correspond to position 0, and the rightmost and bottommost edges correspond to position 1. The third element must be greater than the first element, and the fourth element must be greater than the second element. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md)&gt; | Promise used to return the ColorPicker instance created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Input parameter error. |

**Examples**

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";
import { BusinessError } from "@kit.BasicServicesKit";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}

image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, [0, 0, 1, 1]).then(colorPicker => {
    console.info("color picker=" + colorPicker);
  }).catch( (reason : BusinessError) => {
    console.error("error=" + reason.message);
  })
})
```


## createColorPicker

```TypeScript
function createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void
```

Creates a ColorPicker instance based on a pixel map. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-effectKit-function createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void--><!--Device-effectKit-function createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | image.PixelMap | Yes | PixelMap instance created by the image module. An instance can be obtained by decoding an image or directly created. For details, see Introduction to Image Kit. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md)&gt; | Yes | Callback used to return the ColorPicker instance created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Input parameter error. |

**Examples**

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
    }
  })
})
```


## createColorPicker

```TypeScript
function createColorPicker(source: image.PixelMap, region: Array<double>, callback: AsyncCallback<ColorPicker>): void
```

Creates a ColorPicker instance for the selected region based on a pixel map. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-effectKit-function createColorPicker(source: image.PixelMap, region: Array<double>, callback: AsyncCallback<ColorPicker>): void--><!--Device-effectKit-function createColorPicker(source: image.PixelMap, region: Array<double>, callback: AsyncCallback<ColorPicker>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | image.PixelMap | Yes | PixelMap instance created by the image module. An instance can be obtained by decoding an image or directly created. For details, see Introduction to Image Kit. |
| region | Array&lt;double&gt; | Yes | Color picking region of the image. The array contains four elements, with a value range of [0, 1]. Values outside this range are automatically truncated during implementation. The four elements represent the left, top, right, and bottom positions of the image region, respectively. The leftmost and topmost edges correspond to position 0, and the rightmost and bottommost edges correspond to position 1. The third element must be greater than the first element, and the fourth element must be greater than the second element. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md)&gt; | Yes | Callback used to return the ColorPicker instance created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Input parameter error. |

**Examples**

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, [0, 0, 1, 1], (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
    }
  })
})
```

