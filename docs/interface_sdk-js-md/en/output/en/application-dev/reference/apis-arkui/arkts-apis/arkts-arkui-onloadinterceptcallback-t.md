# OnLoadInterceptCallback

```TypeScript
export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean
```

Represents the callback invoked when resource loading is intercepted.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean--><!--Device-unnamed-export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Event triggered when resource loading is intercepted.  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether resource loading is intercepted. The value **true** indicates that resource loading is |

