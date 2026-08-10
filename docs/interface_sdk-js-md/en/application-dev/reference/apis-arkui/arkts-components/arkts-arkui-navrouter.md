# NavRouter

导航组件，默认提供点击响应处理，不需要开发者自定义点击事件逻辑。

## 子组件

必须包含两个子组件，其中第二个子组件必须为[NavDestination]{@link nav_destination}。

> **说明：**
> 
> 子组件个数异常时：
> 
> 1. 有且仅有1个时，触发路由到NavDestination的能力失效。
> 
> 2. 有且仅有1个时，且使用NavDestination场景下，不进行路由。
> 
> 3. 大于2个时，后续的子组件不显示。
> 
> 4. 第二个子组件不为NavDestination时，触发路由功能失效。

## NavRouter

```TypeScript
NavRouter()
```

创建NavRouter。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 13

**Substitutes:** <!--SUBSTITUTE_API-->NavDestinationAttribute<!--/SUBSTITUTE_API-->

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavRouterInterface-(): NavRouterAttribute--><!--Device-NavRouterInterface-(): NavRouterAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NavRouter

```TypeScript
NavRouter(value: RouteInfo)
```

提供路由信息，指定点击NavRouter时，要跳转的NavDestination页面。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 13

**Substitutes:** <!--SUBSTITUTE_API-->Navigation#NavPathInfo<!--/SUBSTITUTE_API-->

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavRouterInterface-(value: RouteInfo): NavRouterAttribute--><!--Device-NavRouterInterface-(value: RouteInfo): NavRouterAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RouteInfo](../../apis-network-kit/arkts-apis/arkts-network-vpnextension-routeinfo-t.md) | Yes | 路由信息。 |

## Summary

- [RouteInfo](arkts-arkui-navrouter-routeinfo-i.md)
- [NavRouteMode](arkts-arkui-navrouter-navroutemode-e.md)
