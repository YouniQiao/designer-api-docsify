# NavPathInfo

路由页面信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class NavPathInfo--><!--Device-unnamed-export declare class NavPathInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)
```

创建NavPathInfo对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)--><!--Device-NavPathInfo-constructor(name: string, param: Object | null | undefined, onPop?: Callback<PopInfo>, isEntry?: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。该名称匹配开发者设置的路由表中的name，包括以下两种：&lt;br/&gt;1. 自定义路由表，开发者通过 [navDestination](NavigationAttribute.navDestination)方法传递。&lt;br/&gt;2. 系统路由表，通过routerMap中的name设置，可参考 [示例2](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation copy.md#示例2使用导航控制器方法)。 |
| param | Object \| null \| undefined | Yes | 开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。&lt;br/&gt;取值为undefined时，页面信 息无效。 |
| onPop | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;PopInfo&gt; | No | NavDestination页面触发 [pop](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#pop)、 [popToName](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#poptoname)、 [popToIndex](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#poptoindex)时返回的回调。仅 [pop](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#pop)、 [popToName](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#poptoname)、 [popToIndex](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#poptoindex)中设置result参数后触发。 |
| isEntry | boolean | No | 标记NavDestination是否为入口页面。&lt;br/&gt;true：NavDestination是入口页面；false：NavDestination不是入口页面。&lt; br/&gt;默认值：false &lt;br/&gt;标记清理时机：1. 在当前navDestination页面触发一次全局返回事件。2. 应用退至后台。&lt;br/&gt;**说明：**&lt;br/&gt;入口NavDestination不响应应用内的 全局back事件，直接触发应用间的全局back事件 |

## isEntry

```TypeScript
set isEntry(isEntry: boolean | undefined)
```

Set whether it is an entry destination, the default value is false, undefined means set to default value.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-set isEntry(isEntry: boolean | undefined)--><!--Device-NavPathInfo-set isEntry(isEntry: boolean | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
set name(name: string)
```

Set the name of NavDestination.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-set name(name: string)--><!--Device-NavPathInfo-set name(name: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestinationId

```TypeScript
get navDestinationId(): string | undefined
```

获取NavDestination页面唯一标识符。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-get navDestinationId(): string | undefined--><!--Device-NavPathInfo-get navDestinationId(): string | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPop

```TypeScript
set onPop(onPop: Callback<PopInfo> | undefined)
```

Set the callback when next page returns, the default value is nullptr, undefined means set to default value.

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;PopInfo&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-set onPop(onPop: Callback<PopInfo> | undefined)--><!--Device-NavPathInfo-set onPop(onPop: Callback<PopInfo> | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## param

```TypeScript
set param(param: Object | null | undefined)
```

Set the detailed parameter of the NavDestination, default value is undefined, null is also a meaningful input parameter.

**Type:** Object

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathInfo-set param(param: Object | null | undefined)--><!--Device-NavPathInfo-set param(param: Object | null | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

