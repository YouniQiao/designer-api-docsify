# rebootDevice

## rebootDevice

```TypeScript
function rebootDevice(reason: string): void
```

重启系统。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [power.reboot](arkts-basicservices-power-reboot-f-sys.md#reboot)

**需要权限：** ohos.permission.REBOOT

<!--Device-power-function rebootDevice(reason: string): void--><!--Device-power-function rebootDevice(reason: string): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reason | string | 是 |

## 示例

```TypeScript
power.rebootDevice('reboot_test');
```
