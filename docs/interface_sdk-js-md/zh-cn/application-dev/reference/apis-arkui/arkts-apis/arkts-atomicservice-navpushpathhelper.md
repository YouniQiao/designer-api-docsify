# @ohos.atomicservice.NavPushPathHelper

## 导入模块

```TypeScript
import { NavPushPathHelper } from '@kit.ArkUI';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [NavPushPathHelper](arkts-arkui-atomicservice-navpushpathhelper-navpushpathhelper-c.md) | 当跳转的目标[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)在不同的hsp分包，且未被主包依赖，首次运行元服务只会下载安装主包，需要使用NavPushPathHelper先下载安装相应hsp分包，再将指定的[NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面信息入栈。使[Navigation](../../apis-arkui/arkts-components/arkts-arkui-navigation-i)支持动态加载hsp分包后再跳转。 |

