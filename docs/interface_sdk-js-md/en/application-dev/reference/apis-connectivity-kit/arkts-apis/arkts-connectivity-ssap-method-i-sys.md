# Method (System API)

SSAP方法。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-ssap-interface Method--><!--Device-ssap-interface Method-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
```

## methodUuid

```TypeScript
methodUuid: string
```

方法实例的UUID长度必须为36，由16进制数字字符和连字符共36个字符组成，形如“FFFFFFFF-1234-5678-ABCD-000000001234”，代表128比特标识。&lt;br&gt;不允许使用NearLink标准UUID。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Method-methodUuid: string--><!--Device-Method-methodUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

## parameter

```TypeScript
parameter?: ArrayBuffer
```

方法实例的参数

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Method-parameter?: ArrayBuffer--><!--Device-Method-parameter?: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

## result

```TypeScript
result?: ArrayBuffer
```

方法实例的结果

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Method-result?: ArrayBuffer--><!--Device-Method-result?: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

## serviceUuid

```TypeScript
serviceUuid: string
```

方法所属的{@link Service}实例的UUID长度必须为36，由16进制数字字符和连字符共36个字符组成，形如“FFFFFFFF-1234-5678-ABCD-000000001234”，代表128比特标识。&lt;br&gt;不允许使用NearLink标准UUID。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Method-serviceUuid: string--><!--Device-Method-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

