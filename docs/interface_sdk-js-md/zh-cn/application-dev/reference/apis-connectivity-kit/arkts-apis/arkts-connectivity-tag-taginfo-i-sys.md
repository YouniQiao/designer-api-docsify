# TagInfo

Provides tag information.&lt;p&gt;This class provides the technology a tag supports, for example, NFC-A. Applications can create different tags based on the supported technology.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-tag-export interface TagInfo--><!--Device-tag-export interface TagInfo-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## extrasData

```TypeScript
extrasData: PacMap[]
```

The extra data for each technology of this tag.

**类型：** [PacMap](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityhelper-pacmap-i.md)[]

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagInfo-extrasData: PacMap[]--><!--Device-TagInfo-extrasData: PacMap[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**系统接口：** 此接口为系统接口。

## remoteTagService

```TypeScript
remoteTagService: rpc.RemoteObject
```

The extra data for the technology of this tag.

**类型：** rpc.RemoteObject

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagInfo-remoteTagService: rpc.RemoteObject--><!--Device-TagInfo-remoteTagService: rpc.RemoteObject-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**系统接口：** 此接口为系统接口。

## tagRfDiscId

```TypeScript
tagRfDiscId: int
```

The the RF discovery id of this tag.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagInfo-tagRfDiscId: int--><!--Device-TagInfo-tagRfDiscId: int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**系统接口：** 此接口为系统接口。

