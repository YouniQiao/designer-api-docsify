# UsbDataTransferParams

作为通用USB数据传输接口，客户端需要填充这个对象中的参数，用以发起传输请求。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-usbManager-interface UsbDataTransferParams--><!--Device-usbManager-interface UsbDataTransferParams-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## buffer

```TypeScript
buffer: Uint8Array
```

用于存储读或者写请求时的数据。

**Type:** Uint8Array

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UsbDataTransferParams-buffer: Uint8Array--><!--Device-UsbDataTransferParams-buffer: Uint8Array-End-->

**System capability:** SystemCapability.USB.USBManager

## callback

```TypeScript
callback: AsyncCallback<SubmitTransferCallback>
```

传输完成时的回调信息。

**Type:** [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;SubmitTransferCallback&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UsbDataTransferParams-callback: AsyncCallback<SubmitTransferCallback>--><!--Device-UsbDataTransferParams-callback: AsyncCallback<SubmitTransferCallback>-End-->

**System capability:** SystemCapability.USB.USBManager

## devPipe

```TypeScript
devPipe: USBDevicePipe
```

用于确定总线地址和设备地址，需要调用[usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice)获取。

**Type:** [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UsbDataTransferParams-devPipe: USBDevicePipe--><!--Device-UsbDataTransferParams-devPipe: USBDevicePipe-End-->

**System capability:** SystemCapability.USB.USBManager

## endpoint

```TypeScript
endpoint: int
```

端点地址，正整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UsbDataTransferParams-endpoint: int--><!--Device-UsbDataTransferParams-endpoint: int-End-->

**System capability:** SystemCapability.USB.USBManager

## flags

```TypeScript
flags: UsbTransferFlags
```

USB传输标志。

**Type:** [UsbTransferFlags](arkts-basicservices-usbmanager-usbtransferflags-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UsbDataTransferParams-flags: UsbTransferFlags--><!--Device-UsbDataTransferParams-flags: UsbTransferFlags-End-->

**System capability:** SystemCapability.USB.USBManager

## isoPacketCount

```TypeScript
isoPacketCount: int
```

实时传输时数据包的数量，仅用于具有实时传输端点的I/O。必须是非负数，（单位：个数）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UsbDataTransferParams-isoPacketCount: int--><!--Device-UsbDataTransferParams-isoPacketCount: int-End-->

**System capability:** SystemCapability.USB.USBManager

## length

```TypeScript
length: int
```

数据缓冲区的长度，必须是非负数（期望长度）。（单位：字节）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UsbDataTransferParams-length: int--><!--Device-UsbDataTransferParams-length: int-End-->

**System capability:** SystemCapability.USB.USBManager

## timeout

```TypeScript
timeout: int
```

超时时间。（单位：毫秒）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UsbDataTransferParams-timeout: int--><!--Device-UsbDataTransferParams-timeout: int-End-->

**System capability:** SystemCapability.USB.USBManager

## type

```TypeScript
type: UsbEndpointTransferType
```

传输类型。

**Type:** [UsbEndpointTransferType](arkts-basicservices-usbmanager-usbendpointtransfertype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UsbDataTransferParams-type: UsbEndpointTransferType--><!--Device-UsbDataTransferParams-type: UsbEndpointTransferType-End-->

**System capability:** SystemCapability.USB.USBManager

## userData

```TypeScript
userData: Uint8Array
```

用户上下文数据。

**Type:** Uint8Array

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UsbDataTransferParams-userData: Uint8Array--><!--Device-UsbDataTransferParams-userData: Uint8Array-End-->

**System capability:** SystemCapability.USB.USBManager

