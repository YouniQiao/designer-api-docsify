# @ohos.atomicservice.NavPushPathHelper(Defines provides a push method for the target page in the routing table.)

## 子组件

无

## 属性

不支持[通用属性](../arkts-components/arkts-arkui-common-comp.md#common)。

## 事件

不支持[通用事件](../arkts-components/arkts-arkui-common-comp.md#common)

## 导入模块

```TypeScript
import { NavPushPathHelper } from '@kit.ArkUI';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [NavPushPathHelper](arkts-arkui-atomicservice-navpushpathhelper-navpushpathhelper-c.md) | 当跳转的目标[NavDestination](../arkts-components/arkts-arkui-navdestination-comp.md#nav_destination)在不同的hsp分包且未被主包依赖时，首次运行原子化服务只会下载安装主包。此时需要使用NavPushPathHelper先下载安装相应hsp分包，再将指定的[NavDestination](../arkts-components/arkts-arkui-navdestination-comp.md#nav_destination)页面信息入栈或替换当前栈顶页面，从而使[Navigation](../arkts-components/arkts-arkui-navigation-comp.md#navigation)支持动态加载hsp分包后再跳转。 |

## 示例

```TypeScript
主包：
```

```TypeScript
分包hsptest1：
```

```TypeScript
工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}，在route_map.json文件配置如下：
```

```TypeScript
分包hsptest2：
```
