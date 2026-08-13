# OnConnectFn

```TypeScript
type OnConnectFn = (elementName: ElementName, remote: rpc.IRemoteObject) => void
```

与指定的后台服务成功建立连接时，会触发该回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-type OnConnectFn = (elementName: ElementName, remote: rpc.IRemoteObject) => void--><!--Device-unnamed-type OnConnectFn = (elementName: ElementName, remote: rpc.IRemoteObject) => void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| [remote](../../apis-driver-development-kit/arkts-apis/arkts-driverdevelopment-devicemanager-remotedevicedriver-i.md) | rpc.IRemoteObject | 是 |
