# createServer

## Modules to Import

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
```

## createServer

```TypeScript
function createServer(): Server
```

Creates a SSAP server instance.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ssap-function createServer(): Server--><!--Device-ssap-function createServer(): Server-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Server](arkts-connectivity-ssap-server-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
