# NavDestinationContext

NavDestination上下文信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavDestinationContext--><!--Device-unnamed-export declare interface NavDestinationContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getConfigInRouteMap

```TypeScript
getConfigInRouteMap(): RouteMapConfig | undefined
```

获取当前NavDestination的路由配置信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationContext-getConfigInRouteMap(): RouteMapConfig | undefined--><!--Device-NavDestinationContext-getConfigInRouteMap(): RouteMapConfig | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RouteMapConfig](arkts-arkui-navdestination-routemapconfig-i.md) |  |

## mode

```TypeScript
mode?: NavDestinationMode
```

当前NavDestination的类型。

**Type:** [NavDestinationMode](../arkts-components/arkts-arkui-navdestinationmode-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationContext-mode?: NavDestinationMode--><!--Device-NavDestinationContext-mode?: NavDestinationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestinationId

```TypeScript
navDestinationId?: string
```

当前NavDestination的唯一ID，由系统自动生成，和组件通用属性id无关。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationContext-navDestinationId?: string--><!--Device-NavDestinationContext-navDestinationId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pathInfo

```TypeScript
pathInfo: NavPathInfo
```

跳转NavDestination时指定的参数。

**Type:** [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationContext-pathInfo: NavPathInfo--><!--Device-NavDestinationContext-pathInfo: NavPathInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pathStack

```TypeScript
pathStack: NavPathStack
```

当前NavDestination所处的导航控制器。

**Type:** [NavPathStack](../arkts-components/arkts-arkui-navpathstack-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationContext-pathStack: NavPathStack--><!--Device-NavDestinationContext-pathStack: NavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

