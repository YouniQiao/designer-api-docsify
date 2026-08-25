# AudioSpatialDeviceState (System API)

Describes spatial device state.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## address

```TypeScript
address: string
```

Spatial device address.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

## isHeadTrackingSupported

```TypeScript
isHeadTrackingSupported: boolean
```

Whether the spatial device supports head tracking.

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

## isSpatializationSupported

```TypeScript
isSpatializationSupported: boolean
```

Whether the spatial device supports spatial rendering.

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

## spatialDeviceType

```TypeScript
spatialDeviceType: AudioSpatialDeviceType
```

Spatial device type.

**Type:** [AudioSpatialDeviceType](arkts-audio-audio-audiospatialdevicetype-e-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

**Examples**

```TypeScript
import { audio } from '@kit.AudioKit';

let spatialDeviceState: audio.AudioSpatialDeviceState = {
  address: "123",
  isSpatializationSupported: true,
  isHeadTrackingSupported: true,
  spatialDeviceType: audio.AudioSpatialDeviceType.SPATIAL_DEVICE_TYPE_IN_EAR_HEADPHONE
};
```
