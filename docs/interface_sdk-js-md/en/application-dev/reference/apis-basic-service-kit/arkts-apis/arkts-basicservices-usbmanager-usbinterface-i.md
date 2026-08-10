# USBInterface

一个[USBConfiguration](arkts-basicservices-usbmanager-usbconfiguration-i.md)中可以含有多个USBInterface，每个USBInterface提供一个功能。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-usbManager-interface USBInterface--><!--Device-usbManager-interface USBInterface-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## alternateSetting

```TypeScript
alternateSetting: int
```

在同一个接口中的多个描述符中进行切换设置。值的大小表示支持可选模式个数，其中0表示不支持可选模式。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBInterface-alternateSetting: int--><!--Device-USBInterface-alternateSetting: int-End-->

**System capability:** SystemCapability.USB.USBManager

## clazz

```TypeScript
clazz: int
```

设备类型。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBInterface-clazz: int--><!--Device-USBInterface-clazz: int-End-->

**System capability:** SystemCapability.USB.USBManager

## endpoints

```TypeScript
endpoints: Array<USBEndpoint>
```

当前接口所包含的端点。

**Type:** Array&lt;USBEndpoint&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBInterface-endpoints: Array<USBEndpoint>--><!--Device-USBInterface-endpoints: Array<USBEndpoint>-End-->

**System capability:** SystemCapability.USB.USBManager

## id

```TypeScript
id: int
```

接口的唯一标识。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBInterface-id: int--><!--Device-USBInterface-id: int-End-->

**System capability:** SystemCapability.USB.USBManager

## name

```TypeScript
name: string
```

接口名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBInterface-name: string--><!--Device-USBInterface-name: string-End-->

**System capability:** SystemCapability.USB.USBManager

## protocol

```TypeScript
protocol: int
```

接口的协议。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBInterface-protocol: int--><!--Device-USBInterface-protocol: int-End-->

**System capability:** SystemCapability.USB.USBManager

## subClass

```TypeScript
subClass: int
```

设备子类。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBInterface-subClass: int--><!--Device-USBInterface-subClass: int-End-->

**System capability:** SystemCapability.USB.USBManager

