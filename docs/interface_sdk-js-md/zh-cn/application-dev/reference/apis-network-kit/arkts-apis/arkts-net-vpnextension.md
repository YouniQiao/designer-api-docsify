# @ohos.net.vpnExtension(VPN增强管理)

三方VPN管理模块，支持三方VPN的启动和停止功能。三方VPN是指由第三方提供的VPN服务，它们通常提供更多的功能和更广泛的网络连接选项，包括更多的安全和隐私功能，以及更全面的定制选项。当前提供三方VPN能力主要用于创建虚拟网卡及配置 VPN路由信息，连接隧道过程及内部连接的协议需要应用内部自行实现。

> **说明：**&gt;
> 本模块首批接口从 API version 11 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

> 以下模块不支持在VpnExtensionAbility中引用，可能会导致程序异常退出。

> - [@ohos.contact (联系人)](../../apis-contacts-kit/arkts-apis/arkts-contact.md)

> - [@ohos.geolocation](../../apis-location-kit/arkts-apis/arkts-geolocation.md)、
> [@ohos.geoLocationManager (位置服务)](../../apis-location-kit/arkts-apis/arkts-geolocationmanager.md)

> - [@ohos.multimedia.audio(音频管理)](../../apis-audio-kit/arkts-apis/arkts-multimedia-audio.md)

> - [@ohos.multimedia.camera(相机管理)](../../apis-camera-kit/arkts-apis/arkts-multimedia-camera.md)

> - [@ohos.telephony.call (拨打电话)](../../apis-telephony-kit/arkts-apis/arkts-telephony-call.md)

> - [@ohos.telephony.sim (SIM卡管理)](../../apis-telephony-kit/arkts-apis/arkts-telephony-sim.md)

> - [@ohos.telephony.sms (短信服务)](../../apis-telephony-kit/arkts-apis/arkts-telephony-sms.md)

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## 导入模块

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createVpnConnection(VPN增强管理)](arkts-network-vpnextension-createvpnconnection-f.md) |
| [createVpnObserver(VPN增强管理)](arkts-network-vpnextension-createvpnobserver-f.md) |
| [startVpnExtensionAbility(VPN增强管理)](arkts-network-vpnextension-startvpnextensionability-f.md) |
| [stopVpnExtensionAbility(VPN增强管理)](arkts-network-vpnextension-stopvpnextensionability-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [isAlwaysOnVpnEnabled(VPN增强管理)](arkts-network-vpnextension-isalwaysonvpnenabled-f-sys.md) |
| [setAlwaysOnVpnEnabled(VPN增强管理)](arkts-network-vpnextension-setalwaysonvpnenabled-f-sys.md) |
| [updateVpnAuthorizedState(VPN增强管理)](arkts-network-vpnextension-updatevpnauthorizedstate-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [VpnConfig(VPN增强管理)](arkts-network-vpnextension-vpnconfig-i.md) |
| [VpnConnection(VPN增强管理)](arkts-network-vpnextension-vpnconnection-i.md) |
| [VpnObserver(VPN增强管理)](arkts-network-vpnextension-vpnobserver-i.md) |

### 类型

| 名称 |
| --- |
| [LinkAddress(VPN增强管理)](arkts-network-vpnextension-linkaddress-t.md) |
| [RouteInfo(VPN增强管理)](arkts-network-vpnextension-routeinfo-t.md) |
| [VpnExtensionContext(VPN增强管理)](arkts-network-vpnextension-vpnextensioncontext-t.md) |
