# PropertyDescriptor

```TypeScript
interface PropertyDescriptor
```

Defines the descriptor of a property.

**Since:** 26.0.0

<!--Device-ssap-interface PropertyDescriptor--><!--Device-ssap-interface PropertyDescriptor-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from '@kit.ConnectivityKit';
```

## descriptorType

```TypeScript
descriptorType: PropertyDescriptorType
```

Descriptor type of a property.

**Type:** [PropertyDescriptorType](arkts-connectivity-ssap-propertydescriptortype-e.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PropertyDescriptor-descriptorType: PropertyDescriptorType--><!--Device-PropertyDescriptor-descriptorType: PropertyDescriptorType-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## isWriteable

```TypeScript
isWriteable?: boolean
```

The asterisk(*) indicates whether the descriptor is writable. true: writable; false: not writable. The default value is true.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PropertyDescriptor-isWriteable?: boolean--><!--Device-PropertyDescriptor-isWriteable?: boolean-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## propertyUuid

```TypeScript
propertyUuid: string
```

Property UUID, in the same format as **serviceUuid**.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PropertyDescriptor-propertyUuid: string--><!--Device-PropertyDescriptor-propertyUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuid

```TypeScript
serviceUuid: string
```

Indicates the UUID of the Sparkling service. The value is a string of 36 characters consisting of 32 hexadecimal digits and four hyphens(-), for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicates a 128-bit identifier. Starblink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PropertyDescriptor-serviceUuid: string--><!--Device-PropertyDescriptor-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## value

```TypeScript
value: ArrayBuffer
```

Data value of a descriptor.

**Type:** ArrayBuffer

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PropertyDescriptor-value: ArrayBuffer--><!--Device-PropertyDescriptor-value: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base
