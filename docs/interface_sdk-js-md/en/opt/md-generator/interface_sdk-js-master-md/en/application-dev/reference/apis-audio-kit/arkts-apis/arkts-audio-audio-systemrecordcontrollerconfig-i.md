# SystemRecordControllerConfig

Defines the configuration for the system recording controller panel.

**Since:** 26.0.0

<!--Device-audio-interface SystemRecordControllerConfig--><!--Device-audio-interface SystemRecordControllerConfig-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
```

## sourceType

```TypeScript
sourceType: SourceType
```

The system uses this to determine the recording scenario of the application according to the SourceType that the application expects to use for streaming, and provides users with the ability to select matching noise reduction modes. The supported source types include [SOURCE_TYPE_MIC](arkts-audio-audio-sourcetype-e.md#sourcetypemic), [SOURCE_TYPE_CAMCORDER](arkts-audio-audio-sourcetype-e.md#sourcetypecamcorder), and [SOURCE_TYPE_LIVE](arkts-audio-audio-sourcetype-e.md#sourcetypelive).

**Type:** SourceType

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemRecordControllerConfig-sourceType: SourceType--><!--Device-SystemRecordControllerConfig-sourceType: SourceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer
