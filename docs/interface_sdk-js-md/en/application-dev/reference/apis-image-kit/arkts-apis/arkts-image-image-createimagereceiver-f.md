# createImageReceiver

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createImageReceiver

```TypeScript
function createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver
```

通过宽、高、图片格式、容量创建ImageReceiver实例。ImageReceiver做为图片的接收方、消费者，它的参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流  
[createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md/arkts-camera-camera-cameramanager-i.md#createpreviewoutput)。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](arkts-image-image-imagereceiver-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

> **说明：**
> 
> 从API version 9开始支持，从API version 11废弃，建议使用[createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver)代替。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [image.createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver)(size:

<!--Device-image-function createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver--><!--Device-image-function createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | 图像的默认宽度。单位：像素（px）。该参数不会影响接收到的图片宽度，实际宽度由生产者决定，如相机。 |
| height | number | Yes | 图像的默认高度。单位：像素（px）。该参数不会影响接收到的图片高度，实际高度由生产者决定，如相机。 |
| format | number | Yes | 图像格式，取值为[ImageFormat](arkts-image-image-imageformat-e.md)常量（目前仅支持 ImageFormat:JPEG，实际返回格式由生产者决定，如相机 ）。 |
| capacity | number | Yes | 同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) | 如果操作成功，则返回ImageReceiver实例。 |

## Examples

```TypeScript
let receiver: image.ImageReceiver = image.createImageReceiver(8192, 8192, image.ImageFormat.JPEG, 8);
```


## createImageReceiver

```TypeScript
function createImageReceiver(size: Size, format: ImageFormat, capacity: int): ImageReceiver
```

通过图片大小、图片格式、容量创建ImageReceiver实例。ImageReceiver作为图片的接收方、消费者，它的参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流  
[createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md/arkts-camera-camera-cameramanager-i.md#createpreviewoutput)。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](arkts-image-image-imagereceiver-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-image-function createImageReceiver(size: Size, format: ImageFormat, capacity: int): ImageReceiver--><!--Device-image-function createImageReceiver(size: Size, format: ImageFormat, capacity: int): ImageReceiver-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md) | Yes | 图像的默认大小。单位：像素（px）。该参数不会影响接收到的图片大小，实际返回大小由生产者决定，如相机。 |
| format | [ImageFormat](arkts-image-image-imageformat-e.md) | Yes | 图像格式，取值为[ImageFormat](arkts-image-image-imageformat-e.md)常量（目前仅支持 ImageFormat:JPEG，实际返回格式由生产者决 定，如相机）。 |
| capacity | int | Yes | 同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) | 如果操作成功，则返回ImageReceiver实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types; |

## Examples

```TypeScript
let size: image.Size = {
  height: 8192,
  width: 8192
}
let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
```


## createImageReceiver

```TypeScript
function createImageReceiver(size: Size, format: ImageFormat, capacity: int): ImageReceiver | undefined
```

Creates an ImageReceiver instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-image-function createImageReceiver(size: Size, format: ImageFormat, capacity: int): ImageReceiver | undefined--><!--Device-image-function createImageReceiver(size: Size, format: ImageFormat, capacity: int): ImageReceiver | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md) | Yes | The default {@link Size} in pixels of the Images that this receiver will produce. |
| format | [ImageFormat](arkts-image-image-imageformat-e.md) | Yes | The format of the Image that this receiver will produce. This must be one of the {@link ImageFormat} constants. |
| capacity | int | Yes | The maximum number of images the user will want to access simultaneously. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) | Returns the ImageReceiver instance if the operation is successful; returns undefined otherwise. |


## createImageReceiver

```TypeScript
function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined
```

通过ImageReceiverOptions创建ImageReceiver实例。ImageReceiver作为图片的接收方、消费者，其参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流  
[createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md/arkts-camera-camera-cameramanager-i.md#createpreviewoutput)。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](arkts-image-image-imagereceiver-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-image-function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined--><!--Device-image-function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ImageReceiverOptions](arkts-image-image-imagereceiveroptions-i.md) | No | 创建ImageReceiver的属性，包括图片的默认大小和同时访问的最大图片数。 &lt;br&gt;未传入options时，默认的size为1920*1080，单位为像素（px），表示期望接收宽为1920px，高为1080px的图片。 &lt;br&gt;未传入options时，默认的capacity为3，表示期望同时最多有3张图片等待读取。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) | 操作成功时返回ImageReceiver实例，否则返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7900201 | Invalid parameter. |

## Examples

```TypeScript
let options: image.ImageReceiverOptions = {
  size: { width: 480, height: 480 },
  capacity: 3
}
let receiver: image.ImageReceiver | undefined = image.createImageReceiver(options);
```

