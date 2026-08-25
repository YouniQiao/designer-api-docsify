# VolumeEvent

Describes the event received by the application when the volume is changed.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## networkId

```TypeScript
networkId: string
```

Device network id

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

## percentage

```TypeScript
percentage?: int
```

Volume percentage, which is an integer ranging from [0, 100].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

## volumeGroupId

```TypeScript
volumeGroupId: int
```

volumeGroup id

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.
