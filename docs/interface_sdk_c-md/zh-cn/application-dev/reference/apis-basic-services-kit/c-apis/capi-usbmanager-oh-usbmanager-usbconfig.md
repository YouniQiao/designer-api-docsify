# OH_UsbManager_UsbConfig

```c
typedef struct OH_UsbManager_UsbConfig {...} OH_UsbManager_UsbConfig
```

## 概述

定义USB配置。一个[OH_UsbManager_UsbDevice](capi-usbmanager-oh-usbmanager-usbdevice.md)可以包含多个OH_UsbManager_UsbConfig实例。

**起始版本：** 26.1.0

**相关模块：** [UsbManager](capi-usbmanager.md)

**所在头文件：** [ohusb_manager.h](capi-ohusb-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| -- | -- |
| uint8_t id |  |
| uint8_t attributes |  |
| uint8_t maxPower |  |
| const char *name |  |
| bool isRemoteWakeup |  |
| bool isSelfPowered |  |
| [OH_UsbManager_UsbInterface](capi-usbmanager-oh-usbmanager-usbinterface.md) *interfaces |  |
| uint32_t interfaceCount |  |


