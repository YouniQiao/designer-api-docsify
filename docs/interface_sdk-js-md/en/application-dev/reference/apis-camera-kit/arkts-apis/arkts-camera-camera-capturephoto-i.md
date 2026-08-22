# CapturePhoto

*CapturePhoto** provides APIs for obtaining the objects of the full-quality image and the uncompressed image.

**Since:** 23

<!--Device-camera-interface CapturePhoto--><!--Device-camera-interface CapturePhoto-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

## release

```TypeScript
release(): Promise<void>
```

Releases output resources. This API uses a promise to return the result. Model constraint: This API can be used only in the stage model.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CapturePhoto-release(): Promise<void>--><!--Device-CapturePhoto-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

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

Object of the full-quality image and the uncompressed image.

**Type:** [ImageType](arkts-camera-camera-imagetype-t.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CapturePhoto-main: ImageType--><!--Device-CapturePhoto-main: ImageType-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

