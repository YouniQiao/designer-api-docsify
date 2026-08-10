# @ohos.busManager.serial

串口管理

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace serial--><!--Device-unnamed-declare namespace serial-End-->

**System capability:** SystemCapability.BusManager.Serial

## Modules to Import

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getSerialPortList](arkts-basicservices-serial-getserialportlist-f.md#getserialportlist) | 获取串口列表。使用Promise异步回调。 |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [addPortAuthorization](arkts-basicservices-serial-addportauthorization-f-sys.md#addportauthorization) | 添加应用访问串口端口的权限仅面向串口授权弹窗系统应用开放 |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [SerialConfigs](arkts-basicservices-serial-serialconfigs-i.md) | 串口通信配置 |
| [SerialPort](arkts-basicservices-serial-serialport-i.md) | 串口对象，提供串口设备信息和通信相关能力 |
| [SerialPortInfo](arkts-basicservices-serial-serialportinfo-i.md) | 串口设备信息 |

### Enums

| Name | Description |
| --- | --- |
| [DataBits](arkts-basicservices-serial-databits-e.md) | 串口通信中的数据位 |
| [Parity](arkts-basicservices-serial-parity-e.md) | 串口通信中的校验位 |
| [StopBits](arkts-basicservices-serial-stopbits-e.md) | 串口通信中的停止位 |

