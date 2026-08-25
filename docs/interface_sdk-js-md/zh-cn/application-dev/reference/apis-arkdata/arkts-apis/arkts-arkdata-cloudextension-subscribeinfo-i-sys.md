# SubscribeInfo（系统接口）

订阅信息

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cloudExtension } from '@kit.ArkData';
```

## expirationTime

```TypeScript
expirationTime: long
```

订阅过期时间（ms）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

## subscribe

```TypeScript
subscribe: Record<string, Array<SubscribeId>>
```

订阅信息。

**类型：** Record&lt;string, Array&lt;[SubscribeId](arkts-arkdata-cloudextension-subscribeid-i-sys.md)&gt;&gt;

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。
