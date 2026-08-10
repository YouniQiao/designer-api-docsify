# ConnectOptions

在连接指定的后台服务时作为入参，用于接收连接过程中的状态变化，如作为  
[connectServiceExtensionAbility](arkts-ability-uiabilitycontext-c.md#connectserviceextensionability)的入参，连接指定的ServiceExtensionAbility。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ConnectOptions--><!--Device-unnamed-export interface ConnectOptions-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onConnect

```TypeScript
onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void
```

建立连接时的回调函数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ConnectOptions-onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void--><!--Device-ConnectOptions-onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes | 目标Ability的elementName。 |
| remote | rpc.IRemoteObject | Yes | 用于与目标Ability进行IPC通信的IRemoteObject实例。 |

## onConnect

```TypeScript
onConnect: OnConnectFn
```

与指定的后台服务成功建立连接时，会触发该回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ConnectOptions-onConnect: OnConnectFn--><!--Device-ConnectOptions-onConnect: OnConnectFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onDisconnect

```TypeScript
onDisconnect(elementName: ElementName): void
```

断开连接时的回调函数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ConnectOptions-onDisconnect(elementName: ElementName): void--><!--Device-ConnectOptions-onDisconnect(elementName: ElementName): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes | 目标Ability的elementName。 |

## onDisconnect

```TypeScript
onDisconnect: OnDisconnectFn
```

与指定的后台服务成功断开连接时，会触发该回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ConnectOptions-onDisconnect: OnDisconnectFn--><!--Device-ConnectOptions-onDisconnect: OnDisconnectFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onFailed

```TypeScript
onFailed(code: number): void
```

连接失败时的回调函数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ConnectOptions-onFailed(code: number): void--><!--Device-ConnectOptions-onFailed(code: number): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes | 连接指定Ability失败返回的错误码。  错误码详细介绍请参考[通用错误码](../errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。  201 - The application does not have permission to call the interface.  16000001 - The specified ability does not exist.  16000002 - Incorrect ability type.  16000004 - Cannot start an invisible component.  16000005 - The specified process does not have the permission.  16000006 - Cross-user operations are not allowed.  16000008 - The crowdtesting application expires.  16000053 - The ability is not on the top of the UI.  16000055 - Installation-free timed out.  16000050 - Internal error. |

## onFailed

```TypeScript
onFailed: OnFailedFn
```

与指定的后台服务建立连接失败时，会触发该回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ConnectOptions-onFailed: OnFailedFn--><!--Device-ConnectOptions-onFailed: OnFailedFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

