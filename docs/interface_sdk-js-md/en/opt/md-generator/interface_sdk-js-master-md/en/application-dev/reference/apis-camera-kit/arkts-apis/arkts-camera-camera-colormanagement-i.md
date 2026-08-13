# ColorManagement

**ColorManagement** inherits from [ColorManagementQuery](arkts-camera-camera-colormanagementquery-i.md#ColorManagementQuery). It provides the APIs for color space settings.

**Inheritance/Implementation:** ColorManagement extends [ColorManagementQuery](arkts-camera-camera-colormanagementquery-i.md#ColorManagementQuery)

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface ColorManagement--><!--Device-camera-interface ColorManagement-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getActiveColorSpace

```TypeScript
getActiveColorSpace(): colorSpaceManager.ColorSpace
```

Obtains the color space in use.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ColorManagement-getActiveColorSpace(): colorSpaceManager.ColorSpace--><!--Device-ColorManagement-getActiveColorSpace(): colorSpaceManager.ColorSpace-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| colorSpaceManager.ColorSpace |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setColorSpace

```TypeScript
setColorSpace(colorSpace: colorSpaceManager.ColorSpace): void
```

Sets a color space. Before the setting, call [getSupportedColorSpaces](arkts-camera-camera-colormanagementquery-i.md#getSupportedColorSpaces) to obtain the supported color spaces. You are advised to call this API after [addOutput](arkts-camera-camera-session-i.md#addOutput) and before [commitConfig](arkts-camera-camera-session-i.md#commitConfig). If this API is called after [commitConfig](arkts-camera-camera-session-i.md#commitConfig), the camera session configuration will take a longer time. P3 wide color gamut and HDR imaging: An application can deliver different color space parameters to declare its support for P3 and HDR. If an application does not proactively set the color space, SDR is used by default in photo and video recording modes. For different modes, enabling HDR, setting the color space, and configuring [CameraFormat](arkts-camera-camera-cameraformat-e.md#CameraFormat) in the camera output stream [profile](arkts-camera-camera-profile-i.md#Profile) should match. For details, see the table below. For example, to enable HDR in video recording mode, set [CameraFormat](arkts-camera-camera-cameraformat-e.md#CameraFormat) in the camera preview and video output stream [profiles](arkts-camera-camera-profile-i.md#Profile) to **CAMERA_FORMAT_YCRCB_P010** and the color space to **BT2020_HLG_LIMIT**. To obtain HDR images in photo mode, set the color space to **DISPLAY_P3** or **BT2020_HLG**. **BT2020_HLG** provides a wider color gamut, and should be used together with the **CameraFormat**, including **CAMERA_FORMAT_YCRCB_P010** and **CAMERA_FORMAT_YCBCR_P010**, to improve the image quality. Since API version 23, you can call the [getSupportedFullOutputCapability](arkts-camera-camera-cameramanager-i.md#getSupportedFullOutputCapability) API to check whether the preview format P010 is supported in photo mode. - If the application does not set the color space, the default color space in photo mode is SRGB when the **CameraFormat** is **CAMERA_FORMAT_YUV_420_SP**, and the default color space is **BT2020_HLG** when the **CameraFormat** is **CAMERA_FORMAT_YCRCB_P010** or **CAMERA_FORMAT_YCBCR_P010**. - If the application sets the color space, in photo mode, the **CameraFormat** and **ColorSpace** must be configured according to the following mapping table. Otherwise, an error code will be returned in [setColorSpace](#setColorSpace) or [commitConfig](arkts-camera-camera-session-i.md#commitConfig). Photo mode: | SDR/HDR Photo Capture | CameraFormat| ColorSpace| |--------------------|------------| ------------| | SDR(Default) | CAMERA_FORMAT_YUV_420_SP | SRGB | | HDR P3 | CAMERA_FORMAT_YUV_420_SP | DISPLAY_P3 | | HDR BT.2020 | CAMERA_FORMAT_YCRCB_P010,&lt;br&gt;CAMERA_FORMAT_YCBCR_P010 | BT2020_HLG | In video recording mode, if SDR or HDR VIVID is enabled, the camera format and color space must be configured according to the relationships specified in the table below. Configurations that do not match the table will cause issues such as preview exceptions. Recording mode: | SDR/HDR Photo Capture | CameraFormat | ColorSpace | |--------------------|--------------------------|------------------| | SDR(Default) | CAMERA_FORMAT_YUV_420_SP | BT709_LIMIT | | HDR_VIVID | CAMERA_FORMAT_YCRCB_P010 | BT2020_HLG_LIMIT,&lt;br&gt;BT2020_HLG |

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ColorManagement-setColorSpace(colorSpace: colorSpaceManager.ColorSpace): void--><!--Device-ColorManagement-setColorSpace(colorSpace: colorSpaceManager.ColorSpace): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorSpace | colorSpaceManager.ColorSpace | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
