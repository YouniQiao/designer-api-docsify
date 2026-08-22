# AccessibilityOptions

Defines the struct of AccessibilityOptions.

@interface AccessibilityOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface AccessibilityOptions--><!--Device-unnamed-export declare interface AccessibilityOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityPreferred

```TypeScript
accessibilityPreferred?: boolean
```

accessibilityPreferred - Should accessibilityText be prioritized when concatenating child component strings.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityOptions-accessibilityPreferred?: boolean--><!--Device-AccessibilityOptions-accessibilityPreferred?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## actionControllerId

```TypeScript
actionControllerId?: string
```

actionControllerId - the first component of a specific id found within the composition defined by accessibility group will take over part of the accessibility action of the composition

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityOptions-actionControllerId?: string--><!--Device-AccessibilityOptions-actionControllerId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## actionControllerRoleType

```TypeScript
actionControllerRoleType?: AccessibilityRoleType
```

actionControllerRoleType - the first component of a specific type found within the composition defined by accessibility group will take over part of the accessibility action of the composition

**Type:** [AccessibilityRoleType](../../apis-arkui/arkts-components/arkts-arkui-accessibilityroletype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityOptions-actionControllerRoleType?: AccessibilityRoleType--><!--Device-AccessibilityOptions-actionControllerRoleType?: AccessibilityRoleType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stateControllerId

```TypeScript
stateControllerId?: string
```

stateControllerId - the first component of a specific id found within the composition defined by accessibility group will take over the state attributes and announcement of the composition

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityOptions-stateControllerId?: string--><!--Device-AccessibilityOptions-stateControllerId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stateControllerRoleType

```TypeScript
stateControllerRoleType?: AccessibilityRoleType
```

stateControllerType - the first component of a specific type found within the composition defined by accessibility group will take over the state attributes and announcement of the composition

**Type:** [AccessibilityRoleType](../../apis-arkui/arkts-components/arkts-arkui-accessibilityroletype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityOptions-stateControllerRoleType?: AccessibilityRoleType--><!--Device-AccessibilityOptions-stateControllerRoleType?: AccessibilityRoleType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

