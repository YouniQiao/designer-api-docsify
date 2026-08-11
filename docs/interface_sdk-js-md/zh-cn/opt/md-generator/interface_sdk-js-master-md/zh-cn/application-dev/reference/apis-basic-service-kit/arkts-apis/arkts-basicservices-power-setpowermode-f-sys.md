# setPowerMode（系统接口）

## setPowerMode

```TypeScript
function setPowerMode(mode: DevicePowerMode, callback: AsyncCallback<void>): void
```

设置当前设备的电源模式。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.POWER_OPTIMIZATION

<!--Device-power-function setPowerMode(mode: DevicePowerMode, callback: AsyncCallback<void>): void--><!--Device-power-function setPowerMode(mode: DevicePowerMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [DevicePowerMode](arkts-basicservices-power-devicepowermode-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [4900301](../../apis-basic-services-kit/errorcode-power.md#4900301-电源模式设置失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
power.setPowerMode(power.DevicePowerMode.MODE_PERFORMANCE, (err: BusinessError) => {
    if (err) {
        console.error(`Failed to set power mode. Code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info('set power mode to MODE_PERFORMANCE');
});
```


## setPowerMode

```TypeScript
function setPowerMode(mode: DevicePowerMode): Promise<void>
```

设置当前设备的电源模式。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.POWER_OPTIMIZATION

<!--Device-power-function setPowerMode(mode: DevicePowerMode): Promise<void>--><!--Device-power-function setPowerMode(mode: DevicePowerMode): Promise<void>-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [DevicePowerMode](arkts-basicservices-power-devicepowermode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [4900301](../../apis-basic-services-kit/errorcode-power.md#4900301-电源模式设置失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
power.setPowerMode(power.DevicePowerMode.MODE_PERFORMANCE)
.then(() => {
    console.info('set power mode to MODE_PERFORMANCE');
})
.catch((err: BusinessError) => {
    console.error(`Failed to set power mode. Code: ${err.code}, message: ${err.message}`);
});
```
