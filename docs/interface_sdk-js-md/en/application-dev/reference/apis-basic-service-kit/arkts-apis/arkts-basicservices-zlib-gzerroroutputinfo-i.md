# GzErrorOutputInfo

GzError返回信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-zlib-interface GzErrorOutputInfo--><!--Device-zlib-interface GzErrorOutputInfo-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## status

```TypeScript
status: ReturnStatus
```

返回zlib文件状态码，参考ReturnStatus的定义。

**Type:** [ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzErrorOutputInfo-status: ReturnStatus--><!--Device-GzErrorOutputInfo-status: ReturnStatus-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## statusMsg

```TypeScript
statusMsg: string
```

zlib文件上发生的最后一个状态的状态消息。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzErrorOutputInfo-statusMsg: string--><!--Device-GzErrorOutputInfo-statusMsg: string-End-->

**System capability:** SystemCapability.BundleManager.Zlib

