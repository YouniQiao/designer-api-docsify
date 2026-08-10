# AccessibilityOptions

Defines the struct of AccessibilityOptions.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-unnamed-declare interface AccessibilityOptions--><!--Device-unnamed-declare interface AccessibilityOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityPreferred

```TypeScript
accessibilityPreferred?: boolean
```

accessibilityPreferred -在连接子组件字符串时，是否应该优先考虑accessibilityText。

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AccessibilityOptions-accessibilityPreferred?: boolean--><!--Device-AccessibilityOptions-accessibilityPreferred?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## actionControllerId

```TypeScript
actionControllerId?: string
```

通过该可选参数指定特定ID的子组件，配置AccessibilityGroup的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该特定类型的子组件。从而聚合屏幕朗读下的点击事件，避免需要对子组件单独进行聚焦。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AccessibilityOptions-actionControllerId?: string--><!--Device-AccessibilityOptions-actionControllerId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## actionControllerRoleType

```TypeScript
actionControllerRoleType?: AccessibilityRoleType
```

stateControllerRoleType - 通过该可选参数指定特定类型的子组件，配置AccessibilityGroup的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该特定类型的子组件。从而聚合屏幕朗读下的点击事件，避免需要对子组件单独进行聚焦。

**Type:** [AccessibilityRoleType](../arkts-components/arkts-arkui-accessibilityroletype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AccessibilityOptions-actionControllerRoleType?: AccessibilityRoleType--><!--Device-AccessibilityOptions-actionControllerRoleType?: AccessibilityRoleType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stateControllerId

```TypeScript
stateControllerId?: string
```

stateControllerId -通过该可选参数指定特定ID的子组件，配置AccessibilityGroup的容器组件进行无障碍聚合后，会将该子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本。从而聚合屏幕朗读下的状态播报，避免需要对子组件单独进行聚焦。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AccessibilityOptions-stateControllerId?: string--><!--Device-AccessibilityOptions-stateControllerId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stateControllerRoleType

```TypeScript
stateControllerRoleType?: AccessibilityRoleType
```

stateControllerRoleType - 通过该可选参数指定特定类型的子组件，配置AccessibilityGroup的容器组件进行无障碍聚合后，会将该子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本。从而聚合屏幕朗读下的状态播报，避免需要对子组件单独进行聚焦。

**Type:** [AccessibilityRoleType](../arkts-components/arkts-arkui-accessibilityroletype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AccessibilityOptions-stateControllerRoleType?: AccessibilityRoleType--><!--Device-AccessibilityOptions-stateControllerRoleType?: AccessibilityRoleType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

