# NavPathInfo

路由页面信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare class NavPathInfo--><!--Device-unnamed-declare class NavPathInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(name: string, param: unknown, onPop?: import('../api/@ohos.base').Callback<PopInfo>, isEntry?: boolean)
```

创建NavPathInfo对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathInfo-constructor(name: string, param: unknown, onPop?: import('../api/@ohos.base').Callback<PopInfo>, isEntry?: boolean)--><!--Device-NavPathInfo-constructor(name: string, param: unknown, onPop?: import('../api/@ohos.base').Callback<PopInfo>, isEntry?: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。该名称匹配开发者设置的路由表中的name，包括以下两种：&lt;br/&gt;1. 自定义路由表，开发者通过 [navDestination](NavigationAttribute#navDestination)方法传递。&lt;br/&gt;2. 系统路由表，通过routerMap中的name设置，可参考 [示例2](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#示例2使用导航控制器方法)。 |
| param | unknown | Yes | 开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。 |
| onPop | import('../api/@ohos.base').Callback&lt;PopInfo&gt; | No | NavDestination页面触发 [pop](arkts-arkui-navpathstack-c.md#pop)、 [popToName](arkts-arkui-navpathstack-c.md#poptoname)、 [popToIndex](arkts-arkui-navpathstack-c.md#poptoindex)时返回的回调。仅 [pop](arkts-arkui-navpathstack-c.md#pop)、 [popToName](arkts-arkui-navpathstack-c.md#poptoname)、 [popToIndex](arkts-arkui-navpathstack-c.md#poptoindex)中设置result参数后触 发。<br>**Since:** 11 |
| isEntry | boolean | No | 标记NavDestination是否为入口页面。&lt;br/&gt;true：NavDestination是入口页面；false：NavDestination不是入口页面。&lt;br/ &gt;默认值：false &lt;br/&gt;标记清理时机：1. 在当前navDestination页面触发一次全局返回事件。2. 应用退至后台。&lt;br/&gt;**说明：**&lt;br/&gt;入口NavDestination不响应应用内的全局 back事件，直接触发应用间的全局back事件。<br>**Since:** 12 |

## isEntry

```TypeScript
isEntry?: boolean
```

标记NavDestination是否为入口页面。

true：NavDestination是入口页面；false：NavDestination不是入口页面。

默认值：false

标记清理时机：1. 在当前navDestination页面触发一次全局back事件。2. 应用退至后台。

**说明：**

入口NavDestination不响应应用内的全局back事件，直接触发应用间的全局back事件。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathInfo-isEntry?: boolean--><!--Device-NavPathInfo-isEntry?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: string
```

NavDestination页面名称。该名称匹配开发者设置的路由表中的name，包括以下两种：

1. 自定义路由表，开发者通过[navDestination](NavigationAttribute#navDestination)方法传递。2. 系统路由表，通过routerMap中的name设置，可参考[示例2](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#示例2使用导航控制器方法)。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathInfo-name: string--><!--Device-NavPathInfo-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestinationId

```TypeScript
navDestinationId?: string
```

NavDestination页面唯一标识符，该id由系统默认生成且全局唯一，通过[getPathStack](arkts-arkui-navpathstack-c.md#getpathstack)接口可读取，但不可以主动赋新值。

**Type:** string

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NavPathInfo-navDestinationId?: string--><!--Device-NavPathInfo-navDestinationId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPop

```TypeScript
onPop?: import('../api/@ohos.base').Callback<PopInfo>
```

NavDestination页面触发[pop](arkts-arkui-navpathstack-c.md#pop)、  
[popToName](arkts-arkui-navpathstack-c.md#poptoname)、  
[popToIndex](arkts-arkui-navpathstack-c.md#poptoindex)时返回的回调。仅  
[pop](arkts-arkui-navpathstack-c.md#pop)、  
[popToName](arkts-arkui-navpathstack-c.md#poptoname)、  
[popToIndex](arkts-arkui-navpathstack-c.md#poptoindex)中设置result参数后触发。

**Type:** import('../api/@ohos.base').Callback&lt;PopInfo&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathInfo-onPop?: import('../api/@ohos.base').Callback<PopInfo>--><!--Device-NavPathInfo-onPop?: import('../api/@ohos.base').Callback<PopInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## param

```TypeScript
param?: unknown
```

开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。

**Type:** unknown

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathInfo-param?: unknown--><!--Device-NavPathInfo-param?: unknown-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

