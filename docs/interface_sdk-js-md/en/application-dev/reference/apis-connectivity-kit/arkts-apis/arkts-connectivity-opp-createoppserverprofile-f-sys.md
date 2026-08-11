# createOppServerProfile (System API)

## Modules to Import

```TypeScript
import { opp } from 'kits/@kit.ConnectivityKit';
```

## createOppServerProfile

```TypeScript
function createOppServerProfile(): OppServerProfile
```

create the instance of OPP server profile.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-opp-function createOppServerProfile(): OppServerProfile--><!--Device-opp-function createOppServerProfile(): OppServerProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [OppServerProfile](arkts-connectivity-opp-oppserverprofile-i-sys.md) | Returns the instance of opp profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |

