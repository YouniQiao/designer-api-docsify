# OnLoadInterceptCallback

```TypeScript
export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean
```

当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean--><!--Device-unnamed-export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [OnLoadInterceptEvent](../../apis-arkweb/arkts-apis/arkts-arkweb-web-onloadinterceptevent-i.md) | Yes | 当Web组件加载url之前触发的加载拦截事件。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回资源是否被拦截，true表示被拦截，false表示不被拦截。 |

