# AVRecorderConfig

音视频录制的参数。

audioSourceType和videoSourceType参数用于区分纯音频录制、纯视频录制和音视频录制。纯音频录制仅设置audioSourceType。纯视频录制仅设置videoSourceType。音视频录制需同时设置audioSourceType和videoSourceType。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-interface AVRecorderConfig--><!--Device-unnamed-interface AVRecorderConfig-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## metaSourceTypes

```TypeScript
metaSourceTypes?: Array<MetaSourceType>
```

元数据源类型，详见MetaSourceType。

**Type:** Array&lt;MetaSourceType&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVRecorderConfig-metaSourceTypes?: Array<MetaSourceType>--><!--Device-AVRecorderConfig-metaSourceTypes?: Array<MetaSourceType>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**System API:** This is a system API.

