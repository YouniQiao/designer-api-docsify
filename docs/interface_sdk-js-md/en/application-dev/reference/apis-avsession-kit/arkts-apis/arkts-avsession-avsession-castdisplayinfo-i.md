# CastDisplayInfo

Define the information for extended display screen.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-avSession-interface CastDisplayInfo--><!--Device-avSession-interface CastDisplayInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## height

```TypeScript
height: int
```

Display height, in pixels.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CastDisplayInfo-height: int--><!--Device-CastDisplayInfo-height: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

## id

```TypeScript
id: long
```

Display ID.The application can get more display information based on the same id from display interface.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CastDisplayInfo-id: long--><!--Device-CastDisplayInfo-id: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

## name

```TypeScript
name: string
```

Display name.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CastDisplayInfo-name: string--><!--Device-CastDisplayInfo-name: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

## state

```TypeScript
state: CastDisplayState
```

The state of display.

**Type:** [CastDisplayState](arkts-avsession-avsession-castdisplaystate-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CastDisplayInfo-state: CastDisplayState--><!--Device-CastDisplayInfo-state: CastDisplayState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

## width

```TypeScript
width: int
```

Display width, in pixels.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CastDisplayInfo-width: int--><!--Device-CastDisplayInfo-width: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

