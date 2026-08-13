# ProgressMask

Sets the progress, maximum value, and color for a mask.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare class ProgressMask--><!--Device-unnamed-declare class ProgressMask-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: number, total: number, color: ResourceColor)
```

Constructs a **ProgressMask** object.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProgressMask-constructor(value: number, total: number, color: ResourceColor)--><!--Device-ProgressMask-constructor(value: number, total: number, color: ResourceColor)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| total | number | Yes |
| color | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## enableBreathingAnimation

```TypeScript
enableBreathingAnimation(value: boolean): void
```

Sets whether to enable the breathing animation when the progress indicator is full. If this API is not set, the breathing animation is disabled by default.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ProgressMask-enableBreathingAnimation(value: boolean): void--><!--Device-ProgressMask-enableBreathingAnimation(value: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## updateColor

```TypeScript
updateColor(value: ResourceColor): void
```

Updates the color of the progress mask.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProgressMask-updateColor(value: ResourceColor): void--><!--Device-ProgressMask-updateColor(value: ResourceColor): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## updateProgress

```TypeScript
updateProgress(value: number): void
```

Updates the progress value of the progress mask.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProgressMask-updateProgress(value: number): void--><!--Device-ProgressMask-updateProgress(value: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
