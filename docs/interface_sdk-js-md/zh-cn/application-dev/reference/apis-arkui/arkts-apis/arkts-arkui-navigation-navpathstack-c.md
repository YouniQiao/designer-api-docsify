# NavPathStack

Navigation导航控制器，以栈的数据结构管理Navigation中所有的子页面，并提供栈操作的方法用于控制Navigation中子页面的切换。从API version 12开始，NavPathStack允许被继承，派生类对象可以替代基类NavPathStack对象使用。使用示例参见 示例10。

> **说明：**&gt;
> 1.连续调用多个导航控制器操作方法时，中间过程会被忽略，显示最终的栈操作结果。

> 例如：在Page1页面先pop再push一个Page1，系统会认为操作前和操作后的结果一致而不进行任何操作，如果需要强行push一个Page1实例，可以设置
> [NavigationOption](arkts-arkui-navigation-navigationoptions-i.md)中的launchMode属性值为LaunchMode.NEW_INSTANCE模式。&gt;
> 2.不建议开发者通过监听页面生命周期的方式管理自己的导航控制器。&gt;
> 3.在应用处于后台状态下，调用NavPathStack的栈操作方法，会在应用再次回到前台状态时触发刷新。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## clear

```TypeScript
clear(animated?: boolean): void
```

清除栈中所有页面。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

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

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## disableAnimation

```TypeScript
disableAnimation(value: boolean): void
```

关闭（true）或打开（false）当前Navigation中所有转场动画。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

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

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## getIndexByName

```TypeScript
getIndexByName(name: string): Array<int>
```

获取全部名为name的NavDestination页面的位置索引。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;int & gt; |

## getParamByIndex

```TypeScript
getParamByIndex(index: int): Object | null | undefined
```

获取index指定的NavDestination页面的参数信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |

**返回值：**

| 类型 |
| --- |
| Object \| null \| undefined |

## getParamByName

```TypeScript
getParamByName(name: string): Array<Object | null | undefined>
```

获取所有名为name的NavDestination页面的参数信息，按页面索引从小到大排序。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;Object \ | null \| undefined & gt; |

## getParent

```TypeScript
getParent(): NavPathStack | null
```

获取父NavPathStack。当出现Navigation嵌套Navigation的情况时（可以是直接嵌套，也可以是间接嵌套），内部Navigation的NavPathStack能够获取到外层Navigation的NavPathStack。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) \| null |

## getPathStack

```TypeScript
getPathStack(): Array<NavPathInfo>
```

获取当前路由栈中的路由页面信息数组。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| Array&lt;[NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md)&gt; |

## moveIndexToTop

```TypeScript
moveIndexToTop(index: int, animated?: boolean): void
```

将index指定的NavDestination页面移到栈顶。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| animated | boolean | 否 |

## moveToTop

```TypeScript
moveToTop(name: string, animated?: boolean): int
```

将由栈底开始第一个名为name的NavDestination页面移到栈顶。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| int |

## pop

```TypeScript
pop(animated?: boolean): NavPathInfo | undefined
```

弹出路由栈栈顶元素。

> **说明：**&gt;
> 连续调用多个导航控制器方法时，中间被pop的页面会被缓存，后续push同名页面时会优先复用该页面，不会走新的页面创建流程。

> 例如：

> pathStack: NavPathStack = new NavPathStack()

> // 初始页面栈为：[A]

> pathStack.pop()

> pathStack.pushPath(A)

> pathStack.pushPath(B)

> // 操作后页面栈为：[A B]

> 此时A页面会被复用，不会走新的创建流程。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) \| undefined |

## pop

```TypeScript
pop(result: Object, animated?: boolean): NavPathInfo | undefined
```

弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

> **说明：**&gt;
> 连续调用多个导航控制器方法时，中间被pop的页面会被缓存，后续push同名页面时会优先复用该页面，不会走新的页面创建流程。

> 例如：

> pathStack: NavPathStack = new NavPathStack()

> // 初始页面栈为：[A]

> pathStack.pop()

> pathStack.pushPath(A)

> pathStack.pushPath(B)

> // 操作后页面栈为：[A B]

> 此时A页面会被复用，不会走新的创建流程。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | Object | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) \| undefined |

## popToIndex

```TypeScript
popToIndex(index: int, animated?: boolean): void
```

回退路由栈到index指定的NavDestination页面。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| animated | boolean | 否 |

## popToIndex

```TypeScript
popToIndex(index: int, result: Object, animated?: boolean): void
```

回退路由栈到index指定的NavDestination页面，并触发onPop回调传入页面处理结果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| result | Object | 是 |
| animated | boolean | 否 |

## popToName

```TypeScript
popToName(name: string, animated?: boolean): int
```

回退路由栈到由栈底开始第一个名为name的NavDestination页面。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| int |

## popToName

```TypeScript
popToName(name: string, result: Object, animated?: boolean): int
```

回退路由栈到由栈底开始第一个名为name的NavDestination页面，并触发onPop回调传入页面处理结果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| int |

## pushDestination

```TypeScript
pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>
```

将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果。

> **说明：**&gt;
> 不建议在aboutToAppear中使用栈
> 操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [100005](../errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [100006](../errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushDestination

```TypeScript
pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](arkts-arkui-navigation-launchmode-e.md)，来实现不同的行为。

> **说明：**&gt;
> 不建议在aboutToAppear中使用栈
> 操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [100005](../errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [100006](../errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushDestinationByName

```TypeScript
pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>
```

将name指定的NavDestination页面信息入栈，传递的数据为param，使用Promise异步回调返回接口调用结果。

> **说明：**&gt;
> 不建议在aboutToAppear中使用栈
> 操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [100005](../errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [100006](../errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushDestinationByName

```TypeScript
pushDestinationByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>
```

将name指定的NavDestination页面信息入栈，传递的数据为param，并且添加用于页面出栈时处理返回结果的onPop回调，使用Promise异步回调返回接口调用结果。

> **说明：**&gt;
> 不建议在aboutToAppear中使用栈
> 操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Object | 是 |
| onPop | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PopInfo](arkts-arkui-navigation-popinfo-i.md)&gt; | 是 |
| animated | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [100005](../errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [100006](../errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, animated?: boolean): void
```

将info指定的NavDestination页面信息入栈。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) | 是 |
| animated | boolean | 否 |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, options?: NavigationOptions): void
```

将info指定的NavDestination页面信息入栈，具体根据options中指定不同的[LaunchMode](arkts-arkui-navigation-launchmode-e.md)，来实现不同的行为。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | 否 |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: Object | null | undefined, animated?: boolean): void
```

将name指定的NavDestination页面信息入栈，传递的数据为param。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Object \| null \| undefined | 是 |
| animated | boolean | 否 |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): void
```

将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| param | Object | 是 |
| onPop | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PopInfo](arkts-arkui-navigation-popinfo-i.md)&gt; | 是 |
| animated | boolean | 否 |

## removeByIndexes

```TypeScript
removeByIndexes(indexes: Array<int>): int
```

将路由栈内索引值在indexes中的NavDestination页面删除。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| indexes | Array & lt;int & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## removeByName

```TypeScript
removeByName(name: string): int
```

将路由栈内指定name的NavDestination页面删除。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## removeByNavDestinationId

```TypeScript
removeByNavDestinationId(navDestinationId: string): boolean
```

将路由栈内指定navDestinationId的NavDestination页面删除。navDestinationId可以在NavDestination的 onReady回调中获取，也可以在 [NavDestinationInfo](arkts-arkui-uiobserver-navdestinationinfo-i.md)中获取。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

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

替换路由栈操作。使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](arkts-arkui-navigation-launchmode-e.md)，来实现不同的行为。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [100005](../errorcode-router.md#100005-navigation跳转时未注册builder函数) |
| [100006](../errorcode-router.md#100006-navigation跳转时目标页面不存在navdestination组件) |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, animated?: boolean): void
```

将当前路由栈栈顶退出，将info指定的NavDestination页面信息入栈。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) | 是 |
| animated | boolean | 否 |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, options?: NavigationOptions): void
```

替换路由栈操作，具体根据options中指定不同的[LaunchMode](arkts-arkui-navigation-launchmode-e.md)，来实现不同的行为。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) | 是 |
| options | [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | 否 |

## replacePathByName

```TypeScript
replacePathByName(name: string, param: Object, animated?: boolean): void
```

将当前路由栈栈顶退出，将name指定的页面入栈。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

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

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| interception | [NavigationInterception](arkts-arkui-navigation-navigationinterception-i.md) | 是 |

## setPathStack

```TypeScript
setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void
```

将当前路由栈中的路由页面信息数组更新为指定内容，并实现路由转场。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathStack | Array&lt;[NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md)&gt; | 是 |
| animated | boolean | 否 |

## size

```TypeScript
size(): int
```

获取栈大小。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| int |
