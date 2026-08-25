# USBAccessoryHandle

USB配件句柄，包含配件文件描述符，用于通过CoreFileKit提供的read/write接口和配件进行通信。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.USB.USBManager

## 导入模块

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## accessoryFd

```TypeScript
accessoryFd: int
```

配件文件描述符。合法的accessoryFd是正整数。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.USB.USBManager
