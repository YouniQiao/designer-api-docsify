# USBDevice

Represents the USB device information.

**Since:** 23

<!--Device-usbManager-interface USBDevice--><!--Device-usbManager-interface USBDevice-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
import { serialManager } from '@kit.BasicServicesKit';
```

## busNum

```TypeScript
busNum: int
```

Bus address.

**Type:** int

**Since:** 23

<!--Device-USBDevice-busNum: int--><!--Device-USBDevice-busNum: int-End-->

**System capability:** SystemCapability.USB.USBManager

## clazz

```TypeScript
clazz: int
```

Device class.

**Type:** int

**Since:** 23

<!--Device-USBDevice-clazz: int--><!--Device-USBDevice-clazz: int-End-->

**System capability:** SystemCapability.USB.USBManager

## configs

```TypeScript
configs: Array<USBConfiguration>
```

Device configuration descriptor information.

**Type:** Array&lt;[USBConfiguration](arkts-basicservices-usbmanager-usbconfiguration-i.md)&gt;

**Since:** 23

<!--Device-USBDevice-configs: Array<USBConfiguration>--><!--Device-USBDevice-configs: Array<USBConfiguration>-End-->

**System capability:** SystemCapability.USB.USBManager

## devAddress

```TypeScript
devAddress: int
```

Device address.

**Type:** int

**Since:** 23

<!--Device-USBDevice-devAddress: int--><!--Device-USBDevice-devAddress: int-End-->

**System capability:** SystemCapability.USB.USBManager

## manufacturerName

```TypeScript
manufacturerName: string
```

Device manufacturer.

**Type:** string

**Since:** 23

<!--Device-USBDevice-manufacturerName: string--><!--Device-USBDevice-manufacturerName: string-End-->

**System capability:** SystemCapability.USB.USBManager

## name

```TypeScript
name: string
```

Device name.

**Type:** string

**Since:** 23

<!--Device-USBDevice-name: string--><!--Device-USBDevice-name: string-End-->

**System capability:** SystemCapability.USB.USBManager

## productId

```TypeScript
productId: int
```

Product ID.

**Type:** int

**Since:** 23

<!--Device-USBDevice-productId: int--><!--Device-USBDevice-productId: int-End-->

**System capability:** SystemCapability.USB.USBManager

## productName

```TypeScript
productName: string
```

Product name.

**Type:** string

**Since:** 23

<!--Device-USBDevice-productName: string--><!--Device-USBDevice-productName: string-End-->

**System capability:** SystemCapability.USB.USBManager

## protocol

```TypeScript
protocol: int
```

Device protocol code.

**Type:** int

**Since:** 23

<!--Device-USBDevice-protocol: int--><!--Device-USBDevice-protocol: int-End-->

**System capability:** SystemCapability.USB.USBManager

## serial

```TypeScript
serial: string
```

Sequence number.

**Type:** string

**Since:** 23

<!--Device-USBDevice-serial: string--><!--Device-USBDevice-serial: string-End-->

**System capability:** SystemCapability.USB.USBManager

## subClass

```TypeScript
subClass: int
```

Device subclass.

**Type:** int

**Since:** 23

<!--Device-USBDevice-subClass: int--><!--Device-USBDevice-subClass: int-End-->

**System capability:** SystemCapability.USB.USBManager

## vendorId

```TypeScript
vendorId: int
```

Vendor ID.

**Type:** int

**Since:** 23

<!--Device-USBDevice-vendorId: int--><!--Device-USBDevice-vendorId: int-End-->

**System capability:** SystemCapability.USB.USBManager

## version

```TypeScript
version: string
```

Version number.

**Type:** string

**Since:** 23

<!--Device-USBDevice-version: string--><!--Device-USBDevice-version: string-End-->

**System capability:** SystemCapability.USB.USBManager

