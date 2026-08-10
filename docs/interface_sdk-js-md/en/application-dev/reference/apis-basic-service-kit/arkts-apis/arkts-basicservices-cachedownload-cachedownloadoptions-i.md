# CacheDownloadOptions

缓存下载的配置选项。包括HTTP选项、传输选项和任务选项。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cacheDownload-interface CacheDownloadOptions--><!--Device-cacheDownload-interface CacheDownloadOptions-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## caPath

```TypeScript
caPath?: string
```

CA证书路径。目前仅支持.pem格式证书，默认使用系统预设的CA证书。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-CacheDownloadOptions-caPath?: string--><!--Device-CacheDownloadOptions-caPath?: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## cacheStrategy

```TypeScript
cacheStrategy?: CacheStrategy
```

使用缓存刷新策略FORCE或LAZY，默认使用FORCE。

**Type:** [CacheStrategy](arkts-basicservices-cachedownload-cachestrategy-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CacheDownloadOptions-cacheStrategy?: CacheStrategy--><!--Device-CacheDownloadOptions-cacheStrategy?: CacheStrategy-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## headers

```TypeScript
headers?: Record<string, string>
```

缓存下载任务在HTTP传输时使用的请求头。默认值为空。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CacheDownloadOptions-headers?: Record<string, string>--><!--Device-CacheDownloadOptions-headers?: Record<string, string>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## retry

```TypeScript
retry?: RetryOptions
```

Task retry configuration.

**Type:** [RetryOptions](arkts-basicservices-cachedownload-retryoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CacheDownloadOptions-retry?: RetryOptions--><!--Device-CacheDownloadOptions-retry?: RetryOptions-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## sslType

```TypeScript
sslType?: SslType
```

使用安全通信协议TLS或TLCP，默认使用TLS。当前TLS和TLCP均不支持双向认证。

**Type:** [SslType](arkts-basicservices-cachedownload-ssltype-e.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-CacheDownloadOptions-sslType?: SslType--><!--Device-CacheDownloadOptions-sslType?: SslType-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## timeout

```TypeScript
timeout?: TimeoutOptions
```

Task timeout configuration.

**Type:** [TimeoutOptions](arkts-basicservices-cachedownload-timeoutoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CacheDownloadOptions-timeout?: TimeoutOptions--><!--Device-CacheDownloadOptions-timeout?: TimeoutOptions-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

