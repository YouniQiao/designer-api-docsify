# MultiNavPathStack

当前，MultiNavigation的路由栈仅支持由使用方自行创建，不支持通过回调方式获取。请勿使用[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)的  
[onReady](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#onready11)等类似事件或接口来获取NavPathStack并进行栈操作，因为这可能会导致不可预知的问题。

**Inheritance/Implementation:** MultiNavPathStack extends [NavPathStack](arkts-arkui-navigation-navpathstack-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class MultiNavPathStack extends NavPathStack--><!--Device-unnamed-export declare class MultiNavPathStack extends NavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { MultiNavPathStack, MultiNavigation, SplitPolicy } from 'kits/@kit.ArkUI';
```

## clear

```TypeScript
clear(animated?: boolean): void
```

清除栈中所有页面。

> **说明：**
> 
> 当调用[keepBottomPage](arkts-arkui-arkui-advanced-multinavigation-multinavpathstack-c.md#keepbottompage)接口并设置为true时，会保留栈底页面。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-clear(animated?: boolean): void--><!--Device-MultiNavPathStack-clear(animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |

## constructor

```TypeScript
constructor()
```

Creates an instance of MultiNavPathStack.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-constructor()--><!--Device-MultiNavPathStack-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableAnimation

```TypeScript
disableAnimation(disable: boolean): void
```

关闭（true）或打开（false）当前MultiNavigation中所有转场动画。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-disableAnimation(disable: boolean): void--><!--Device-MultiNavPathStack-disableAnimation(disable: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| disable | boolean | Yes | 是否关闭转场动画。&lt;br/&gt;默认值：false&lt;br/&gt;true：关闭转场动画。&lt;br/&gt;false：不关闭转场动画。 |

## getAllPathName

```TypeScript
getAllPathName(): Array<string>
```

获取栈中所有NavDestination页面的名称。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-getAllPathName(): Array<string>--><!--Device-MultiNavPathStack-getAllPathName(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 返回栈中所有NavDestination页面的名称。 |

## getIndexByName

```TypeScript
getIndexByName(name: string): Array<int>
```

获取全部名为name的NavDestination页面的位置索引。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-getIndexByName(name: string): Array<int>--><!--Device-MultiNavPathStack-getIndexByName(name: string): Array<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;int&gt; | 返回全部名为name的NavDestination页面的位置索引。&lt;br/&gt;number/int类型的取值范围：[0, +∞) |

## getParamByIndex

```TypeScript
getParamByIndex(index: int): Object | undefined
```

获取index指定的NavDestination页面的参数信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-getParamByIndex(index: int): Object | undefined--><!--Device-MultiNavPathStack-getParamByIndex(index: int): Object | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | NavDestination页面的位置索引。&lt;br/&gt;取值范围：[0, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| Object | Returns the detailed parameter of the NavDestination if it exists in the stack, otherwise returns undefined. |

## getParamByName

```TypeScript
getParamByName(name: string): Array<Object | null | undefined>
```

获取全部名为name的NavDestination页面的参数信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-getParamByName(name: string): Array<Object | null | undefined>--><!--Device-MultiNavPathStack-getParamByName(name: string): Array<Object | null | undefined>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Object \| null \| undefined&gt; | Returns the detailed parameter of all the NavDestinations. |

## keepBottomPage

```TypeScript
keepBottomPage(keepBottom: boolean): void
```

设置在调用pop和clear接口时是否保留栈底页面。

> **说明：**
> 
> MultiNavigation将主页也当作了NavDestination页面入栈，所以调用pop或clear接口时会将栈底页面也出栈。
> > 应用调用此接口并设置为true时，MultiNavigation会在调用pop和clear接口时保留栈底页面。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-keepBottomPage(keepBottom: boolean): void--><!--Device-MultiNavPathStack-keepBottomPage(keepBottom: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keepBottom | boolean | Yes | 是否保留栈底页面。&lt;br/&gt;默认值：false&lt;br/&gt;true：保留栈底页面。&lt;br/&gt;false：不保留栈底页面。 |

## moveIndexToTop

```TypeScript
moveIndexToTop(index: int, animated?: boolean): void
```

将指定index的NavDestination页面移到栈顶。

> **说明：**
> 
> 根据找到的第一个名为name的页面的不同，MultiNavigation会进行不同的处理：
> 
> 1)当找到的是最上层主页或者全屏页，此时不做任何处理；
> 
> 2)当找到的是最上层主页对应的详情页，则会将对应的详情页移到栈顶；
> 
> 3)当找到的是非最上层的主页，则会将主页和对应所有详情页移到栈顶，详情页相对栈关系不变；
> 
> 4)当找到的是非最上层的详情页，则会将主页和对应所有详情页移到栈顶，且将目标详情页移动到对应所有详情页的栈顶；
> 
> 5)当找到的是非最上层的全屏页，则会将全屏页移动到栈顶。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-moveIndexToTop(index: int, animated?: boolean): void--><!--Device-MultiNavPathStack-moveIndexToTop(index: int, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | NavDestination页面的位置索引。&lt;br/&gt;取值范围：[0, +∞) |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |

## moveToTop

```TypeScript
moveToTop(name: string, animated?: boolean): int
```

将由栈底开始第一个名为name的NavDestination页面移到栈顶。

> **说明：**
> 
> 根据找到的第一个名为name的页面的不同，MultiNavigation会进行不同的处理：
> 
> 1)当找到的是最上层主页或者全屏页，此时不做任何处理；
> 
> 2)当找到的是最上层主页对应的详情页，则会将对应的详情页移到栈顶；
> 
> 3)当找到的是非最上层的主页，则会将主页和对应所有详情页移到栈顶，详情页相对栈关系不变；
> 
> 4)当找到的是非最上层的详情页，则会将主页和对应所有详情页移到栈顶，且将目标详情页移动到对应所有详情页的栈顶；
> 
> 5)当找到的是非最上层的全屏页，则会将全屏页移动到栈顶。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-moveToTop(name: string, animated?: boolean): int--><!--Device-MultiNavPathStack-moveToTop(name: string, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。 |

## pop

```TypeScript
pop(result?: Object, animated?: boolean): NavPathInfo | undefined
```

弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

> **说明：**
> 
> 当调用[keepBottomPage](arkts-arkui-arkui-advanced-multinavigation-multinavpathstack-c.md#keepbottompage)接口并设置为true时，会保留栈底页面。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-pop(result?: Object, animated?: boolean): NavPathInfo | undefined--><!--Device-MultiNavPathStack-pop(result?: Object, animated?: boolean): NavPathInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | Object | No | 页面自定义处理结果。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Returns the top NavPathInfo if the stack is not empty, otherwise returns undefined. |

## popToIndex

```TypeScript
popToIndex(index: int, animated?: boolean): void
```

回退路由栈到index指定的NavDestination页面。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-popToIndex(index: int, animated?: boolean): void--><!--Device-MultiNavPathStack-popToIndex(index: int, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | NavDestination页面的位置索引。&lt;br/&gt;取值范围：[0, +∞) |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |

## popToIndex

```TypeScript
popToIndex(index: int, result: Object, animated?: boolean): void
```

回退路由栈到index指定的NavDestination页面，并触发onPop回调传入页面处理结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-popToIndex(index: int, result: Object, animated?: boolean): void--><!--Device-MultiNavPathStack-popToIndex(index: int, result: Object, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | NavDestination页面的位置索引。&lt;br/&gt;取值范围：[0, +∞) |
| result | Object | Yes | 页面自定义处理结果。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |

## popToName

```TypeScript
popToName(name: string, animated?: boolean): int
```

回退路由栈到由栈底开始第一个名为name的NavDestination页面。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-popToName(name: string, animated?: boolean): int--><!--Device-MultiNavPathStack-popToName(name: string, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。&lt;br/&gt;取值范围：[-1, +∞) |

## popToName

```TypeScript
popToName(name: string, result: Object, animated?: boolean): int
```

回退路由栈到由栈底开始第一个名为name的NavDestination页面，并触发onPop回调传入页面处理结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-popToName(name: string, result: Object, animated?: boolean): int--><!--Device-MultiNavPathStack-popToName(name: string, result: Object, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| result | Object | Yes | 页面自定义处理结果。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。 |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, animated?: boolean, policy?: SplitPolicy): void
```

将指定的NavDestination页面信息入栈。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-pushPath(info: NavPathInfo, animated?: boolean, policy?: SplitPolicy): void--><!--Device-MultiNavPathStack-pushPath(info: NavPathInfo, animated?: boolean, policy?: SplitPolicy): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | Indicates the NavDestination to be pushed. |
| animated | boolean | No | Indicates whether the transition is animated. |
| policy | [SplitPolicy](arkts-arkui-arkui-advanced-multinavigation-splitpolicy-e.md) | No | SplitPolicy of the NavDestination which is currently pushed in stack. Default splitPolicy is DETAIL_PAGE. |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, options?: NavigationOptions, policy?: SplitPolicy): void
```

将指定的NavDestination页面信息入栈，通过NavigationOptions设置页面栈操作选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions, policy?: SplitPolicy): void--><!--Device-MultiNavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions, policy?: SplitPolicy): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | Indicates the NavDestination to be pushed. |
| options | [NavigationOptions](../arkts-components/arkts-arkui-navigationoptions-i.md) | No | Indicates options of stack operation. |
| policy | [SplitPolicy](arkts-arkui-arkui-advanced-multinavigation-splitpolicy-e.md) | No | SplitPolicy of the NavDestination which is currently pushed in stack. Default splitPolicy is DETAIL_PAGE. |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: Object, animated?: boolean, policy?: SplitPolicy): void
```

将name指定的NavDestination页面信息入栈，传递的数据为param。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-pushPathByName(name: string, param: Object, animated?: boolean, policy?: SplitPolicy): void--><!--Device-MultiNavPathStack-pushPathByName(name: string, param: Object, animated?: boolean, policy?: SplitPolicy): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| param | Object | Yes | NavDestination页面详细参数。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |
| policy | [SplitPolicy](arkts-arkui-arkui-advanced-multinavigation-splitpolicy-e.md) | No | 当前入栈页面的策略。默认值：DETAIL_PAGE |

## pushPathByName

```TypeScript
pushPathByName(
    name: string, param: Object, onPop?: Callback<PopInfo>, animated?: boolean, policy?: SplitPolicy): void
```

将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-pushPathByName(    name: string, param: Object, onPop?: Callback<PopInfo>, animated?: boolean, policy?: SplitPolicy): void--><!--Device-MultiNavPathStack-pushPathByName(    name: string, param: Object, onPop?: Callback<PopInfo>, animated?: boolean, policy?: SplitPolicy): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| param | Object | Yes | NavDestination页面详细参数。 |
| onPop | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PopInfo](../arkts-components/arkts-arkui-popinfo-i.md)&gt; | No | Callback回调，用于页面出栈时触发该回调处理返回结果。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |
| policy | [SplitPolicy](arkts-arkui-arkui-advanced-multinavigation-splitpolicy-e.md) | No | 当前入栈页面的策略。默认值：DETAIL_PAGE |

## removeByIndexes

```TypeScript
removeByIndexes(indexes: Array<int>): int
```

将页面栈内索引值在indexes中的NavDestination页面删除。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-removeByIndexes(indexes: Array<int>): int--><!--Device-MultiNavPathStack-removeByIndexes(indexes: Array<int>): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indexes | Array&lt;int&gt; | Yes | 待删除NavDestination页面的索引值数组。&lt;br/&gt;number/int类型的取值范围：[0, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回删除的NavDestination页面数量。 |

## removeByName

```TypeScript
removeByName(name: string): int
```

将页面栈内指定name的NavDestination页面删除。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-removeByName(name: string): int--><!--Device-MultiNavPathStack-removeByName(name: string): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 待删除NavDestination页面的名字。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回删除的NavDestination页面数量。 |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, animated?: boolean): void
```

将当前页面栈栈顶退出，将指定的NavDestination页面信息入栈，新页面的分栏策略继承原栈顶页面的策略。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void--><!--Device-MultiNavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | Indicates the new NavDestination in top of the stack. |
| animated | boolean | No | Indicates whether the transition is animated. |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, options?: NavigationOptions): void
```

将当前页面栈栈顶退出，将指定的NavDestination页面信息入栈，新页面的分栏策略继承原栈顶页面的策略，通过NavigationOptions设置页面栈操作选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void--><!--Device-MultiNavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | Indicates the new NavDestination in top of the stack. |
| options | [NavigationOptions](../arkts-components/arkts-arkui-navigationoptions-i.md) | No | Indicates options of stack operation. |

## replacePathByName

```TypeScript
replacePathByName(name: string, param: Object, animated?: boolean): void
```

将当前页面栈栈顶退出，将name指定的页面入栈，新页面的分栏策略继承原栈顶页面的策略。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void--><!--Device-MultiNavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| param | Object | Yes | NavDestination页面详细参数。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;默认值：true&lt;br/&gt;true：支持转场动画。&lt;br/&gt;false：不支持转场动画。 |

## setHomeWidthRange

```TypeScript
setHomeWidthRange(minPercent: double, maxPercent: double): void
```

设置主页宽度可拖动范围。应用不设置的情况下宽度为50%，且不可拖动。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-setHomeWidthRange(minPercent: double, maxPercent: double): void--><!--Device-MultiNavPathStack-setHomeWidthRange(minPercent: double, maxPercent: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minPercent | double | Yes | 最小主页宽度百分比。 |
| maxPercent | double | Yes | 最大主页宽度百分比。 |

## setPlaceholderPage

```TypeScript
setPlaceholderPage(info: NavPathInfo): void
```

设置占位页面。

> **说明：**
> 
> 占位页面为特殊页面类型，当应用设置后，在一些大屏设备上会和主页默认形成左右分栏的效果，即左边主页，右边占位页。
> 
> 当应用可绘制区域小于600vp、折叠屏由展开态切换为折叠态及平板横屏转竖屏等场景时，会自动将占位页出栈，只显示主页；
> > 而当应用可绘制区域大于等于600vp、折叠屏由折叠态切换为展开态及平板竖屏转横屏等场景时，会自动补充占位页，形成分栏。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-setPlaceholderPage(info: NavPathInfo): void--><!--Device-MultiNavPathStack-setPlaceholderPage(info: NavPathInfo): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | 占位页页面信息。 |

## size

```TypeScript
size(): int
```

获取栈大小。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-size(): int--><!--Device-MultiNavPathStack-size(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回栈大小。&lt;br/&gt;取值范围：[0, +∞) |

## switchFullScreenState

```TypeScript
switchFullScreenState(isFullScreen?: boolean): boolean
```

切换当前顶栈详情页面的显示模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-switchFullScreenState(isFullScreen?: boolean): boolean--><!--Device-MultiNavPathStack-switchFullScreenState(isFullScreen?: boolean): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isFullScreen | boolean | No | Whether to switch to full screen. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 切换成功或失败。&lt;br/&gt;true：切换成功。&lt;br/&gt;false：切换失败。 |

