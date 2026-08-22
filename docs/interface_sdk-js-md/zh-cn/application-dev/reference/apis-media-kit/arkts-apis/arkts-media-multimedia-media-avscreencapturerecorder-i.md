# AVScreenCaptureRecorder

屏幕录制管理类，用于进行屏幕录制。在调用AVScreenCaptureRecorder的方法前，需要先通过 [createAVScreenCaptureRecorder()](arkts-media-media-createavscreencapturerecorder-f.md)创建一个 AVScreenCaptureRecorder实例。

> **说明：**
> 
> - 本Interface首批接口从API version 12开始支持。

**起始版本：** 23

<!--Device-unnamed-interface AVScreenCaptureRecorder--><!--Device-unnamed-interface AVScreenCaptureRecorder-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## excludePickerWindows

```TypeScript
excludePickerWindows(excludedWindows: Array<int>): Promise<void>
```

设置在Picker中隐藏的窗口列表，在下一次显示Picker时生效。使用Promise异步回调。

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-excludePickerWindows(excludedWindows: Array<int>): Promise<void>--><!--Device-AVScreenCaptureRecorder-excludePickerWindows(excludedWindows: Array<int>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| excludedWindows | Array&lt;int&gt; | 是 | 需要在Picker中隐藏的窗口列表，窗口属性获取方法可以参考 [getWindowProperties](../../../reference/apis-arkui/arkts-apis-window-Window.md#getwindowproperties9)。 |

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

async function testExcludePickerWindows() {
  let excludedWindows: number[] = [101, 102, 103];
  
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用excludePickerWindows方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.excludePickerWindows(excludedWindows).then(() => {
      console.info('Succeeded in excluding picker windows.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to exclude picker windows. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## init

```TypeScript
init(config: AVScreenCaptureRecordConfig): Promise<void>
```

进行录屏初始化，设置录屏参数。使用Promise异步回调。

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-init(config: AVScreenCaptureRecordConfig): Promise<void>--><!--Device-AVScreenCaptureRecorder-init(config: AVScreenCaptureRecordConfig): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [AVScreenCaptureRecordConfig](arkts-media-multimedia-media-avscreencapturerecordconfig-i.md) | 是 | 配置屏幕录制的相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3. Parameter verification failed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { fileIo } from '@kit.CoreFileKit';

async function testInit() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 创建文件。
  let filesDir = '/data/storage/el2/base/haps';
  let file = fileIo.openSync(filesDir + '/screenCapture.mp4', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);

  let avCaptureConfig: media.AVScreenCaptureRecordConfig = {
      fd: file.fd, // 文件需要先由调用者创建，通常是MP4文件，赋予写权限，将文件fd传给此参数。
      frameWidth: 640,
      frameHeight: 480
      // 补充其他参数。
  };

  // 调用init方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.init(avCaptureConfig).then(() => {
      console.info('Succeeded in initializing avScreenCaptureRecorder');
    }).catch((err: BusinessError) => {
      console.error(`Failed to init avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅错误回调事件。用户可以指定填入错误回调方法来取消订阅。

**起始版本：** 12

<!--Device-AVScreenCaptureRecorder-off(type: 'error', callback?: ErrorCallback): void--><!--Device-AVScreenCaptureRecorder-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'error' | 是 | 状态切换事件回调类型，支持的事件：'error'。 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 | 录屏错误事件回调方法，不填此参数则会取消最后一次订阅事件。 |

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: Callback<AVScreenCaptureStateCode>): void
```

取消订阅状态切换回调事件。用户可以指定填入状态切换的回调方法来取消订阅。

**起始版本：** 12

<!--Device-AVScreenCaptureRecorder-off(type: 'stateChange', callback?: Callback<AVScreenCaptureStateCode>): void--><!--Device-AVScreenCaptureRecorder-off(type: 'stateChange', callback?: Callback<AVScreenCaptureStateCode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'stateChange' | 是 | 状态切换事件回调类型，支持的事件：'stateChange'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVScreenCaptureStateCode](arkts-media-multimedia-media-avscreencapturestatecode-e.md)&gt; | 否 | 状态切换事件回调方法， AVScreenCaptureStateCode表示切换到的状态，不填此参数则会取消最后一次 订阅事件。 |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from AVScreenCaptureRecorder errors. You can specify a callback to cancel the specified subscription.

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-offError(callback?: ErrorCallback): void--><!--Device-AVScreenCaptureRecorder-offError(callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 | Callback used for unsubscription. If this parameter is not specified, the last subscription is canceled. |

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

## offStateChange

```TypeScript
offStateChange(callback?: Callback<AVScreenCaptureStateCode>): void
```

Unsubscribes from screen capture state changes. You can specify a callback to cancel the specified subscription.

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-offStateChange(callback?: Callback<AVScreenCaptureStateCode>): void--><!--Device-AVScreenCaptureRecorder-offStateChange(callback?: Callback<AVScreenCaptureStateCode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVScreenCaptureStateCode](arkts-media-multimedia-media-avscreencapturestatecode-e.md)&gt; | 否 | Callback used for unsubscription. AVScreenCaptureStateCode indicates the new state. If this parameter is not specified, the last subscription is canceled. |

**示例**

```TypeScript
avRecorder.offStateChange();
```

```TypeScript
avScreenCaptureRecorder.offStateChange();
```

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅AVScreenCaptureRecorder的错误事件，用户可以根据应用自身逻辑对错误事件进行处理。用户只能订阅一个错误事件的回调方法，重复订阅时，以最后一次订阅的回调接口为准。

**起始版本：** 12

<!--Device-AVScreenCaptureRecorder-on(type: 'error', callback: ErrorCallback): void--><!--Device-AVScreenCaptureRecorder-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'error' | 是 | 错误事件回调类型，支持的事件：'error'。 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | 录屏错误事件回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | permission denied. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by ErrorCallback. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by ErrorCallback. |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: Callback<AVScreenCaptureStateCode>): void
```

订阅录屏状态切换的事件，当状态发生的时候，会通过订阅的回调通知用户。用户只能订阅一个状态切换的回调方法，重复订阅时，以最后一次订阅的回调接口为准。

**起始版本：** 12

<!--Device-AVScreenCaptureRecorder-on(type: 'stateChange', callback: Callback<AVScreenCaptureStateCode>): void--><!--Device-AVScreenCaptureRecorder-on(type: 'stateChange', callback: Callback<AVScreenCaptureStateCode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'stateChange' | 是 | 状态切换事件回调类型，支持的事件：'stateChange'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVScreenCaptureStateCode](arkts-media-multimedia-media-avscreencapturestatecode-e.md)&gt; | 是 | 状态切换事件回调方法， AVScreenCaptureStateCode表示切换到的状态。 |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to AVScreenCaptureRecorder errors. You can handle the errors based on the application logic. An application can subscribe to only one AVScreenCaptureRecorder error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-onError(callback: ErrorCallback): void--><!--Device-AVScreenCaptureRecorder-onError(callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | Callback invoked when the event is triggered. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | permission denied. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by ErrorCallback. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by ErrorCallback. |

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

## onStateChange

```TypeScript
onStateChange(callback: Callback<AVScreenCaptureStateCode>): void
```

Subscribes to screen capture state changes. An application can subscribe to only one screen capture state change event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-onStateChange(callback: Callback<AVScreenCaptureStateCode>): void--><!--Device-AVScreenCaptureRecorder-onStateChange(callback: Callback<AVScreenCaptureStateCode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVScreenCaptureStateCode](arkts-media-multimedia-media-avscreencapturestatecode-e.md)&gt; | 是 | Callback invoked when the event is triggered. AVScreenCaptureStateCode indicates the new state. |

**示例**

```TypeScript
avRecorder.onStateChange((state: media.AVRecorderState, reason: media.StateChangeReason) => {
  console.info('case state has changed, new state is :' + state + ',and new reason is : ' + reason);
});
```

```TypeScript
avScreenCaptureRecorder.onStateChange((state: media.AVScreenCaptureStateCode) => {
    console.info('avScreenCaptureRecorder stateChange to ' + state);
});
```

## pauseRecording

```TypeScript
pauseRecording(): Promise<void>
```

暂停录屏。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVScreenCaptureRecorder-pauseRecording(): Promise<void>--><!--Device-AVScreenCaptureRecorder-pauseRecording(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not be permitted. Return by promise. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function testPauseRecording() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用pauseRecording方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.pauseRecording().then(() => {
      console.info('Succeeded in pausing avScreenCaptureRecorder');
    }).catch((err: BusinessError) => {
      console.error(`Failed to pause avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## presentPicker

```TypeScript
presentPicker(): Promise<void>
```

录屏开始后，调用该接口再次弹出Picker，可动态更新录制源（窗口、屏幕）。使用Promise异步回调。

> **说明：**
> 
> - 更新录制源过程中，原录制流程不中断。
> 
> - 通过picker动态更新录制源后，按照新的录制源进行录制。

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-presentPicker(): Promise<void>--><!--Device-AVScreenCaptureRecorder-presentPicker(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

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

async function testPresentPicker() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用presentPicker方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.presentPicker().then(() => {
      console.info('Succeeded in presenting picker avScreenCaptureRecorder.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to present picker avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## release

```TypeScript
release(): Promise<void>
```

释放录屏。使用Promise异步回调。

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-release(): Promise<void>--><!--Device-AVScreenCaptureRecorder-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
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

## resumeRecording

```TypeScript
resumeRecording(): Promise<void>
```

恢复录屏。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVScreenCaptureRecorder-resumeRecording(): Promise<void>--><!--Device-AVScreenCaptureRecorder-resumeRecording(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not be permitted. Return by promise. |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function testResumeRecording() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用resumeRecording方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.resumeRecording().then(() => {
      console.info('Succeeded in resuming avScreenCaptureRecorder');
    }).catch((err: BusinessError) => {
      console.error(`Failed to resume avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## setMicEnabled

```TypeScript
setMicEnabled(enable: boolean): Promise<void>
```

设置麦克风开关。使用Promise异步回调。

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-setMicEnabled(enable: boolean): Promise<void>--><!--Device-AVScreenCaptureRecorder-setMicEnabled(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 麦克风开关控制，true代表麦克风打开，false代表麦克风关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function testSetMicEnable() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用setMicEnabled方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.setMicEnabled(true).then(() => {
      console.info('Succeeded in setting microphone enabled.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to set microphone enabled. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## setPickerMode

```TypeScript
setPickerMode(pickerMode: PickerMode): Promise<void>
```

设置Picker显示模式，在下一次显示Picker时生效。使用Promise异步回调。

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-setPickerMode(pickerMode: PickerMode): Promise<void>--><!--Device-AVScreenCaptureRecorder-setPickerMode(pickerMode: PickerMode): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pickerMode | [PickerMode](arkts-media-multimedia-media-pickermode-e.md) | 是 | 选择Picker模式。<br>定义了在Picker中显示的内容类型：<br>- SCREEN_ONLY：仅显示屏幕列表。<br>- WINDOW_ONLY： 仅显示窗口列表。<br>- SCREEN_AND_WINDOW：同时显示屏幕列表和窗口列表（默认值）。 |

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

async function testSetPickerMode() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用setPickerMode方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.setPickerMode(media.PickerMode.WINDOW_ONLY).then(() => {
      console.info('Succeeded in setting picker mode.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to set picker mode. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## skipPrivacyMode

```TypeScript
skipPrivacyMode(windowIDs: Array<int>): Promise<void>
```

录屏时，应用可对本应用的隐私窗口做安全豁免。使用Promise异步回调。

如录屏时，用户在本应用进行输入密码等操作，应用不会进行黑屏处理。

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-skipPrivacyMode(windowIDs: Array<int>): Promise<void>--><!--Device-AVScreenCaptureRecorder-skipPrivacyMode(windowIDs: Array<int>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowIDs | Array&lt;int&gt; | 是 | 需要豁免隐私的窗口列表，包括主窗口id和子窗口id，窗口属性获取方法可以参考 [getWindowProperties](../../../reference/apis-arkui/arkts-apis-window-Window.md#getwindowproperties9)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function testSkipPrivacyMode() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用skipPrivacyMode方法。
  if (avScreenCaptureRecorder) {
    let windowIDs = [];
    avScreenCaptureRecorder.skipPrivacyMode(windowIDs).then(() => {
      console.info('Succeeded in skipping privacy mode');
    }).catch((err: BusinessError) => {
      console.error(`Failed to skip privacy mode. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## startRecording

```TypeScript
startRecording(): Promise<void>
```

开始录屏，在使用前需要先调用init接口。使用Promise异步回调。

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-startRecording(): Promise<void>--><!--Device-AVScreenCaptureRecorder-startRecording(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function testStartRecording() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用startRecording方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.startRecording().then(() => {
      console.info('Succeeded in starting avScreenCaptureRecorder');
    }).catch((err: BusinessError) => {
      console.error(`Failed to start avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## stopRecording

```TypeScript
stopRecording(): Promise<void>
```

结束录屏。使用Promise异步回调。

**起始版本：** 23

<!--Device-AVScreenCaptureRecorder-stopRecording(): Promise<void>--><!--Device-AVScreenCaptureRecorder-stopRecording(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) | Service died. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function testStopRecording() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用stopRecording方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.stopRecording().then(() => {
      console.info('Succeeded in stopping avScreenCaptureRecorder');
    }).catch((err: BusinessError) => {
      console.error(`Failed to stop avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

