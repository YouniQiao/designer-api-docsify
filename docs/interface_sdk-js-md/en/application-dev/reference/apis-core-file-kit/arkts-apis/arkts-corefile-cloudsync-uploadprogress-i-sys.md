# UploadProgress (System API)

文件上传进度信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cloudSync-interface UploadProgress--><!--Device-cloudSync-interface UploadProgress-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## error

```TypeScript
error: ErrorType
```

上传的错误类型。

**Type:** [ErrorType](../../apis-media-kit/arkts-apis/arkts-media-soundpool-errortype-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UploadProgress-error: ErrorType--><!--Device-UploadProgress-error: ErrorType-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## processed

```TypeScript
processed: long
```

已上传数据大小，取值范围[0, 9223372036854775807]，单位：Byte。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UploadProgress-processed: long--><!--Device-UploadProgress-processed: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## size

```TypeScript
size: long
```

当前文件总大小，取值范围[0, 9223372036854775807]，单位：Byte。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UploadProgress-size: long--><!--Device-UploadProgress-size: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## state

```TypeScript
state: UploadState
```

文件上传状态。

**Type:** [UploadState](arkts-corefile-cloudsync-uploadstate-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UploadProgress-state: UploadState--><!--Device-UploadProgress-state: UploadState-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## uri

```TypeScript
uri: string
```

当前文件的URI。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UploadProgress-uri: string--><!--Device-UploadProgress-uri: string-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

