# @ohos.usbManager.serial

This module provides the serial port management functions, including enabling and disabling the serial port of the device, writing and reading data, setting and obtaining the configuration parameters of the serial port, and managing permissions.

**Since:** 19

<!--Device-unnamed-declare namespace serialManager--><!--Device-unnamed-declare namespace serialManager-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

## Modules to Import

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelSerialRight](arkts-basicservices-serialmanager-cancelserialright-f.md#cancelserialright) |
| [close](arkts-basicservices-serialmanager-close-f.md#close) |
| [getAttribute](arkts-basicservices-serialmanager-getattribute-f.md#getattribute) |
| [getPortList](arkts-basicservices-serialmanager-getportlist-f.md#getportlist) |
| [hasSerialRight](arkts-basicservices-serialmanager-hasserialright-f.md#hasserialright) |
| [open](arkts-basicservices-serialmanager-open-f.md#open) |
| [read](arkts-basicservices-serialmanager-read-f.md#read) |
| [readSync](arkts-basicservices-serialmanager-readsync-f.md#readsync) |
| [requestSerialRight](arkts-basicservices-serialmanager-requestserialright-f.md#requestserialright) |
| [setAttribute](arkts-basicservices-serialmanager-setattribute-f.md#setattribute) |
| [write](arkts-basicservices-serialmanager-write-f.md#write) |
| [writeSync](arkts-basicservices-serialmanager-writesync-f.md#writesync) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSerialRight](arkts-basicservices-serialmanager-addserialright-f-sys.md#addserialright) |
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
