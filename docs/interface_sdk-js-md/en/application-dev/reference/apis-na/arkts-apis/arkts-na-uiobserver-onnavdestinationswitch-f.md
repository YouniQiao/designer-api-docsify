# onNavDestinationSwitch

## onNavDestinationSwitch

```TypeScript
export function onNavDestinationSwitch(
    context: UIAbilityContext | UIContext,
    callback: Callback<NavDestinationSwitchInfo>
  ): void
```

Registers a callback function to be called when the navigation switched to a new navDestination.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onNavDestinationSwitch(    context: UIAbilityContext | UIContext,    callback: Callback<NavDestinationSwitchInfo>  ): void--><!--Device-uiObserver-export function onNavDestinationSwitch(    context: UIAbilityContext | UIContext,    callback: Callback<NavDestinationSwitchInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) \| [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | The context scope of the observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NavDestinationSwitchInfo](../../apis-arkui/arkts-apis/arkts-arkui-uiobserver-navdestinationswitchinfo-i.md)&gt; | Yes | The callback function to be called when the navigation switched to a new navDestination. |


## onNavDestinationSwitch

```TypeScript
export function onNavDestinationSwitch(
    context: UIAbilityContext | UIContext,
    observerOptions: NavDestinationSwitchObserverOptions,
    callback: Callback<NavDestinationSwitchInfo>
  ): void
```

Registers a callback function to be called when the navigation switched to a new navDestination.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onNavDestinationSwitch(    context: UIAbilityContext | UIContext,    observerOptions: NavDestinationSwitchObserverOptions,    callback: Callback<NavDestinationSwitchInfo>  ): void--><!--Device-uiObserver-export function onNavDestinationSwitch(    context: UIAbilityContext | UIContext,    observerOptions: NavDestinationSwitchObserverOptions,    callback: Callback<NavDestinationSwitchInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) \| [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | The context scope of the observer. |
| observerOptions | [NavDestinationSwitchObserverOptions](../../apis-arkui/arkts-apis/arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) | Yes | Options. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NavDestinationSwitchInfo](../../apis-arkui/arkts-apis/arkts-arkui-uiobserver-navdestinationswitchinfo-i.md)&gt; | Yes | The callback function to be called when the navigation switched to a new navDestination. |

