# USBDeviceRequestParams

Represents control transfer parameters.

**Since:** 12

<!--Device-usbManager-interface USBDeviceRequestParams--><!--Device-usbManager-interface USBDeviceRequestParams-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## bRequest

```TypeScript
bRequest: number
```

Request type.

**Type:** number

**Since:** 12

<!--Device-USBDeviceRequestParams-bRequest: int--><!--Device-USBDeviceRequestParams-bRequest: int-End-->

**System capability:** SystemCapability.USB.USBManager

## bmRequestType

```TypeScript
bmRequestType: number
```

Control request type.

**Type:** number

**Since:** 12

<!--Device-USBDeviceRequestParams-bmRequestType: int--><!--Device-USBDeviceRequestParams-bmRequestType: int-End-->

**System capability:** SystemCapability.USB.USBManager

## data

```TypeScript
data: Uint8Array
```

Buffer for writing or reading data.

**Type:** Uint8Array

**Since:** 12

<!--Device-USBDeviceRequestParams-data: Uint8Array--><!--Device-USBDeviceRequestParams-data: Uint8Array-End-->

**System capability:** SystemCapability.USB.USBManager

## wIndex

```TypeScript
wIndex: number
```

Index of the request parameter.

**Type:** number

**Since:** 12

<!--Device-USBDeviceRequestParams-wIndex: int--><!--Device-USBDeviceRequestParams-wIndex: int-End-->

**System capability:** SystemCapability.USB.USBManager

## wLength

```TypeScript
wLength: number
```

Length of the requested data.Unit: bytes.

**Type:** number

**Since:** 12

<!--Device-USBDeviceRequestParams-wLength: int--><!--Device-USBDeviceRequestParams-wLength: int-End-->

**System capability:** SystemCapability.USB.USBManager

## wValue

```TypeScript
wValue: number
```

Request parameter.

**Type:** number

**Since:** 12

<!--Device-USBDeviceRequestParams-wValue: int--><!--Device-USBDeviceRequestParams-wValue: int-End-->

**System capability:** SystemCapability.USB.USBManager

