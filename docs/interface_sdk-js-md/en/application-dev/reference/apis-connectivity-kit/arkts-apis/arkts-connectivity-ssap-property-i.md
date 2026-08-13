# Property

Describes the SSAP property.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-ssap-interface Property--><!--Device-ssap-interface Property-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from '@kit.ConnectivityKit';
```

## descriptors

```TypeScript
descriptors?: PropertyDescriptor[]
```

The list of propertyDescriptor contained in the property.

**Type:** PropertyDescriptor[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-descriptors?: PropertyDescriptor[]--><!--Device-Property-descriptors?: PropertyDescriptor[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## operation

```TypeScript
operation?: int
```

Indications specify how data values and descriptor values are accessed [Operation](arkts-connectivity-ssap-operation-e.md#Operation). The value is the OR operation of enumerated values. The value should be an integer. Default value: 3(READABLE | WRITE_NO_RESPONSE).

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-operation?: int--><!--Device-Property-operation?: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## propertyUuid

```TypeScript
propertyUuid: string
```

The UUID of a Property instance. The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-), for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier. &lt;br&gt;NearLink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-propertyUuid: string--><!--Device-Property-propertyUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the [Service](arkts-connectivity-ssap-service-i.md#Service) instance which the property belongs to. The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-), for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier. &lt;br&gt;NearLink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-serviceUuid: string--><!--Device-Property-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## value

```TypeScript
value: ArrayBuffer
```

The value of a Property instance.

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-value: ArrayBuffer--><!--Device-Property-value: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

