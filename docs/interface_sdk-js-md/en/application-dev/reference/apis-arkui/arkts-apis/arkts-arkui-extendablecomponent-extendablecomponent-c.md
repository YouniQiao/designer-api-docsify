# ExtendableComponent

可扩展组件，是自定义组件和自定义对话框的基类。

**Inheritance/Implementation:** ExtendableComponent implements [LifeCycle](arkts-arkui-extendablecomponent-lifecycle-i.md), [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md)

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
| promptAction.DialogController | The controller of dialog, or undefined if the custom component does not display in the dialog. |

## getUIContext

```TypeScript
getUIContext(): UIContext
```

获取UIContext对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-getUIContext(): UIContext--><!--Device-ExtendableComponent-getUIContext(): UIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 返回UIContext实例对象。在异步调用的回调方法中使用该接口，或者该接口的起始调用不在当前页面时，可能导致接口调用发生在自定义组件销毁之后，返回undefined。 |

## getUniqueId

```TypeScript
getUniqueId(): int
```

获取当前组件的UniqueId。UniqueId为系统为每个组件分配的Id，可保证当前应用中的唯一性。若在组件对应的节点未创建或已销毁时获取，返回无效UniqueId：-1。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-getUniqueId(): int--><!--Device-ExtendableComponent-getUniqueId(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回当前Component的UniqueId。 |

## onWillApplyTheme

```TypeScript
onWillApplyTheme(theme: Theme): void
```

onWillApplyTheme函数用于获取当前组件上下文的Theme对象，在创建自定义组件的新实例后，在执行其build()函数之前执行。允许在onWillApplyTheme函数中改变状态变量，更改将在后续执行build()函数中生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-onWillApplyTheme(theme: Theme): void--><!--Device-ExtendableComponent-onWillApplyTheme(theme: Theme): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| theme | [Theme](arkts-arkui-arkui-theme-theme-i.md) | Yes | 自定义组件当前生效的Theme对象。 |

## queryNavDestinationInfo

```TypeScript
queryNavDestinationInfo(): NavDestinationInfo | undefined
```

查询自定义组件所属的NavDestination信息，仅当自定义组件在NavDestination的内部时才生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-queryNavDestinationInfo(): NavDestinationInfo | undefined--><!--Device-ExtendableComponent-queryNavDestinationInfo(): NavDestinationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NavDestinationInfo](../arkts-components/arkts-arkui-navdestinationinfo-t.md) | The navigation destination information, or undefined if it is not available. |

## queryNavDestinationInfo

```TypeScript
queryNavDestinationInfo(isInner: boolean | undefined): NavDestinationInfo | undefined
```

查询当前自定义组件距离最近的NavDestination信息（要求该NavDestination是Navigation的导航页或子页），isInner为true表示向内查找，false表示向外查找。

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
| [NavDestinationInfo](../arkts-components/arkts-arkui-navdestinationinfo-t.md) | The navigation destination information, or undefined if it is not available. |

## queryNavigationInfo

```TypeScript
queryNavigationInfo(): NavigationInfo | undefined
```

查询自定义组件所属的Navigation信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-queryNavigationInfo(): NavigationInfo | undefined--><!--Device-ExtendableComponent-queryNavigationInfo(): NavigationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationInfo](../arkts-components/arkts-arkui-navigationinfo-t.md) | The navigation information, or undefined if it is not available |

## queryRouterPageInfo

```TypeScript
queryRouterPageInfo(): RouterPageInfo | undefined
```

获取RouterPageInfo实例对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableComponent-queryRouterPageInfo(): RouterPageInfo | undefined--><!--Device-ExtendableComponent-queryRouterPageInfo(): RouterPageInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RouterPageInfo](../arkts-components/arkts-arkui-routerpageinfo-t.md) | The router page information, or undefined if it is not available. |

