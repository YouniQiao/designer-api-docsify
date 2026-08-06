# RepeatMode

Defines the Border Image Repeat Mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum RepeatMode--><!--Device-unnamed-export declare enum RepeatMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Repeat

```TypeScript
Repeat = 0
```

The source image's slices are tiled. Tiles beyond the border box will be clipped.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatMode-Repeat = 0--><!--Device-RepeatMode-Repeat = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Stretch

```TypeScript
Stretch = 1
```

The source image's slices are stretched to fill the border box.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatMode-Stretch = 1--><!--Device-RepeatMode-Stretch = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Round

```TypeScript
Round = 2
```

The source image's slices are tiled to fill the border box. Tiles may be compressed when needed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatMode-Round = 2--><!--Device-RepeatMode-Round = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Space

```TypeScript
Space = 3
```

The source image's slices are tiled to fill the border box. Extra space will be distributed in between tiles.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatMode-Space = 3--><!--Device-RepeatMode-Space = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

