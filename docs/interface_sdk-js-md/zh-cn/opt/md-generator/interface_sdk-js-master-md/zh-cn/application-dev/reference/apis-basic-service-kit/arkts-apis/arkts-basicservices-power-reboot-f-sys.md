# reboot（系统接口）

## reboot

```TypeScript
function reboot(reason: string): void
```

重启设备。

**起始版本：** 9

**需要权限：** ohos.permission.REBOOT

<!--Device-power-function reboot(reason: string): void--><!--Device-power-function reboot(reason: string): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reason | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-连接服务失败) |

## 示例

```TypeScript
try {
    power.reboot('reboot_test');
} catch (err) {
    console.error(`Failed to reboot. Code: ${err.code}, message: ${err.message}`);
}
```
