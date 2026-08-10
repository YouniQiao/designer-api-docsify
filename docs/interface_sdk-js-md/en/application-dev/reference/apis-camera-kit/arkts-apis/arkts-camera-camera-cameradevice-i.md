# CameraDevice

相机设备信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-interface CameraDevice--><!--Device-camera-interface CameraDevice-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## automotiveCameraPosition

```TypeScript
readonly automotiveCameraPosition?: AutomotiveCameraPosition
```

Car设备摄像头位置。

**Type:** [AutomotiveCameraPosition](arkts-camera-camera-automotivecameraposition-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CameraDevice-readonly automotiveCameraPosition?: AutomotiveCameraPosition--><!--Device-CameraDevice-readonly automotiveCameraPosition?: AutomotiveCameraPosition-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## cameraId

```TypeScript
readonly cameraId: string
```

相机ID。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraDevice-readonly cameraId: string--><!--Device-CameraDevice-readonly cameraId: string-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## cameraOrientation

```TypeScript
readonly cameraOrientation: int
```

相机安装角度，不会随着屏幕旋转而改变。取值范围为[0, 360]。单位：度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraDevice-readonly cameraOrientation: int--><!--Device-CameraDevice-readonly cameraOrientation: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## cameraPosition

```TypeScript
readonly cameraPosition: CameraPosition
```

相机位置。

**Type:** [CameraPosition](arkts-camera-camera-cameraposition-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraDevice-readonly cameraPosition: CameraPosition--><!--Device-CameraDevice-readonly cameraPosition: CameraPosition-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## cameraType

```TypeScript
readonly cameraType: CameraType
```

相机类型。

**Type:** [CameraType](arkts-camera-camera-cameratype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraDevice-readonly cameraType: CameraType--><!--Device-CameraDevice-readonly cameraType: CameraType-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## connectionType

```TypeScript
readonly connectionType: ConnectionType
```

相机连接类型。

**Type:** [ConnectionType](arkts-camera-camera-connectiontype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraDevice-readonly connectionType: ConnectionType--><!--Device-CameraDevice-readonly connectionType: ConnectionType-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## constituentCameraDevices

```TypeScript
readonly constituentCameraDevices?: Array<CameraDevice>
```

组成此逻辑相机的物理相机列表。

**Type:** Array&lt;[CameraDevice](arkts-camera-camera-cameradevice-i.md)&gt;

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraDevice-readonly constituentCameraDevices?: Array<CameraDevice>--><!--Device-CameraDevice-readonly constituentCameraDevices?: Array<CameraDevice>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## hostDeviceName

```TypeScript
readonly hostDeviceName: string
```

远端设备名称。若当前无远端设备，返回为空。

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraDevice-readonly hostDeviceName: string--><!--Device-CameraDevice-readonly hostDeviceName: string-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## hostDeviceType

```TypeScript
readonly hostDeviceType: HostDeviceType
```

远端设备类型。

**Type:** [HostDeviceType](arkts-camera-camera-hostdevicetype-e.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraDevice-readonly hostDeviceType: HostDeviceType--><!--Device-CameraDevice-readonly hostDeviceType: HostDeviceType-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## isLogicalCamera

```TypeScript
readonly isLogicalCamera?: boolean
```

是否为逻辑摄像头（由多个物理相机组成）, true表示是逻辑摄像头，false表示是物理摄像头。

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraDevice-readonly isLogicalCamera?: boolean--><!--Device-CameraDevice-readonly isLogicalCamera?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## lensDistortion

```TypeScript
readonly lensDistortion?: Array<double>
```

镜头畸变参数数组。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraDevice-readonly lensDistortion?: Array<double>--><!--Device-CameraDevice-readonly lensDistortion?: Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## lensEquivalentFocalLength

```TypeScript
readonly lensEquivalentFocalLength?: Array<int>
```

相机镜头等效焦距。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraDevice-readonly lensEquivalentFocalLength?: Array<int>--><!--Device-CameraDevice-readonly lensEquivalentFocalLength?: Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## lensFocalLength

```TypeScript
readonly lensFocalLength?: double
```

镜头实际焦距。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraDevice-readonly lensFocalLength?: double--><!--Device-CameraDevice-readonly lensFocalLength?: double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## lensIntrinsicCalibration

```TypeScript
readonly lensIntrinsicCalibration?: Array<double>
```

镜头内参标定参数数组。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraDevice-readonly lensIntrinsicCalibration?: Array<double>--><!--Device-CameraDevice-readonly lensIntrinsicCalibration?: Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## minimumFocusDistance

```TypeScript
readonly minimumFocusDistance?: double
```

相机最小对焦距离。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraDevice-readonly minimumFocusDistance?: double--><!--Device-CameraDevice-readonly minimumFocusDistance?: double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## sensorColorFilterArrangement

```TypeScript
readonly sensorColorFilterArrangement?: SensorColorFilterArrangement
```

传感器颜色滤镜排列方式。

**Type:** [SensorColorFilterArrangement](arkts-camera-camera-sensorcolorfilterarrangement-e.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraDevice-readonly sensorColorFilterArrangement?: SensorColorFilterArrangement--><!--Device-CameraDevice-readonly sensorColorFilterArrangement?: SensorColorFilterArrangement-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## sensorPhysicalSize

```TypeScript
readonly sensorPhysicalSize?: Array<double>
```

传感器物理尺寸（宽度和高度）。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraDevice-readonly sensorPhysicalSize?: Array<double>--><!--Device-CameraDevice-readonly sensorPhysicalSize?: Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## sensorPixelArraySize

```TypeScript
readonly sensorPixelArraySize?: Array<int>
```

传感器像素阵列尺寸（宽度和高度。单位：像素）。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraDevice-readonly sensorPixelArraySize?: Array<int>--><!--Device-CameraDevice-readonly sensorPixelArraySize?: Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

