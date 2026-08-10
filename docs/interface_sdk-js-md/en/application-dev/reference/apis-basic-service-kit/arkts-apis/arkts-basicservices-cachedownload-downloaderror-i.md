# DownloadError

预下载错误回调的返回信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cacheDownload-interface DownloadError--><!--Device-cacheDownload-interface DownloadError-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## errorCode

```TypeScript
readonly errorCode: ErrorCode
```

预下载错误回调返回的特定错误类型。

**Type:** [ErrorCode](arkts-basicservices-cachedownload-errorcode-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DownloadError-readonly errorCode: ErrorCode--><!--Device-DownloadError-readonly errorCode: ErrorCode-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## message

```TypeScript
readonly message: string
```

返回[通用错误码](../../../reference/errorcode-universal.md)或  
[HTTP错误码](../../../reference/apis-network-kit/errorcode-net-http.md)。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DownloadError-readonly message: string--><!--Device-DownloadError-readonly message: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

