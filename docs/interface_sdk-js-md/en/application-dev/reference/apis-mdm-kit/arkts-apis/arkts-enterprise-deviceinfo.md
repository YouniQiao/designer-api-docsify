# @ohos.enterprise.deviceInfo(设备信息管理)

本模块提供企业设备信息管理能力，支持获取设备序列号、设备名称、SIM卡信息等。企业管理员可通过此模块查询设备详细信息，实现设备资产的统一管理和追踪。

**使用场景：**

- 设备资产管理与追踪  
- 企业设备合规性检查  
- 设备信息采集与统计  
- 故障诊断与设备识别

> **说明：**
> 
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare namespace deviceInfo--><!--Device-unnamed-declare namespace deviceInfo-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { deviceInfo } from 'kits/@kit.MDMKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getDeviceInfo](arkts-mdm-deviceinfo-getdeviceinfo-f.md#getdeviceinfo) | 获取设备信息。 |
| [getDeviceName](arkts-mdm-deviceinfo-getdevicename-f.md#getdevicename) | 获取设备名称，使用callback异步回调。 |
| [getDeviceName](arkts-mdm-deviceinfo-getdevicename-f.md#getdevicename-1) | 获取设备名称，使用Promise异步回调。 |
| [getDeviceSerial](arkts-mdm-deviceinfo-getdeviceserial-f.md#getdeviceserial) | 获取设备序列号，使用callback异步回调。 |
| [getDeviceSerial](arkts-mdm-deviceinfo-getdeviceserial-f.md#getdeviceserial-1) | 获取设备序列号，使用Promise异步回调。 |
| [getDisplayVersion](arkts-mdm-deviceinfo-getdisplayversion-f.md#getdisplayversion) | 获取设备版本号，使用callback异步回调。 |
| [getDisplayVersion](arkts-mdm-deviceinfo-getdisplayversion-f.md#getdisplayversion-1) | 获取设备版本号，使用Promise异步回调。 |

