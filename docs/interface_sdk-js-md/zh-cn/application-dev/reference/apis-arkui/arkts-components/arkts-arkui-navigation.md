# Navigation

Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（ NavDestination的子组件），首页和非首页通过路由进行切换。
> **说明：**
> - 该组件从API version 11开始默认支持安全区避让特性(默认值为：expandSafeArea(> [SafeAreaType.SYSTEM, SafeAreaType.KEYBOARD, SafeAreaType.CUTOUT], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]))，开发者可以重> 写该属性覆盖默认行为，API version 11之前的版本需配合[expandSafeArea](arkts-arkui-commonmethod-c.md#expandsafearea)属性实现安全区避让。>> - [NavBar](arkts-arkui-navbar-t.md)嵌套使用Navigation时，内层NavDestination的生命周期不和外层NavDestination以及全模态的生命周期进行联动。>> - Navigation未设置主副标题（[title](arkts-arkui-navigation-attribute.md#title)或[subTitle](arkts-arkui-navigation-attribute.md#subtitle)）且> [hideBackButton](arkts-arkui-navigation-attribute.md#hidebackbutton)属性设置为true时，不显示标题栏。>> - Navigation的子页面切换时，新页面会主动请求焦点。>> - 不建议在aboutToAppear中使用栈操作，此时的页面还未构建完成，会导致白屏或跳转失败等问题。

## 子组件

可以包含子组件。从API version 9开始，推荐与NavRouter组件搭配使用。从API version 10开始，推荐使用[NavPathStack](arkts-arkui-navpathstack-c.md)配合[navDestination](arkts-arkui-navigation-attribute.md#navdestination)属 性进行页面路由。

## Navigation

```TypeScript
Navigation()
```

创建路由导航的根视图容器，适用于使用NavRouter组件进行页面路由。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## Navigation

```TypeScript
Navigation(pathInfos: NavPathStack)
```

绑定导航控制器到Navigation组件，适用于使用[NavPathStack](arkts-arkui-navpathstack-c.md)配合 [navDestination](arkts-arkui-navigation-attribute.md#navdestination)属性进行页面路由。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navpathstack-c.md) | 是 |

## Navigation

```TypeScript
Navigation(pathInfos: NavPathStack, homeDestination: HomePathInfo)
```

绑定路由栈到Navigation组件，指定一个NavDestination作为Navigation的导航页（主页），适用于使用[NavPathStack](arkts-arkui-navpathstack-c.md)配合 [navDestination](arkts-arkui-navigation-attribute.md#navdestination)属性或者系统路由表进行页面路由。使用示例参考 示例16（Navigation使用NavDestination作为导航页）。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navpathstack-c.md) | 是 |
| homeDestination | [HomePathInfo](arkts-arkui-homepathinfo-i.md) | 是 |

## 汇总

### 接口

| 名称 |
| --- |

### 类型

| 名称 |
| --- |

### 枚举

| 名称 |
| --- |
