# DepthData（系统接口）

Describes a depth data object.

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## release

```TypeScript
release(): Promise<void>
```

Releases depth data output resources. This API uses a promise to return the result.

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## dataAccuracy

```TypeScript
readonly dataAccuracy: DepthDataAccuracy
```

Accuracy of the depth data, which can be either relative accuracy or absolute accuracy.

**类型：** [DepthDataAccuracy](arkts-camera-camera-depthdataaccuracy-e-sys.md)

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## depthMap

```TypeScript
readonly depthMap: image.PixelMap
```

Depth map.

**类型：** image.PixelMap

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## format

```TypeScript
readonly format: CameraFormat
```

Camera output format.

**类型：** [CameraFormat](arkts-camera-camera-cameraformat-e.md)

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## qualityLevel

```TypeScript
readonly qualityLevel: DepthDataQualityLevel
```

Quality level of the depth map.

**类型：** [DepthDataQualityLevel](arkts-camera-camera-depthdataqualitylevel-e-sys.md)

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。
