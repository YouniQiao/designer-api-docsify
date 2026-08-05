# IntervalInfo

You can obtain the timestamp information from the event callback, including the timestamp when the current frame arrives and the timestamp when the next frame is expected to arrive.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-displaySync-interface IntervalInfo--><!--Device-displaySync-interface IntervalInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetTimestamp

```TypeScript
targetTimestamp: long
```

Expected arrival time of the next frame, in nanoseconds.

**Type:** long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-IntervalInfo-targetTimestamp: long--><!--Device-IntervalInfo-targetTimestamp: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: long
```

Time when the current frame arrives, in nanoseconds.

**Type:** long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-IntervalInfo-timestamp: long--><!--Device-IntervalInfo-timestamp: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

