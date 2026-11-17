# IntervalInfo

```TypeScript
interface IntervalInfo
```

Developers can obtain the timestamp information of frame drawing from the callback function, including the timestamp when the current frame arrives and the targetTimestamp when the next frame is expected to arrive.

**Since:** 11

<!--Device-displaySync-interface IntervalInfo--><!--Device-displaySync-interface IntervalInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { displaySync } from '@kit.ArkGraphics2D';
```

## targetTimestamp

```TypeScript
targetTimestamp: number
```

Expected arrival time of the next frame (in nanoseconds). Monotonically increasing time since system startup. The value must be greater than timestamp.

**Type:** number

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 26.0.1.

<!--Device-IntervalInfo-targetTimestamp: long--><!--Device-IntervalInfo-targetTimestamp: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: number
```

Time when the current frame arrives (in nanoseconds). Monotonically increasing time since system startup.

**Type:** number

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 26.0.1.

<!--Device-IntervalInfo-timestamp: long--><!--Device-IntervalInfo-timestamp: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
