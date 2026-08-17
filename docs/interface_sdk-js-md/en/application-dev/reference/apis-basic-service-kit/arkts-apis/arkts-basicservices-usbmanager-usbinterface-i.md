# USBInterface

Represents a USB interface. One [USBConfiguration](arkts-basicservices-usbmanager-usbconfiguration-i.md#usbconfiguration) object can contain multiple * *USBInterface** instances, each providing a specific function.

**Since:** 23

<!--Device-usbManager-interface USBInterface--><!--Device-usbManager-interface USBInterface-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## alternateSetting

```TypeScript
alternateSetting: int
```

Settings for alternating between descriptors of the same USB interface. The value size indicates the number of optional modes. The value 0 indicates that no optional mode is supported.

**Type:** int

**Since:** 23

<!--Device-USBInterface-alternateSetting: int--><!--Device-USBInterface-alternateSetting: int-End-->

**System capability:** SystemCapability.USB.USBManager

## clazz

```TypeScript
clazz: int
```

Device type.

**Type:** int

**Since:** 23

<!--Device-USBInterface-clazz: int--><!--Device-USBInterface-clazz: int-End-->

**System capability:** SystemCapability.USB.USBManager

## endpoints

```TypeScript
endpoints: Array<USBEndpoint>
```

Endpoints that belong to the USB interface.

**Type:** Array&lt;USBEndpoint&gt;

**Since:** 23

<!--Device-USBInterface-endpoints: Array<USBEndpoint>--><!--Device-USBInterface-endpoints: Array<USBEndpoint>-End-->

**System capability:** SystemCapability.USB.USBManager

## id

```TypeScript
id: int
```

Unique ID of the USB interface.

**Type:** int

**Since:** 23

<!--Device-USBInterface-id: int--><!--Device-USBInterface-id: int-End-->

**System capability:** SystemCapability.USB.USBManager

## name

```TypeScript
name: string
```

Interface name.

**Type:** string

**Since:** 23

<!--Device-USBInterface-name: string--><!--Device-USBInterface-name: string-End-->

**System capability:** SystemCapability.USB.USBManager

## protocol

```TypeScript
protocol: int
```

Interface protocol.

**Type:** int

**Since:** 23

<!--Device-USBInterface-protocol: int--><!--Device-USBInterface-protocol: int-End-->

**System capability:** SystemCapability.USB.USBManager

## subClass

```TypeScript
subClass: int
```

Device subclass.

**Type:** int

**Since:** 23

<!--Device-USBInterface-subClass: int--><!--Device-USBInterface-subClass: int-End-->

**System capability:** SystemCapability.USB.USBManager

