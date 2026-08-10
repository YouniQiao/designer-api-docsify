# createVpnObserver

## 导入模块

```TypeScript
import { vpnExtension } from 'kits/@kit.NetworkKit';
```

## createVpnObserver

```TypeScript
function createVpnObserver(): VpnObserver
```

Create a VPN observer.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-vpnExtension-function createVpnObserver(): VpnObserver--><!--Device-vpnExtension-function createVpnObserver(): VpnObserver-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VpnObserver](arkts-network-vpnextension-vpnobserver-i.md) | The VpnObserver instance. |

## 示例

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';

let vpnObserver: vpnExtension.VpnObserver = vpnExtension.createVpnObserver();
```

