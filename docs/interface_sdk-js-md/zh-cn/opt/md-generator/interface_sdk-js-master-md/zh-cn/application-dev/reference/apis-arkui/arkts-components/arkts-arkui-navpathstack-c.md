# NavPathStack

Navigation导航控制器，以栈的数据结构管理Navigation中所有的子页面，并提供栈操作的方法用于控制Navigation中子页面的切换。

从API version 12开始，NavPathStack允许被继承，派生类对象可以替代基类NavPathStack对象使用。使用示例参见  
[示例10](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#示例10定义导航控制器派生类)。

> **说明：**
> 
> 1.连续调用多个导航控制器操作方法时，中间过程会被忽略，显示最终的栈操作结果。

> 例如：在Page1页面先pop再push一个Page1，系统会认为操作前和操作后的结果一致而不进行任何操作，如果需要强行push一个Page1实例，可以设置
> [NavigationOption](arkts-arkui-navigationoptions-i.md)中的launchMode属性值为LaunchMode.NEW_INSTANCE模式。
> 
> 2.不建议开发者通过监听页面生命周期的方式管理自己的导航控制器。
> 
> 3.在应用处于后台状态下，调用NavPathStack的栈操作方法，会在应用再次回到前台状态时触发刷新。

**起始版本：** 10

<!--Device-unnamed-declare class NavPathStack--><!--Device-unnamed-declare class NavPathStack-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## clear

```TypeScript
clear(animated?: boolean): void
```

清除栈中所有页面。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-clear(animated?: boolean): void--><!--Device-NavPathStack-clear(animated?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| animated | boolean | 否 |

## constructor

```TypeScript
constructor()
```

创建NavPathStack对象。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-constructor()--><!--Device-NavPathStack-constructor()-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## disableAnimation

```TypeScript
disableAnimation(value: boolean): void
```

关闭（true）或打开（false）当前Navigation中所有转场动画。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-disableAnimation(value: boolean): void--><!--Device-NavPathStack-disableAnimation(value: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## getAllPathName

```TypeScript
getAllPathName(): Array<string>
```

获取栈中所有NavDestination页面的名称。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-getAllPathName(): Array<string>--><!--Device-NavPathStack-getAllPathName(): Array<string>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| Array&lt;string&gt; |

## getIndexByName

```TypeScript
getIndexByName(name: string): Array<number>
```

获取全部名为name的NavDestination页面的位置索引。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-getIndexByName(name: string): Array<number>--><!--Device-NavPathStack-getIndexByName(name: string): Array<number>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;number&gt; |

## getParamByIndex

```TypeScript
getParamByIndex(index: number): unknown | undefined
```

获取index指定的NavDestination页面的参数信息。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-getParamByIndex(index: number): unknown | undefined--><!--Device-NavPathStack-getParamByIndex(index: number): unknown | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| unknown |

## getParamByName

```TypeScript
getParamByName(name: string): Array<unknown>
```

获取所有名为name的NavDestination页面的参数信息，按页面索引从小到大排序。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-getParamByName(name: string): Array<unknown>--><!--Device-NavPathStack-getParamByName(name: string): Array<unknown>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;unknown&gt; |

## getParent

```TypeScript
getParent(): NavPathStack | null
```

获取父NavPathStack。

当出现Navigation嵌套Navigation的情况时（可以是直接嵌套，也可以是间接嵌套），内部Navigation的NavPathStack能够获取到外层Navigation的NavPathStack。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-getParent(): NavPathStack | null--><!--Device-NavPathStack-getParent(): NavPathStack | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [NavPathStack](arkts-arkui-navpathstack-c.md) |

## getPathStack

```TypeScript
getPathStack(): Array<NavPathInfo>
```

获取当前路由栈中的路由页面信息数组。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-getPathStack(): Array<NavPathInfo>--><!--Device-NavPathStack-getPathStack(): Array<NavPathInfo>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| Array&lt;NavPathInfo&gt; |

## moveIndexToTop

```TypeScript
moveIndexToTop(index: number, animated?: boolean): void
```

将index指定的NavDestination页面移到栈顶。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-moveIndexToTop(index: number, animated?: boolean): void--><!--Device-NavPathStack-moveIndexToTop(index: number, animated?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| animated | boolean | 否 |

## moveToTop

```TypeScript
moveToTop(name: string, animated?: boolean): number
```

将由栈底开始第一个名为name的NavDestination页面移到栈顶。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-moveToTop(name: string, animated?: boolean): number--><!--Device-NavPathStack-moveToTop(name: string, animated?: boolean): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| number |

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

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-pop(animated?: boolean): NavPathInfo | undefined--><!--Device-NavPathStack-pop(animated?: boolean): NavPathInfo | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [NavPathInfo](arkts-arkui-navpathinfo-c.md) |

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

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-pop(result: Object, animated?: boolean): NavPathInfo | undefined--><!--Device-NavPathStack-pop(result: Object, animated?: boolean): NavPathInfo | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | Object | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [NavPathInfo](arkts-arkui-navpathinfo-c.md) |

## popToIndex

```TypeScript
popToIndex(index: number, animated?: boolean): void
```

回退路由栈到index指定的NavDestination页面。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-popToIndex(index: number, animated?: boolean): void--><!--Device-NavPathStack-popToIndex(index: number, animated?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| animated | boolean | 否 |

## popToIndex

```TypeScript
popToIndex(index: number, result: Object, animated?: boolean): void
```

回退路由栈到index指定的NavDestination页面，并触发onPop回调传入页面处理结果。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-popToIndex(index: number, result: Object, animated?: boolean): void--><!--Device-NavPathStack-popToIndex(index: number, result: Object, animated?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| result | Object | 是 |
| animated | boolean | 否 |

## popToName

```TypeScript
popToName(name: string, animated?: boolean): number
```

回退路由栈到栈底第一个名为name的NavDestination页面。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-popToName(name: string, animated?: boolean): number--><!--Device-NavPathStack-popToName(name: string, animated?: boolean): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## popToName

```TypeScript
popToName(name: string, result: Object, animated?: boolean): number
```

回退路由栈到由栈底开始第一个名为name的NavDestination页面，并触发onPop回调传入页面处理结果。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-popToName(name: string, result: Object, animated?: boolean): number--><!--Device-NavPathStack-popToName(name: string, result: Object, animated?: boolean): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| result | Object | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## pushDestination

```TypeScript
pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>
```

将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100005](../errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [100006](../errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushDestination

```TypeScript
pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](arkts-arkui-launchmode-e.md)，来实现不同的行为。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPathStack-pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](arkts-arkui-navigationoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100005](../errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [100006](../errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushDestinationByName

```TypeScript
pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>
```

将name指定的NavDestination页面信息入栈，传递的数据为param，使用Promise异步回调返回接口调用结果。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Object | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100005](../errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [100006](../errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushDestinationByName

```TypeScript
pushDestinationByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): Promise<void>
```

将name指定的NavDestination页面信息入栈，传递的数据为param，并且添加用于页面出栈时处理返回结果的onPop回调，使用Promise异步回调返回接口调用结果。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Object | 是 |
| onPop | import('../api/@ohos.base').Callback&lt;PopInfo&gt; | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100005](../errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [100006](../errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, animated?: boolean): void
```

将info指定的NavDestination页面信息入栈。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-pushPath(info: NavPathInfo, animated?: boolean): void--><!--Device-NavPathStack-pushPath(info: NavPathInfo, animated?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | 是 |
| animated | boolean | 否 |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, options?: NavigationOptions): void
```

将info指定的NavDestination页面信息入栈，具体根据options中指定不同的[LaunchMode](arkts-arkui-launchmode-e.md)，来实现不同的行为。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions): void--><!--Device-NavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](arkts-arkui-navigationoptions-i.md) | 否 |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: unknown, animated?: boolean): void
```

将name指定的NavDestination页面信息入栈，传递的数据为param。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-pushPathByName(name: string, param: unknown, animated?: boolean): void--><!--Device-NavPathStack-pushPathByName(name: string, param: unknown, animated?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | unknown | 是 |
| animated | boolean | 否 |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): void
```

将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-pushPathByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): void--><!--Device-NavPathStack-pushPathByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Object | 是 |
| onPop | import('../api/@ohos.base').Callback&lt;PopInfo&gt; | 是 |
| animated | boolean | 否 |

## removeByIndexes

```TypeScript
removeByIndexes(indexes: Array<number>): number
```

将路由栈内索引值在indexes中的NavDestination页面删除。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-removeByIndexes(indexes: Array<number>): number--><!--Device-NavPathStack-removeByIndexes(indexes: Array<number>): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| indexes | Array&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## removeByName

```TypeScript
removeByName(name: string): number
```

将路由栈内指定name的NavDestination页面删除。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-removeByName(name: string): number--><!--Device-NavPathStack-removeByName(name: string): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## removeByNavDestinationId

```TypeScript
removeByNavDestinationId(navDestinationId: string): boolean
```

将路由栈内指定navDestinationId的NavDestination页面删除。navDestinationId可以在NavDestination的  
[onReady](NavDestinationAttribute#onReady)回调中获取，也可以在  
[NavDestinationInfo](../arkts-apis/arkts-arkui-uiobserver-navdestinationinfo-i.md/arkts-arkui-uiobserver-navdestinationinfo-i.md)中获取。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-removeByNavDestinationId(navDestinationId: string): boolean--><!--Device-NavPathStack-removeByNavDestinationId(navDestinationId: string): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| navDestinationId | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## replaceDestination

```TypeScript
replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

替换路由栈操作。使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](arkts-arkui-launchmode-e.md)，来实现不同的行为。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPathStack-replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](arkts-arkui-navigationoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100005](../errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [100006](../errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, animated?: boolean): void
```

将当前路由栈栈顶退出，将info指定的NavDestination页面信息入栈。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void--><!--Device-NavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | 是 |
| animated | boolean | 否 |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, options?: NavigationOptions): void
```

替换路由栈操作，具体根据options中指定不同的[LaunchMode](arkts-arkui-launchmode-e.md)，来实现不同的行为。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void--><!--Device-NavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](arkts-arkui-navigationoptions-i.md) | 否 |

## replacePathByName

```TypeScript
replacePathByName(name: string, param: Object, animated?: boolean): void
```

将当前路由栈栈顶退出，将name指定的页面入栈。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void--><!--Device-NavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Object | 是 |
| animated | boolean | 否 |

## setInterception

```TypeScript
setInterception(interception: NavigationInterception): void
```

设置Navigation页面跳转拦截回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-setInterception(interception: NavigationInterception): void--><!--Device-NavPathStack-setInterception(interception: NavigationInterception): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| interception | [NavigationInterception](arkts-arkui-navigationinterception-i.md) | 是 |

## setPathStack

```TypeScript
setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void
```

将当前路由栈中的路由页面信息数组更新为指定内容，并实现路由转场。

> **说明：**
> 
> 1. 开发者可以在原有栈的基础上批量添加或删除页面。批量入栈的页面中，只有可见的页面会触发创建，其他页面虽已入栈但不会立即创建，当这些页面变为可见时，才会触发创建。
> 
> 2. 通过批量入栈功能更新的路由栈，各页面的生命周期事件触发顺序为从栈顶到底部依次触发，这与其它入栈接口从栈底到顶部的触发顺序不同。
> 
> 3. 开发者可以通过[NavPathInfo](arkts-arkui-navpathinfo-c.md)中的页面唯一标识符navDestinationId来操作已有页面，该id由系统默认生成且全局唯一（可以通过
> [getPathStack](arkts-arkui-navpathstack-c.md#getpathstack)接口获取，不可主动赋新值）。若该id在当前路由栈中不存在，则表示新增页面，若在当前路由栈中存在，同时对应的name相同，则表示复用已
> 有页面。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void--><!--Device-NavPathStack-setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathStack | Array&lt;NavPathInfo&gt; | 是 |
| animated | boolean | 否 |

## size

```TypeScript
size(): number
```

获取栈大小。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NavPathStack-size(): number--><!--Device-NavPathStack-size(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |
