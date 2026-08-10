# OverflowInfo

Provides OverflowInfo about funInteraction or sceneAnimation form

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-formInfo-interface OverflowInfo--><!--Device-formInfo-interface OverflowInfo-End-->

**System capability:** SystemCapability.Ability.Form

## Modules to Import

```TypeScript
import { formInfo } from 'kits/@kit.FormKit';
```

## area

```TypeScript
area: Rect
```

The overflow animation area

**Type:** [Rect](arkts-form-forminfo-rect-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-OverflowInfo-area: Rect--><!--Device-OverflowInfo-area: Rect-End-->

**System capability:** SystemCapability.Ability.Form

## duration

```TypeScript
duration: int
```

The overflow animation duration, unit is ms Unit: milliseconds, The value must be an integer within [0,3500].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-OverflowInfo-duration: int--><!--Device-OverflowInfo-duration: int-End-->

**System capability:** SystemCapability.Ability.Form

## useDefaultAnimation

```TypeScript
useDefaultAnimation?: boolean
```

Whether use default animation, default is true

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-OverflowInfo-useDefaultAnimation?: boolean--><!--Device-OverflowInfo-useDefaultAnimation?: boolean-End-->

**System capability:** SystemCapability.Ability.Form

