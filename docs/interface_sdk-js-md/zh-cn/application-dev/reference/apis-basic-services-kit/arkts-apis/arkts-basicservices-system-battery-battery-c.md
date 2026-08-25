# Battery

该模块提供充电状态及剩余电量的查询功能。

**起始版本：** 3

**废弃版本：** 6

**系统能力：** SystemCapability.PowerManager.BatteryManager.Lite

## 导入模块

```TypeScript
import { Battery, BatteryResponse, GetStatusOptions } from 'kits/@kit.BasicServicesKit';
```

## getStatus

```TypeScript
static getStatus(options?: GetStatusOptions): void
```

获取设备当前的充电状态及剩余电量。

**起始版本：** 3

**废弃版本：** 6

**系统能力：** SystemCapability.PowerManager.BatteryManager.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GetStatusOptions](arkts-basicservices-system-battery-getstatusoptions-i.md) | 否 |
