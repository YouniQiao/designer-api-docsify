# createImageReceiver

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

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [image.createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver)(size:

<!--Device-image-function createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver--><!--Device-image-function createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |
| format | number | 是 |
| capacity | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) |

## 示例

```TypeScript
let receiver: image.ImageReceiver = image.createImageReceiver(8192, 8192, image.ImageFormat.JPEG, 8);
```


## createImageReceiver

```TypeScript
function createImageReceiver(size: Size, format: ImageFormat, capacity: number): ImageReceiver
```

通过图片大小、图片格式、容量创建ImageReceiver实例。ImageReceiver作为图片的接收方、消费者，它的参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流  
[createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md/arkts-camera-camera-cameramanager-i.md#createpreviewoutput)。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](arkts-image-image-imagereceiver-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 11

<!--Device-image-function createImageReceiver(size: Size, format: ImageFormat, capacity: int): ImageReceiver--><!--Device-image-function createImageReceiver(size: Size, format: ImageFormat, capacity: int): ImageReceiver-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md) | 是 |
| format | [ImageFormat](arkts-image-image-imageformat-e.md) | 是 |
| capacity | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
let size: image.Size = {
  height: 8192,
  width: 8192
}
let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
```


## createImageReceiver

```TypeScript
function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined
```

通过ImageReceiverOptions创建ImageReceiver实例。ImageReceiver作为图片的接收方、消费者，其参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流  
[createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md/arkts-camera-camera-cameramanager-i.md#createpreviewoutput)。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](arkts-image-image-imagereceiver-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-image-function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined--><!--Device-image-function createImageReceiver(options?: ImageReceiverOptions): ImageReceiver | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ImageReceiverOptions](arkts-image-image-imagereceiveroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7900201](../errorcode-image.md#7900201-无效参数) |

## 示例

```TypeScript
let options: image.ImageReceiverOptions = {
  size: { width: 480, height: 480 },
  capacity: 3
}
let receiver: image.ImageReceiver | undefined = image.createImageReceiver(options);
```
