# ConnectResult

客户端调用connect()后，返回的连接结果。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-linkEnhance-interface ConnectResult--><!--Device-linkEnhance-interface ConnectResult-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { linkEnhance } from 'kits/@kit.DistributedServiceKit';
```

## deviceId

```TypeScript
deviceId: string
```

对端设备ID，成功返回对端设备的deviceId，失败返回空字符串。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectResult-deviceId: string--><!--Device-ConnectResult-deviceId: string-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## reason

```TypeScript
reason: int
```

连接成功返回0，连接失败返回错误码：

- 32390200：表示客户端连接超时。  
- 32390201：表示服务端服务未启动。  
- 32390300：表示内部错误。

更多关于错误码的详细介绍请参考[增强连接错误码](../../../reference/apis-distributedservice-kit/errorcode-link-enhance.md)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectResult-reason: int--><!--Device-ConnectResult-reason: int-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## success

```TypeScript
success: boolean
```

连接结果，true表示连接成功，false表示连接失败。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectResult-success: boolean--><!--Device-ConnectResult-success: boolean-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

