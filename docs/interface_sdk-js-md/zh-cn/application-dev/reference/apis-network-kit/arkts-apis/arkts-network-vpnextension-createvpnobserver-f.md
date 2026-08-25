# createVpnObserver

## 导入模块

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';
```

## createVpnObserver

```TypeScript
function createVpnObserver(): VpnObserver
```

创建一个VPN观察者对象。用于监听VPN相关事件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 |
| --- |
| [VpnObserver](arkts-network-vpnextension-vpnobserver-i.md) |

**示例**

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';

let vpnObserver: vpnExtension.VpnObserver = vpnExtension.createVpnObserver();
```
