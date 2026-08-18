# off_navDestinationUpdate

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## off_navDestinationUpdate('navDestinationUpdate')

```TypeScript
export function off(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback?: Callback<NavDestinationInfo>): void
```

Unsubscribes from status changes of the **NavDestination** component. Compared with [uiObserver.off](#off_navdestinationupdatenavdestinationupdate), this API supports the **options** parameter, which enables you to specify the ID of the target **Navigation** component to observe.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function off(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback?: Callback<NavDestinationInfo>): void--><!--Device-uiObserver-export function off(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback?: Callback<NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationUpdate' | Yes | Event type. Set to **'navDestinationUpdate'** for **NavDestination** component status change events. |
| options | { navigationId: ResourceStr } | Yes | ID of the target **Navigation** component. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;NavDestinationInfo&gt; | No | Callback used to return the result. It provides the current state of the **NavDestination** component. |


## off_navDestinationUpdate('navDestinationUpdate')

```TypeScript
export function off(type: 'navDestinationUpdate', callback?: Callback<NavDestinationInfo>): void
```

Unsubscribes from status changes of the **NavDestination** component.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function off(type: 'navDestinationUpdate', callback?: Callback<NavDestinationInfo>): void--><!--Device-uiObserver-export function off(type: 'navDestinationUpdate', callback?: Callback<NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationUpdate' | Yes | Event type. Set to **'navDestinationUpdate'** for **NavDestination** component status change events. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;NavDestinationInfo&gt; | No | Callback used to return the result. It provides the current state of the **NavDestination** component. |

