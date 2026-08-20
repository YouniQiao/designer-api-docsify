# Navigation

## Navigation

```TypeScript
@ComponentBuilder
export declare function Navigation(
    pathInfos?: NavPathStack, 
    content_?: CustomBuilder
): NavigationAttribute
```

Defines Navigation Component

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Navigation(    pathInfos?: NavPathStack,     content_?: CustomBuilder): NavigationAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Navigation(    pathInfos?: NavPathStack,     content_?: CustomBuilder): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-navigation-navpathstack-c.md) | No | Navigation constructor options |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationAttribute](arkts-navigation-attribute.md) |  |


## Navigation

```TypeScript
@ComponentBuilder
export declare function Navigation(
    pathInfos?: NavPathStack, 
    homeDestination?: HomePathInfo,
    content_?: CustomBuilder
): NavigationAttribute
```

Defines Navigation Component

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Navigation(    pathInfos?: NavPathStack,     homeDestination?: HomePathInfo,    content_?: CustomBuilder): NavigationAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Navigation(    pathInfos?: NavPathStack,     homeDestination?: HomePathInfo,    content_?: CustomBuilder): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-navigation-navpathstack-c.md) | No | Navigation constructor options |
| homeDestination | [HomePathInfo](arkts-navigation-homepathinfo-i.md) | No | The custom home destination info.<br>**Since:** 26.0.0 |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationAttribute](arkts-navigation-attribute.md) |  |


## Navigation

```TypeScript
@Builder
export declare function Navigation(
 style_: CustomBuilderT<NavigationAttribute>,
 content_?: CustomBuilder,
): NavigationAttribute
```

Defines Navigation Component

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Navigation( style_: CustomBuilderT<NavigationAttribute>, content_?: CustomBuilder,): NavigationAttribute--><!--Device-unnamed-@Builderexport declare function Navigation( style_: CustomBuilderT<NavigationAttribute>, content_?: CustomBuilder,): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[NavigationAttribute](arkts-navigation-attribute.md)&gt; | Yes | navigation attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationAttribute](arkts-navigation-attribute.md) | Returns the instance of the NavigationAttribute. |

