# PickerProfile

相机选择器的配置信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cameraPicker-class PickerProfile--><!--Device-cameraPicker-class PickerProfile-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { cameraPicker } from 'kits/@kit.CameraKit';
```

## cameraPosition

```TypeScript
cameraPosition: camera.CameraPosition
```

相机的位置。

**Type:** camera.CameraPosition

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerProfile-cameraPosition: camera.CameraPosition--><!--Device-PickerProfile-cameraPosition: camera.CameraPosition-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## saveUri

```TypeScript
saveUri?: string
```

保存配置信息的uri，默认值请参考[文件uri](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-fileuri-c.md/arkts-corefile-fileuri-fileuri-c.md#constructor)。当前saveUri参数为可选参数，若未配置该参数，则拍摄的照片和视频会默认存入媒体库中；若不想将照片和视频存入媒体库中，请自行配置应用沙箱内的文件资源路径，如自行传入资源路径时请确保该文件存在且具备写入权限，否则会保存失败。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerProfile-saveUri?: string--><!--Device-PickerProfile-saveUri?: string-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## videoDuration

```TypeScript
videoDuration?: int
```

录制的最大时长（单位：秒）。默认为0，不设置最大录制时长。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerProfile-videoDuration?: int--><!--Device-PickerProfile-videoDuration?: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

