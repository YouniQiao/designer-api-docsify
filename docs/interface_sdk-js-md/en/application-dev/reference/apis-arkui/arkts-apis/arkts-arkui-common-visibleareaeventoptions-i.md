# VisibleAreaEventOptions

Defines the options about VisibleAreaEvent.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## expectedUpdateInterval

```TypeScript
expectedUpdateInterval?: int
```

The value of expectedUpdateInterval indicates desired update period(ms).

**Type:** int

**Default:** 1000

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## measureFromViewport

```TypeScript
measureFromViewport?: boolean
```

When this parameter is set to true, the parts of the component that exceed the parent component's area will also be included in the visible area calculation. However, this only applies if the parent component does not explicitly set the clip property to true. If the parent component sets clip to true, regardless of the value of this parameter, the parts that exceed the parent component's area will still be treated as invisible in the visible area calculation.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ratios

```TypeScript
ratios: Array<double>
```

Each number in ratios indicates the value of visibility ratio. Each number in the Array value range in [0, 1].

**Type:** Array&lt;double&gt;

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
