# OH_UsbManager_UsbConfig

```c
struct OH_UsbManager_UsbConfig {...}
```

## Overview

Defines a USB configuration. One [OH_UsbManager_UsbDevice](capi-usbmanager-oh-usbmanager-usbdevice.md) can contain multiple **OH_UsbManager_UsbConfig** instances.

**System capability**: SystemCapability.USB.USBManager

**Since**: 26.1.0

**Related module**: [UsbManager](capi-usbmanager.md)

**Header file**: [ohusb_manager.h](capi-ohusb-manager-h.md)

## Summary

### Member variables

| Name | Description |
| -- | -- |
| uint8_t id |  |
| uint8_t attributes |  |
| uint8_t maxPower |  |
| const char *name |  |
| bool isRemoteWakeup |  |
| bool isSelfPowered |  |
| OH_UsbManager_UsbInterface *interfaces |  |
| uint32_t interfaceCount |  |


