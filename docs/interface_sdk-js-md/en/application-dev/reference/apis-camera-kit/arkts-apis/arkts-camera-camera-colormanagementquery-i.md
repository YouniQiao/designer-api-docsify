# ColorManagementQuery

色彩管理类，用于查询色彩空间参数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface ColorManagementQuery--><!--Device-camera-interface ColorManagementQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getSupportedColorSpaces

```TypeScript
getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>
```

获取支持的色彩空间列表。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ColorManagementQuery-getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>--><!--Device-ColorManagementQuery-getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;colorSpaceManager.ColorSpace&gt; | 支持的色彩空间列表。若接口调用失败，返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400103 | Session not config, only throw in session usage.<br>**Applicable version:** 12 - 17 |

