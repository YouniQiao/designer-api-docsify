# setConfiguration

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## setConfiguration

```TypeScript
function setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): number
```

设置设备配置。适用于多功能USB设备需要切换工作模式的场景，如打印机+扫描仪组合设备切换为打印模式或扫描模式、设备从低功耗配置切换到高功耗配置以启用全部功能等。调用成功后设备的配置将被切换为指定的配置，后续的数据传输和设备操作将基 于新配置进行。

> **说明：**&gt;
> 在调用该接口前需要调用[usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md) claim通信接口。

**起始版本：** 9

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |
| config | [USBConfiguration](arkts-basicservices-usbmanager-usbconfiguration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
