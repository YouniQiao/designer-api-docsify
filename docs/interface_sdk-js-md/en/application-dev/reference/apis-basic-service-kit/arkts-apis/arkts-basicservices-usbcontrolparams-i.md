# USBControlParams

Represents control transfer parameters.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [USBDeviceRequestParams](arkts-basicservices-usbdevicerequestparams-i.md)

<!--Device-usbManager-interface USBControlParams--><!--Device-usbManager-interface USBControlParams-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## data

```TypeScript
data: Uint8Array
```

Buffer for writing or reading data.

**Type:** Uint8Array

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [USBDeviceRequestParams](arkts-basicservices-usbdevicerequestparams-i.md)

<!--Device-USBControlParams-data: Uint8Array--><!--Device-USBControlParams-data: Uint8Array-End-->

**System capability:** SystemCapability.USB.USBManager

## index

```TypeScript
index: number
```

Index of the request parameter.

**Type:** number

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [USBDeviceRequestParams](arkts-basicservices-usbdevicerequestparams-i.md)

<!--Device-USBControlParams-index: number--><!--Device-USBControlParams-index: number-End-->

**System capability:** SystemCapability.USB.USBManager

## reqType

```TypeScript
reqType: USBControlRequestType
```

Control request type.

**Type:** USBControlRequestType

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [USBDeviceRequestParams](arkts-basicservices-usbdevicerequestparams-i.md)

<!--Device-USBControlParams-reqType: USBControlRequestType--><!--Device-USBControlParams-reqType: USBControlRequestType-End-->

**System capability:** SystemCapability.USB.USBManager

## request

```TypeScript
request: number
```

Request type.

**Type:** number

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [USBDeviceRequestParams](arkts-basicservices-usbdevicerequestparams-i.md)

<!--Device-USBControlParams-request: number--><!--Device-USBControlParams-request: number-End-->

**System capability:** SystemCapability.USB.USBManager

## target

```TypeScript
target: USBRequestTargetType
```

Request target type.

**Type:** USBRequestTargetType

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [USBDeviceRequestParams](arkts-basicservices-usbdevicerequestparams-i.md)

<!--Device-USBControlParams-target: USBRequestTargetType--><!--Device-USBControlParams-target: USBRequestTargetType-End-->

**System capability:** SystemCapability.USB.USBManager

## value

```TypeScript
value: number
```

Request parameter.

**Type:** number

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [USBDeviceRequestParams](arkts-basicservices-usbdevicerequestparams-i.md)

<!--Device-USBControlParams-value: number--><!--Device-USBControlParams-value: number-End-->

**System capability:** SystemCapability.USB.USBManager

