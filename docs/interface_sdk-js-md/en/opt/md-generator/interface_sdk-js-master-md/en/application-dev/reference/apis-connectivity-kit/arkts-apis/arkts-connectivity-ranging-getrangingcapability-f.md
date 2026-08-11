# getRangingCapability

## Modules to Import

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## getRangingCapability

```TypeScript
function getRangingCapability(): Promise<RangingCapabilitySupported>
```

Queries whether the current device supports ranging capability.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ranging-function getRangingCapability(): Promise<RangingCapabilitySupported>--><!--Device-ranging-function getRangingCapability(): Promise<RangingCapabilitySupported>-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RangingCapabilitySupported&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 34900053 |
| [201](../../errorcode-universal.md#201-permission-denied) |
