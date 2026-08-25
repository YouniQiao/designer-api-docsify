# @ohos.nearlink.manager(星闪基础管理能力)

本模块提供了星闪基础管理能力，包括打开/关闭星闪、获取本机MAC地址、设置连接模式等能力。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

## 导入模块

```TypeScript
import { manager } from '@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getLocalName(星闪基础管理能力)](arkts-connectivity-manager-getlocalname-f.md) |
| [getPairedDevices(星闪基础管理能力)](arkts-connectivity-manager-getpaireddevices-f.md) |
| [getState(星闪基础管理能力)](arkts-connectivity-manager-getstate-f.md) |
| [isNearLinkSupported(星闪基础管理能力)](arkts-connectivity-manager-isnearlinksupported-f.md) |
| [offStateChange(星闪基础管理能力)](arkts-connectivity-manager-offstatechange-f.md) |
| [onStateChange(星闪基础管理能力)](arkts-connectivity-manager-onstatechange-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [disable(星闪基础管理能力)](arkts-connectivity-manager-disable-f-sys.md) |
| [enable(星闪基础管理能力)](arkts-connectivity-manager-enable-f-sys.md) |
| [factoryReset(星闪基础管理能力)](arkts-connectivity-manager-factoryreset-f-sys.md) |
| [getLocalAddress(星闪基础管理能力)](arkts-connectivity-manager-getlocaladdress-f-sys.md) |
| [setConnectionMode(星闪基础管理能力)](arkts-connectivity-manager-setconnectionmode-f-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [NearlinkState(星闪基础管理能力)](arkts-connectivity-manager-nearlinkstate-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ConnectionMode(星闪基础管理能力)](arkts-connectivity-manager-connectionmode-e-sys.md) |
<!--DelEnd-->
