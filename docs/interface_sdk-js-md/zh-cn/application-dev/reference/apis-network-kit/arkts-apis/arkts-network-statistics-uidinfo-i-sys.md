# UidInfo（系统接口）

Parameters for obtaining detailed information on application traffic usage.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-statistics-export interface UidInfo--><!--Device-statistics-export interface UidInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## ifaceInfo

```TypeScript
ifaceInfo: IfaceInfo
```

See {@link IfaceInfo}

**类型：** [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-UidInfo-ifaceInfo: IfaceInfo--><!--Device-UidInfo-ifaceInfo: IfaceInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## uid

```TypeScript
uid: int
```

Uid of app for querying traffic.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-UidInfo-uid: int--><!--Device-UidInfo-uid: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

