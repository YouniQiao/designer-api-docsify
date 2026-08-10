# NavPathStack

Navigation导航控制器，以栈的数据结构管理Navigation中所有的子页面，并提供栈操作的方法用于控制Navigation中子页面的切换。

从API version 12开始，NavPathStack允许被继承，派生类对象可以替代基类NavPathStack对象使用。使用示例参见  
[示例10](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation copy.md#示例10定义导航控制器派生类)。

> **说明：**
> 
> 1.连续调用多个导航控制器操作方法时，中间过程会被忽略，显示最终的栈操作结果。

> 例如：在Page1页面先pop再push一个Page1，系统会认为操作前和操作后的结果一致而不进行任何操作，如果需要强行push一个Page1实例，可以设置
> [NavigationOption](../arkts-components/arkts-arkui-navigationoptions-i.md/arkts-arkui-navigationoptions-i.md)中的launchMode属性值为LaunchMode.NEW_INSTANCE模式。
> 
> 2.不建议开发者通过监听页面生命周期的方式管理自己的导航控制器。
> 
> 3.在应用处于后台状态下，调用NavPathStack的栈操作方法，会在应用再次回到前台状态时触发刷新。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class NavPathStack--><!--Device-unnamed-export declare class NavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clear

```TypeScript
clear(animated?: boolean): void
```

清除栈中所有页面。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-clear(animated?: boolean): void--><!--Device-NavPathStack-clear(animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

## constructor

```TypeScript
constructor()
```

创建NavPathStack对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-constructor()--><!--Device-NavPathStack-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableAnimation

```TypeScript
disableAnimation(value: boolean): void
```

关闭（true）或打开（false）当前Navigation中所有转场动画。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-disableAnimation(value: boolean): void--><!--Device-NavPathStack-disableAnimation(value: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | 是否关闭转场动画，&lt;br/&gt;默认值：false&lt;br/&gt;true：关闭转场动画。&lt;br/&gt;false：不关闭转场动画。 |

## getAllPathName

```TypeScript
getAllPathName(): Array<string>
```

获取栈中所有NavDestination页面的名称。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getAllPathName(): Array<string>--><!--Device-NavPathStack-getAllPathName(): Array<string>-End-->

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

<!--Device-NavPathStack-getIndexByName(name: string): Array<int>--><!--Device-NavPathStack-getIndexByName(name: string): Array<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;int&gt; | 返回全部名为name的NavDestination页面的位置索引。 当路由栈中不存在此name，返回空数组。索引取值范围为[0, 路由栈大小-1] |

## getParamByIndex

```TypeScript
getParamByIndex(index: int): Object | null | undefined
```

获取index指定的NavDestination页面的参数信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getParamByIndex(index: int): Object | null | undefined--><!--Device-NavPathStack-getParamByIndex(index: int): Object | null | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | NavDestination页面的位置索引。 索引值从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | Returns the detailed parameter of the NavDestination if it exists in the stack, otherwise returns undefined; |

## getParamByName

```TypeScript
getParamByName(name: string): Array<Object | null | undefined>
```

获取所有名为name的NavDestination页面的参数信息，按页面索引从小到大排序。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getParamByName(name: string): Array<Object | null | undefined>--><!--Device-NavPathStack-getParamByName(name: string): Array<Object | null | undefined>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Object \| null \| undefined&gt; | Returns the detailed parameter of all the NavDestinations. |

## getParent

```TypeScript
getParent(): NavPathStack | null
```

获取父NavPathStack。

当出现Navigation嵌套Navigation的情况时（可以是直接嵌套，也可以是间接嵌套），内部Navigation的NavPathStack能够获取到外层Navigation的NavPathStack。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getParent(): NavPathStack | null--><!--Device-NavPathStack-getParent(): NavPathStack | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | Returns the parent of the current stack. If no parent, it returns null. |

## getPathStack

```TypeScript
getPathStack(): Array<NavPathInfo>
```

获取当前路由栈中的路由页面信息数组。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getPathStack(): Array<NavPathInfo>--><!--Device-NavPathStack-getPathStack(): Array<NavPathInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;NavPathInfo&gt; | 当前路由栈中的路由页面信息数组。 |

## moveIndexToTop

```TypeScript
moveIndexToTop(index: int, animated?: boolean): void
```

将index指定的NavDestination页面移到栈顶。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-moveIndexToTop(index: int, animated?: boolean): void--><!--Device-NavPathStack-moveIndexToTop(index: int, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | NavDestination页面的位置索引。索引值从0开始。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

## moveToTop

```TypeScript
moveToTop(name: string, animated?: boolean): int
```

将由栈底开始第一个名为name的NavDestination页面移到栈顶。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-moveToTop(name: string, animated?: boolean): int--><!--Device-NavPathStack-moveToTop(name: string, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

**Return value:**

| Type | Description |
| --- | --- |
| int | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的当前索引，否则返回-1。 |

## pop

```TypeScript
pop(animated?: boolean): NavPathInfo | undefined
```

弹出路由栈栈顶元素。

> **说明：**
> 
> 连续调用多个导航控制器方法时，中间被pop的页面会被缓存，后续push同名页面时会优先复用该页面，不会走新的页面创建流程。

> 例如：

> pathStack: NavPathStack = new NavPathStack()

> // 初始页面栈为：[A]

> pathStack.pop()

> pathStack.pushPath(A)

> pathStack.pushPath(B)

> // 操作后页面栈为：[A B]

> 此时A页面会被复用，不会走新的创建流程。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pop(animated?: boolean): NavPathInfo | undefined--><!--Device-NavPathStack-pop(animated?: boolean): NavPathInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt; &lt;br&gt;默认值： true。 |

**Return value:**

| Type | Description |
| --- | --- |
| [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Returns the top NavPathInfo if the stack is not empty, otherwise returns undefined. |

## pop

```TypeScript
pop(result: Object, animated?: boolean): NavPathInfo | undefined
```

弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

> **说明：**
> 
> 连续调用多个导航控制器方法时，中间被pop的页面会被缓存，后续push同名页面时会优先复用该页面，不会走新的页面创建流程。

> 例如：

> pathStack: NavPathStack = new NavPathStack()

> // 初始页面栈为：[A]

> pathStack.pop()

> pathStack.pushPath(A)

> pathStack.pushPath(B)

> // 操作后页面栈为：[A B]

> 此时A页面会被复用，不会走新的创建流程。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pop(result: Object, animated?: boolean): NavPathInfo | undefined--><!--Device-NavPathStack-pop(result: Object, animated?: boolean): NavPathInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | Object | Yes | 页面自定义处理结果。不支持boolean类型。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt; &lt;br&gt;默认值： true。 |

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

<!--Device-NavPathStack-popToIndex(index: int, animated?: boolean): void--><!--Device-NavPathStack-popToIndex(index: int, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | NavDestination页面的位置索引。索引值从0开始。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

## popToIndex

```TypeScript
popToIndex(index: int, result: Object, animated?: boolean): void
```

回退路由栈到index指定的NavDestination页面，并触发onPop回调传入页面处理结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-popToIndex(index: int, result: Object, animated?: boolean): void--><!--Device-NavPathStack-popToIndex(index: int, result: Object, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | NavDestination页面的位置索引。索引值从0开始。 |
| result | Object | Yes | 页面自定义处理结果。不支持boolean类型。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

## popToName

```TypeScript
popToName(name: string, animated?: boolean): int
```

回退路由栈到由栈底开始第一个名为name的NavDestination页面。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-popToName(name: string, animated?: boolean): int--><!--Device-NavPathStack-popToName(name: string, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

**Return value:**

| Type | Description |
| --- | --- |
| int | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。 |

## popToName

```TypeScript
popToName(name: string, result: Object, animated?: boolean): int
```

回退路由栈到由栈底开始第一个名为name的NavDestination页面，并触发onPop回调传入页面处理结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-popToName(name: string, result: Object, animated?: boolean): int--><!--Device-NavPathStack-popToName(name: string, result: Object, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| result | Object | Yes | 页面自定义处理结果。不支持boolean类型。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

**Return value:**

| Type | Description |
| --- | --- |
| int | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。 |

## pushDestination

```TypeScript
pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>
```

将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果。

> **说明：**
> 
> 不建议在[aboutToAppear](../../../reference/apis-arkui/arkui-ts/ts-custom-component-lifecycle.md#abouttoappear)中使用栈
> 操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | NavDestination页面的信息。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 异步返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

## pushDestination

```TypeScript
pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](../arkts-components/arkts-arkui-launchmode-e.md/arkts-arkui-launchmode-e.md)，来实现不同的行为。

> **说明：**
> 
> 不建议在[aboutToAppear](../../../reference/apis-arkui/arkui-ts/ts-custom-component-lifecycle.md#abouttoappear)中使用栈
> 操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPathStack-pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | NavDestination页面的信息。 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | No | 路由栈操作选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 异常返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

## pushDestinationByName

```TypeScript
pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>
```

将name指定的NavDestination页面信息入栈，传递的数据为param，使用Promise异步回调返回接口调用结果。

> **说明：**
> 
> 不建议在[aboutToAppear](../../../reference/apis-arkui/arkui-ts/ts-custom-component-lifecycle.md#abouttoappear)中使用栈
> 操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| param | Object | Yes | 开发者设置的NavDestination页面详细参数。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 异常返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

## pushDestinationByName

```TypeScript
pushDestinationByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>
```

将name指定的NavDestination页面信息入栈，传递的数据为param，并且添加用于页面出栈时处理返回结果的onPop回调，使用Promise异步回调返回接口调用结果。

> **说明：**
> 
> 不建议在[aboutToAppear](../../../reference/apis-arkui/arkui-ts/ts-custom-component-lifecycle.md#abouttoappear)中使用栈
> 操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| param | Object | Yes | 开发者设置的NavDestination页面详细参数。 |
| onPop | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;PopInfo&gt; | Yes | Callback回调，用于页面出栈时处理返回结果。仅 [pop](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#pop)、 [popToName](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#poptoname)、 [popToIndex](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#poptoindex)中设置result参数后触发。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 异常返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, animated?: boolean): void
```

将info指定的NavDestination页面信息入栈。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushPath(info: NavPathInfo, animated?: boolean): void--><!--Device-NavPathStack-pushPath(info: NavPathInfo, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | NavDestination页面的信息。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;传入参数非法时，按true处理。 |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, options?: NavigationOptions): void
```

将info指定的NavDestination页面信息入栈，具体根据options中指定不同的[LaunchMode](../arkts-components/arkts-arkui-launchmode-e.md/arkts-arkui-launchmode-e.md)，来实现不同的行为。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions): void--><!--Device-NavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | NavDestination页面的信息。 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | No | 路由栈操作选项。 |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: Object | null | undefined, animated?: boolean): void
```

将name指定的NavDestination页面信息入栈，传递的数据为param。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushPathByName(name: string, param: Object | null | undefined, animated?: boolean): void--><!--Device-NavPathStack-pushPathByName(name: string, param: Object | null | undefined, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| param | Object \| null \| undefined | Yes | 开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。&lt;br/&gt;取值为undefined时，页面信 息无效。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): void
```

将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushPathByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): void--><!--Device-NavPathStack-pushPathByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| param | Object | Yes | 开发者设置的NavDestination页面详细参数。 |
| onPop | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;PopInfo&gt; | Yes | Callback回调，用于页面出栈时触发该回调处理返回结果。仅 [pop](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#pop)、 [popToName](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#poptoname)、 [popToIndex](../arkts-components/arkts-arkui-navpathstack-c.md/arkts-arkui-navpathstack-c.md#poptoindex)中设置result参数后触发。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

## removeByIndexes

```TypeScript
removeByIndexes(indexes: Array<int>): int
```

将路由栈内索引值在indexes中的NavDestination页面删除。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-removeByIndexes(indexes: Array<int>): int--><!--Device-NavPathStack-removeByIndexes(indexes: Array<int>): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indexes | Array&lt;int&gt; | Yes | 待删除NavDestination页面的索引值数组。索引值从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回删除的NavDestination页面数量。 |

## removeByName

```TypeScript
removeByName(name: string): int
```

将路由栈内指定name的NavDestination页面删除。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-removeByName(name: string): int--><!--Device-NavPathStack-removeByName(name: string): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 删除的NavDestination页面的名字。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回删除的NavDestination页面数量。 |

## removeByNavDestinationId

```TypeScript
removeByNavDestinationId(navDestinationId: string): boolean
```

将路由栈内指定navDestinationId的NavDestination页面删除。navDestinationId可以在NavDestination的  
[onReady](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#onready11)回调中获取，也可以在  
[NavDestinationInfo](arkts-arkui-uiobserver-navdestinationinfo-i.md)中获取。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-removeByNavDestinationId(navDestinationId: string): boolean--><!--Device-NavPathStack-removeByNavDestinationId(navDestinationId: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| navDestinationId | string | Yes | 删除的NavDestination页面的唯一标识符navDestinationId。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回是否成功删除该页面，&lt;br/&gt;true：删除成功。&lt;br/&gt;false：删除失败。 |

## replaceDestination

```TypeScript
replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

替换路由栈操作。使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](../arkts-components/arkts-arkui-launchmode-e.md/arkts-arkui-launchmode-e.md)，来实现不同的行为。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPathStack-replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | NavDestination页面的信息。 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | No | 路由栈操作选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 异常返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, animated?: boolean): void
```

将当前路由栈栈顶退出，将info指定的NavDestination页面信息入栈。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void--><!--Device-NavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | 新栈顶页面参数信息。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, options?: NavigationOptions): void
```

替换路由栈操作，具体根据options中指定不同的[LaunchMode](../arkts-components/arkts-arkui-launchmode-e.md/arkts-arkui-launchmode-e.md)，来实现不同的行为。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void--><!--Device-NavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes | 新栈顶页面参数信息。 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | No | 路由栈操作选项。 |

## replacePathByName

```TypeScript
replacePathByName(name: string, param: Object, animated?: boolean): void
```

将当前路由栈栈顶退出，将name指定的页面入栈。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void--><!--Device-NavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | NavDestination页面名称。 |
| param | Object | Yes | 开发者设置的NavDestination页面详细参数。 |
| animated | boolean | No | 是否支持转场动画。&lt;br/&gt;true：支持转场动画；false：不支持转场动画。&lt;br/&gt;默认值：true |

## setInterception

```TypeScript
setInterception(interception: NavigationInterception): void
```

设置Navigation页面跳转拦截回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-setInterception(interception: NavigationInterception): void--><!--Device-NavPathStack-setInterception(interception: NavigationInterception): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| interception | [NavigationInterception](arkts-arkui-navigation-navigationinterception-i.md) | Yes | 设置Navigation跳转拦截对象。 |

## setPathStack

```TypeScript
setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void
```

将当前路由栈中的路由页面信息数组更新为指定内容，并实现路由转场。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void--><!--Device-NavPathStack-setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathStack | Array&lt;NavPathInfo&gt; | Yes | 设置当前路由栈中的路由页面信息数组。&lt;br/&gt;**说明：**&lt;br/&gt;数组长度无限制。 |
| animated | boolean | No | 是否开启转场动画。&lt;br/&gt;true：开启转场动画；false：不开启转场动画。&lt;br /&gt; 默认值：true |

## size

```TypeScript
size(): int
```

获取栈大小。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-size(): int--><!--Device-NavPathStack-size(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回栈大小。&lt;br/&gt;取值范围：[0, +∞) |

