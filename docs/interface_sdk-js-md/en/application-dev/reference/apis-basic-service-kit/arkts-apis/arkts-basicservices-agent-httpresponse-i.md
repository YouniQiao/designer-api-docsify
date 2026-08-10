# HttpResponse

任务响应头的数据结构。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-agent-interface HttpResponse--><!--Device-agent-interface HttpResponse-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## headers

```TypeScript
readonly headers: Map<string, Array<string>>
```

Http响应头部。

**Type:** Map&lt;string, Array&lt;string&gt;&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HttpResponse-readonly headers: Map<string, Array<string>>--><!--Device-HttpResponse-readonly headers: Map<string, Array<string>>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## reason

```TypeScript
readonly reason: string
```

Http响应原因。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HttpResponse-readonly reason: string--><!--Device-HttpResponse-readonly reason: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## statusCode

```TypeScript
readonly statusCode: int
```

Http响应状态码。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HttpResponse-readonly statusCode: int--><!--Device-HttpResponse-readonly statusCode: int-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## version

```TypeScript
readonly version: string
```

Http版本。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HttpResponse-readonly version: string--><!--Device-HttpResponse-readonly version: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

