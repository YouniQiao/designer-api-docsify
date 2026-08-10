# NavDestinationBuilder

```TypeScript
export type NavDestinationBuilder = (name: string, param?: Object) => void
```

用于创建NavDestination组件内容的构建器类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export type NavDestinationBuilder = (name: string, param?: Object) => void--><!--Device-unnamed-export type NavDestinationBuilder = (name: string, param?: Object) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面名称。 |
| param | Object | No | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面详细参数。默认值为空。 |

