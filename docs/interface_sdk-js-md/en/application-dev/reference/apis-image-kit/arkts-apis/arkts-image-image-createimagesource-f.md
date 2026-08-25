# createImageSource

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createImageSource

```TypeScript
function createImageSource(uri: string): ImageSource
```

Creates an ImageSource instance based on a given URI.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.The SVG tags are supported since API version 10. The used version is (SVG) 1.1, and the width and height of the SVG tag must be set. An XML declaration can be added to an SVG file and start with **&lt;?xml**. The following tags are supported:  
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

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

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
function createImageSource(uri: string, options: SourceOptions): ImageSource
```

Creates an ImageSource instance based on a given URI.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.The SVG tags are supported since API version 10. The used version is (SVG) 1.1, and the width and height of the SVG tag must be set. An XML declaration can be added to an SVG file and start with **&lt;?xml**. The following tags are supported:  
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

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(fd: number): ImageSource
```

Creates an ImageSource instance based on a given file descriptor.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

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
function createImageSource(fd: number, options: SourceOptions): ImageSource
```

Creates an ImageSource instance based on a given file descriptor.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer): ImageSource
```

Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call [image.createPixelMapSync](arkts-image-image-imagesource-i.md#createpixelmapsync). Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource
```

Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call [image.createPixelMapSync](arkts-image-image-imagesource-i.md#createpixelmapsync). Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource
```

Creates an ImageSource instance based on the raw file descriptor of an image resource file. Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rawfile | resourceManager.RawFileDescriptor | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |
