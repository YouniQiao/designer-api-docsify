# OH_AudioSuite_MetaFrame

```c
typedef struct OH_AudioSuite_MetaFrame {...} OH_AudioSuite_MetaFrame
```

## Overview

Define the audio meta data frame structure.This structure is used to pass audio data and meta data together.

**Since**: 26.0.0

**Related module**: [OHAudioSuite](capi-ohaudiosuite.md)

**Header file**: [native_audio_suite_base.h](capi-native-audio-suite-base-h.md)

## Summary

### Member variables

| Name | Description |
| -- | -- |
| void* audioData | Audio data pointer.<br>**Since**: 26.0.0 |
| int32_t audioDataSize | Audio data size.<br>**Since**: 26.0.0 |
| void* metaData | Meta data pointer.<br>**Since**: 26.0.0 |
| int32_t metaDataSize | Meta data size.<br>**Since**: 26.0.0 |


