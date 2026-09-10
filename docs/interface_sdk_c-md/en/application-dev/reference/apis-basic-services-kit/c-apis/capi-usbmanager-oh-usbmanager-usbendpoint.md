# OH_UsbManager_UsbEndpoint

```c
typedef struct OH_UsbManager_UsbEndpoint {...} OH_UsbManager_UsbEndpoint
```

## Overview

Defines the USB endpoint from which data is sent or received. An endpointis obtained from [OH_UsbManager_UsbInterface](capi-usbmanager-oh-usbmanager-usbinterface.md).

**Since**: 26.1.0

**Related module**: [UsbManager](capi-usbmanager.md)

**Header file**: [ohusb_manager.h](capi-ohusb-manager-h.md)

## Summary

### Member variables

| Name | Description |
| -- | -- |
| uint8_t address |  |
| uint8_t attributes |  |
| uint8_t interval |  |
| uint16_t maxPacketSize |  |
| [OH_UsbManager_RequestDirection](capi-ohusb-manager-h.md#oh_usbmanager_requestdirection) direction |  |
| uint8_t number |  |
| uint8_t type |  |
| uint8_t interfaceId |  |


