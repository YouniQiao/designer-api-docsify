# @ohos.busManager.serial

Serial port management.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BusManager.Serial

## Modules to Import

```TypeScript
import { serial } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getSerialPortList](arkts-basicservices-serial-getserialportlist-f.md) | Obtains the serial port list. This API returns the result asynchronously through a promise. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [addPortAuthorization](arkts-basicservices-serial-addportauthorization-f-sys.md) | Adds the permission for applications to access the serial port. This API is open only to system applications that display a pop-up window for serial port authorization. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [SerialConfigs](arkts-basicservices-serial-serialconfigs-i.md) | Serial port communication configuration. |
| [SerialPort](arkts-basicservices-serial-serialport-i.md) | Serial port object, which provides information and communication capabilities of the serial port device. |
| [SerialPortInfo](arkts-basicservices-serial-serialportinfo-i.md) | Serial port device information. |

### Enums

| Name | Description |
| --- | --- |
| [DataBits](arkts-basicservices-serial-databits-e.md) | Data bits in serial port communication. |
| [Parity](arkts-basicservices-serial-parity-e.md) | Parity bits in serial port communication. |
| [StopBits](arkts-basicservices-serial-stopbits-e.md) | Stop bits in serial port communication. |
