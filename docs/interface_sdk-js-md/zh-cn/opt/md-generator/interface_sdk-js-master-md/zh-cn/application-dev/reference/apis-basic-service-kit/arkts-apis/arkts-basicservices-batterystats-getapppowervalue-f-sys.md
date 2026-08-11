# getAppPowerValue（系统接口）

## getAppPowerValue

```TypeScript
function getAppPowerValue(uid: number): number
```

获取应用的耗电量，单位毫安时。

**起始版本：** 8

<!--Device-batteryStats-function getAppPowerValue(uid: int): double--><!--Device-batteryStats-function getAppPowerValue(uid: int): double-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [4600101](../../apis-basic-services-kit/errorcode-batteryStatistics.md#4600101-连接服务失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
try {
    let value = batteryStats.getAppPowerValue(10021); // 10021为示例UID，实际使用时需通过bundleManager.getBundleInfoForSelf等接口获取应用UID
    console.info('battery statistics value of app is: ' + value);
} catch (err) {
    console.error(`Failed to get battery statistics value of app. Code: ${err.code}, message: ${err.message}`);
}
```
