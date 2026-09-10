# OH_UsbManager_UsbDevice

```c
typedef struct OH_UsbManager_UsbDevice {...} OH_UsbManager_UsbDevice
```

## 概述

定义USB设备的扁平化表示。

**起始版本：** 26.1.0

**相关模块：** [UsbManager](capi-usbmanager.md)

**所在头文件：** [ohusb_manager.h](capi-ohusb-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
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


