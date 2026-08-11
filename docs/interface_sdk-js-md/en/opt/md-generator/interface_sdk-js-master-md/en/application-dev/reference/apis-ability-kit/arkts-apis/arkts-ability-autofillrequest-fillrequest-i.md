# FillRequest

Defines the information about an auto-fill request.

**Since:** 26.0.0

<!--Device-unnamed-export interface FillRequest--><!--Device-unnamed-export interface FillRequest-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## customData

```TypeScript
customData: CustomData
```

Custom data.

**Type:** [CustomData](arkts-ability-customdata-i-sys.md)

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequest-customData: CustomData--><!--Device-FillRequest-customData: CustomData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## isPopup

```TypeScript
isPopup: boolean
```

Whether a dialog box is displayed for the auto-fill request.

**true**: A dialog box is displayed

**false**: A modal window is displayed

**Type:** boolean

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequest-isPopup: boolean--><!--Device-FillRequest-isPopup: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## triggerType

```TypeScript
triggerType?: AutoFillTriggerType
```

Trigger type for the autofill service.

**Type:** [AutoFillTriggerType](arkts-ability-autofilltriggertype-e.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FillRequest-triggerType?: AutoFillTriggerType--><!--Device-FillRequest-triggerType?: AutoFillTriggerType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## type

```TypeScript
type: AutoFillType
```

Type of the element to be automatically filled in.

**Type:** [AutoFillType](arkts-ability-autofilltype-e.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FillRequest-type: AutoFillType--><!--Device-FillRequest-type: AutoFillType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## viewData

```TypeScript
viewData: ViewData
```

Page data.

**Type:** [ViewData](arkts-ability-viewdata-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FillRequest-viewData: ViewData--><!--Device-FillRequest-viewData: ViewData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore
