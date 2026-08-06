# ExtendableComponent

Definition of extendable component, which is base class of custom component and custom dialog.

**Inheritance/Implementation:** ExtendableComponent implements [LifeCycle](extendablecomponent-lifecycle-i.md), [IVariableOwner](../arkts-na-statemanagement/decorator-ivariableowner-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class ExtendableComponent implements LifeCycle, IVariableOwner--><!--Device-unnamed-export declare abstract class ExtendableComponent implements LifeCycle, IVariableOwner-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDialogController

```TypeScript
getDialogController(): promptAction.DialogController | undefined
```

The dialog controller of the custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-getDialogController(): promptAction.DialogController | undefined--><!--Device-ExtendableComponent-getDialogController(): promptAction.DialogController | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| promptAction.DialogController | The controller of dialog, |

## getUIContext

```TypeScript
getUIContext(): UIContext
```

Get current UIContext.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-getUIContext(): UIContext--><!--Device-ExtendableComponent-getUIContext(): UIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The UIContext that the custom component belongs to. |

## getUniqueId

```TypeScript
getUniqueId(): int
```

Get uniqueId of the custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-getUniqueId(): int--><!--Device-ExtendableComponent-getUniqueId(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | - The uniqueId of the custom component. |

## onWillApplyTheme

```TypeScript
onWillApplyTheme(theme: Theme): void
```

The onWillApplyTheme function is a custom hook to get active theme object from the context.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-onWillApplyTheme(theme: Theme): void--><!--Device-ExtendableComponent-onWillApplyTheme(theme: Theme): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| theme | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Custom theme init params. |

## queryNavDestinationInfo

```TypeScript
queryNavDestinationInfo(): NavDestinationInfo | undefined
```

Queries the navigation destination information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-queryNavDestinationInfo(): NavDestinationInfo | undefined--><!--Device-ExtendableComponent-queryNavDestinationInfo(): NavDestinationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The navigation destination information, or undefined if it is not |

## queryNavDestinationInfo

```TypeScript
queryNavDestinationInfo(isInner: boolean | undefined): NavDestinationInfo | undefined
```

Queries the navigation destination information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-queryNavDestinationInfo(isInner: boolean | undefined): NavDestinationInfo | undefined--><!--Device-ExtendableComponent-queryNavDestinationInfo(isInner: boolean | undefined): NavDestinationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isInner | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | - The navigation destination information, |

## queryNavigationInfo

```TypeScript
queryNavigationInfo(): NavigationInfo | undefined
```

Query the navigation information of the current custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-queryNavigationInfo(): NavigationInfo | undefined--><!--Device-ExtendableComponent-queryNavigationInfo(): NavigationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The navigation information, or undefined if it is not available |

## queryRouterPageInfo

```TypeScript
queryRouterPageInfo(): RouterPageInfo | undefined
```

Query the router page information of the current custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-queryRouterPageInfo(): RouterPageInfo | undefined--><!--Device-ExtendableComponent-queryRouterPageInfo(): RouterPageInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The router page information, or undefined if it is not available. |

