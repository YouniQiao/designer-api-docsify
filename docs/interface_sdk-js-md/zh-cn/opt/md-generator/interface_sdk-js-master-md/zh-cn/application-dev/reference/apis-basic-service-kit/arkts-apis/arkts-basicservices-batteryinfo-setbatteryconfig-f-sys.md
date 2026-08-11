# setBatteryConfig（系统接口）

## setBatteryConfig

```TypeScript
function setBatteryConfig(sceneName: string, sceneValue: string): number
```

按场景名称设置电池配置。

**起始版本：** 11

<!--Device-batteryInfo-function setBatteryConfig(sceneName: string, sceneValue: string): number--><!--Device-batteryInfo-function setBatteryConfig(sceneName: string, sceneValue: string): number-End-->

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sceneName | string | 是 |
| sceneValue | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [5100101](../../apis-basic-services-kit/errorcode-battery-info.md#5100101-连接服务失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';

let sceneName = 'xxx';
let sceneValue = '0';
let result = batteryInfo.setBatteryConfig(sceneName, sceneValue);

console.info('The result is: ' + result);
```
