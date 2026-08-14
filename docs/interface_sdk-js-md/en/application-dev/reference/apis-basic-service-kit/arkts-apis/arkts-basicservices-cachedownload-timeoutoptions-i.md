# TimeoutOptions

Task timeout configuration.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-cacheDownload-interface TimeoutOptions--><!--Device-cacheDownload-interface TimeoutOptions-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { cacheDownload } from 'cacheDownload';
```

## httpTotalTimeout

```TypeScript
httpTotalTimeout?: int
```

Complete HTTP request-response cycle timeout, in seconds. The default value is 60. The minimum value is 1. The value should be an integer.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimeoutOptions-httpTotalTimeout?: int--><!--Device-TimeoutOptions-httpTotalTimeout?: int-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## networkCheckTimeout

```TypeScript
networkCheckTimeout?: int
```

Network availability check timeout, in seconds. The default value is 20. The minimum value is 0. The maximum value is 20. When set to 0, no check will be performed. The value should be an integer.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimeoutOptions-networkCheckTimeout?: int--><!--Device-TimeoutOptions-networkCheckTimeout?: int-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

