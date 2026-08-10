# OnConnectFn

```TypeScript
type OnConnectFn = (elementName: ElementName, remote: rpc.IRemoteObject) => void
```

与指定的后台服务成功建立连接时，会触发该回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-type OnConnectFn = (elementName: ElementName, remote: rpc.IRemoteObject) => void--><!--Device-unnamed-type OnConnectFn = (elementName: ElementName, remote: rpc.IRemoteObject) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes | 目标Ability的elementName。 |
| remote | rpc.IRemoteObject | Yes | 用于与目标Ability进行IPC通信的IRemoteObject实例。 |

