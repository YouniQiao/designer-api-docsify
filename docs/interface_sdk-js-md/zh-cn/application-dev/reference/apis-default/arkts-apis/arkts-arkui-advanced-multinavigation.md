# @ohos.arkui.advanced.MultiNavigation

## 导入模块

```TypeScript
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [MultiNavPathStack](arkts-arkui-advanced-multinavigation-multinavpathstack-c.md) | 当前，MultiNavigation的路由栈仅支持由使用方自行创建，不支持通过回调方式获取。请勿使用NavDestination的 [onReady](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#onready11)等类似事件或接口来获取 NavPathStack并进行栈操作，因为这可能会导致不可预知的问题。 |

### 结构体

| 名称 | 说明 |
| --- | --- |
| [MultiNavigation](arkts-arkui-advanced-multinavigation-multinavigation-s.md) | MultiNavigation({navDestination: PageMapBuilder \| undefined, multiStack: MultiNavPathStack, onNavigationModeChange?: OnNavigationModeChangeCallback, onHomeShowOnTop?: OnHomeShowOnTopCallback}) |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [SplitPolicy](arkts-arkui-advanced-multinavigation-splitpolicy-e.md) | 表示MultiNavigation中页面的类型。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [OnHomeShowOnTopCallback](arkts-onhomeshowontopcallback-t.md) | 当主页在栈顶显示时触发的回调函数。 |
| [OnNavigationModeChangeCallback](arkts-onnavigationmodechangecallback-t.md) | 当MultiNavigation的mode变化时触发的回调函数。 |

