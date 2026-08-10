# ContentForm

内容卡片类型数据，用于跨应用共享内容卡片信息。典型使用场景包括：资讯应用分享文章卡片、电商应用分享商品卡片、社交应用分享内容预览等。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-uniformDataStruct-interface ContentForm--><!--Device-uniformDataStruct-interface ContentForm-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { uniformDataStruct } from 'kits/@kit.ArkData';
```

## appIcon

```TypeScript
appIcon?: Uint8Array
```

内容卡片中的应用图标数据。默认值为空。

**Type:** Uint8Array

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-appIcon?: Uint8Array--><!--Device-ContentForm-appIcon?: Uint8Array-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## appName

```TypeScript
appName?: string
```

内容卡片中应用的应用名。默认值为空字符串。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-appName?: string--><!--Device-ContentForm-appName?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## description

```TypeScript
description?: string
```

内容卡片中的描述信息。默认值为空字符串。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-description?: string--><!--Device-ContentForm-description?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## linkUri

```TypeScript
linkUri?: string
```

内容卡片对应的跳转超链接，需符合URI格式规范。默认值为空字符串。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-linkUri?: string--><!--Device-ContentForm-linkUri?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## thumbData

```TypeScript
thumbData?: Uint8Array
```

内容卡片对应的图片数据。默认值为空。

**Type:** Uint8Array

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-thumbData?: Uint8Array--><!--Device-ContentForm-thumbData?: Uint8Array-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## title

```TypeScript
title: string
```

内容卡片的标题。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-title: string--><!--Device-ContentForm-title: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uniformDataType

```TypeScript
readonly uniformDataType: 'general.content-form'
```

统一数据类型标识为内容卡片类型数据，固定为“general.content-form”。

**Type:** 'general.content-form'

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-readonly uniformDataType: 'general.content-form'--><!--Device-ContentForm-readonly uniformDataType: 'general.content-form'-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

