# MetadataSalientDetectionObject

Salient subject metadata detected by the camera, which is extended from   
[MetadataObject](arkts-camera-camera-metadataobject-i.md#MetadataObject). It serves as the data source of the camera information in   
[CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput). It is obtained by calling metadataOutput.  
[on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)).

**Inheritance/Implementation:** MetadataSalientDetectionObject extends [MetadataObject](arkts-camera-camera-metadataobject-i.md#MetadataObject)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-camera-interface MetadataSalientDetectionObject extends MetadataObject--><!--Device-camera-interface MetadataSalientDetectionObject extends MetadataObject-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

