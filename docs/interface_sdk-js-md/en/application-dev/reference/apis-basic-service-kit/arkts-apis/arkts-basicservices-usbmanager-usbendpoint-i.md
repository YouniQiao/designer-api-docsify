# USBEndpoint

通过USB发送和接收数据的端口。通过[USBInterface](arkts-basicservices-usbmanager-usbinterface-i.md)获取。

> **说明：**
> 
> 主机控制器按照Endpoint类型调度。
> 
> 协议层打包时依赖type决定传输特性。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-usbManager-interface USBEndpoint--><!--Device-usbManager-interface USBEndpoint-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## address

```TypeScript
address: int
```

端点地址。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-address: int--><!--Device-USBEndpoint-address: int-End-->

**System capability:** SystemCapability.USB.USBManager

## attributes

```TypeScript
attributes: int
```

端点属性。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-attributes: int--><!--Device-USBEndpoint-attributes: int-End-->

**System capability:** SystemCapability.USB.USBManager

## direction

```TypeScript
direction: USBRequestDirection
```

端点的方向。

**Type:** [USBRequestDirection](arkts-basicservices-usb-usbrequestdirection-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-direction: USBRequestDirection--><!--Device-USBEndpoint-direction: USBRequestDirection-End-->

**System capability:** SystemCapability.USB.USBManager

## endpointAddr

```TypeScript
endpointAddr: int
```

Endpoint address

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-USBEndpoint-endpointAddr: int--><!--Device-USBEndpoint-endpointAddr: int-End-->

**System capability:** SystemCapability.USB.USBManager

## interfaceId

```TypeScript
interfaceId: int
```

端点所属的接口的唯一标识。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-interfaceId: int--><!--Device-USBEndpoint-interfaceId: int-End-->

**System capability:** SystemCapability.USB.USBManager

## interval

```TypeScript
interval: int
```

端点间隔。（单位：毫秒）

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-interval: int--><!--Device-USBEndpoint-interval: int-End-->

**System capability:** SystemCapability.USB.USBManager

## maxPacketSize

```TypeScript
maxPacketSize: int
```

端点最大数据包大小。（单位：字节）

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-maxPacketSize: int--><!--Device-USBEndpoint-maxPacketSize: int-End-->

**System capability:** SystemCapability.USB.USBManager

## number

```TypeScript
number: number
```

端点号。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-USBEndpoint-number: number--><!--Device-USBEndpoint-number: number-End-->

**System capability:** SystemCapability.USB.USBManager

## type

```TypeScript
type: int
```

端点类型。取值见[UsbEndpointTransferType](arkts-basicservices-usbmanager-usbendpointtransfertype-e.md)

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-type: int--><!--Device-USBEndpoint-type: int-End-->

**System capability:** SystemCapability.USB.USBManager

