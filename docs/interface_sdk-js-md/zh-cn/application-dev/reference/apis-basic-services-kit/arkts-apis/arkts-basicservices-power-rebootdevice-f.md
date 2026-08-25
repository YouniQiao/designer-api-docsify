# rebootDevice

## 导入模块

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## rebootDevice

```TypeScript
function rebootDevice(reason: string): void
```

重启设备。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [reboot](arkts-basicservices-power-reboot-f-sys.md)

**需要权限：** ohos.permission.REBOOT

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reason | string | 是 |
