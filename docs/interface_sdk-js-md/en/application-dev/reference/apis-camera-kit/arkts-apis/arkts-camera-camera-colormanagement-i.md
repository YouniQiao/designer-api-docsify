# ColorManagement

ColorManagement** inherits from [ColorManagementQuery]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

It provides the APIs for color space settings.

**Inheritance/Implementation:** ColorManagement extends [ColorManagementQuery](arkts-camera-camera-colormanagementquery-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface ColorManagement extends ColorManagementQuery--><!--Device-camera-interface ColorManagement extends ColorManagementQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## getActiveColorSpace

```TypeScript
getActiveColorSpace(): colorSpaceManager.ColorSpace
```

Obtains the color space in use.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ColorManagement-getActiveColorSpace(): colorSpaceManager.ColorSpace--><!--Device-ColorManagement-getActiveColorSpace(): colorSpaceManager.ColorSpace-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| colorSpaceManager.ColorSpace | Color space. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

## setColorSpace

```TypeScript
setColorSpace(colorSpace: colorSpaceManager.ColorSpace): void
```

Sets a color space.

Before the setting, call [getSupportedColorSpaces]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to obtain the supported color spaces. You are advised to call this API after  
[addOutput]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and before [commitConfig]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_. If this API is called after [commitConfig]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, the camera session configuration will take a longer time.

P3 wide color gamut and HDR imaging:

An application can deliver different color space parameters to declare its support for P3 and HDR. If an application does not proactively set the color space, SDR is used by default in photo and video recording modes.

For different modes, enabling HDR, setting the color space, and configuring  
[CameraFormat]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ in the camera output stream [profile]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ should match. For details, see the table below. For example, to enable HDR in video recording mode, set  
[CameraFormat]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ in the camera preview and video output stream  
[profiles]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_ to **CAMERA\_FORMAT\_YCRCB\_P010** and the color space to **BT2020\_HLG\_LIMIT**.

To obtain HDR images in photo mode, set the color space to **DISPLAY\_P3** or **BT2020\_HLG**. **BT2020\_HLG**  
provides a wider color gamut, and should be used together with the **CameraFormat**, including  
**CAMERA\_FORMAT\_YCRCB\_P010** and **CAMERA\_FORMAT\_YCBCR\_P010**, to improve the image quality.

Since API version 23, you can call the  
[getSupportedFullOutputCapability]\_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_ API to check whether the preview format P010 is supported in photo mode.

- If the application does not set the color space, the default color space in photo mode is SRGB when the  
**CameraFormat** is **CAMERA\_FORMAT\_YUV\_420\_SP**, and the default color space is **BT2020\_HLG** when the  
**CameraFormat** is **CAMERA\_FORMAT\_YCRCB\_P010** or **CAMERA\_FORMAT\_YCBCR\_P010**.  
- If the application sets the color space, in photo mode, the **CameraFormat** and **ColorSpace** must be  
configured according to the following mapping table. Otherwise, an error code will be returned in  
[setColorSpace]\_\_\_JSDOC\_LINK\_DESC\_USD\_9\_\_\_ or  
[commitConfig]\_\_\_JSDOC\_LINK\_DESC\_USD\_10\_\_\_.

Photo mode:

| SDR/HDR Photo Capture | CameraFormat| ColorSpace|  
|--------------------|------------| ------------|  
| SDR(Default) | CAMERA\_FORMAT\_YUV\_420\_SP | SRGB |  
| HDR P3 | CAMERA\_FORMAT\_YUV\_420\_SP | DISPLAY\_P3 |  
| HDR BT.2020 | CAMERA\_FORMAT\_YCRCB\_P010,\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_CAMERA\_FORMAT\_YCBCR\_P010 | BT2020\_HLG |

In video recording mode, if SDR or HDR VIVID is enabled, the camera format and color space must be configured according to the relationships specified in the table below. Configurations that do not match the table will cause issues such as preview exceptions.

Recording mode:

| SDR/HDR Photo Capture | CameraFormat | ColorSpace |  
|--------------------|--------------------------|------------------|  
| SDR(Default) | CAMERA\_FORMAT\_YUV\_420\_SP | BT709\_LIMIT |  
| HDR\_VIVID | CAMERA\_FORMAT\_YCRCB\_P010 | BT2020\_HLG\_LIMIT,\_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_BT2020\_HLG |

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ColorManagement-setColorSpace(colorSpace: colorSpaceManager.ColorSpace): void--><!--Device-ColorManagement-setColorSpace(colorSpace: colorSpaceManager.ColorSpace): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorSpace | colorSpaceManager.ColorSpace | Yes | The type of color space. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | The colorSpace does not match the format. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

