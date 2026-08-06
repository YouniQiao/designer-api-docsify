# ColorManagementQuery

ColorManagementQuery provides the APIs for color space query.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface ColorManagementQuery--><!--Device-camera-interface ColorManagementQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## getSupportedColorSpaces

```TypeScript
getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>
```

Obtains the supported color spaces.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ColorManagementQuery-getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>--><!--Device-ColorManagementQuery-getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;colorSpaceManager.ColorSpace&gt; | Array of color spaces supported. If the API call fails, undefined is returned. |

