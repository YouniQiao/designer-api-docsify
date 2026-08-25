# VpnObserver

VPN观察者对象。用于监听VPN相关事件。在调用VpnObserver的方法前，需要先通过[vpnExtension.createVpnObserver](arkts-network-vpnextension-createvpnobserver-f.md) 创建VPN连接对象。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## 导入模块

```TypeScript
import { vpnExtension } from 'kits/@kit.NetworkKit';
```

## offAuthorizationResult

```TypeScript
offAuthorizationResult(callback?: Callback<boolean>): void
```

取消注册用户授权结果监听器。

> **注意**&gt;
> 多次调用[onAuthorizationResult](#onauthorizationresult)注册监听时，若需取消授权结果监听，需要传最后一次调用时传入的callback，或者不传入参数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback & lt;boolean & gt; | 否 |

## onAuthorizationResult

```TypeScript
onAuthorizationResult(callback: Callback<boolean>): void
```

注册用户授权结果监听器。授权结果在调用[startVpnExtensionAbility](arkts-network-vpnextension-startvpnextensionability-f.md)弹出授权弹窗，用户点击弹窗后通知，仅接收当前 VPN的结果。在不需要监听授权结果时可以调用[offAuthorizationResult](#offauthorizationresult)接口取消注册。

> **注意**&gt;
> 多次调用该接口时，仅最后一次传入的callback生效。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback & lt;boolean & gt; | 是 |
