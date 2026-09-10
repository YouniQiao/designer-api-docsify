# OH_UsbManager_UsbInterface

```c
typedef struct OH_UsbManager_UsbInterface {...} OH_UsbManager_UsbInterface
```

## 概述

定义USB接口。一个[OH_UsbManager_UsbConfig](capi-usbmanager-oh-usbmanager-usbconfig.md)可以包含多个OH_UsbManager_UsbInterface实例，每个实例提供特定功能。

**起始版本：** 26.1.0

**相关模块：** [UsbManager](capi-usbmanager.md)

**所在头文件：** [ohusb_manager.h](capi-ohusb-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| -- | -- |
| uint8_t id |  |
| uint8_t protocol |  |
| uint8_t clazz |  |
| uint8_t subClass |  |
| uint8_t alternateSetting |  |
| const char *name |  |
| [OH_UsbManager_UsbEndpoint](capi-usbmanager-oh-usbmanager-usbendpoint.md) *endpoints |  |
| uint32_t endpointCount |  |


