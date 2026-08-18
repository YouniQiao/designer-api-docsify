# configure (System API)

## Modules to Import

```TypeScript
```

## configure

```TypeScript
function configure(featureId: UserStatusFeature, detail: string): number
```

Configures feature parameters.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-userStatus-function configure(featureId: UserStatusFeature, detail: string): int--><!--Device-userStatus-function configure(featureId: UserStatusFeature, detail: string): int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| featureId | [UserStatusFeature](arkts-multimodalawareness-userstatus-userstatusfeature-e-sys.md) | Yes |
| detail | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-service-exception) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
