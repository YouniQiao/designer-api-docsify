# ContentForm

Represents data of the content widget type.

**Since:** 23

<!--Device-uniformDataStruct-interface ContentForm--><!--Device-uniformDataStruct-interface ContentForm-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { uniformDataStruct } from '@kit.ArkData';
```

## appIcon

```TypeScript
appIcon?: Uint8Array
```

Application icon data in the content widget.

**Type:** Uint8Array

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-appIcon?: Uint8Array--><!--Device-ContentForm-appIcon?: Uint8Array-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## appName

```TypeScript
appName?: string
```

Application name in the content widget.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-appName?: string--><!--Device-ContentForm-appName?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## description

```TypeScript
description?: string
```

Description of the content widget.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-description?: string--><!--Device-ContentForm-description?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## linkUri

```TypeScript
linkUri?: string
```

Hyperlink in the content widget.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-linkUri?: string--><!--Device-ContentForm-linkUri?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## thumbData

```TypeScript
thumbData?: Uint8Array
```

Image data in the content widget.

**Type:** Uint8Array

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-thumbData?: Uint8Array--><!--Device-ContentForm-thumbData?: Uint8Array-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## title

```TypeScript
title: string
```

Title of the content widget.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-title: string--><!--Device-ContentForm-title: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uniformDataType

```TypeScript
readonly uniformDataType: 'general.content-form'
```

Uniform data type, which has a fixed value of **general.content-form**.

**Type:** 'general.content-form'

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentForm-readonly uniformDataType: 'general.content-form'--><!--Device-ContentForm-readonly uniformDataType: 'general.content-form'-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Examples**

```TypeScript
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
let thumbDataU8Array = new Uint8Array([1, 2, 3, 4, 5]);
let appIconU8Array = new Uint8Array([6, 7, 8, 9, 10]);
let contentForm : uniformDataStruct.ContentForm = {
  uniformDataType : 'general.content-form',
  title : 'MyTitle',
  thumbData : thumbDataU8Array,
  description : 'MyDescription',
  appName : 'MyAppName',
  linkUri : 'MyLinkUri',
  appIcon : appIconU8Array
}
console.info('contentForm.uniformDataType: ' + contentForm.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.CONTENT_FORM, contentForm);
```

