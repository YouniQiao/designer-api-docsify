# TabsController

Tabs组件的控制器，用于控制Tabs组件进行页签切换。不支持一个TabsController控制多个Tabs组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## changeIndex

```TypeScript
changeIndex(value: int): void
```

控制Tabs切换到指定页签。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

## constructor

```TypeScript
constructor()
```

TabsController的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## preloadItems

```TypeScript
preloadItems(indices: Array<int> | undefined): Promise<void>
```

控制Tabs预加载指定子节点。调用该接口后会一次性加载所有指定的子节点，因此为了性能考虑，建议分批加载子节点。

> **说明：**&gt;
> - Tabs的preloadItems需要在Tabs创建之后去调用，首次预加载推荐在Tabs的
> onAppear生命周期中去控制。&gt;
> - 如果TabsController对象未绑定任何Tabs组件，直接调用该接口，会抛出JS异常。因此使用该接口时，建议通过try-catch捕获异常。&gt;
> - 使用preloadItems预加载标签页时，若需自定义TabBar上的显示内容，推荐使用ComponentContent实现，使用示例请参考
> [示例9](../../../reference/apis-arkui/arkui-ts/ts-container-tabcontent.md#示例9通过componentcontent设置tabbar)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| indices | Array & lt;int & gt; \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setTabBarOpacity

```TypeScript
setTabBarOpacity(opacity: double): void
```

设置TabBar的不透明度。

> **说明：**&gt;
> 当使用
> [bindTabsToScrollable](arkts-arkui-arkui-uicontext-uicontext-c.md#bindtabstoscrollable)
> 或
> [bindTabsToNestedScrollable](arkts-arkui-arkui-uicontext-uicontext-c.md#bindtabstonestedscrollable)
> 等接口绑定了Tabs组件和可滚动容器组件后，在滑动可滚动容器组件时，会触发所有与其绑定的Tabs组件的TabBar的显示和隐藏动效，调用setTabBarOpacity接口设置的TabBar不透明度会失效。因此不建议同时使
> 用bindTabsToScrollable、bindTabsToNestedScrollable和setTabBarOpacity接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| opacity | double | 是 |

## setTabBarTranslate

```TypeScript
setTabBarTranslate(translate: TranslateOptions): void
```

设置TabBar的平移距离。

> **说明：**&gt;
> 当使用
> [bindTabsToScrollable](arkts-arkui-arkui-uicontext-uicontext-c.md#bindtabstoscrollable)
> 或
> [bindTabsToNestedScrollable](arkts-arkui-arkui-uicontext-uicontext-c.md#bindtabstonestedscrollable)
> 等接口绑定了Tabs组件和可滚动容器组件后，在滑动可滚动容器组件时，会触发所有与其绑定的Tabs组件的TabBar的显示和隐藏动效，调用setTabBarTranslate接口设置的TabBar平移距离会失效。因此不建议同
> 时使用bindTabsToScrollable、bindTabsToNestedScrollable和setTabBarTranslate接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| translate | [TranslateOptions](../arkts-components/arkts-arkui-translateoptions-i.md) | 是 |
