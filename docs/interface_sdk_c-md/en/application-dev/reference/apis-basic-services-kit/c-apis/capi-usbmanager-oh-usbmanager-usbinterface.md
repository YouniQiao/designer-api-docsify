# OH_UsbManager_UsbInterface

```c
typedef struct OH_UsbManager_UsbInterface {...} OH_UsbManager_UsbInterface
```

## Overview

Defines a USB interface. One [OH_UsbManager_UsbConfig](capi-usbmanager-oh-usbmanager-usbconfig.md) can containmultiple OH_UsbManager_UsbInterface instances, each providing a specific function.

**Since**: 26.1.0

**Related module**: [UsbManager](capi-usbmanager.md)

**Header file**: [ohusb_manager.h](capi-ohusb-manager-h.md)

## Summary

### Member variables

| Name | Description |
| -- | -- |
| uint8_t id |  |
| uint8_t protocol |  |
| uint8_t clazz |  |
| uint8_t subClass |  |
| uint8_t alternateSetting |  |
| const char *name |  |
| [OH_UsbManager_UsbEndpoint](capi-usbmanager-oh-usbmanager-usbendpoint.md) *endpoints |  |
| uint32_t endpointCount |  |


