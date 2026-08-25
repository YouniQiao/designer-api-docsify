# getBatteryStats（系统接口）

## 导入模块

```TypeScript
import { batteryStats } from 'kits/@kit.BasicServicesKit';
```

## getBatteryStats

```TypeScript
function getBatteryStats(): Promise<Array<BatteryStatsInfo>>
```

获取耗电信息列表，用于电池监控应用查看各应用及硬件的耗电情况。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.PowerManager.BatteryStatistics

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[BatteryStatsInfo](arkts-basicservices-batterystats-batterystatsinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4600101](../errorcode-batteryStatistics.md#4600101-连接服务失败) |


## getBatteryStats

```TypeScript
function getBatteryStats(callback: AsyncCallback<Array<BatteryStatsInfo>>): void
```

获取耗电信息列表，用于电池监控应用查看各应用及硬件的耗电情况。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.PowerManager.BatteryStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BatteryStatsInfo](arkts-basicservices-batterystats-batterystatsinfo-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4600101](../errorcode-batteryStatistics.md#4600101-连接服务失败) |
