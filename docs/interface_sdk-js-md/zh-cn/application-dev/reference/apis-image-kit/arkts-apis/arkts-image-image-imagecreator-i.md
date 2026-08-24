# ImageCreator

ImageCreator类，作为图片的生产者，用于将图片写入到Surface中。在调用以下方法前需要先通过[image.createImageCreator](arkts-image-image-createimagecreator-f.md)创建ImageCreator实例，ImageCreator不支持多线程。由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](#release)方法 及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

> **说明：**&gt;
> - 本Interface首批接口从API version 9开始支持。

**起始版本：** 23

<!--Device-image-interface ImageCreator--><!--Device-image-interface ImageCreator-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

## 导入模块

```TypeScript
import { image } from '@kit.ImageKit';
```

## dequeueImage

```TypeScript
dequeueImage(callback: AsyncCallback<Image>): void
```

从空闲队列中获取buffer图片，用于绘制UI内容。使用callback异步回调。

**起始版本：** 23

<!--Device-ImageCreator-dequeueImage(callback: AsyncCallback<Image>): void--><!--Device-ImageCreator-dequeueImage(callback: AsyncCallback<Image>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Image&gt; | 是 | 回调函数，当获取最新图片成功，err为undefined，data为获取到的最新图片；否则为错误对象。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function DequeueImage(creator : image.ImageCreator) {
  creator.dequeueImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(`Failed to dequeue the Image.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in dequeuing the Image.');
    }
  });
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function DequeueImageFunc(creator: image.ImageCreator): void {
  try {
    creator.dequeueImage((err: BusinessError | null, img: image.Image | undefined) => {
      if (err) {
        console.error(0x00000, 'DequeueImageFunc', 'dequeueImage failed! err:' + err);
      } else {
        console.info(0x00000, 'DequeueImageFunc', 'dequeueImage success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'DequeueImageFunc', 'DequeueImageFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function DequeueImage(creator : image.ImageCreator) {
  creator.dequeueImage().then((img: image.Image) => {
    console.info('Succeeded in dequeuing the Image.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to dequeue the Image.code ${error.code},message is ${error.message}`);
  })
```

ArkTS-Sta示例：

```TypeScript
function DequeueImageFunc(creator: image.ImageCreator): void {
  try {
    let image: image.Image = await creator.dequeueImage();
    console.info(0x00000, 'DequeueImageFunc', 'dequeueImage success!');
  } catch (err) {
    console.error(0x00000, 'DequeueImageFunc', 'DequeueImageFunc failed: ' + err);
  }
}
```

## dequeueImage

```TypeScript
dequeueImage(): Promise<Image>
```

从空闲队列中获取buffer图片，用于绘制UI内容。使用Promise异步回调。

**起始版本：** 23

<!--Device-ImageCreator-dequeueImage(): Promise<Image>--><!--Device-ImageCreator-dequeueImage(): Promise<Image>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Image&gt; | Promise对象，返回最新图片。 |

**示例**

参见 [dequeueImage](#dequeueimage)

## off('imageRelease')

```TypeScript
off(type: 'imageRelease', callback?: AsyncCallback<void>): void
```

释放buffer时，移除注册的回调函数。使用callback异步回调。

**起始版本：** 13

<!--Device-ImageCreator-off(type: 'imageRelease', callback?: AsyncCallback<void>): void--><!--Device-ImageCreator-off(type: 'imageRelease', callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'imageRelease' | 是 | 监听事件类型，如'imageRelease'。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 | 回调函数。当移除注册成功时，err为undefined，否则为错误对象。 |

## offImageRelease

```TypeScript
offImageRelease(callback?: AsyncCallback<void>): void
```

Remove callback subscriptions when releasing buffer

**起始版本：** 23

<!--Device-ImageCreator-offImageRelease(callback?: AsyncCallback<void>): void--><!--Device-ImageCreator-offImageRelease(callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 | Callback to be removed. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function OffFunc(creator: image.ImageCreator): void {
  try{
    creator.onImageRelease('imageRelease', (err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'OffFunc', 'on failed: ' + err);
      } else {
        console.info(0x00000, 'OffFunc', 'on success!');
      }
    });
    // 移除注册的回调函数。
    creator.offImageRelease('imageRelease', (err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'OffFunc', 'off failed: ' + err);
      } else {
        console.info(0x00000, 'OffFunc', 'off success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'OffFunc', 'OffFunc failed: ' + err);
  }
}
```

## on('imageRelease')

```TypeScript
on(type: 'imageRelease', callback: AsyncCallback<void>): void
```

监听imageRelease事件。使用callback异步回调。

**起始版本：** 9

<!--Device-ImageCreator-on(type: 'imageRelease', callback: AsyncCallback<void>): void--><!--Device-ImageCreator-on(type: 'imageRelease', callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'imageRelease' | 是 | 监听事件类型，如'imageRelease'。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数，当监听事件触发成功，err为undefined，否则为错误对象。 |

## onImageRelease

```TypeScript
onImageRelease(callback: AsyncCallback<void>): void
```

Subscribe callback when releasing buffer

**起始版本：** 23

<!--Device-ImageCreator-onImageRelease(callback: AsyncCallback<void>): void--><!--Device-ImageCreator-onImageRelease(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | Callback used to return the operation result. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function OnFunc(creator: image.ImageCreator): void {
  try{
    creator.onImageRelease('imageRelease', (err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'OnFunc', 'on failed: ' + err);
      } else {
        console.info(0x00000, 'OnFunc', 'on success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'OnFunc', 'OnFunc failed: ' + err);
  }
}
```

## queueImage

```TypeScript
queueImage(image: Image, callback: AsyncCallback<void>): void
```

将绘制好的图片放入队列。使用callback异步回调。

**起始版本：** 23

<!--Device-ImageCreator-queueImage(image: Image, callback: AsyncCallback<void>): void--><!--Device-ImageCreator-queueImage(image: Image, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Image | 是 | 绘制好的buffer图像。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数，当将图片放入队列成功，err为undefined，否则为错误对象。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function QueueImage(creator : image.ImageCreator) {
  creator.dequeueImage().then((img: image.Image) => {
    // 绘制图片。
    img.getComponent(4).then((component : image.Component) => {
      let bufferArr: Uint8Array = new Uint8Array(component.byteBuffer);
      for (let i = 0; i < bufferArr.length; i += 4) {
        bufferArr[i] = 0; // B
        bufferArr[i + 1] = 0; // G
        bufferArr[i + 2] = 255; // R
        bufferArr[i + 3] = 255; // A
      }
    })
    creator.queueImage(img, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to queue the Image.code ${err.code},message is ${err.message}`);
      } else {
        console.info('Succeeded in queuing the Image.');
      }
    })
  })
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function QueueImageFunc(creator: image.ImageCreator): void {
  try {
    let image: image.Image = await creator.dequeueImage(); // 从空闲队列获取Image对象用于绘制。
    creator.queueImage(image, (err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'QueueImageFunc', 'queueImage failed! err:' + err);
      } else {
        console.info(0x00000, 'QueueImageFunc', 'queueImage success!');
      }
    }); // 将绘制完成的Image放入队列供消费者使用。
  } catch (err) {
    console.error(0x00000, 'QueueImageFunc', 'QueueImageFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function QueueImage(creator : image.ImageCreator) {
  creator.dequeueImage().then((img: image.Image) => {
    // 绘制图片。
    img.getComponent(4).then((component: image.Component) => {
      let bufferArr: Uint8Array = new Uint8Array(component.byteBuffer);
      for (let i = 0; i < bufferArr.length; i += 4) {
        bufferArr[i] = 0; // B
        bufferArr[i + 1] = 0; // G
        bufferArr[i + 2] = 255; // R
        bufferArr[i + 3] = 255; // A
      }
    })
    creator.queueImage(img).then(() => {
      console.info('Succeeded in queuing the Image.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to queue the Image.code ${error.code},message is ${error.message}`);
    })
  })
```

ArkTS-Sta示例：

```TypeScript
function QueueImageFunc(creator: image.ImageCreator): void {
  try {
    let image: image.Image = await creator.dequeueImage();
    await creator.queueImage(image);
    console.info(0x00000, 'QueueImageFunc', 'queueImage success!');
  } catch (err) {
    console.error(0x00000, 'QueueImageFunc', 'QueueImageFunc failed: ' + err);
  }
}
```

## queueImage

```TypeScript
queueImage(image: Image): Promise<void>
```

将绘制好的图片放入队列。使用Promise异步回调。

**起始版本：** 23

<!--Device-ImageCreator-queueImage(image: Image): Promise<void>--><!--Device-ImageCreator-queueImage(image: Image): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Image | 是 | 绘制好的buffer图像。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**示例**

参见 [queueImage](#queueimage)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放当前图像。使用callback异步回调。由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 23

<!--Device-ImageCreator-release(callback: AsyncCallback<void>): void--><!--Device-ImageCreator-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数，当图像释放成功，err为undefined，否则为错误对象。 |

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

释放当前图像。使用Promise异步回调。由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 23

<!--Device-ImageCreator-release(): Promise<void>--><!--Device-ImageCreator-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

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

<!--Device-ImageCreator-readonly capacity: int--><!--Device-ImageCreator-readonly capacity: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

## format

```TypeScript
readonly format: ImageFormat
```

图像格式。

**类型：** [ImageFormat](arkts-image-image-imageformat-e.md)

**起始版本：** 23

<!--Device-ImageCreator-readonly format: ImageFormat--><!--Device-ImageCreator-readonly format: ImageFormat-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

