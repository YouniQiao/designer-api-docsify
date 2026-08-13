# getBatteryConfig（系统接口）

## getBatteryConfig

```TypeScript
function getBatteryConfig(sceneName: string): string
```

按场景名称查询电池配置。

**起始版本：** 11

**废弃版本：** -1

<!--Device-batteryInfo-function getBatteryConfig(sceneName: string): string--><!--Device-batteryInfo-function getBatteryConfig(sceneName: string): string-End-->

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [sceneName](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-unifiedgroupinfo-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5100101](../../apis-basic-services-kit/errorcode-battery-info.md#5100101-连接服务失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';

let sceneName = 'xxx';
let result = batteryInfo.getBatteryConfig(sceneName);

console.info('The result is: ' + result);
```
