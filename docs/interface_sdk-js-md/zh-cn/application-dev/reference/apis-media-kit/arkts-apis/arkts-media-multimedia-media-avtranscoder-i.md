# AVTranscoder

视频转码管理类，用于视频转码。在调用AVTranscoder的方法前，需要先通过 [createAVTranscoder()](arkts-media-media-createavtranscoder-f.md)构建一个AVTranscoder实例。视频转码demo可参考：[视频转码开发指导](../../../media/media/using-avtranscoder-for-transcodering.md)

> **说明：**&gt;
> - 本Interface首批接口从API version 12开始支持。

**起始版本：** 23

<!--Device-unnamed-interface AVTranscoder--><!--Device-unnamed-interface AVTranscoder-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## addWatermark

```TypeScript
addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>
```

为视频转码添加水印。使用Promise异步回调。 应用最多可以添加5个水印。 此接口只能在prepared状态之前调用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVTranscoder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>--><!--Device-AVTranscoder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| watermark | image.PixelMap | 是 | : 水印图像。 |
| config | [WatermarkConfiguration](arkts-media-multimedia-media-watermarkconfiguration-i.md) | 是 | : 水印配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;int&gt; | Promise对象，返回添加的水印ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) | The parameter check failed, parameter value out of range. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

let watermark: image.PixelMap | undefined = undefined; // 通过image.createImageSource创建ImageSource对象后调用createPixelMap接口（@kit.ImageKit）获取PixelMap。水印图像不能为空。
let watermarkConfig: media.WatermarkConfiguration = { top: 100, left: 100, width: 100, height: 100 };

if (watermark) {
    avRecorder.addWatermark(watermark, watermarkConfig).then((num: number) => {
      console.info(`Succeeded in adding watermark, watermarkNum is ${num}`);
    })
    .catch((error: BusinessError) => {
      console.error(`Failed to add watermark and catch error is: Code: ${error.code}, message: ${error.message}`);
    });
}
```

ArkTS-Sta示例：

```TypeScript
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

let watermark: image.PixelMap | undefined = undefined; // 可以通过获取本地资源文件并转换为PixelMap，水印图像不能为空。
let watermarkConfig: media.WatermarkConfiguration = { top: 100, left: 100, width: 100, height: 100 };

if (watermark) {
    avRecorder.addWatermark(watermark, watermarkConfig).then((num: int) => {
      console.info(`Succeeded in adding watermark, watermarkNum is ${num}`);
    })
    .catch((error: Error) => {
      console.error(`Failed to add watermark and catch error is: Code: ${error.code}, message: ${error.message}`);
    });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

async function testAddWaterMark() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  let watermark: image.PixelMap | undefined = undefined; // 可以通过获取本地资源文件并转换为PixelMap，水印图像不能为空。
  let watermarkConfig: media.WatermarkConfiguration = { top: 100, left: 100, width: 100, height: 100 };

  if (watermark && avScreenCaptureRecorder) {
    avScreenCaptureRecorder.addWatermark(watermark, watermarkConfig).then((num: number) => {
      console.info(`Succeeded in adding watermark, watermarkNum is ${num}`);
    })
    .catch((error: BusinessError) => {
      console.error(`Failed to add watermark and catch error is: Code: ${error.code}, message: ${error.message}`);
    });
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

async function testAddWaterMark() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  let watermark: image.PixelMap | undefined = undefined; // 可以通过获取本地资源文件并转换为PixelMap，水印图像不能为空。
  let watermarkConfig: media.WatermarkConfiguration = { top: 100, left: 100, width: 100, height: 100 };

  if (watermark && avScreenCaptureRecorder) {
      avScreenCaptureRecorder.addWatermark(watermark, watermarkConfig).then((num: int) => {
        console.info(`Succeeded in adding watermark, watermarkNum is ${num}`);
      })
      .catch((error: Error) => {
        console.error(`Failed to add watermark and catch error is: Code: ${error.code}, message: ${error.message}`);
      });
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { image } from '@kit.ImageKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  
  // 配置水印参数。
  let watermarkConfig: media.WatermarkConfiguration = {
      // 根据实际需求配置水印参数，单位为像素（px）。
      top : 40,
      left : 40,
      width: 200,
      height: 300,
  };

  avTranscoder.addWatermark(watermarkPixelMap, watermarkConfig).then((watermarkId: number) => {
    console.info('addWatermark success, watermarkId: ' + watermarkId);
  }).catch((err: BusinessError) => {
    console.error('addWatermark failed and catch error is ' + err.message);
  });
}
```

## cancel

```TypeScript
cancel(): Promise<void>
```

取消视频转码。使用Promise异步回调。需要在prepare()、start()、 pause()或resume()事件成功触发后，才能调用cancel方法。

**起始版本：** 23

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-cancel(): Promise<void>--><!--Device-AVTranscoder-cancel(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.cancel().then(() => {
    console.info('cancel AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('cancel AVTranscoder failed and catch error is ' + err.message);
  });
}
```

## off('complete')

```TypeScript
off(type:'complete', callback?: Callback<void>):void
```

取消注册转码完成事件。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-off(type:'complete', callback?: Callback<void>):void--><!--Device-AVTranscoder-off(type:'complete', callback?: Callback<void>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'complete' | 是 | 转码完成事件回调类型，支持的事件：'complete'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 | 完成事件回调方法。 |

## off('error')

```TypeScript
off(type:'error', callback?: ErrorCallback):void
```

取消注册转码错误事件，取消后不再接收到AVTranscoder的错误事件。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-off(type:'error', callback?: ErrorCallback):void--><!--Device-AVTranscoder-off(type:'error', callback?: ErrorCallback):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'error' | 是 | 转码错误事件回调类型'error'。 <br>- 'error'：转码过程中发生错误，触发该事件。 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 | 错误事件回调方法。 |

## off('progressUpdate')

```TypeScript
off(type:'progressUpdate', callback?: Callback<int>):void
```

取消注册转码进度更新事件。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-off(type:'progressUpdate', callback?: Callback<int>):void--><!--Device-AVTranscoder-off(type:'progressUpdate', callback?: Callback<int>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'progressUpdate' | 是 | 进度更新事件回调类型，支持的事件：'progressUpdate'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 | 已注册的进度更新事件回调。由于当前回调注册时，仅会保留最后一次注册的回调，建议此参数缺省。 |

## offComplete

```TypeScript
offComplete(callback?: Callback<void>):void
```

Unsubscribes from the event indicating that transcoding is complete. This event can be triggered by both user operations and the system.

**起始版本：** 23

<!--Device-AVTranscoder-offComplete(callback?: Callback<void>):void--><!--Device-AVTranscoder-offComplete(callback?: Callback<void>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 | Callback that has been registered to listen for transcoding completion events. |

**示例**

```TypeScript
avTranscoder.offComplete();
```

## offError

```TypeScript
offError(callback?: ErrorCallback):void
```

Unsubscribes from AVTranscoder errors. After the unsubscription, your application can no longer receive AVTranscoder errors. This event is triggered when an error occurs during transcoding.

**起始版本：** 23

<!--Device-AVTranscoder-offError(callback?: ErrorCallback):void--><!--Device-AVTranscoder-offError(callback?: ErrorCallback):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 | Callback that has been registered to listen for AVTranscoder errors. |

**示例**

```TypeScript
avPlayer.offError();
```

```TypeScript
avRecorder.offError();
```

```TypeScript
avScreenCaptureRecorder.offError();
```

```TypeScript
avTranscoder.offError();
```

## offProgressUpdate

```TypeScript
offProgressUpdate(callback?: Callback<int>):void
```

Unsubscribes from transcoding progress updates. This event can be triggered by both user operations and the system.

**起始版本：** 23

<!--Device-AVTranscoder-offProgressUpdate(callback?: Callback<int>):void--><!--Device-AVTranscoder-offProgressUpdate(callback?: Callback<int>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 | Called that has been registered to listen for progress updates. You are advised to use the default value because only the last registered callback is retained in the current allback mechanism. |

**示例**

```TypeScript
avTranscoder.offProgressUpdate();
```

## on('complete')

```TypeScript
on(type:'complete', callback: Callback<void>):void
```

注册转码完成事件，并通过注册的回调方法通知开发者。开发者只能注册一个进度更新事件的回调方法，当开发者重复注册时，以最后一次注册的回调接口为准。使用callback异步回调。当AVTranscoder上报complete事件时，当前转码操作已完成，开发者需要通过release()退出转码操作。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-on(type:'complete', callback: Callback<void>):void--><!--Device-AVTranscoder-on(type:'complete', callback: Callback<void>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'complete' | 是 | 完成事件回调类型，支持的事件：'complete'，在转码过程中系统会自动触发此事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | 回调函数，返回完成事件回调方法。 |

## on('error')

```TypeScript
on(type:'error', callback: ErrorCallback):void
```

注册AVTranscoder的错误事件，该事件仅用于错误提示。如果AVTranscoder上报error事件，开发者需要通过release()退出转码操作 。使用callback异步回调。开发者只能订阅一个错误事件的回调方法，当开发者重复订阅时，以最后一次订阅的回调接口为准。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-on(type:'error', callback: ErrorCallback):void--><!--Device-AVTranscoder-on(type:'error', callback: ErrorCallback):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'error' | 是 | 转码错误事件回调类型'error'。 <br>- 'error'：录制过程中发生错误，触发该事件。 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | 转码错误事件回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The parameter check failed. |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |
| [5400101](../errorcode-media.md#5400101-内存分配失败) | No memory. |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | I/O error. |
| [5400104](../errorcode-media.md#5400104-操作超时) | Time out. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. |
| [5400106](../errorcode-media.md#5400106-不支持的规格) | Unsupported format. |

## on('progressUpdate')

```TypeScript
on(type:'progressUpdate', callback: Callback<int>):void
```

注册转码进度更新事件，并通过注册的回调方法通知开发者。开发者只能注册一个进度更新事件的回调方法，当开发者重复注册时，以最后一次注册的回调接口为准。使用callback异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-on(type:'progressUpdate', callback: Callback<int>):void--><!--Device-AVTranscoder-on(type:'progressUpdate', callback: Callback<int>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'progressUpdate' | 是 | 进度更新事件回调类型，支持的事件：'progressUpdate'，在转码过程中系统会自动触发此事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 | 回调函数，返回进度更新事件，函数中的参数number，表示当前转码进度。 |

## onComplete

```TypeScript
onComplete(callback: Callback<void>):void
```

Subscribes to the event indicating that transcoding is complete. An application can subscribe to only one transcoding completion event. When the application initiates multiple subscriptions to this event, the last subscription is applied.When this event is reported, the current transcoding operation is complete. You need to call [release()](#release) to exit the transcoding.

**起始版本：** 23

<!--Device-AVTranscoder-onComplete(callback: Callback<void>):void--><!--Device-AVTranscoder-onComplete(callback: Callback<void>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | Callback that has been registered to listen for transcoding completion events. |

**示例**

```TypeScript
avTranscoder.onComplete(async () => {
  console.info('avTranscoder complete');
  // 开发者须在此监听转码完成事件。
  // 须等待avTranscoder.release()之后，再对转码后的文件进行转发、上传、转存等处理。
  await avTranscoder.release();
  avTranscoder = undefined;
});
```

## onError

```TypeScript
onError(callback: ErrorCallback):void
```

Subscribes to AVTranscoder errors. If this event is reported, call [release()](#release) to exit the transcoding.An application can subscribe to only one AVTranscoder error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**起始版本：** 23

<!--Device-AVTranscoder-onError(callback: ErrorCallback):void--><!--Device-AVTranscoder-onError(callback: ErrorCallback):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | Callback invoked when the event is triggered. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The parameter check failed. |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |
| [5400101](../errorcode-media.md#5400101-内存分配失败) | No memory. |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | I/O error. |
| [5400104](../errorcode-media.md#5400104-操作超时) | Time out. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. |
| [5400106](../errorcode-media.md#5400106-不支持的规格) | Unsupported format. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.onError((err: BusinessError) => {
  console.info('case avRecorder.onError(error) called, errMessage is ' + err.message);
});
```

```TypeScript
avScreenCaptureRecorder.onError((err: BusinessError) => {
    console.error('avScreenCaptureRecorder error:' + err.message);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avTranscoder.onError((err: BusinessError) => {
  console.info('case avTranscoder.on(error) called, errMessage is ' + err.message);
});
```

## onProgressUpdate

```TypeScript
onProgressUpdate(callback: Callback<int>):void
```

Subscribes to transcoding progress updates. An application can subscribe to only one transcoding progress update event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**起始版本：** 23

<!--Device-AVTranscoder-onProgressUpdate(callback: Callback<int>):void--><!--Device-AVTranscoder-onProgressUpdate(callback: Callback<int>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 | Callback invoked when the event is triggered. **progress** is a number that indicates the current transcoding progress, in percentage. |

**示例**

```TypeScript
avTranscoder.onProgressUpdate((progress: number) => {
  console.info('avTranscoder progressUpdate = ' + progress);
});
```

## pause

```TypeScript
pause(): Promise<void>
```

暂停视频转码。使用Promise异步回调。需要start()事件成功触发后，才能调用pause方法，可以通过调用resume()接 口来恢复转码。

**起始版本：** 23

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-pause(): Promise<void>--><!--Device-AVTranscoder-pause(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.pause((err: BusinessError) => {
  if (err == null) {
    console.info('pause videorecorder success');
  } else {
    console.error('pause videorecorder failed and error is ' + err.message);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.pause().then(() => {
  console.info('pause videorecorder success');
}).catch((err: BusinessError) => {
  console.error('pause videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioPlayer.on('pause', () => {    // 设置'pause'事件回调。
  console.info('audio pause called');
});
audioPlayer.pause();
```

```TypeScript
audioRecorder.on('pause', () => {    // 设置'pause'事件回调。
  console.info('audio recorder pause called');
});
audioRecorder.pause();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至playing状态后才能调用。
  avPlayer.pause((err: BusinessError) => {
    if (err) {
      console.error(`Failed to pause.Code:${err.code},message:${err.message}`);
    } else {
      console.info('Succeeded in pausing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至playing状态后才能调用。
  avPlayer.pause().then(() => {
    console.info('Succeeded in pausing');
  }, (err: BusinessError) => {
    console.error(`Failed to pause.Code:${err.code},message:${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.pause((err: BusinessError) => {
  if (err) {
    console.error(`Failed to pause AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in pausing');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to pause AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.pause().then(() => {
    console.info('pause AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('pause AVTranscoder failed and catch error is ' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause((err: BusinessError) => {
  if (err) {
    console.error('Failed to pause!');
  } else {
    console.info('Succeeded in pausing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## prepare

```TypeScript
prepare(config: AVTranscoderConfig): Promise<void>
```

进行视频转码的参数设置。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-prepare(config: AVTranscoderConfig): Promise<void>--><!--Device-AVTranscoder-prepare(config: AVTranscoderConfig): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [AVTranscoderConfig](arkts-media-multimedia-media-avtranscoderconfig-i.md) | 是 | 配置视频转码的相关参数。 <!--RP1--><!--RP1End--> |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |
| [5400106](../errorcode-media.md#5400106-不支持的规格) | Unsupported format. Returned by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 配置参数以实际硬件设备支持的范围为准。
let videoProfile: media.VideoRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
}

let videoConfig: media.VideoRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : videoProfile,
  url : 'fd://xx', // 文件需先由调用者创建，并给予适当的权限。
  rotation : 0,
  location : { latitude : 30, longitude : 130 }
}

// asyncallback.
videoRecorder.prepare(videoConfig, (err: BusinessError) => {
  if (err == null) {
    console.info('prepare success');
  } else {
    console.error('prepare failed and error is ' + err.message);
  }
})
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 配置参数以实际硬件设备支持的范围为准。
let videoProfile: media.VideoRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
}

let videoConfig: media.VideoRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : videoProfile,
  url : 'fd://xx', // 文件需先由调用者创建，并给予适当的权限。
  rotation : 0,
  location : { latitude : 30, longitude : 130 }
}

// promise.
videoRecorder.prepare(videoConfig).then(() => {
  console.info('prepare success');
}).catch((err: BusinessError) => {
  console.error('prepare failed and catch error is ' + err.message);
});
```

```TypeScript
let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://1',       // fd通过fs.open()获取。文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130},
};
audioRecorder.on('prepare', () => {    // 设置'prepare'事件回调。
  console.info('prepare called');
});
audioRecorder.prepare(audioRecorderConfig);
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
  avPlayer.prepare((err: BusinessError) => {
    if (err) {
      console.error(`Failed to prepare.Code:${err.code},message:${err.message}`);
    } else {
      console.info('Succeeded in preparing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
  avPlayer.prepare().then(() => {
    console.info('Succeeded in preparing');
  }, (err: BusinessError) => {
    console.error(`Failed to prepare.Code:${err.code},message:${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 配置参数以实际硬件设备支持的范围为准。
let avRecorderProfile: media.AVRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
};
let videoMetaData: media.AVMetadata = {
  videoOrientation: '0' // 合理值0、90、180、270，非合理值prepare接口报错。
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : avRecorderProfile,
  url : 'fd://', // 文件需先通过fs.open接口（@kit.FileKit）打开获取文件描述符fd，赋予读写权限，将fd传给此参数，详见文件管理开发指导。
  metadata: videoMetaData,
  location : { latitude : 30, longitude : 130 }
};

avRecorder.prepare(avRecorderConfig, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to prepare and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in preparing');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 配置参数以实际硬件设备支持的范围为准。
let avRecorderProfile: media.AVRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
};
let videoMetaData: media.AVMetadata = {
  videoOrientation: '0' // 合理值0、90、180、270，非合理值prepare接口报错。
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : avRecorderProfile,
  url : 'fd://',  // 文件需先通过fileIo.open接口（@kit.CoreFileKit）打开获取文件描述符fd，赋予读写权限，将fd传给此参数。
  metadata : videoMetaData,
  location : { latitude : 30, longitude : 130 }
};

avRecorder.prepare(avRecorderConfig).then(() => {
  console.info('Succeeded in preparing');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to prepare and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  // 配置参数以实际硬件设备支持的范围为准。
  let avTranscoderConfig: media.AVTranscoderConfig = {
    audioBitrate : 200000,
    audioCodec : media.CodecMimeType.AUDIO_AAC,
    fileFormat : media.ContainerFormatType.CFT_MPEG_4,
    videoBitrate : 3000000,
    videoCodec : media.CodecMimeType.VIDEO_AVC,
  };

  avTranscoder.prepare(avTranscoderConfig).then(() => {
    console.info('prepare success');
  }).catch((err: BusinessError) => {
    console.error('prepare failed and catch error is ' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare((err: BusinessError) => {
  if (err) {
    console.error('Failed to prepare!');
  } else {
    console.info('Succeeded in preparing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare().then(() => {
  console.info('Succeeded in preparing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## release

```TypeScript
release(): Promise<void>
```

释放视频转码资源。使用Promise异步回调。释放视频转码资源之后，该AVTranscoder实例不能再进行任何操作。

**起始版本：** 23

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-release(): Promise<void>--><!--Device-AVTranscoder-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.release((err: BusinessError) => {
  if (err == null) {
    console.info('release videorecorder success');
  } else {
    console.error('release videorecorder failed and error is ' + err.message);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.release().then(() => {
  console.info('release videorecorder success');
}).catch((err: BusinessError) => {
  console.error('release videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioPlayer.release();
audioPlayer = undefined;
```

```TypeScript
audioRecorder.on('release', () => {    // 设置'release'事件回调。
  console.info('audio recorder release called');
});
audioRecorder.release();
audioRecorder = undefined;
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;

// 释放资源。
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.release((error: BusinessError) => {
      if (error) {
        console.error(`Failed to release, code: ${error.code}, message: ${error.message}`);
        return;
      }
      console.info(`Succeeded in releasing`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, code: ${err.code}, message: ${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;

// 释放资源。
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.release().then(() => {
      console.info(`Succeeded in releasing.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to release, code: ${error.code}, message: ${error.message}`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, code: ${err.code}, message: ${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建AVMetadataExtractor对象。
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release((error: BusinessError) => {
    if (error) {
      console.error(`Failed to release, code: ${error.code} message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in releasing.`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建AVMetadataExtractor对象。
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  if (avMetadataExtractor) {
    avMetadataExtractor.release().then(() => {
      console.info(`Succeeded in releasing.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to release, code: ${error.code} message: ${error.message}`);
    });
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发除released以外的状态才能调用。
  avPlayer.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release.Code:${err.code},message:${err.message}`);
    } else {
      console.info('Succeeded in releasing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发除released以外的状态才能调用。
  avPlayer.release().then(() => {
    console.info('Succeeded in releasing');
  }, (err: BusinessError) => {
    console.error(`Failed to release.Code:${err.code},message:${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release((err: BusinessError) => {
  if (err) {
    console.error(`Failed to release AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in releasing AVRecorder');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release().then(() => {
  console.info('Succeeded in releasing AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to release AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function testRelease() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用release方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.release().then(() => {
      console.info('Succeeded in releasing avScreenCaptureRecorder');
    }).catch((err: BusinessError) => {
      console.error(`Failed to release avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.release().then(() => {
    console.info('release AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('release AVTranscoder failed and catch error is ' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release((err: BusinessError) => {
  if (err) {
    console.error('Failed to release!');
  } else {
    console.info('Succeeded in releasing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release().then(() => {
  console.info('Succeeded in releasing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## resume

```TypeScript
resume(): Promise<void>
```

恢复视频转码。使用Promise异步回调。需要在pause()事件成功触发后，才能调用resume方法。

**起始版本：** 23

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-resume(): Promise<void>--><!--Device-AVTranscoder-resume(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.resume((err: BusinessError) => {
  if (err == null) {
    console.info('resume videorecorder success');
  } else {
    console.error('resume videorecorder failed and error is ' + err.message);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.resume().then(() => {
  console.info('resume videorecorder success');
}).catch((err: BusinessError) => {
  console.error('resume videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioRecorder.on('resume', () => {    // 设置'resume'事件回调。
  console.info('audio recorder resume called');
});
audioRecorder.resume();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.resume((err: BusinessError) => {
  if (err) {
    console.error(`Failed to resume AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in resuming AVRecorder');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.resume().then(() => {
  console.info('Succeeded in resuming AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to resume AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.resume().then(() => {
    console.info('resume AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('resume AVTranscoder failed and catch error is ' + err.message);
  });
}
```

## start

```TypeScript
start(): Promise<void>
```

开始视频转码。使用Promise异步回调。需要prepare()事件成功触发后，才能调用start方法。

**起始版本：** 23

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-start(): Promise<void>--><!--Device-AVTranscoder-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.start((err: BusinessError) => {
  if (err == null) {
    console.info('start videorecorder success');
  } else {
    console.error('start videorecorder failed and error is ' + err.message);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.start().then(() => {
  console.info('start videorecorder success');
}).catch((err: BusinessError) => {
  console.error('start videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioRecorder.on('start', () => {    // 设置'start'事件回调。
  console.info('audio recorder start called');
});
audioRecorder.start();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.start((err: BusinessError) => {
  if (err) {
    console.error(`Failed to start AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in starting AVRecorder');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.start().then(() => {
  console.info('Succeeded in starting AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to start AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.start().then(() => {
    console.info('start AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('start AVTranscoder failed and catch error is ' + err.message);
  });
}
```

## fdDst

```TypeScript
fdDst: int
```

目标媒体文件描述，通过该属性设置数据输出。在创建AVTranscoder实例后，必须设置fdSrc和fdDst属性。  
**说明：**
- 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator /AVTranscoder。 - 同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。

**类型：** int

**起始版本：** 23

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-fdDst: int--><!--Device-AVTranscoder-fdDst: int-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

源媒体文件描述，通过该属性设置数据源。  
**使用示例**：假设一个连续存储的媒体文件，地址偏移：0，字节长度：100。其文件描述为AVFileDescriptor{ fd = 资源句柄; offset = 0; length = 100; }。  
**说明：**
- 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator /AVTranscoder。 - 同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。

**类型：** [AVFileDescriptor](arkts-media-multimedia-media-avfiledescriptor-i.md)

**起始版本：** 23

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-fdSrc: AVFileDescriptor--><!--Device-AVTranscoder-fdSrc: AVFileDescriptor-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

