# OH_UsbManager_UsbDevice

```c
typedef struct OH_UsbManager_UsbDevice {...} OH_UsbManager_UsbDevice
```

## Overview

Defines a flat representation of a USB device.

**Since**: 26.1.0

**Related module**: [UsbManager](capi-usbmanager.md)

**Header file**: [ohusb_manager.h](capi-ohusb-manager-h.md)

## Summary

### Member variables

| Name | Description |
| -- | -- |
| uint8_t busNum |  |
| uint8_t devAddress |  |
| const char *name |  |
| const char *manufacturerName |  |
| const char *productName |  |
| const char *version |  |
| uint16_t vendorId |  |
| uint16_t productId |  |
| uint8_t clazz |  |
| uint8_t subClass |  |
| uint8_t protocol |  |
| [OH_UsbManager_UsbConfig](capi-usbmanager-oh-usbmanager-usbconfig.md) *configs |  |
| uint32_t configCount |  |


