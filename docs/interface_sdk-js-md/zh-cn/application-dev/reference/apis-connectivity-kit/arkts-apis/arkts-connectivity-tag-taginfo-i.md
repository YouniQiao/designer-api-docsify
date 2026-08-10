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

## supportedProfiles

```TypeScript
supportedProfiles: number[]
```

The supported technology list of this tag.

**类型：** number[]

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.nfc.tag/tag.TagInfo#technology

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagInfo-supportedProfiles: number[]--><!--Device-TagInfo-supportedProfiles: number[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## technology

```TypeScript
technology: int[]
```

The supported technology list of this tag.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TagInfo-technology: int[]--><!--Device-TagInfo-technology: int[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## uid

```TypeScript
uid: int[]
```

The uid of this tag, it.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TagInfo-uid: int[]--><!--Device-TagInfo-uid: int[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

