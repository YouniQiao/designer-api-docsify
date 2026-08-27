# AudioSpatialDeviceState (System API)

Describes spatial device state.

**Since:** 11

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

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

## isHeadTrackingSupported

```TypeScript
isHeadTrackingSupported: boolean
```

Whether the spatial device supports head tracking.

**Type:** boolean

**Since:** 11

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

**Examples**

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isHeadTrackingSupported: boolean = audioSpatializationManager.isHeadTrackingSupported();
  console.info(`AudioSpatializationManager isHeadTrackingSupported: ${isHeadTrackingSupported}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

## isSpatializationSupported

```TypeScript
isSpatializationSupported: boolean
```

Whether the spatial device supports spatial rendering.

**Type:** boolean

**Since:** 11

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

**System API:** This is a system API.

**Examples**

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let isSpatializationSupported: boolean = audioSpatializationManager.isSpatializationSupported();
  console.info(`AudioSpatializationManager isSpatializationSupported: ${isSpatializationSupported}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

## spatialDeviceType

```TypeScript
spatialDeviceType: AudioSpatialDeviceType
```

Spatial device type.

**Type:** [AudioSpatialDeviceType](arkts-audio-audio-audiospatialdevicetype-e-sys.md)

**Since:** 11

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
