# createImageSource

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createImageSource

```TypeScript
function createImageSource(uri: string): ImageSource
```

通过传入的uri创建ImageSource实例。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。从API version 10开始支持SVG标签，使用版本为(SVG) 1.1, SVG标签需设置width和height。SVG文件可添加XML声明，应以**&lt;?xml**开头，当前支持的标签列表有：  
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

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(uri: string, options: SourceOptions): ImageSource
```

通过传入的uri创建ImageSource实例。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。  
* 从API version 10开始支持SVG标签，使用版本为(SVG) 1.1, SVG标签需设置width和height。SVG文件可添加XML声明，应以**&lt;?xml**开头，当前支持的标签列表有：  
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
- uses

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(fd: number): ImageSource
```

通过传入文件描述符来创建ImageSource实例。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(fd: number, options: SourceOptions): ImageSource
```

通过传入文件描述符来创建ImageSource实例。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer): ImageSource
```

通过缓冲区创建ImageSource实例。buf数据是未解码的数据，不可以传入类似于RBGA，YUV的像素buffer数据，如果想通过像素buffer数据创建pixelMap，可以调用 [image.createPixelMapSync](arkts-image-image-createpixelmapsync-f.md)这一类接口。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource
```

通过缓冲区创建ImageSource实例。buf数据是未解码的数据，不可以传入类似于RBGA，YUV的像素buffer数据，如果想通过像素buffer数据创建pixelMap，可以调用 [image.createPixelMapSync](arkts-image-image-createpixelmapsync-f.md)这一类接口。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource
```

通过图像资源文件的RawFileDescriptor创建ImageSource实例。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rawfile | resourceManager.RawFileDescriptor | 是 |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |
