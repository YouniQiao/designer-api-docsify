# ExpectedFrameRateRange

Interface for ExpectedFrameRateRange.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## expected

```TypeScript
expected: int
```

The expected frame rate of dynamical callback rate range. The value should be between the minimum and maximum value. Otherwise, the actual callback rate will be dynamically adjusted to better align with other animation sources.

**Type:** int

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## max

```TypeScript
max: int
```

The maximum animation drawing FPS. The maximum value should be greater than or equal to the minimum value.

**Type:** int

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## min

```TypeScript
min: int
```

The minimum animation drawing FPS. The minimum value should be less than or equal to the maximum value.

**Type:** int

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
