# @ohos.atomicservice.NavPushPathHelper(Defines provides a push method for the target page in the routing table.)

###### 子组件
 无
 ###### 属性
 不支持[通用属性](./@internal/component/ets/common)。
 ###### 事件
 不支持[通用事件](./@internal/component/ets/common)


## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [NavPushPathHelper](arkts-arkui-atomicservice-navpushpathhelper-navpushpathhelper-c.md) | 当跳转的目标[NavDestination](./@internal/component/ets/nav_destination)在不同的hsp分包且未被主包依赖时，首次运行原子化服务只会下载安装主包。此时需要使用NavPushPathHelper先下载安装相应hsp分包，再将指定的[NavDestination](./@internal/component/ets/nav_destination)页面信息入栈或替换当前栈顶页面，从而使[Navigation](./@internal/component/ets/navigation)支持动态加载hsp分包后再跳转。 |

