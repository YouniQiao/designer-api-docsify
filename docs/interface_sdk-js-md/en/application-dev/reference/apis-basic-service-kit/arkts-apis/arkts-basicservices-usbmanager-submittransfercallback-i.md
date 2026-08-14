# SubmitTransferCallback

Transfers USB data packets in an asynchronous manner.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-usbManager-interface SubmitTransferCallback--><!--Device-usbManager-interface SubmitTransferCallback-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## actualLength

```TypeScript
actualLength: int
```

Actual length of the read or written data.Unit: bytes.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SubmitTransferCallback-actualLength: int--><!--Device-SubmitTransferCallback-actualLength: int-End-->

**System capability:** SystemCapability.USB.USBManager

## isoPacketDescs

```TypeScript
isoPacketDescs: Array<Readonly<UsbIsoPacketDescriptor>>
```

Packet information transferred in real time.

**Type:** Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;[UsbIsoPacketDescriptor](arkts-basicservices-usbmanager-usbisopacketdescriptor-i.md)&gt;&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SubmitTransferCallback-isoPacketDescs: Array<Readonly<UsbIsoPacketDescriptor>>--><!--Device-SubmitTransferCallback-isoPacketDescs: Array<Readonly<UsbIsoPacketDescriptor>>-End-->

**System capability:** SystemCapability.USB.USBManager

## status

```TypeScript
status: UsbTransferStatus
```

Status after reading or writing is complete.

**Type:** [UsbTransferStatus](arkts-basicservices-usbmanager-usbtransferstatus-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SubmitTransferCallback-status: UsbTransferStatus--><!--Device-SubmitTransferCallback-status: UsbTransferStatus-End-->

**System capability:** SystemCapability.USB.USBManager

