# FillRequest (System API)

Defines the information about an auto-fill request.

**Since:** 23

<!--Device-unnamed-export interface FillRequest--><!--Device-unnamed-export interface FillRequest-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## customData

```TypeScript
customData: CustomData
```

Custom data.

**Type:** [CustomData](arkts-ability-customdata-i-sys.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequest-customData: CustomData--><!--Device-FillRequest-customData: CustomData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## isPopup

```TypeScript
isPopup: boolean
```

Whether a dialog box is displayed for the auto-fill request. **true**: A dialog box is displayed **false**: A modal window is displayed

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequest-isPopup: boolean--><!--Device-FillRequest-isPopup: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## triggerType

```TypeScript
triggerType?: AutoFillTriggerType
```

Trigger type for the autofill service.

**Type:** [AutoFillTriggerType](arkts-ability-autofilltriggertype-e-sys.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FillRequest-triggerType?: AutoFillTriggerType--><!--Device-FillRequest-triggerType?: AutoFillTriggerType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## type

```TypeScript
type: AutoFillType
```

Type of the element to be automatically filled in.

**Type:** [AutoFillType](arkts-ability-autofilltype-e-sys.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FillRequest-type: AutoFillType--><!--Device-FillRequest-type: AutoFillType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## viewData

```TypeScript
viewData: ViewData
```

Page data.

**Type:** [ViewData](arkts-ability-viewdata-i-sys.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FillRequest-viewData: ViewData--><!--Device-FillRequest-viewData: ViewData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

