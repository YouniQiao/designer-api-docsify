# PropertyDescriptor

Describes the SSAP descriptor for property.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-ssap-interface PropertyDescriptor--><!--Device-ssap-interface PropertyDescriptor-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from 'ssap';
```

## descriptorType

```TypeScript
descriptorType: PropertyDescriptorType
```

The type of the propertyDescriptor instance.

**Type:** [PropertyDescriptorType](arkts-connectivity-ssap-propertydescriptortype-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyDescriptor-descriptorType: PropertyDescriptorType--><!--Device-PropertyDescriptor-descriptorType: PropertyDescriptorType-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## isWriteable

```TypeScript
isWriteable?: boolean
```

Indicates whether the descriptor is writable. Default value: true.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyDescriptor-isWriteable?: boolean--><!--Device-PropertyDescriptor-isWriteable?: boolean-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## propertyUuid

```TypeScript
propertyUuid: string
```

The UUID of the [Property](arkts-connectivity-ssap-property-i.md#Property) instance which the propertyDescriptor belongs to. The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-), for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier. <br>NearLink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyDescriptor-propertyUuid: string--><!--Device-PropertyDescriptor-propertyUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the [Service](arkts-connectivity-ssap-service-i.md#Service) instance which the master property of descriptor belongs to. The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-), for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier. <br>NearLink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyDescriptor-serviceUuid: string--><!--Device-PropertyDescriptor-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## value

```TypeScript
value: ArrayBuffer
```

The value of the propertyDescriptor instance.

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyDescriptor-value: ArrayBuffer--><!--Device-PropertyDescriptor-value: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

