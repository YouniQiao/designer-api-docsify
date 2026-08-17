# OnConnectFn

```TypeScript
type OnConnectFn = (elementName: ElementName, remote: rpc.IRemoteObject) => void
```

Callback invoked when a connection is set up.

**Since:** 23

<!--Device-unnamed-type OnConnectFn = (elementName: ElementName, remote: rpc.IRemoteObject) => void--><!--Device-unnamed-type OnConnectFn = (elementName: ElementName, remote: rpc.IRemoteObject) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes | Element name of the ability. |
| remote | rpc.IRemoteObject | Yes | IRemoteObject instance. |

