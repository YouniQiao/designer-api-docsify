# NavDestinationContext

Indicates the context of NavDestination.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavDestinationContext--><!--Device-unnamed-export declare interface NavDestinationContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getConfigInRouteMap

```TypeScript
getConfigInRouteMap(): RouteMapConfig | undefined
```

Get configuration of current Destination in module.json

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

The mode of NavDestination.

**Type:** [NavDestinationMode](arkts-arkui-navdestination-navdestinationmode-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationContext-mode?: NavDestinationMode--><!--Device-NavDestinationContext-mode?: NavDestinationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestinationId

```TypeScript
navDestinationId?: string
```

Get the unique id of NavDestination, which is different from common property id of Component.

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

Get path info.

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

Get stack of the Navigation where the NavDestination is located.

**Type:** [NavPathStack](../arkts-components/arkts-arkui-navpathstack-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationContext-pathStack: NavPathStack--><!--Device-NavDestinationContext-pathStack: NavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

