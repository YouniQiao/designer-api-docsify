# CapturePhoto

获取全质量图和未压缩图的对象。

**起始版本：** 23

<!--Device-camera-interface CapturePhoto--><!--Device-camera-interface CapturePhoto-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## 导入模块

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

## release

```TypeScript
release(): Promise<void>
```

释放输出资源。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-CapturePhoto-release(): Promise<void>--><!--Device-CapturePhoto-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**示例**

```TypeScript
async function releaseDepthData(depthData: camera.DepthData): Promise<void> {
  await depthData.release();
}
```

```TypeScript
async function releaseDeferredPhotoProxy(proxyObj: camera.DeferredPhotoProxy): Promise<void> {
  await proxyObj.release();
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function releasePreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the Preview output instance ${err.code}`);
      return;
    }
    console.info('Callback invoked to indicate that the preview output instance is released successfully.');
  });
}

function releaseVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the video output instance ${err.code}`);
      return;
    }
    console.info('Callback invoked to indicate that the video output instance is released successfully.');
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function releasePreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.release((err: BusinessError | null) => {
    if (err && err!.code !== 0) {
      console.error(`Failed to release the Preview output instance ${err.code}`);
      return;
    }
    console.info('Callback invoked to indicate that the preview output instance is released successfully.');
  });
}

function releaseVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.release((err: BusinessError | null) => {
    if (err && err!.code !== 0) {
      console.error(`Failed to release the video output instance ${err.code}`);
      return;
    }
    console.info('Callback invoked to indicate that the video output instance is released successfully.');
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function releasePreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.release().then(() => {
    console.info('Promise returned to indicate that the preview output instance is released successfully.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to preview output release, error code: ${error.code}`);
  });
}

function releaseVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.release().then(() => {
    console.info('Promise returned to indicate that the video output instance is released successfully.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to video output release, error code: ${error.code}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function releasePreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.release().then(() => {
    console.info('Promise returned to indicate that the preview output instance is released successfully.');
  }).catch((error) => {
    let err = error as BusinessError;
    console.error(`Failed to preview output release, error code: ${err.code}`);
  });
}

function releaseVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.release().then(() => {
    console.info('Promise returned to indicate that the video output instance is released successfully.');
  }).catch((error) => {
    let err = error as BusinessError;
    console.error(`Failed to video output release, error code: ${err.code}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function releaseCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the CaptureSession instance, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate that the CaptureSession instance is released successfully.');
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function releaseCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.release().then(() => {
    console.info('Promise returned to indicate that the CaptureSession instance is released successfully.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to release the CaptureSession instance, error code: ${err.code}.`);
  });
}
```

```TypeScript
async function releasePhoto(photo: camera.Photo): Promise<void> {
  await photo.release();
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function releaseCaptureSession(session: camera.Session): void {
  session.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the session instance, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate that the session instance is released successfully.');
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function releaseCaptureSession(session: camera.Session): void {
  session.release().then(() => {
    console.info('Promise returned to indicate that the session instance is released successfully.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the session instance, error code: ${error.code}.`);
  });
}
```

```TypeScript
import { camera } from '@kit.CameraKit';

async function releaseCapturePhoto(capturePhoto: camera.CapturePhoto): Promise<void> {
  await capturePhoto.release();
}
```

## main

```TypeScript
main: ImageType
```

全质量图和未压缩图的对象。

**类型：** [ImageType](arkts-camera-camera-imagetype-t.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-CapturePhoto-main: ImageType--><!--Device-CapturePhoto-main: ImageType-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

