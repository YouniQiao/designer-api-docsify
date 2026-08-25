# onSteadyStandingDetect

## 导入模块

```TypeScript
import { deviceStatus } from '@kit.MultimodalAwarenessKit';
```

## onSteadyStandingDetect

```TypeScript
function onSteadyStandingDetect(callback: Callback<SteadyStandingStatus>): void
```

订阅设备静止姿态感知（支架态）事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MultimodalAwareness.DeviceStatus

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SteadyStandingStatus](arkts-multimodalawareness-devicestatus-steadystandingstatus-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [32500001](../errorcode-deviceStatus.md#32500001-服务异常) |
| [32500002](../errorcode-deviceStatus.md#32500002-订阅失败) |

**示例**

```TypeScript
try {
     deviceStatus.onSteadyStandingDetect((data:deviceStatus.SteadyStandingStatus) => {
         console.info('now status = ' + data);
     });
 } catch (err) {
     console.info('on failed, err = ' + err);
 }
```
