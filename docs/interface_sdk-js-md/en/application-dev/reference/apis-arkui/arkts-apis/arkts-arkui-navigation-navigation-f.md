# Navigation

## Navigation

```TypeScript
export declare function Navigation(
    pathInfos?: NavPathStack, 
    content_?: CustomBuilder
): NavigationAttribute
```

绑定导航控制器到Navigation组件，适用于使用[NavPathStack](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md)配合  
[navDestination](NavigationAttribute.navDestination)属性进行页面路由。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Navigation(    pathInfos?: NavPathStack,     content_?: CustomBuilder): NavigationAttribute--><!--Device-unnamed-export declare function Navigation(    pathInfos?: NavPathStack,     content_?: CustomBuilder): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | No | 导航控制器对象。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 子组件。 |

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

绑定导航控制器到Navigation组件，并设置自定义首页，适用于使用[NavPathStack](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md)配合  
[navDestination](NavigationAttribute.navDestination)属性进行页面路由。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Navigation(   pathInfos?: NavPathStack,    homeDestination?: HomePathInfo,   content_?: CustomBuilder): NavigationAttribute--><!--Device-unnamed-export declare function Navigation(   pathInfos?: NavPathStack,    homeDestination?: HomePathInfo,   content_?: CustomBuilder): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | No | 导航控制器对象。 |
| homeDestination | [HomePathInfo](arkts-arkui-navigation-homepathinfo-i.md) | No | 自定义首页信息。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 子组件。 |

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

绑定导航控制器到Navigation组件，适用于使用[NavPathStack](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md)配合  
[navDestination](NavigationAttribute.navDestination)属性进行页面路由。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Navigation( style_: CustomBuilderT<NavigationAttribute>, content_?: CustomBuilder,): NavigationAttribute--><!--Device-unnamed-export declare function Navigation( style_: CustomBuilderT<NavigationAttribute>, content_?: CustomBuilder,): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;NavigationAttribute&gt; | Yes | 导航控制器对象。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 子组件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [NavigationAttribute](../arkts-components/arkts-arkui-navigation-attribute.md) | Returns the instance of the NavigationAttribute. |

