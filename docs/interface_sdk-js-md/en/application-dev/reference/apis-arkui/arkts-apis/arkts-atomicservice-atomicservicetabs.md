# @ohos.atomicservice.AtomicServiceTabs(Provides an advanced struct of tabs for atomic services)

###### 子组件
 无。
 ###### 属性
 不支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)。


## Modules to Import

```TypeScript
import { TabBarPosition, TabBarOptions, AtomicServiceTabs, TabContentBuilder, OnContentWillChangeCallback } from 'kits/@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [TabBarOptions](arkts-arkui-atomicservice-atomicservicetabs-tabbaroptions-c.md) | 页签选项。 |

### Structs

| Name | Description |
| --- | --- |
| [AtomicServiceTabs](arkts-arkui-atomicservice-atomicservicetabs-atomicservicetabs-s.md) | AtomicServiceTabs高级组件，对Tabs组件中不需要暴露给用户进行自定义的属性进行简化，限制最多显示5个页签，固定页签的样式、位置和大小。 |

### Enums

| Name | Description |
| --- | --- |
| [TabBarPosition](arkts-arkui-atomicservice-atomicservicetabs-tabbarposition-e.md) | 设置页签栏位置，默认值为TabBarPosition.BOTTOM。 |

### Types

| Name | Description |
| --- | --- |
| [OnContentWillChangeCallback](arkts-arkui-oncontentwillchangecallback-t.md) | 页面内容即将发生变化时触发的回调函数，用于拦截页面切换，开发者可通过返回值控制是否允许切换。 |
| [TabContentBuilder](arkts-arkui-tabcontentbuilder-t.md) | 内容视图构建器，用于构建TabContent页签内容的函数。 |

