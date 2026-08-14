# off_densityUpdate

## Modules to Import

```TypeScript
import { uiObserver } from 'uiObserver';
```

## off_densityUpdate

```TypeScript
export function off(type: 'densityUpdate', context: UIContext, callback?: Callback<DensityInfo>): void
```

Unregisters the listener for screen pixel density changes.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function off(type: 'densityUpdate', context: UIContext, callback?: Callback<DensityInfo>): void--><!--Device-uiObserver-export function off(type: 'densityUpdate', context: UIContext, callback?: Callback<DensityInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'densityUpdate' | Yes | Event type. Set to **'densityUpdate'** for screen pixel density change events. |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DensityInfo](arkts-arkui-uiobserver-densityinfo-c.md)&gt; | No | Target listener to unregister. If no parameter is provided, all listeners for the **densityUpdate** event under the current UI context are unregistered. |

