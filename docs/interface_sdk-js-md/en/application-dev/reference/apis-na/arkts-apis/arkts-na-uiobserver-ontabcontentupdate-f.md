# onTabContentUpdate

## Modules to Import

```TypeScript
```

## onTabContentUpdate

```TypeScript
export function onTabContentUpdate(options: ObserverOptions, callback: Callback<TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onTabContentUpdate(options: ObserverOptions, callback: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function onTabContentUpdate(options: ObserverOptions, callback: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TabContentInfo](arkts-na-uiobserver-tabcontentinfo-i.md)&gt; | Yes | The callback function to be called when when the tabContent is showed or hidden. |


## onTabContentUpdate

```TypeScript
export function onTabContentUpdate(callback: Callback<TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onTabContentUpdate(callback: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function onTabContentUpdate(callback: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TabContentInfo](arkts-na-uiobserver-tabcontentinfo-i.md)&gt; | Yes | The callback function to be called when the tabContent is showed or hidden. |

