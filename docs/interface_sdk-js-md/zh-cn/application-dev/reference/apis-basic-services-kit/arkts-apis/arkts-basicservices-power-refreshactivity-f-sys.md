# refreshActivity（系统接口）

## 导入模块

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## refreshActivity

```TypeScript
function refreshActivity(reason: string): void
```

刷新设备活动状态（如：重设屏幕超时灭屏时间等）。<br><br>此接口仅在设备活动状态下生效。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.REFRESH_USER_ACTION

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reason | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4900101](../errorcode-power.md#4900101-连接服务失败) |
| [4900201](../errorcode-power.md#4900201-设备活跃状态刷新间隔过短) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

**示例**

```TypeScript
try {
    power.refreshActivity('refreshActivity_test');
} catch(err) {
    console.error('refreshActivity failed, err: ' + err);
}
```
