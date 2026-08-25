# @ohos.enterprise.deviceControl(设备控制管理)

本模块提供设备控制能力，用于企业设备管理场景。管理员可以通过本模块远程控制设备，包括设备重启、关机、锁屏、恢复出厂设置等操作，帮助企业实现设备统一管理和安全管控。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { deviceControl } from '@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [operateDevice(设备控制管理)](arkts-mdm-devicecontrol-operatedevice-f.md) |
| [operateDevice(设备控制管理)](arkts-mdm-devicecontrol-operatedevice-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [lockScreen(设备控制管理)](arkts-mdm-devicecontrol-lockscreen-f-sys.md) |
| [reboot(设备控制管理)](arkts-mdm-devicecontrol-reboot-f-sys.md) |
| [resetFactory(设备控制管理)](arkts-mdm-devicecontrol-resetfactory-f-sys.md) |
| [resetFactory(设备控制管理)](arkts-mdm-devicecontrol-resetfactory-f-sys.md) |
| [shutdown(设备控制管理)](arkts-mdm-devicecontrol-shutdown-f-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [Operation(设备控制管理)](arkts-mdm-devicecontrol-operation-e.md) |
