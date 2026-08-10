# AVMetadata

Defines the audio and video metadata. Parameters that are not declared as read-only in  
[AVRecorderConfig](#AVRecorderConfig) can be used as input parameters for recording of  
[AVRecorder](#AVRecorder).

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-media-interface AVMetadata--><!--Device-media-interface AVMetadata-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## gltf_offset

```TypeScript
gltf_offset?: string
```

The offset value of GLTF 3D model in media file. This parameter is not supported in AVRecorder settings.If the media file has no GLTF 3D model, gltf_offset is undefined.

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-AVMetadata-gltf_offset?: string--><!--Device-AVMetadata-gltf_offset?: string-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**System API:** This is a system API.

