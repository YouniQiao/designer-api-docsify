# ServerResponse

服务端对指定读或写请求的响应的参数。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-ssap-interface ServerResponse--><!--Device-ssap-interface ServerResponse-End-->

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

<!--Device-ServerResponse-address: string--><!--Device-ServerResponse-address: string-End-->

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

<!--Device-ServerResponse-requestId: int--><!--Device-ServerResponse-requestId: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## value

```TypeScript
value: ArrayBuffer
```

响应数据。

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServerResponse-value: ArrayBuffer--><!--Device-ServerResponse-value: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

