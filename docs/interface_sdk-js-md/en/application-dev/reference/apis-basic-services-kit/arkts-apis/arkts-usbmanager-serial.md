# @ohos.usbManager.serial

This module provides the serial port management functions, including enabling and disabling the serial port of the device, writing and reading data, setting and obtaining the configuration parameters of the serial port, and managing permissions.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**System capability:** SystemCapability.USB.USBManager.Serial

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelSerialRight](arkts-basicservices-serialmanager-cancelserialright-f.md) |
| [close](arkts-basicservices-serialmanager-close-f.md) |
| [getAttribute](arkts-basicservices-serialmanager-getattribute-f.md) |
| [getPortList](arkts-basicservices-serialmanager-getportlist-f.md) |
| [hasSerialRight](arkts-basicservices-serialmanager-hasserialright-f.md) |
| [open](arkts-basicservices-serialmanager-open-f.md) |
| [read](arkts-basicservices-serialmanager-read-f.md) |
| [readSync](arkts-basicservices-serialmanager-readsync-f.md) |
| [requestSerialRight](arkts-basicservices-serialmanager-requestserialright-f.md) |
| [setAttribute](arkts-basicservices-serialmanager-setattribute-f.md) |
| [write](arkts-basicservices-serialmanager-write-f.md) |
| [writeSync](arkts-basicservices-serialmanager-writesync-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSerialRight](arkts-basicservices-serialmanager-addserialright-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SerialAttribute](arkts-basicservices-serialmanager-serialattribute-i.md) |
| [SerialPort](arkts-basicservices-serialmanager-serialport-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BaudRates](arkts-basicservices-serialmanager-baudrates-e.md) |
| [DataBits](arkts-basicservices-serialmanager-databits-e.md) |
| [Parity](arkts-basicservices-serialmanager-parity-e.md) |
| [StopBits](arkts-basicservices-serialmanager-stopbits-e.md) |
