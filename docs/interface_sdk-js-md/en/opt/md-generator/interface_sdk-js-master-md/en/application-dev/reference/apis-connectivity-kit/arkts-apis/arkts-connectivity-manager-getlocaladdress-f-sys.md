# getLocalAddress (System API)

## Modules to Import

```TypeScript
```

## getLocalAddress

```TypeScript
function getLocalAddress(): string
```

Gets the MAC address of the local device.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.GET_NEARLINK_LOCAL_MAC

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function getLocalAddress(): string--><!--Device-manager-function getLocalAddress(): string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
