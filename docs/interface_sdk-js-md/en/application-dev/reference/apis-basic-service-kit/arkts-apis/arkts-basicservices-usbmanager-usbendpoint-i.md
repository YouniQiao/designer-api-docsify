# USBEndpoint

Represents the USB endpoint from which data is sent or received. You can obtain the USB endpoint through  
[USBInterface](arkts-basicservices-usbmanager-usbinterface-i.md).

> **NOTE：**
> 
> The host controller schedules the endpoint based on the endpoint type.
> 
> The transmission characteristics are determined by the type during protocol layer packaging.

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

Endpoint address.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-address: int--><!--Device-USBEndpoint-address: int-End-->

**System capability:** SystemCapability.USB.USBManager

## attributes

```TypeScript
attributes: int
```

Endpoint attributes.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-attributes: int--><!--Device-USBEndpoint-attributes: int-End-->

**System capability:** SystemCapability.USB.USBManager

## direction

```TypeScript
direction: USBRequestDirection
```

Endpoint direction.

**Type:** [USBRequestDirection](arkts-basicservices-usb-usbrequestdirection-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-direction: USBRequestDirection--><!--Device-USBEndpoint-direction: USBRequestDirection-End-->

**System capability:** SystemCapability.USB.USBManager

## endpointAddr

```TypeScript
endpointAddr: int
```

Endpoint address.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-USBEndpoint-endpointAddr: int--><!--Device-USBEndpoint-endpointAddr: int-End-->

**System capability:** SystemCapability.USB.USBManager

## interfaceId

```TypeScript
interfaceId: int
```

Unique ID of the interface to which the endpoint belongs.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-interfaceId: int--><!--Device-USBEndpoint-interfaceId: int-End-->

**System capability:** SystemCapability.USB.USBManager

## interval

```TypeScript
interval: int
```

Endpoint interval.Unit: milliseconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-interval: int--><!--Device-USBEndpoint-interval: int-End-->

**System capability:** SystemCapability.USB.USBManager

## maxPacketSize

```TypeScript
maxPacketSize: int
```

Maximum size of data packets on the endpoint.Unit: bytes.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-maxPacketSize: int--><!--Device-USBEndpoint-maxPacketSize: int-End-->

**System capability:** SystemCapability.USB.USBManager

## number

```TypeScript
number: number
```

Endpoint number.

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-USBEndpoint-number: number--><!--Device-USBEndpoint-number: number-End-->

**System capability:** SystemCapability.USB.USBManager

## type

```TypeScript
type: int
```

Endpoint type. For details, see [UsbEndpointTransferType](arkts-basicservices-usbmanager-usbendpointtransfertype-e.md).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBEndpoint-type: int--><!--Device-USBEndpoint-type: int-End-->

**System capability:** SystemCapability.USB.USBManager

