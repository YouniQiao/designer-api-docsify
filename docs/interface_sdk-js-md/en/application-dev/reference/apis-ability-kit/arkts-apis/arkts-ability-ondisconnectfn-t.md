# OnDisconnectFn

```TypeScript
type OnDisconnectFn = (elementName: ElementName) => void
```

与指定的后台服务成功断开连接时，会触发该回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-type OnDisconnectFn = (elementName: ElementName) => void--><!--Device-unnamed-type OnDisconnectFn = (elementName: ElementName) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes | 目标Ability的elementName。 |

