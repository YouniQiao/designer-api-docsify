# CommonTransition

Provides interfaces for common transitions.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class CommonTransition--><!--Device-unnamed-export declare class CommonTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## opacity

```TypeScript
opacity(value: double): this
```

Called when the transparency value of the starting point of entry or the ending point of exit is set.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonTransition-opacity(value: double): this--><!--Device-CommonTransition-opacity(value: double): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## scale

```TypeScript
scale(value: ScaleOptions): this
```

Called when setting the zoom effect of page transition.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonTransition-scale(value: ScaleOptions): this--><!--Device-CommonTransition-scale(value: ScaleOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScaleOptions](../../apis-arkui/arkts-components/arkts-arkui-scaleoptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## slide

```TypeScript
slide(value: SlideEffect): this
```

Called when the slide in effect of the transition is set.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonTransition-slide(value: SlideEffect): this--><!--Device-CommonTransition-slide(value: SlideEffect): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SlideEffect](arkts-pagetransition-slideeffect-e.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## translate

```TypeScript
translate(value: TranslateOptions): this
```

Called when the translation effect of page transition is set.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonTransition-translate(value: TranslateOptions): this--><!--Device-CommonTransition-translate(value: TranslateOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TranslateOptions](../../apis-arkui/arkts-components/arkts-arkui-translateoptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

