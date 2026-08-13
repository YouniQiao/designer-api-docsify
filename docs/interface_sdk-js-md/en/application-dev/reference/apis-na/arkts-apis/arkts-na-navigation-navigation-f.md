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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Navigation(    pathInfos?: NavPathStack,     content_?: CustomBuilder): NavigationAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Navigation(    pathInfos?: NavPathStack,     content_?: CustomBuilder): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-na-navigation-navpathstack-c.md) | No | Navigation constructor options |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationAttribute](arkts-na-navigation-navigationattribute-i.md) |  |


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

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Navigation(    pathInfos?: NavPathStack,     homeDestination?: HomePathInfo,    content_?: CustomBuilder): NavigationAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Navigation(    pathInfos?: NavPathStack,     homeDestination?: HomePathInfo,    content_?: CustomBuilder): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-na-navigation-navpathstack-c.md) | No | Navigation constructor options |
| homeDestination | [HomePathInfo](arkts-na-navigation-homepathinfo-i.md) | No | The custom home destination info.<br>**Since:** 26.0.0 |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationAttribute](arkts-na-navigation-navigationattribute-i.md) |  |


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

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Navigation( style_: CustomBuilderT<NavigationAttribute>, content_?: CustomBuilder,): NavigationAttribute--><!--Device-unnamed-@Builderexport declare function Navigation( style_: CustomBuilderT<NavigationAttribute>, content_?: CustomBuilder,): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[NavigationAttribute](arkts-na-navigation-navigationattribute-i.md)&gt; | Yes | navigation attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationAttribute](arkts-na-navigation-navigationattribute-i.md) | Returns the instance of the NavigationAttribute. |

