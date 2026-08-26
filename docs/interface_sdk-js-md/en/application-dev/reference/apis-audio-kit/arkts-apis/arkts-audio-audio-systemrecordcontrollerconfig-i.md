# SystemRecordControllerConfig

Defines the configuration for the system recording controller panel.

**Since:** 26.0.0

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import audio from '@kit.AudioKit';
import audioHaptic from '@kit.AudioKitHaptic';
```

## sourceType

```TypeScript
sourceType: SourceType
```

The system uses this to determine the recording scenario of the application according to the SourceType that the application expects to use for streaming, and provides users with the ability to select matching noise reduction modes. The supported source types include [SOURCE_TYPE_MIC](arkts-audio-audio-sourcetype-e.md#source_type_mic), [SOURCE_TYPE_CAMCORDER](arkts-audio-audio-sourcetype-e.md#source_type_camcorder), and [SOURCE_TYPE_LIVE](arkts-audio-audio-sourcetype-e.md#source_type_live).

**Type:** SourceType

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Capturer
