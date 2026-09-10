# OH_UsbManager_UsbEndpoint

```c
typedef struct OH_UsbManager_UsbEndpoint {...} OH_UsbManager_UsbEndpoint
```

## 概述

定义用于发送或接收数据的USB端点。端点从[OH_UsbManager_UsbInterface](capi-usbmanager-oh-usbmanager-usbinterface.md)获取。

**起始版本：** 26.1.0

**相关模块：** [UsbManager](capi-usbmanager.md)

**所在头文件：** [ohusb_manager.h](capi-ohusb-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| -- | -- |
| uint8_t address |  |
| uint8_t attributes |  |
| uint8_t interval |  |
| uint16_t maxPacketSize |  |
| [OH_UsbManager_RequestDirection](capi-ohusb-manager-h.md#oh_usbmanager_requestdirection) direction |  |
| uint8_t number |  |
| uint8_t type |  |
| uint8_t interfaceId |  |


