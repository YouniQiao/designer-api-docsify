# ProgressMask

Implements a ProgressMask object to set the progress, maximum value, and color of the mask.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ProgressMask--><!--Device-unnamed-export declare class ProgressMask-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: double, total: double, color: ResourceColor)
```

constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressMask-constructor(value: double, total: double, color: ResourceColor)--><!--Device-ProgressMask-constructor(value: double, total: double, color: ResourceColor)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | Current value of the progress mask. Value range: [0.0, +∞). |
| total | double | Yes | Maximum value of the progress mask. Value range: [0.0, +∞). |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) | Yes | Color of the progress mask. |

## enableBreathingAnimation

```TypeScript
enableBreathingAnimation(value: boolean): void
```

Enable the breathe animation of mask.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressMask-enableBreathingAnimation(value: boolean): void--><!--Device-ProgressMask-enableBreathingAnimation(value: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes |  |

## updateColor

```TypeScript
updateColor(value: ResourceColor): void
```

Update the color of the mask.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressMask-updateColor(value: ResourceColor): void--><!--Device-ProgressMask-updateColor(value: ResourceColor): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) | Yes | Color of the progress mask. |

## updateProgress

```TypeScript
updateProgress(value: double): void
```

Updates the progress value of the progress mask.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressMask-updateProgress(value: double): void--><!--Device-ProgressMask-updateProgress(value: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | Current value of the progress mask. |

