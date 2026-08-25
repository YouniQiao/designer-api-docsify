# setPowerKeyFilteringStrategy（系统接口）

## 导入模块

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## setPowerKeyFilteringStrategy

```TypeScript
function setPowerKeyFilteringStrategy(strategy: PowerKeyFilteringStrategy): void
```

设置电源键过滤策略，在电源服务订阅电源键事件后，用于配置电源键事件的处理方式。电源键过滤策略见[power.PowerKeyFilteringStrategy](arkts-basicservices-power-powerkeyfilteringstrategy-e.md)接口。

**起始版本：** 21

**需要权限：** ohos.permission.POWER_MANAGER

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strategy | [PowerKeyFilteringStrategy](arkts-basicservices-power-powerkeyfilteringstrategy-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4900101](../errorcode-power.md#4900101-连接服务失败) |
