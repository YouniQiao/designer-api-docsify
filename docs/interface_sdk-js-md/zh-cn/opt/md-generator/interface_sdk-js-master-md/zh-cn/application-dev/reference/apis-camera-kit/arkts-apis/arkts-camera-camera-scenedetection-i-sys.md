# SceneDetection（系统接口）

Provides the scene detection capability. It inherits from [SceneDetectionQuery](arkts-camera-camera-scenedetectionquery-i-sys.md#SceneDetectionQuery).

**继承/实现关系：** SceneDetection extends [SceneDetectionQuery](arkts-camera-camera-scenedetectionquery-i-sys.md#SceneDetectionQuery)

**起始版本：** 12

<!--Device-camera-interface SceneDetection extends SceneDetectionQuery--><!--Device-camera-interface SceneDetection extends SceneDetectionQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## enableSceneFeature

```TypeScript
enableSceneFeature(type: SceneFeatureType, enabled: boolean): void
```

Enables or disables a scene feature. This API must be called after  
[SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md#SceneFeatureDetectionResult) of the corresponding scene feature is received.

**起始版本：** 12

<!--Device-SceneDetection-enableSceneFeature(type: SceneFeatureType, enabled: boolean): void--><!--Device-SceneDetection-enableSceneFeature(type: SceneFeatureType, enabled: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | 是 |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-无效入参) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function enableSceneFeature(photoSession: camera.PhotoSessionForSys, cameraInput: camera.CameraInput, previewOutput: camera.PreviewOutput): void {
  photoSession.beginConfig();
  photoSession.addInput(cameraInput);
  photoSession.addOutput(previewOutput);
  photoSession.commitConfig();

  photoSession.on('featureDetection', camera.SceneFeatureType.MOON_CAPTURE_BOOST,
    (err: BusinessError, statusObject: camera.SceneFeatureDetectionResult) => {
      if (err !== undefined && err.code !== 0) {
        console.error(`Callback Error, errorCode: ${err.code}`);
        return;
      }
      console.info(
        `on featureDetectionStatus featureType:${statusObject.featureType} detected:${statusObject.detected}`);
      if (statusObject.featureType === camera.SceneFeatureType.MOON_CAPTURE_BOOST) {
        try {
          photoSession.enableSceneFeature(statusObject.featureType, statusObject.detected);
        } catch (error) {
          let err = error as BusinessError;
          console.error(`The enableSceneFeature call failed. error code: ${err.code}`);
        }
      }
    });
}
```
