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

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-effectKit-function createColorPicker(source: image.PixelMap): Promise<ColorPicker>--><!--Device-effectKit-function createColorPicker(source: image.PixelMap): Promise<ColorPicker>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | image.PixelMap | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a buffer for image effects.
const colorBuffer = new ArrayBuffer(96);
// Set image initialization options.
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};

// Create a PixelMap instance.
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
  // Create a ColorPicker instance.
  effectKit.createColorPicker(pixelMap).then(colorPicker => {
    console.info('Succeeded in creating colorPicker.');
  }).catch((err : BusinessError) => {
    console.error(`Failed to create colorPicker. Code: ${err.code}, message: ${err.message}`);
  });
});
```


## createColorPicker

```TypeScript
function createColorPicker(source: image.PixelMap, region: Array<number>): Promise<ColorPicker>
```

Creates a ColorPicker instance for the selected region based on a pixel map. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-effectKit-function createColorPicker(source: image.PixelMap, region: Array<double>): Promise<ColorPicker>--><!--Device-effectKit-function createColorPicker(source: image.PixelMap, region: Array<double>): Promise<ColorPicker>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | image.PixelMap | Yes |
| region | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a buffer for image effects.
const colorBuffer = new ArrayBuffer(96);
// Set image initialization options.
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};

// Create a PixelMap instance.
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
  // Create a ColorPicker instance for the specified color sampling area.
  effectKit.createColorPicker(pixelMap, [0, 0, 1, 1]).then(colorPicker => {
    console.info('Succeeded in creating colorPicker.');
  }).catch((err : BusinessError) => {
    console.error(`Failed to create colorPicker. Code: ${err.code}, message: ${err.message}`);
  });
});
```


## createColorPicker

```TypeScript
function createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void
```

Creates a ColorPicker instance based on a pixel map. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-effectKit-function createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void--><!--Device-effectKit-function createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | image.PixelMap | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';

// Create a buffer for image effects.
const colorBuffer = new ArrayBuffer(96);
// Set image initialization options.
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
// Create a PixelMap instance.
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
  // Create a ColorPicker instance.
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error(`Failed to create color picker. Code: ${error.code}, message: ${error.message}`);
    } else {
      console.info('Succeeded in creating color picker.');
    }
  });
});
```


## createColorPicker

```TypeScript
function createColorPicker(source: image.PixelMap, region: Array<number>, callback: AsyncCallback<ColorPicker>): void
```

Creates a ColorPicker instance for the selected region based on a pixel map. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-effectKit-function createColorPicker(source: image.PixelMap, region: Array<double>, callback: AsyncCallback<ColorPicker>): void--><!--Device-effectKit-function createColorPicker(source: image.PixelMap, region: Array<double>, callback: AsyncCallback<ColorPicker>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | image.PixelMap | Yes |
| region | Array & lt;number & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';

// Create a buffer for image effects.
const colorBuffer = new ArrayBuffer(96);
// Set image initialization options.
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
// Create a PixelMap instance.
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
  // Create a ColorPicker instance for the specified color sampling area.
  effectKit.createColorPicker(pixelMap, [0, 0, 1, 1], (error, colorPicker) => {
    if (error) {
      console.error(`Failed to create color picker. Code: ${error.code}, message: ${error.message}`);
    } else {
      console.info('Succeeded in creating color picker.');
    }
  });
});
```
