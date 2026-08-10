# @ohos.multimedia.cameraPicker(相机选择器)

本模块提供相机拍照与录制的能力。应用可选择媒体类型实现拍照和录制的功能。调用此类接口时，应用必须在界面UIAbility中调用，否则无法启动cameraPicker应用。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace cameraPicker--><!--Device-unnamed-declare namespace cameraPicker-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { cameraPicker } from 'kits/@kit.CameraKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [pick](arkts-camera-camerapicker-pick-f.md#pick) | 拉起相机选择器，根据媒体类型进入相应的模式。使用Promise异步回调。 |

### Classes

| Name | Description |
| --- | --- |
| [PickerProfile](arkts-camera-camerapicker-pickerprofile-c.md) | 相机选择器的配置信息。 |
| [PickerResult](arkts-camera-camerapicker-pickerresult-c.md) | 相机选择器的处理结果。 |

### Enums

| Name | Description |
| --- | --- |
| [PickerMediaType](arkts-camera-camerapicker-pickermediatype-e.md) | 枚举，相机选择器的媒体类型。 |

