# PropertyWriteRequest

SSAP客户端属性写请求参数说明。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-ssap-interface PropertyWriteRequest--><!--Device-ssap-interface PropertyWriteRequest-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

设备地址。长度必须为17，由16进制数字和冒号组成，形如 "11:22:33:AA:BB:FF"。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyWriteRequest-address: string--><!--Device-PropertyWriteRequest-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## propertyUuid

```TypeScript
propertyUuid: string
```

客户端请求写入的属性实例的UUID。长度必须为36，由16进制数字字符和连字符共36个字符组成，形如“FFFFFFFF-1234-5678-ABCD-000000001234”，代表128比特标识。&lt;br&gt;禁止使用星闪标准服务UUID。禁止使用星闪标准服务UUID。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyWriteRequest-propertyUuid: string--><!--Device-PropertyWriteRequest-propertyUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## requestId

```TypeScript
requestId: int
```

请求ID。取值范围为全体整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyWriteRequest-requestId: int--><!--Device-PropertyWriteRequest-requestId: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuid

```TypeScript
serviceUuid: string
```

属性所属的{@link Service}实例的UUID长度必须为32，禁止使用星闪标准服务UUID。&lt;br&gt;不允许使用NearLink标准UUID。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyWriteRequest-serviceUuid: string--><!--Device-PropertyWriteRequest-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## value

```TypeScript
value: ArrayBuffer
```

需要写入的数据。

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyWriteRequest-value: ArrayBuffer--><!--Device-PropertyWriteRequest-value: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## writeType

```TypeScript
writeType: PropertyWriteType
```

此请求的写入类型。

**Type:** [PropertyWriteType](arkts-connectivity-ssap-propertywritetype-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PropertyWriteRequest-writeType: PropertyWriteType--><!--Device-PropertyWriteRequest-writeType: PropertyWriteType-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

