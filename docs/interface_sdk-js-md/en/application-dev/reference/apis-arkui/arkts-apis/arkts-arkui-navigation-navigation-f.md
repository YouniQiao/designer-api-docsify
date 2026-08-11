# Navigation

## Navigation

```TypeScript
export declare function Navigation(
    pathInfos?: NavPathStack, 
    content_?: CustomBuilder
): NavigationAttribute
```

Defines Navigation Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Navigation(    pathInfos?: NavPathStack,     content_?: CustomBuilder): NavigationAttribute--><!--Device-unnamed-export declare function Navigation(    pathInfos?: NavPathStack,     content_?: CustomBuilder): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | No | Navigation constructor options |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationAttribute](../arkts-components/arkts-arkui-navigation-attribute.md) |  |


## Navigation

```TypeScript
export declare function Navigation(
    pathInfos?: NavPathStack, 
    homeDestination?: HomePathInfo,
    content_?: CustomBuilder
): NavigationAttribute
```

Defines Navigation Component

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Navigation(    pathInfos?: NavPathStack,     homeDestination?: HomePathInfo,    content_?: CustomBuilder): NavigationAttribute--><!--Device-unnamed-export declare function Navigation(    pathInfos?: NavPathStack,     homeDestination?: HomePathInfo,    content_?: CustomBuilder): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | No | Navigation constructor options |
| homeDestination | [HomePathInfo](arkts-arkui-navigation-homepathinfo-i.md) | No | The custom home destination info.<br>**Since:** 26.0.0 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationAttribute](../arkts-components/arkts-arkui-navigation-attribute.md) |  |


## Navigation

```TypeScript
export declare function Navigation(
 style_: CustomBuilderT<NavigationAttribute>,
 content_?: CustomBuilder,
): NavigationAttribute
```

Defines Navigation Component

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Navigation( style_: CustomBuilderT<NavigationAttribute>, content_?: CustomBuilder,): NavigationAttribute--><!--Device-unnamed-export declare function Navigation( style_: CustomBuilderT<NavigationAttribute>, content_?: CustomBuilder,): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;NavigationAttribute&gt; | Yes | navigation attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationAttribute](../arkts-components/arkts-arkui-navigation-attribute.md) | Returns the instance of the NavigationAttribute. |

