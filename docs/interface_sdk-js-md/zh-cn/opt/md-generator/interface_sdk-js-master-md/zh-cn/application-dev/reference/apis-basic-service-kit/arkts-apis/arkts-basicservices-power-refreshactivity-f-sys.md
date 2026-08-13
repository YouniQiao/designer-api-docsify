# refreshActivity（系统接口）

## refreshActivity

```TypeScript
function refreshActivity(reason: string): void
```

刷新设备活动状态（如：重设屏幕超时息屏时间等）。 只有设备在活动状态下生效，设备活动状态见[power.isActive](arkts-basicservices-power-isactive-f.md#isActive)接口。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.REFRESH_USER_ACTION

<!--Device-power-function refreshActivity(reason: string): void--><!--Device-power-function refreshActivity(reason: string): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reason | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [4900201](../../apis-basic-services-kit/errorcode-power.md#4900201-设备活跃状态刷新间隔过短) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-连接服务失败) |

## 示例

```TypeScript
try {
    power.refreshActivity('refreshActivity_test');
} catch (err) {
    console.error(`Failed to refresh activity. Code: ${err.code}, message: ${err.message}`);
}
```
