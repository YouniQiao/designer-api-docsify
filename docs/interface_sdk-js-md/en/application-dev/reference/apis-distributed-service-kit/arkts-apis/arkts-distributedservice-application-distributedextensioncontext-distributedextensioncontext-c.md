# DistributedExtensionContext

用于分布式扩展功能的实现。

**Inheritance/Implementation:** DistributedExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class DistributedExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class DistributedExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { DistributedExtensionContext } from 'kits/@kit.DistributedServiceKit';
```

## connectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

ArkTS-Sta:
```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): long
```

连接到远程服务扩展能力。

此方法连接到远程设备上的服务扩展能力。必须实现{@link ConnectOptions}接口才能获取目标的代理连接时的服务扩展。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-DistributedExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 指示要连接的服务扩展 |
| options | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | Yes | 连接回调 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 返回连接ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |

## disconnectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
disconnectServiceExtensionAbility(connection: long): Promise<void>
```

断开与远程服务扩展功能的连接。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-DistributedExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 从connectServiceExtensionAbility返回的连接ID |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 函数返回的promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 16000003 | The connection id does not exist. |
| 16000011 | The ability has been destroyed. The context is no longer valid, meaning the context does not exist. |

