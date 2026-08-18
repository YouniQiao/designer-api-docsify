# offTabContentUpdate

## Modules to Import

```TypeScript
```

## offTabContentUpdate

```TypeScript
export function offTabContentUpdate(options: ObserverOptions, callback?: Callback<TabContentInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offTabContentUpdate(options: ObserverOptions, callback?: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function offTabContentUpdate(options: ObserverOptions, callback?: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[TabContentInfo](arkts-na-uiobserver-tabcontentinfo-i.md)&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and Tabs ID will be removed. |


## offTabContentUpdate

```TypeScript
export function offTabContentUpdate(callback?: Callback<TabContentInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offTabContentUpdate(callback?: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function offTabContentUpdate(callback?: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[TabContentInfo](arkts-na-uiobserver-tabcontentinfo-i.md)&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

