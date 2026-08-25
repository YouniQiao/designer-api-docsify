# setCurrentFunctions（系统接口）

## 导入模块

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## setCurrentFunctions

```TypeScript
function setCurrentFunctions(funcs: FunctionType): Promise<boolean>
```

在设备模式下，设置当前的USB功能列表。

**起始版本：** 9

**废弃版本：** 9

**替代接口：** [setCurrentFunctions](arkts-basicservices-usbmanager-setcurrentfunctions-f-sys.md)

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| funcs | [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
