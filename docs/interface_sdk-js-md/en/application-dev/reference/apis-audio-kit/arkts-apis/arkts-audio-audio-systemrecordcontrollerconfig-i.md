# SystemRecordControllerConfig

定义系统录像控制器面板配置。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-audio-interface SystemRecordControllerConfig--><!--Device-audio-interface SystemRecordControllerConfig-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## sourceType

```TypeScript
sourceType: SourceType
```

系统使用它来确定应用程序的录制场景，根据应用程序期望用于流式传输的源类型，并为用户提供选择匹配降噪模式的能力。支持的源类型包括{@link SourceType#Source_TYPE_MIC},{@link SourceType#Source_TYPE_CAMCORDER}，以及{@link SourceType#Source_TYPE_LIVE}。

**Type:** [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemRecordControllerConfig-sourceType: SourceType--><!--Device-SystemRecordControllerConfig-sourceType: SourceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

