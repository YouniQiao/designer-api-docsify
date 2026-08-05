# Property

Describes the SSAP property.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-ssap-interface Property--><!--Device-ssap-interface Property-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## descriptors

```TypeScript
descriptors?: PropertyDescriptor[]
```

The list of \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ contained in the property.

**Type:** PropertyDescriptor[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-descriptors?: PropertyDescriptor[]--><!--Device-Property-descriptors?: PropertyDescriptor[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## operation

```TypeScript
operation?: int
```

Indications specify how data values and descriptor values are accessed \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. The value is the OR operation of enumerated values. The value should be an integer. Default value: 3(READABLE | WRITE\_NO\_RESPONSE).

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-operation?: int--><!--Device-Property-operation?: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## propertyUuid

```TypeScript
propertyUuid: string
```

The UUID of a Property instance. The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-), for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_NearLink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-propertyUuid: string--><!--Device-Property-propertyUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance which the property belongs to. The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-), for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NearLink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-value: ArrayBuffer--><!--Device-Property-value: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

