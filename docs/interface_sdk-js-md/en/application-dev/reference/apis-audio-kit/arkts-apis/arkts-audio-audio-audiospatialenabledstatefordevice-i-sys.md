# AudioSpatialEnabledStateForDevice (System API)

This interface is used to notify the listener of any device Spatialization or Head Tracking enable or Adaptive Spatial Rendering state change.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioSpatialEnabledStateForDevice--><!--Device-audio-interface AudioSpatialEnabledStateForDevice-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## deviceDescriptor

```TypeScript
deviceDescriptor: AudioDeviceDescriptor
```

Audio device description.

**Type:** [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AudioSpatialEnabledStateForDevice-deviceDescriptor: AudioDeviceDescriptor--><!--Device-AudioSpatialEnabledStateForDevice-deviceDescriptor: AudioDeviceDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

## enabled

```TypeScript
enabled: boolean
```

Spatialization or Head Tracking or Adaptive Spatial Rendering enable state.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AudioSpatialEnabledStateForDevice-enabled: boolean--><!--Device-AudioSpatialEnabledStateForDevice-enabled: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

