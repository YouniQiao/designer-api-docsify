# off_navDestinationSwitch

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## off_navDestinationSwitch

```TypeScript
export function off(
    type: 'navDestinationSwitch',
    context: UIAbilityContext | UIContext,
    callback?: Callback<NavDestinationSwitchInfo>
  ): void
```

Unsubscribes from **Navigation** component page switching events.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function off(    type: 'navDestinationSwitch',    context: UIAbilityContext | UIContext,    callback?: Callback<NavDestinationSwitchInfo>  ): void--><!--Device-uiObserver-export function off(    type: 'navDestinationSwitch',    context: UIAbilityContext | UIContext,    callback?: Callback<NavDestinationSwitchInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'navDestinationSwitch' | Yes |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) \| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NavDestinationSwitchInfo](arkts-arkui-uiobserver-navdestinationswitchinfo-i.md)&gt; | No |


## off_navDestinationSwitch

```TypeScript
export function off(
    type: 'navDestinationSwitch',
    context: UIAbilityContext | UIContext,
    observerOptions: NavDestinationSwitchObserverOptions,
    callback?: Callback<NavDestinationSwitchInfo>
  ): void
```

Unsubscribes from **Navigation** component page switching events. Compared with [uiObserver.off](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#off_navDestinationUpdate), this API supports the **observerOptions** parameter, which enables you to configure observation options.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function off(    type: 'navDestinationSwitch',    context: UIAbilityContext | UIContext,    observerOptions: NavDestinationSwitchObserverOptions,    callback?: Callback<NavDestinationSwitchInfo>  ): void--><!--Device-uiObserver-export function off(    type: 'navDestinationSwitch',    context: UIAbilityContext | UIContext,    observerOptions: NavDestinationSwitchObserverOptions,    callback?: Callback<NavDestinationSwitchInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'navDestinationSwitch' | Yes |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) \| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| observerOptions | [NavDestinationSwitchObserverOptions](arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NavDestinationSwitchInfo](arkts-arkui-uiobserver-navdestinationswitchinfo-i.md)&gt; | No |
