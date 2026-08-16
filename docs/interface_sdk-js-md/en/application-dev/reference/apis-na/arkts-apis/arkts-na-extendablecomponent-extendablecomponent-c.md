# ExtendableComponent

Definition of extendable component, which is base class of custom component and custom dialog.

**Inheritance/Implementation:** ExtendableComponent implements [LifeCycle](arkts-na-extendablecomponent-lifecycle-i.md#LifeCycle), [IVariableOwner](arkts-na-decorator-ivariableowner-i.md#IVariableOwner)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare abstract class ExtendableComponent--><!--Device-unnamed-export declare abstract class ExtendableComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDialogController

```TypeScript
getDialogController(): promptAction.DialogController | undefined
```

The dialog controller of the custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-getDialogController(): promptAction.DialogController | undefined--><!--Device-ExtendableComponent-getDialogController(): promptAction.DialogController | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| promptAction.DialogController | The controller of dialog, or undefined if the custom component does not display in the dialog. |

## getUIContext

```TypeScript
getUIContext(): UIContext
```

Get current UIContext.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-getUIContext(): UIContext--><!--Device-ExtendableComponent-getUIContext(): UIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | The UIContext that the custom component belongs to. |

## getUniqueId

```TypeScript
getUniqueId(): int
```

Get uniqueId of the custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-getUniqueId(): int--><!--Device-ExtendableComponent-getUniqueId(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | The uniqueId of the custom component. |

## onWillApplyTheme

```TypeScript
onWillApplyTheme(theme: Theme): void
```

The onWillApplyTheme function is a custom hook to get active theme object from the context.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-onWillApplyTheme(theme: Theme): void--><!--Device-ExtendableComponent-onWillApplyTheme(theme: Theme): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| theme | [Theme](arkts-na-arkui-theme-theme-i.md) | Yes | Custom theme init params. |

## queryNavDestinationInfo

```TypeScript
queryNavDestinationInfo(): NavDestinationInfo | undefined
```

Queries the navigation destination information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-queryNavDestinationInfo(): NavDestinationInfo | undefined--><!--Device-ExtendableComponent-queryNavDestinationInfo(): NavDestinationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NavDestinationInfo](../../apis-arkui/arkts-components/arkts-arkui-navdestinationinfo-t.md) | The navigation destination information, or undefined if it is not available. |

## queryNavDestinationInfo

```TypeScript
queryNavDestinationInfo(isInner: boolean | undefined): NavDestinationInfo | undefined
```

Queries the navigation destination information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

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
| [NavDestinationInfo](../../apis-arkui/arkts-components/arkts-arkui-navdestinationinfo-t.md) | The navigation destination information, or undefined if it is not available. |

## queryNavigationInfo

```TypeScript
queryNavigationInfo(): NavigationInfo | undefined
```

Query the navigation information of the current custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-queryNavigationInfo(): NavigationInfo | undefined--><!--Device-ExtendableComponent-queryNavigationInfo(): NavigationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationInfo](../../apis-arkui/arkts-components/arkts-arkui-navigationinfo-t.md) | The navigation information, or undefined if it is not available |

## queryRouterPageInfo

```TypeScript
queryRouterPageInfo(): RouterPageInfo | undefined
```

Query the router page information of the current custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-queryRouterPageInfo(): RouterPageInfo | undefined--><!--Device-ExtendableComponent-queryRouterPageInfo(): RouterPageInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RouterPageInfo](../../apis-arkui/arkts-components/arkts-arkui-routerpageinfo-t.md) | The router page information, or undefined if it is not available. |

