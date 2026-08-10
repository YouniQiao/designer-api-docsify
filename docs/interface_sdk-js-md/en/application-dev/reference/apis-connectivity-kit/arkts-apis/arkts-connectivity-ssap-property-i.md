# Property

SSAP属性。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-ssap-interface Property--><!--Device-ssap-interface Property-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
```

## descriptors

```TypeScript
descriptors?: PropertyDescriptor[]
```

属性中包含的描述符列表。

**Type:** [PropertyDescriptor](arkts-connectivity-ssap-propertydescriptor-i.md)[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-descriptors?: PropertyDescriptor[]--><!--Device-Property-descriptors?: PropertyDescriptor[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## operation

```TypeScript
operation?: int
```

指示如何访问数据值和描述符值。取值为枚举值的或运算。取值范围为全体整数。 默认值： 默认值：READABLE | WRITE_NO_RESPONSE。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-operation?: int--><!--Device-Property-operation?: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## propertyUuid

```TypeScript
propertyUuid: string
```

Property实例的UUID长度必须为32，由16进制数字字符和连字符共36个字符组成，形如“FFFFFFFF-1234-5678-ABCD-000000001234”，代表128比特标识。&lt;br&gt;不允许使用NearLink标准UUID。

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

属性所属的{@link Service}实例的UUID长度必须为32，禁止使用星闪标准服务UUID。&lt;br&gt;不允许使用NearLink标准UUID。

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

Property实例的值。

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Property-value: ArrayBuffer--><!--Device-Property-value: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

