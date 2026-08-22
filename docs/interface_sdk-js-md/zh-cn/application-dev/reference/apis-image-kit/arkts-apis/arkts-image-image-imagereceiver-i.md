# ImageReceiver

ImageReceiver类，用于获取组件surface id、接收最新的图片和读取下一张图片以及释放ImageReceiver实例。ImageReceiver作为图片的接收方和消费者，其参数属性实际上不会对接收到的图片产生影响。 图片属性的配置应在发送方和生产者上进行，如相机预览流 [createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md#createpreviewoutput) 。

在调用以下方法前需要先通过[image.createImageReceiver](arkts-image-image-createimagereceiver-f.md)创建ImageReceiver实例。

从API version 23开始，更推荐使用[image.createImageReceiver](arkts-image-image-createimagereceiver-f.md)，通过传入 [ImageReceiverOptions](arkts-image-image-imagereceiveroptions-i.md)创建ImageReceiver实例。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](#release) 方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

> **说明：**
> 
> - 本Interface首批接口从API version 9开始支持。

**起始版本：** 23

<!--Device-image-interface ImageReceiver--><!--Device-image-interface ImageReceiver-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

## 导入模块

```TypeScript
import { image } from '@kit.ImageKit';
```

## getReceivingSurfaceId

```TypeScript
getReceivingSurfaceId(callback: AsyncCallback<string>): void
```

用于获取一个surface id供Camera或其他组件使用。使用callback异步回调。

**起始版本：** 23

<!--Device-ImageReceiver-getReceivingSurfaceId(callback: AsyncCallback<string>): void--><!--Device-ImageReceiver-getReceivingSurfaceId(callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 | 回调函数，当获取surface id成功，err为undefined，data为获取到的surface id；否则为错误对象。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetReceivingSurfaceId(receiver : image.ImageReceiver) {
  receiver.getReceivingSurfaceId((err: BusinessError, id: string) => {
    if (err) {
      console.error(`Failed to get the ReceivingSurfaceId.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in getting the ReceivingSurfaceId.');
    }
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function GetReceivingSurfaceIdFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    receiver.getReceivingSurfaceId((err: BusinessError | null, id: string | undefined) => {
      if (err) {
        console.error(0x00000, 'GetReceivingSurfaceIdFunc', 'getReceivingSurfaceId failed: ' + err);
      } else {
        console.info(0x00000, 'GetReceivingSurfaceIdFunc', 'getReceivingSurfaceId success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'GetReceivingSurfaceIdFunc', 'GetReceivingSurfaceIdFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetReceivingSurfaceId(receiver : image.ImageReceiver) {
  receiver.getReceivingSurfaceId().then((id: string) => { 
    console.info('Succeeded in getting the ReceivingSurfaceId.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get the ReceivingSurfaceId.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
async function GetReceivingSurfaceIdFunc(): Promise<void> {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    await receiver.getReceivingSurfaceId();
    console.info(0x00000, 'GetReceivingSurfaceIdFunc', 'getReceivingSurfaceId success!');
  } catch (err) {
    console.error(0x00000, 'GetReceivingSurfaceIdFunc', 'GetReceivingSurfaceIdFunc failed: ' + err);
  }
}
```

## getReceivingSurfaceId

```TypeScript
getReceivingSurfaceId(): Promise<string>
```

用于获取一个surface id供Camera或其他组件使用。使用Promise异步回调。

**起始版本：** 23

<!--Device-ImageReceiver-getReceivingSurfaceId(): Promise<string>--><!--Device-ImageReceiver-getReceivingSurfaceId(): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回surface id。 |

**示例**

参见 [getReceivingSurfaceId](#getreceivingsurfaceid)

## off('imageArrival')

```TypeScript
off(type: 'imageArrival', callback?: AsyncCallback<void>): void
```

释放buffer时移除注册回调。使用callback异步回调。

**起始版本：** 13

<!--Device-ImageReceiver-off(type: 'imageArrival', callback?: AsyncCallback<void>): void--><!--Device-ImageReceiver-off(type: 'imageArrival', callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'imageArrival' | 是 | 注册事件的类型，固定为'imageArrival'，释放buffer时触发。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 | 移除的回调函数。 |

## offImageArrival

```TypeScript
offImageArrival(callback?: AsyncCallback<void>): void
```

Remove callback subscriptions when releasing buffer.

**起始版本：** 23

<!--Device-ImageReceiver-offImageArrival(callback?: AsyncCallback<void>): void--><!--Device-ImageReceiver-offImageArrival(callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 | Callback to be removed. |

**示例**

```TypeScript
function OffFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    receiver.onImageArrival(() => {
      console.info(0x00000, 'OffFunc', 'on success!');
    });
    receiver.offImageArrival(() => {
      console.info(0x00000, 'OffFunc', 'off success!');
    });
  } catch (err) {
    console.error(0x00000, 'OffFunc', 'OffFunc failed: ' + err);
  }
}
```

## on('imageArrival')

```TypeScript
on(type: 'imageArrival', callback: AsyncCallback<void>): void
```

接收图片时注册回调。使用callback异步回调。

**起始版本：** 9

<!--Device-ImageReceiver-on(type: 'imageArrival', callback: AsyncCallback<void>): void--><!--Device-ImageReceiver-on(type: 'imageArrival', callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'imageArrival' | 是 | 注册事件的类型，固定为'imageArrival'，接收图片到达时触发。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数，当注册事件触发成功，err为undefined，否则为错误对象。 |

## onImageArrival

```TypeScript
onImageArrival(callback: AsyncCallback<void>): void
```

Subscribe callback when receiving an image.

**起始版本：** 23

<!--Device-ImageReceiver-onImageArrival(callback: AsyncCallback<void>): void--><!--Device-ImageReceiver-onImageArrival(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | Callback used to return image. |

**示例**

```TypeScript
import { image } from '@kit.ImageKit';

function OnImageArrivalFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    receiver.onImageArrival(() => {
      console.info(0x00000, 'OnFunc', 'on success!');
    });
  } catch (err) {
    console.error(0x00000, 'OnFunc', 'OnFunc failed: ' + err);
  }
}
```

## readLatestImage

```TypeScript
readLatestImage(callback: AsyncCallback<Image>): void
```

从ImageReceiver读取最新的图片。使用callback异步回调。

> **注意**：
> 
> 此接口需要在[on](#onimagearrival)回调触发后调用，才能正常的接收到数
> 据。且此接口返回的[Image](arkts-image-image-image-i.md)对象使用完毕后需要调用
> [release](arkts-image-image-image-i.md#release)方法释放，释放后才可以继续接收新的数据。

**起始版本：** 23

<!--Device-ImageReceiver-readLatestImage(callback: AsyncCallback<Image>): void--><!--Device-ImageReceiver-readLatestImage(callback: AsyncCallback<Image>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Image&gt; | 是 | 回调函数，当读取最新图片成功，err为undefined，data为获取到的最新图片；否则为错误对象。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadLatestImage(receiver : image.ImageReceiver) {
  receiver.readLatestImage((err: BusinessError, latestImage: image.Image) => {
    if (err || latestImage === undefined) {
      console.error('Failed to readLatestImage.');
      return;
    }
    // 解析图像内容。
    latestImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError,
      imgComponent: image.Component) => {
      if (err || imgComponent === undefined) {
        console.error('Failed to getComponent.');
        return;
      }
      if (imgComponent.byteBuffer) {
        // 处理二进制图像数据。
        console.info(`getComponent with width:${latestImage.size.width} height:${latestImage.size.height}`);
      } else {
        console.error('byteBuffer is null');
      }
    })
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReadLatestImageFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    // 创建imageReceiver实例。
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    receiver.readLatestImage((err: BusinessError | null, img: image.Image | undefined) => {
      if (err) {
        console.error(0x00000, 'ReadLatestImageFunc', 'readLatestImage failed: ' + err);
      } else {
        console.info(0x00000, 'ReadLatestImageFunc', 'readLatestImage success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReadLatestImageFunc', 'ReadLatestImageFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadLatestImage(receiver : image.ImageReceiver) {
  receiver.readLatestImage().then((latestImage: image.Image) => {
    // 解析图像内容。
    latestImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError,
      imgComponent: image.Component) => {
      if (err || imgComponent === undefined) {
        console.error('Failed to getComponent.');
        return;
      }
      if (imgComponent.byteBuffer) {
        // 处理二进制图像数据。
        console.info(`getComponent with width:${latestImage.size.width} height:${latestImage.size.height}`);
      } else {
        console.error('byteBuffer is null');
      }
    })    
  }).catch((error: BusinessError) => {
    console.error(`Failed to read the latest Image.code ${error.code},message is ${error.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
async function ReadLatestImageFunc(): Promise<void> {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    await receiver.readLatestImage();
    console.info(0x00000, 'ReadLatestImageFunc', 'readLatestImage success!');
  } catch (err) {
    console.error(0x00000, 'ReadLatestImageFunc', 'ReadLatestImageFunc failed: ' + err);
  }
}
```

## readLatestImage

```TypeScript
readLatestImage(): Promise<Image>
```

从ImageReceiver读取最新的图片。使用Promise异步回调。

> **注意**：
> 
> 此接口需要在[on](#onimagearrival)回调触发后调用，才能正常的接收到数
> 据。且此接口返回的[Image](arkts-image-image-image-i.md)对象使用完毕后需要调用
> [release](arkts-image-image-image-i.md#release)方法释放，释放后才可以继续接收新的数据。

**起始版本：** 23

<!--Device-ImageReceiver-readLatestImage(): Promise<Image>--><!--Device-ImageReceiver-readLatestImage(): Promise<Image>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Image&gt; | Promise对象，返回最新图片。 |

**示例**

参见 [readLatestImage](#readlatestimage)

## readNextImage

```TypeScript
readNextImage(callback: AsyncCallback<Image>): void
```

从ImageReceiver读取下一张图片。使用callback异步回调。

> **注意**：
> 
> 此接口需要在[on](#onimagearrival)回调触发后调用，才能正常的接收到数
> 据。且此接口返回的[Image](arkts-image-image-image-i.md)对象使用完毕后需要调用
> [release](arkts-image-image-image-i.md#release)方法释放，释放后才可以继续接收新的数据。

**起始版本：** 23

<!--Device-ImageReceiver-readNextImage(callback: AsyncCallback<Image>): void--><!--Device-ImageReceiver-readNextImage(callback: AsyncCallback<Image>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Image&gt; | 是 | 回调函数，当获取下一张图片成功，err为undefined，data为获取到的下一张图片；否则为错误对象。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadNextImage(receiver : image.ImageReceiver) {
  receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
    if (err || nextImage === undefined) {
      console.error('Failed to readNextImage.');
      return;
    }
    // 解析图像内容。
    nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError,
      imgComponent: image.Component) => {
      if (err || imgComponent === undefined) {
        console.error('Failed to getComponent.');
        return;
      }
      if (imgComponent.byteBuffer) {
        // 处理二进制图像数据。
        console.info(`getComponent with width:${nextImage.size.width} height:${nextImage.size.height} stride:${imgComponent.rowStride}`);
      } else {
        console.error('byteBuffer is null');
      }
    })
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReadNextImageFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    receiver.readNextImage((err: BusinessError | null, img: image.Image | undefined) => {
      if (err) {
        console.error(0x00000, 'ReadNextImageFunc', 'readNextImage failed: ' + err);
      } else {
        console.info(0x00000, 'ReadNextImageFunc', 'ReadNextImageFunc success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReadNextImageFunc', 'ReadNextImageFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadNextImage(receiver : image.ImageReceiver) {
  receiver.readNextImage().then((nextImage: image.Image) => {
    console.info('Succeeded in reading the next Image.');
    nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError,
      imgComponent: image.Component) => {
      if (err || imgComponent === undefined) {
        console.error('Failed to getComponent.');
        return;
      }
      if (imgComponent.byteBuffer) {
        // 处理二进制图像数据。
        console.info(`getComponent with width:${nextImage.size.width} height:${nextImage.size.height} stride:${imgComponent.rowStride}`);
      } else {
        console.error('byteBuffer is null');
      }
    })
  }).catch((error: BusinessError) => {
    console.error(`Failed to read the next Image.code ${error.code},message is ${error.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
async function ReleaseFunc(): Promise<void> {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    await receiver.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

## readNextImage

```TypeScript
readNextImage(): Promise<Image>
```

从ImageReceiver读取下一张图片。使用Promise异步回调。

> **注意**：
> 
> 此接口需要在[on](#onimagearrival)回调触发后调用，才能正常的接收到数
> 据。且此接口返回的[Image](arkts-image-image-image-i.md)对象使用完毕后需要调用
> [release](arkts-image-image-image-i.md#release)方法释放，释放后才可以继续接收新的数据。

**起始版本：** 23

<!--Device-ImageReceiver-readNextImage(): Promise<Image>--><!--Device-ImageReceiver-readNextImage(): Promise<Image>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Image&gt; | Promise对象，返回下一张图片。 |

**示例**

参见 [readNextImage](#readnextimage)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放ImageReceiver实例。使用callback异步回调。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 23

<!--Device-ImageReceiver-release(callback: AsyncCallback<void>): void--><!--Device-ImageReceiver-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数，当释放ImageReceiver实例成功，err为undefined，否则为错误对象。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
async function Release(auxPictureObj: image.AuxiliaryPicture) {
  let funcName = "Release";
  if (auxPictureObj != null) {
    auxPictureObj.release();
    if (auxPictureObj.getType() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
if (context != undefined) {
  let auxPicture: image.AuxiliaryPicture | null = GetAuxiliaryPicture(context)
  if (auxPicture != null) {
    auxPicture.release();
  } else {
    console.error(0x00000, 'GetAuxiliaryPicture', 'auxPicture is null!');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image instance.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@ohos.base';

function ReleaseFunc(img: image.Image): void {
  try {
    img.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    })
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release().then(() => {
    console.info('Succeeded in releasing the image instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image instance.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(img: image.Image): void {
  try {
    await img.release()
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(creator : image.ImageCreator) {
  creator.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the creator.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing creator.');
    }
  });
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(creator: image.ImageCreator): void {
  try {
    creator.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    })
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(creator : image.ImageCreator) {
  creator.release().then(() => {
    console.info('Succeeded in releasing creator.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the creator.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(creator: image.ImageCreator): void {
  try {
    await creator.release();
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release((err: BusinessError)=>{
    if (err) {
      console.error(`Failed to release image packaging.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing image packaging.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(): void {
  try {
    let imagePacker: image.ImagePacker = image.createImagePacker();
    imagePacker.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release().then(() => {
    console.info('Succeeded in releasing image packaging.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release image packaging.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
async function ReleaseFunc(): Promise<void> {
  try {
    let imagePacker: image.ImagePacker = image.createImagePacker();
    await imagePacker.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the receiver.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the receiver.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    receiver.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'ReleaseFunc success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release().then(() => {
    console.info('Succeeded in releasing the receiver.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the receiver.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    await receiver.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image source instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image source instance.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(imageSource: image.ImageSource): void {
  try {
    imageSource.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release().then(() => {
    console.info('Succeeded in releasing the image source instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image source instance.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
async function ReleaseFunc(imageSource: image.ImageSource): Promise<void> {
  try {
    await imageSource.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
async function Release(pictureObj : image.Picture) {
  let funcName = "Release";
  if (pictureObj != null) {
    pictureObj.release();
    if (pictureObj.getMainPixelmap() == null) {
      console.info(funcName, 'Succeeded in releasing a picture.');
    } else {
      console.error(funcName, 'Failed to release a picture.');
    }
  } else {
    console.error('Picture object is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(picture: image.Picture): void {
  try {
    picture.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function release(pixelMap: image.PixelMap) {
  pixelMap.release().then(() => {
    console.info('Succeeded in releasing the PixelMap object.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to release the PixelMap object. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function release(pixelMap: image.PixelMap) {
  pixelMap.release().then(() => {
    console.info('Succeeded in releasing the PixelMap object.');
  }).catch((err: Error) => {
    console.error(`Failed to release the PixelMap object. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function release(pixelMap: image.PixelMap) {
  pixelMap.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the PixelMap object. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in releasing the PixelMap object.');
  });
}
```

## release

```TypeScript
release(): Promise<void>
```

释放ImageReceiver实例。使用Promise异步回调。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 23

<!--Device-ImageReceiver-release(): Promise<void>--><!--Device-ImageReceiver-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**示例**

参见 [release](#release)

## capacity

```TypeScript
readonly capacity: int
```

同时访问的图像数。该参数仅作为期望值，实际capacity由设备硬件决定。

**类型：** int

**起始版本：** 23

<!--Device-ImageReceiver-readonly capacity: int--><!--Device-ImageReceiver-readonly capacity: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

## format

```TypeScript
readonly format: ImageFormat
```

图像格式，取值为[ImageFormat](arkts-image-image-imageformat-e.md)常量（目前仅支持 ImageFormat:JPEG，实际返回格式由生产者决定，如相机）。

**类型：** [ImageFormat](arkts-image-image-imageformat-e.md)

**起始版本：** 23

<!--Device-ImageReceiver-readonly format: ImageFormat--><!--Device-ImageReceiver-readonly format: ImageFormat-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

## size

```TypeScript
readonly size: Size
```

图片大小。该参数不会影响接收到的图片大小，实际返回大小由生产者决定，如相机。

**类型：** Size

**起始版本：** 23

<!--Device-ImageReceiver-readonly size: Size--><!--Device-ImageReceiver-readonly size: Size-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

