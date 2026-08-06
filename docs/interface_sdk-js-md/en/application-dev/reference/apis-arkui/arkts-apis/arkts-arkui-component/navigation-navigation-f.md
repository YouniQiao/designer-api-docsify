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
| pathInfos | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Navigation constructor options |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |


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
| pathInfos | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Navigation constructor options |
| homeDestination | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The custom home destination info.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 26.0.0 |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |


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
| style\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes | navigation attribute instance |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Returns the instance of the NavigationAttribute. |

