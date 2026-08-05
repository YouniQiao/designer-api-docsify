# FractionStop

```TypeScript
export type FractionStop = [
    double,
    double
]
```

Defines the segment of blur. The first element in the tuple means fraction. The range of this value is [0,1]. A value of 1 means opaque and 0 means completely transparent. The second element means the stop position. The range of this value is [0,1]. A value of 1 means region ending position and 0 means region starting position.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type FractionStop = [    double,    double]--><!--Device-unnamed-export type FractionStop = [    double,    double]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Property type:** [
    double,
    double
]

