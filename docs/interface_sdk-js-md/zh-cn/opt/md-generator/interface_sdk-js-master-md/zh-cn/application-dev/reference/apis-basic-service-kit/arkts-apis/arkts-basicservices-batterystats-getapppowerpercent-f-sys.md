# getAppPowerPercent（系统接口）

## 导入模块

```TypeScript
```

## getAppPowerPercent

```TypeScript
function getAppPowerPercent(uid: number): number
```

获取应用的耗电百分比。

**起始版本：** 23

<!--Device-batteryStats-function getAppPowerPercent(uid: int): double--><!--Device-batteryStats-function getAppPowerPercent(uid: int): double-End-->

**系统能力：** SystemCapability.PowerManager.BatteryStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4600101](../../apis-basic-services-kit/errorcode-batteryStatistics.md#4600101-连接服务失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
try {
    let percent = batteryStats.getAppPowerPercent(10021); // 10021为示例UID，实际使用时需通过bundleManager.getBundleInfoForSelf等接口获取应用UID
    console.info('battery statistics percent of app is: ' + percent);
} catch (err) {
    console.error(`Failed to get battery statistics percent of app. Code: ${err.code}, message: ${err.message}`);
}
```
