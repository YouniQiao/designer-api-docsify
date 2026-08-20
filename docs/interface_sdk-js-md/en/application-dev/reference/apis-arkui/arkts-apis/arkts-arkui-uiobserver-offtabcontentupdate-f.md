# off_tabContentUpdate

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## off('tabContentUpdate')

```TypeScript
export function off(type: 'tabContentUpdate', options: ObserverOptions, callback?: Callback<TabContentInfo>): void
```

Unsubscribes from **TabContent** page switching events for the specified **Tabs** component identified by its ID.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function off(type: 'tabContentUpdate', options: ObserverOptions, callback?: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function off(type: 'tabContentUpdate', options: ObserverOptions, callback?: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabContentUpdate' | Yes | Event type. Set to **'tabContentUpdate'** for **TabContent** page switching events. |
| options | ObserverOptions | Yes | ID of the target **Tabs** component. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[TabContentInfo](arkts-arkui-uiobserver-tabcontentinfo-i.md)&gt; | No | Target listener to unregister. |


## off('tabContentUpdate')

```TypeScript
export function off(type: 'tabContentUpdate', callback?: Callback<TabContentInfo>): void
```

Unsubscribes from the **TabContent** switching event.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function off(type: 'tabContentUpdate', callback?: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function off(type: 'tabContentUpdate', callback?: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabContentUpdate' | Yes | Event type. Set to **'tabContentUpdate'** for **TabContent** page switching events. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[TabContentInfo](arkts-arkui-uiobserver-tabcontentinfo-i.md)&gt; | No | Target listener to unregister. |

