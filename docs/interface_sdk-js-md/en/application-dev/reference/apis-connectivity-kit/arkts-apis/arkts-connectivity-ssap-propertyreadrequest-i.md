# PropertyReadRequest

Describes the parameters of the SSAP client's property read request.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-ssap-interface PropertyReadRequest--><!--Device-ssap-interface PropertyReadRequest-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## address

```TypeScript
address: string
```

Indicates the device address.The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyReadRequest-address: string--><!--Device-PropertyReadRequest-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## propertyUuid

```TypeScript
propertyUuid: string
```

The UUID of the Property instance which client request to read.The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-),for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_NearLink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyReadRequest-propertyUuid: string--><!--Device-PropertyReadRequest-propertyUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## requestId

```TypeScript
requestId: int
```

The request ID.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyReadRequest-requestId: int--><!--Device-PropertyReadRequest-requestId: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance which the property belongs to.The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-),for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NearLink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyReadRequest-serviceUuid: string--><!--Device-PropertyReadRequest-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

