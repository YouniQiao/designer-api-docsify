# factoryReset (System API)

## Modules to Import

```TypeScript
import { manager } from 'kits/@kit.ConnectivityKit';
```

## factoryReset

```TypeScript
function factoryReset(): Promise<void>
```

Restores NearLink settings.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function factoryReset(): Promise<void>--><!--Device-manager-function factoryReset(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
