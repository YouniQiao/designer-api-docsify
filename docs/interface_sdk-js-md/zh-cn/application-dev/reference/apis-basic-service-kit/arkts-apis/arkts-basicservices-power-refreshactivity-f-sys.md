# refreshActivity（系统接口）

## 导入模块

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## refreshActivity

```TypeScript
function refreshActivity(reason: string): void
```

刷新设备活动状态（如：重设屏幕超时息屏时间等）。

只有设备在活动状态下生效，设备活动状态见[power.isActive](arkts-basicservices-power-isactive-f.md#isactive)接口。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.REFRESH_USER_ACTION

<!--Device-power-function refreshActivity(reason: string): void--><!--Device-power-function refreshActivity(reason: string): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | string | 是 | 刷新设备活动状态的原因。该参数必须为字符串类型。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. This API cannot work in car devices.<br>**适用版本：** 26.1.0+ |
| 4900201 | The device activity is being refreshed too frequently; the minimum time interval is 100 ms. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 4900101 | Failed to connect to the service. |

## 示例

```TypeScript
try {
    power.refreshActivity('refreshActivity_test');
} catch (err) {
    console.error(`Failed to refresh activity. Code: ${err.code}, message: ${err.message}`);
}
```

