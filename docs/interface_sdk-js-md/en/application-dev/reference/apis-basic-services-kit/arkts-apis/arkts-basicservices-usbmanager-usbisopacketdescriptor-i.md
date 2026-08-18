# UsbIsoPacketDescriptor

Describes packet information returned in real time by the transfer callback.

**Since:** 23

<!--Device-usbManager-interface UsbIsoPacketDescriptor--><!--Device-usbManager-interface UsbIsoPacketDescriptor-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
import { serialManager } from '@kit.BasicServicesKit';
```

## actualLength

```TypeScript
actualLength: int
```

Actual length of the read or written data.Unit: bytes.

**Type:** int

**Since:** 23

<!--Device-UsbIsoPacketDescriptor-actualLength: int--><!--Device-UsbIsoPacketDescriptor-actualLength: int-End-->

**System capability:** SystemCapability.USB.USBManager

## length

```TypeScript
length: int
```

Expected length of the read or written data.Unit: bytes.

**Type:** int

**Since:** 23

<!--Device-UsbIsoPacketDescriptor-length: int--><!--Device-UsbIsoPacketDescriptor-length: int-End-->

**System capability:** SystemCapability.USB.USBManager

## status

```TypeScript
status: UsbTransferStatus
```

Status returned by callback.

**Type:** [UsbTransferStatus](arkts-basicservices-usbmanager-usbtransferstatus-e.md)

**Since:** 23

<!--Device-UsbIsoPacketDescriptor-status: UsbTransferStatus--><!--Device-UsbIsoPacketDescriptor-status: UsbTransferStatus-End-->

**System capability:** SystemCapability.USB.USBManager

