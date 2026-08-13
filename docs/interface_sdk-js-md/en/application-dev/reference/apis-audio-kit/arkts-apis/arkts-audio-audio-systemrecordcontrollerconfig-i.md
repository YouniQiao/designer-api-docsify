# SystemRecordControllerConfig

Defines the configuration for the system recording controller panel.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-audio-interface SystemRecordControllerConfig--><!--Device-audio-interface SystemRecordControllerConfig-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## sourceType

```TypeScript
sourceType: SourceType
```

The system uses this to determine the recording scenario of the application according to the SourceType that the application expects to use for streaming, and provides users with the ability to select matching noise reduction modes. The supported source types include [SOURCE_TYPE_MIC](arkts-audio-audio-sourcetype-e.md#SOURCE_TYPE_MIC), [SOURCE_TYPE_CAMCORDER](arkts-audio-audio-sourcetype-e.md#SOURCE_TYPE_CAMCORDER), and [SOURCE_TYPE_LIVE](arkts-audio-audio-sourcetype-e.md#SOURCE_TYPE_LIVE).

**Type:** SourceType

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemRecordControllerConfig-sourceType: SourceType--><!--Device-SystemRecordControllerConfig-sourceType: SourceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

