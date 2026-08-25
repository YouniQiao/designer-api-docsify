# createImageSource

## Modules to Import

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## createImageSource

```TypeScript
function createImageSource(uri: string): ImageSource
```

Creates an ImageSource instance based on a given URI.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-sendableimage-pixelmap-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.从API version 10开始支持SVG标签，使用版本为(SVG) 1.1, SVG标签需设置width和height。SVG文件可添加XML声明，应以**&lt;?xml**开头，当前支持的标签列表有：  
- a  
- circle  
- clipPath  
- defs  
- ellipse  
- feBlend  
- feColorMatrix  
- feComposite  
- feDiffuseLighting  
- feDisplacementMap  
- feDistantLight  
- feFlood  
- feGaussianBlur  
- feImage  
- feMorphology  
- feOffset  
- fePointLight  
- feSpecularLighting  
- feSpotLight  
- feTurbulence  
- filter  
- g  
- image  
- line  
- linearGradient  
- mask  
- path  
- pattern  
- polygon  
- polyline  
- radialGradient  
- rect  
- stop  
- svg  
- text  
- textPath  
- tspan  
- use

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(fd: number): ImageSource
```

Creates an ImageSource instance based on a given file descriptor.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-sendableimage-pixelmap-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer): ImageSource
```

Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call [sendableImage.createPixelMap](arkts-image-sendableimage-createpixelmap-f.md).Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-sendableimage-pixelmap-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |
