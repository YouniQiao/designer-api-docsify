# USBDeviceRequestParams

Represents control transfer parameters.

**Since:** 23

<!--Device-usbManager-interface USBDeviceRequestParams--><!--Device-usbManager-interface USBDeviceRequestParams-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## bmRequestType

```TypeScript
bmRequestType: int
```

Control request type.

**Type:** int

**Since:** 23

<!--Device-USBDeviceRequestParams-bmRequestType: int--><!--Device-USBDeviceRequestParams-bmRequestType: int-End-->

**System capability:** SystemCapability.USB.USBManager

## bRequest

```TypeScript
bRequest: int
```

Request type.

**Type:** int

**Since:** 23

<!--Device-USBDeviceRequestParams-bRequest: int--><!--Device-USBDeviceRequestParams-bRequest: int-End-->

**System capability:** SystemCapability.USB.USBManager

## data

```TypeScript
data: Uint8Array
```

Buffer for writing or reading data.

**Type:** Uint8Array

**Since:** 23

<!--Device-USBDeviceRequestParams-data: Uint8Array--><!--Device-USBDeviceRequestParams-data: Uint8Array-End-->

**System capability:** SystemCapability.USB.USBManager

## wIndex

```TypeScript
wIndex: int
```

Index of the request parameter.

**Type:** int

**Since:** 23

<!--Device-USBDeviceRequestParams-wIndex: int--><!--Device-USBDeviceRequestParams-wIndex: int-End-->

**System capability:** SystemCapability.USB.USBManager

## wLength

```TypeScript
wLength: int
```

Length of the requested data.Unit: bytes.

**Type:** int

**Since:** 23

<!--Device-USBDeviceRequestParams-wLength: int--><!--Device-USBDeviceRequestParams-wLength: int-End-->

**System capability:** SystemCapability.USB.USBManager

## wValue

```TypeScript
wValue: int
```

Request parameter.

**Type:** int

**Since:** 23

<!--Device-USBDeviceRequestParams-wValue: int--><!--Device-USBDeviceRequestParams-wValue: int-End-->

**System capability:** SystemCapability.USB.USBManager

