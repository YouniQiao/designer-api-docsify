# ConnectOptions

在连接指定的后台服务时作为入参，用于接收连接过程中的状态变化，如作为  
[connectServiceExtensionAbility](arkts-ability-uiabilitycontext-c.md#connectserviceextensionability)的入参，连接指定的ServiceExtensionAbility。

**起始版本：** 7

<!--Device-unnamed-export interface ConnectOptions--><!--Device-unnamed-export interface ConnectOptions-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onConnect

```TypeScript
onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void
```

建立连接时的回调函数。

**起始版本：** 7

<!--Device-ConnectOptions-onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void--><!--Device-ConnectOptions-onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| remote | rpc.IRemoteObject | 是 |

## onDisconnect

```TypeScript
onDisconnect(elementName: ElementName): void
```

断开连接时的回调函数。

**起始版本：** 7

<!--Device-ConnectOptions-onDisconnect(elementName: ElementName): void--><!--Device-ConnectOptions-onDisconnect(elementName: ElementName): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |

## onFailed

```TypeScript
onFailed(code: number): void
```

连接失败时的回调函数。

**起始版本：** 7

<!--Device-ConnectOptions-onFailed(code: number): void--><!--Device-ConnectOptions-onFailed(code: number): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
