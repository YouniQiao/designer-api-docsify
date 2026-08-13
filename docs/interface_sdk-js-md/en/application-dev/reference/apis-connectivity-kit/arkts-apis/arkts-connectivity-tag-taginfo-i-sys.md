# TagInfo

Provides tag information. &lt;p&gt;This class provides the technology a tag supports, for example, NFC-A. Applications can create different tags based on the supported technology.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-tag-export interface TagInfo--><!--Device-tag-export interface TagInfo-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## extrasData

```TypeScript
extrasData: PacMap[]
```

The extra data for each technology of this tag.

**Type:** [PacMap](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityhelper-pacmap-i.md)[]

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagInfo-extrasData: PacMap[]--><!--Device-TagInfo-extrasData: PacMap[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**System API:** This is a system API.

## remoteTagService

```TypeScript
remoteTagService: rpc.RemoteObject
```

The extra data for the technology of this tag.

**Type:** rpc.RemoteObject

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagInfo-remoteTagService: rpc.RemoteObject--><!--Device-TagInfo-remoteTagService: rpc.RemoteObject-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**System API:** This is a system API.

## tagRfDiscId

```TypeScript
tagRfDiscId: int
```

The the RF discovery id of this tag.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagInfo-tagRfDiscId: int--><!--Device-TagInfo-tagRfDiscId: int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**System API:** This is a system API.

