# ColorPicker

A color picker class used to obtain the main color from image data. It is suitable for scenarios such as UI theme color extraction, image color scheme analysis, and intelligent color scheme recommendation, helping developers dynamically generate harmonious color schemes based on image content. Before calling the methods of ColorPicker, you need to create a ColorPicker instance via createColorPicker.

**Since:** 23

<!--Device-effectKit-interface ColorPicker--><!--Device-effectKit-interface ColorPicker-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
```

## getAverageColor

```TypeScript
getAverageColor(): Color
```

Reads the average color value from the image and writes the result to a Color instance. This API returns the result synchronously. It is commonly used in scenarios such as obtaining the overall tone of an image, such as image tone statistics and adaptive background color.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ColorPicker-getAverageColor(): Color--><!--Device-ColorPicker-getAverageColor(): Color-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-na/arkts-apis/arkts-na-enums-color-e.md) |

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';

// Create a buffer for image effects.
const colorBuffer = new ArrayBuffer(96);
// Set image initialization options.
let opts: image.InitializationOptions = {
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
      // Obtain the average color of the image.
      let averageColor = colorPicker.getAverageColor();
      console.info('get average color =' + averageColor);
    }
  });
});
```

## getHighestSaturationColor

```TypeScript
getHighestSaturationColor(): Color
```

Reads the color value with the highest saturation from the image and writes the result to a Color instance. This API returns the result synchronously. It is commonly used in scenarios such as extracting the most vivid color in an image, such as UI theme accent color extraction and icon highlight color selection.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ColorPicker-getHighestSaturationColor(): Color--><!--Device-ColorPicker-getHighestSaturationColor(): Color-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-na/arkts-apis/arkts-na-enums-color-e.md) |

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';

// Create a buffer for image effects.
const colorBuffer = new ArrayBuffer(96);
// Set image initialization options.
let opts: image.InitializationOptions = {
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
      // Obtain the color with the highest saturation in the image.
      let saturationColor = colorPicker.getHighestSaturationColor();
      console.info('get highest saturation color =' + saturationColor);
    }
  });
});
```

## getLargestProportionColor

```TypeScript
getLargestProportionColor(): Color
```

Reads the color value with the largest proportion in the image and writes the result to a Color instance. This API returns the result synchronously. This API uses the median cut algorithm to partition the color space and obtains the average color of the color space with the largest proportion. It is commonly used in scenarios such as identifying the largest color area in an image, such as icon background color extraction and image content analysis.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ColorPicker-getLargestProportionColor(): Color--><!--Device-ColorPicker-getLargestProportionColor(): Color-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-na/arkts-apis/arkts-na-enums-color-e.md) |

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';

// Create a buffer for the image effect.
const colorBuffer = new ArrayBuffer(96);
// Set the image initialization options.
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
      // Obtain the most dominant color in the image.
      let largestColor = colorPicker.getLargestProportionColor();
      console.info('get largest proportion color =' + largestColor);
    }
  });
});
```

## getMainColor

```TypeScript
getMainColor(): Promise<Color>
```

Reads the color value of the main color from the image and writes the result to a Color instance. This API uses a promise to return the result. This API uses the image scaling algorithm to calculate the weighted value of surrounding pixels and reduce the original image to one pixel to obtain the main color. It is commonly used in scenarios such as automatic app theme color extraction, automatic UI color matching based on images, and dynamic background color adjustment of music players based on album covers.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ColorPicker-getMainColor(): Promise<Color>--><!--Device-ColorPicker-getMainColor(): Promise<Color>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Color & gt; |

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';

// Create a buffer for image effects.
const colorBuffer = new ArrayBuffer(96);
// Set image initialization options.
let opts: image.InitializationOptions = {
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
      // Obtain the dominant color of the image.
      colorPicker.getMainColor().then(mainColor => {
        console.info('Succeeded in getting main color.');
        console.info(`color[ARGB]=${mainColor.alpha},${mainColor.red},${mainColor.green},${mainColor.blue}`);
      });
    }
  });
});
```

## getMainColorSync

```TypeScript
getMainColorSync(): Color
```

Reads the color value of the main color from the image and writes the result to a Color instance. This API returns the result synchronously. This API uses the image scaling algorithm to calculate the weighted value of surrounding pixels and reduces the original image to one pixel to obtain the main color. It is commonly used in scenarios such as automatic app theme color extraction, automatic UI color matching based on images, and dynamic background color adjustment of music players based on album covers.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ColorPicker-getMainColorSync(): Color--><!--Device-ColorPicker-getMainColorSync(): Color-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-na/arkts-apis/arkts-na-enums-color-e.md) |

**Examples**

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
      // Obtain the main color of the image synchronously.
      let mainColor = colorPicker.getMainColorSync();
      console.info('get main color =' + mainColor);
    }
  });
});
```

## getTopProportionColors

```TypeScript
getTopProportionColors(colorCount: number): Array<Color | null>
```

Reads the top proportion colors from the image, with the number specified by colorCount, and writes the results to an array of Color instances. This API returns the result synchronously. It is commonly used in scenarios such as extracting the top multiple colors by proportion in an image, such as multi-tone color scheme generation and image color distribution analysis.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ColorPicker-getTopProportionColors(colorCount: int): Array<Color | null>--><!--Device-ColorPicker-getTopProportionColors(colorCount: int): Array<Color | null>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorCount | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Color \ | null & gt; |

**Examples**

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
      // Obtain the top two dominant colors in the image.
      let colors = colorPicker.getTopProportionColors(2);
      for (let index = 0; index < colors.length; index++) {
        if (colors[index]) {
          console.info('get top proportion colors: index ' + index + ', color ' + colors[index]);
        }
      }
    }
  });
});
```

## isBlackOrWhiteOrGrayColor

```TypeScript
isBlackOrWhiteOrGrayColor(color: number): boolean
```

Determines whether the specified color value is a black, white, or gray color, and returns true or false. It is commonly used in scenarios such as determining whether a color belongs to the achromatic color system, such as intelligent color scheme filtering and image color classification.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ColorPicker-isBlackOrWhiteOrGrayColor(color: long): boolean--><!--Device-ColorPicker-isBlackOrWhiteOrGrayColor(color: long): boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';

// Create a buffer for image effects.
const colorBuffer = new ArrayBuffer(96);
// Set image initialization options.
let opts: image.InitializationOptions = {
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
      // Determine whether the color is black, white, or gray.
      let isBlackOrWhiteOrGray = colorPicker.isBlackOrWhiteOrGrayColor(0xFFFFFFFF);
      console.info('is black or white or gray color[bool](white) =' + isBlackOrWhiteOrGray);
    }
  });
});
```
