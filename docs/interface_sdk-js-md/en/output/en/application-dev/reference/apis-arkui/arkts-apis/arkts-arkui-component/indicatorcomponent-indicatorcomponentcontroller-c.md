# IndicatorComponentController

Provides methods for switching components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class IndicatorComponentController--><!--Device-unnamed-export declare class IndicatorComponentController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changeIndex

```TypeScript
changeIndex(index: int | undefined, useAnimation?: boolean): void
```

Controlling IndicatorComponent to change to the specified subcomponent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentController-changeIndex(index: int | undefined, useAnimation?: boolean): void--><!--Device-IndicatorComponentController-changeIndex(index: int | undefined, useAnimation?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int \| undefined | Yes | The index of item to be redirected, default value is 0.undefined means set to default value. |
| useAnimation | boolean | No | If true, swipe to index item with animation.If false, swipe to index item without animation.The default value is false. |

## constructor

```TypeScript
constructor()
```

constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentController-constructor()--><!--Device-IndicatorComponentController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showNext

```TypeScript
showNext(): void
```

Called when the next child component is displayed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentController-showNext(): void--><!--Device-IndicatorComponentController-showNext(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showPrevious

```TypeScript
showPrevious(): void
```

Called when the previous subcomponent is displayed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentController-showPrevious(): void--><!--Device-IndicatorComponentController-showPrevious(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

