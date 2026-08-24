# MetadataOutput

metadata流。继承[CameraOutput](arkts-camera-camera-cameraoutput-i.md)。

**继承/实现关系：** MetadataOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md)

**起始版本：** 23

<!--Device-camera-interface MetadataOutput--><!--Device-camera-interface MetadataOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## 导入模块

```TypeScript
import { camera } from '@kit.CameraKit';
```

## isLockMetadataObjectTrackingSupported

```TypeScript
isLockMetadataObjectTrackingSupported(): boolean
```

检查设备是否支持锁定元数据对象（如猫脸、狗脸）追踪功能。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-isLockMetadataObjectTrackingSupported(): boolean--><!--Device-MetadataOutput-isLockMetadataObjectTrackingSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否支持锁定元数据对象追踪功能。true表示支持，false表示不支持。 |

**示例**

```TypeScript
function checkLockMetadataSupport(metadataOutput: camera.MetadataOutput): void {
  let isSupported: boolean = metadataOutput.isLockMetadataObjectTrackingSupported();
  console.info(`Lock metadata object tracking supported: ${isSupported}`);
}
```

## lockMetadataObjectTracking

```TypeScript
lockMetadataObjectTracking(point: Point): void
```

锁定对特定元数据对象（如猫脸、狗脸）的追踪。

> **说明：**&gt;
> - 该功能以point所指向的点所在的对象为追踪对象，如果该点不存在追踪对象，则功能不生效。&gt;
> - 被锁定追踪的对象离开取景范围超过三秒或调用解锁追踪后，锁定追踪自动取消。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-lockMetadataObjectTracking(point: Point): void--><!--Device-MetadataOutput-lockMetadataObjectTracking(point: Point): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 锁定元数据对象追踪的点位。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) | Session not config, only throw in session usage. |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) | Camera service fatal error. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function lockMetadata(metadataOutput: camera.MetadataOutput, point: camera.Point): void {
  try {
    metadataOutput.lockMetadataObjectTracking(point);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`lockMetadataObjectTracking error. error code: ${err.code}`);
  }
}
```

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

注销监听metadata流的错误。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-off(type: 'error', callback?: ErrorCallback): void--><!--Device-MetadataOutput-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'error' | 是 | 监听事件，固定为'error'，metadataOutput创建成功后可监听。 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## off('metadataObjectsAvailable')

```TypeScript
off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void
```

注销监听检测到的metadata对象。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void--><!--Device-MetadataOutput-off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'metadataObjectsAvailable' | 是 | 监听事件，固定为'metadataObjectsAvailable'，metadataOutput创建成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MetadataObject](arkts-camera-camera-metadataobject-i.md)&gt;&gt; | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有 callback。 |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**起始版本：** 23

<!--Device-MetadataOutput-offError(callback?: ErrorCallback): void--><!--Device-MetadataOutput-offError(callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 | Callback used to get the metadata output errors. |

**示例**

```TypeScript
function unregisterCameraInputError(cameraInput: camera.CameraInput, camera: camera.CameraDevice): void {
   cameraInput.offError(camera);
}
```

```TypeScript
function unregisterMetadataOutputError(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.offError();
}
```

## offMetadataObjectsAvailable

```TypeScript
offMetadataObjectsAvailable(callback?: AsyncCallback<Array<MetadataObject>>): void
```

Unsubscribes from metadata objects available event callback.

**起始版本：** 23

<!--Device-MetadataOutput-offMetadataObjectsAvailable(callback?: AsyncCallback<Array<MetadataObject>>): void--><!--Device-MetadataOutput-offMetadataObjectsAvailable(callback?: AsyncCallback<Array<MetadataObject>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MetadataObject](arkts-camera-camera-metadataobject-i.md)&gt;&gt; | 否 | Callback used to get the available metadata objects. |

**示例**

```TypeScript
function unregisterMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.offMetadataObjectsAvailable();
}
```

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听metadata流的错误，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**&gt;
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-on(type: 'error', callback: ErrorCallback): void--><!--Device-MetadataOutput-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'error' | 是 | 监听事件，固定为'error'，metadataOutput创建成功后可监听。metadata接口使用错误时触发该事件并返回对应错误码，比如调用 [start](#start)，[CameraOutput.release](arkts-camera-camera-cameraoutput-i.md#release)接口时发生 错误返回对应错误信息。 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md)。 |

## on('metadataObjectsAvailable')

```TypeScript
on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void
```

监听检测到的metadata对象，通过注册回调函数获取结果。使用callback异步回调。

> **说明：**&gt;
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void--><!--Device-MetadataOutput-on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'metadataObjectsAvailable' | 是 | 监听事件，固定为'metadataObjectsAvailable'，metadataOutput创建成功后可监听。 <br>检测到有效的metadata数据时，触发该事件发生并返回相应的metadata数据。如果输入错误字段，则不会创建有效监听。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MetadataObject](arkts-camera-camera-metadataobject-i.md)&gt;&gt; | 是 | 回调函数，用于获取metadata数据。 |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**起始版本：** 23

<!--Device-MetadataOutput-onError(callback: ErrorCallback): void--><!--Device-MetadataOutput-onError(callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | Callback used to get the metadata output errors. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(`Camera input error code: ${err.code}`);
}

function registerCameraInputError(cameraInput: camera.CameraInput, camera: camera.CameraDevice): void {
   cameraInput.onError(camera, callback);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function callback(metadataOutputError: BusinessError): void {
  console.error(`Metadata output error code: ${metadataOutputError.code}`);
}

function registerMetadataOutputError(metadataOutput: camera.MetadataOutput): void {
   metadataOutput.onError(callback);
}
```

## onMetadataObjectsAvailable

```TypeScript
onMetadataObjectsAvailable(callback: AsyncCallback<Array<MetadataObject>>): void
```

Subscribes to metadata objects available event callback.

**起始版本：** 23

<!--Device-MetadataOutput-onMetadataObjectsAvailable(callback: AsyncCallback<Array<MetadataObject>>): void--><!--Device-MetadataOutput-onMetadataObjectsAvailable(callback: AsyncCallback<Array<MetadataObject>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MetadataObject](arkts-camera-camera-metadataobject-i.md)&gt;&gt; | 是 | Callback used to get the available metadata objects. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError | null, metadataObjectArr: Array<camera.MetadataObject> | undefined): void {
  if (err !== undefined && err!.code !== 0) {
    console.error(`Callback Error, errorCode: ${err!.code}`);
    return;
  }
  console.info('metadata output metadataObjectsAvailable');
}

function registerMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.onMetadataObjectsAvailable(callback);
}
```

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

开始输出metadata，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-start(callback: AsyncCallback<void>): void--><!--Device-MetadataOutput-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当开始输出metadata成功，err为undefined，否则为错误对象。错误码类型 [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md)。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) | Camera service fatal error. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startDepthDataOutput(depthDataOutput: camera.DepthDataOutput): void {
  depthDataOutput.start().then(() => {
    console.info('Promise returned to indicate that start method execution success.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to depth data output start, error code: ${error.code}.`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start the session, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the session start success.');
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.start().then(() => {
    console.info('Promise returned to indicate the session start success.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to start the session, error code: ${err.code}.`);
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start metadata output, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with metadata output started.');
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.start((error:Error | null) => {
    let err = error as BusinessError;
    if (err && err!.code !== 0) {
      console.error(`Failed to start metadata output, error code: ${err!.code}.`);
      return;
    }
    console.info('Callback returned with metadata output started.');
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.start().then(() => {
    console.info('Callback returned with metadata output started.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to metadata output start, error code: ${error.code}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.start().then(() => {
    console.info('Callback returned with metadata output started.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to metadata output stop, error code: ${err.code}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start the preview output, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with preview output started.');
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.start().then(() => {
    console.info('Promise returned with preview output started.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to preview output start, error code: ${error.code}.`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(session: camera.Session): void {
  session.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start the session, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the session start success.');
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(session: camera.Session): void {
  session.start().then(() => {
    console.info('Promise returned to indicate the session start success.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to start the session, error code: ${error.code}.`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.start((err: BusinessError) => {
    if (err.code) {
      console.error(`Failed to start the video output, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the video output start success.');
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function startVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.start().then(() => {
    console.info('Promise returned to indicate that start method execution success.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to video output start, error code: ${error.code}.`);
  });
}
```

## start

```TypeScript
start(): Promise<void>
```

开始输出metadata。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-start(): Promise<void>--><!--Device-MetadataOutput-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) | Camera service fatal error. |

**示例**

参见 [start](#start)

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止输出metadata，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-stop(callback: AsyncCallback<void>): void--><!--Device-MetadataOutput-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当停止输出metadata成功，err为undefined，否则为错误对象。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopDepthDataOutput(depthDataOutput: camera.DepthDataOutput): void {
  depthDataOutput.stop().then(() => {
    console.info('Promise returned to indicate that stop method execution success.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to depth data output stop, error code: ${error.code}.`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the session, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the session stop success.');
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.stop().then(() => {
    console.info('Promise returned to indicate the session stop success.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to stop the session, error code: ${err.code}.`);
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the metadata output, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with metadata output stopped.');
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.stop((error: Error | null) => {
    let err = error as BusinessError;
    if (err && err!.code !== 0) {
      console.error(`Failed to stop the metadata output, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with metadata output stopped.');
  })
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.stop().then(() => {
    console.info('Callback returned with metadata output stopped.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to metadata output stop, error code: ${error.code}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.stop().then(() => {
    console.info('Callback returned with metadata output stopped.');
  }).catch((error) => {
    let err = error as BusinessError;
    console.error(`Failed to metadata output stop, error code: ${err.code}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the preview output, error code: ${err.code}.`);
      return;
    }
    console.info('Returned with preview output stopped.');
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.stop().then(() => {
    console.info('Callback returned with preview output stopped.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to preview output stop, error code: ${error.code}.`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopCaptureSession(session: camera.Session): void {
  session.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the session, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the session stop success.');
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopCaptureSession(session: camera.Session): void {
  session.stop().then(() => {
    console.info('Promise returned to indicate the session stop success.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to stop the session, error code: ${error.code}.`);
  });
}
```

```TypeScript
function stopVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.stop(() => {
    console.info('Callback invoked to indicate the video output stop success.');
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function stopVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.stop().then(() => {
    console.info('Promise returned to indicate that stop method execution success.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to video output stop, error code: ${error.code}.`);
  });
}
```

## stop

```TypeScript
stop(): Promise<void>
```

停止输出metadata。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-stop(): Promise<void>--><!--Device-MetadataOutput-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**示例**

参见 [stop](#stop)

## unlockMetadataObjectTracking

```TypeScript
unlockMetadataObjectTracking(): void
```

解锁元数据对象（如猫脸、狗脸）追踪。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataOutput-unlockMetadataObjectTracking(): void--><!--Device-MetadataOutput-unlockMetadataObjectTracking(): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) | Session not config, only throw in session usage. |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) | Camera service fatal error. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function unlockMetadata(metadataOutput: camera.MetadataOutput): void {
  try {
    metadataOutput.unlockMetadataObjectTracking();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`unlockMetadataObjectTracking error. error code: ${err.code}`);
  }
}
```

