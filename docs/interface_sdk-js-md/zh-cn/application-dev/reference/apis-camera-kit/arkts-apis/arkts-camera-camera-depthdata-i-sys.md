# DepthData（系统接口）

Describes a depth data object.

**起始版本：** 23

<!--Device-camera-interface DepthData--><!--Device-camera-interface DepthData-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { camera } from '@kit.CameraKit';
```

## release

```TypeScript
release(): Promise<void>
```

Releases depth data output resources. This API uses a promise to return the result.

**起始版本：** 23

<!--Device-DepthData-release(): Promise<void>--><!--Device-DepthData-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not System Application. |

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

## dataAccuracy

```TypeScript
readonly dataAccuracy: DepthDataAccuracy
```

Accuracy of the depth data, which can be either relative accuracy or absolute accuracy.

**类型：** [DepthDataAccuracy](arkts-camera-camera-depthdataaccuracy-e-sys.md)

**起始版本：** 23

<!--Device-DepthData-readonly dataAccuracy: DepthDataAccuracy--><!--Device-DepthData-readonly dataAccuracy: DepthDataAccuracy-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## depthMap

```TypeScript
readonly depthMap: image.PixelMap
```

Depth map.

**类型：** image.PixelMap

**起始版本：** 23

<!--Device-DepthData-readonly depthMap: image.PixelMap--><!--Device-DepthData-readonly depthMap: image.PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## format

```TypeScript
readonly format: CameraFormat
```

Camera output format.

**类型：** [CameraFormat](arkts-camera-camera-cameraformat-e.md)

**起始版本：** 23

<!--Device-DepthData-readonly format: CameraFormat--><!--Device-DepthData-readonly format: CameraFormat-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## qualityLevel

```TypeScript
readonly qualityLevel: DepthDataQualityLevel
```

Quality level of the depth map.

**类型：** [DepthDataQualityLevel](arkts-camera-camera-depthdataqualitylevel-e-sys.md)

**起始版本：** 23

<!--Device-DepthData-readonly qualityLevel: DepthDataQualityLevel--><!--Device-DepthData-readonly qualityLevel: DepthDataQualityLevel-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

