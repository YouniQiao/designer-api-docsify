# setConnectionMode (System API)

## Modules to Import

```TypeScript
import { manager } from '@kit.ConnectivityKit';
```

## setConnectionMode

```TypeScript
function setConnectionMode(mode: ConnectionMode, duration: number): Promise<void>
```

Sets the NearLink connection mode for a device.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function setConnectionMode(mode: ConnectionMode, duration: int): Promise<void>--><!--Device-manager-function setConnectionMode(mode: ConnectionMode, duration: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [ConnectionMode](arkts-connectivity-manager-connectionmode-e-sys.md) | Yes |
| duration | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 36100040 |
