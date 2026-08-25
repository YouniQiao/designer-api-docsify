# FenceExtensionContext

class of static subscriber extension context.@extends ExtensionContext

**Inheritance/Implementation:** FenceExtensionContext extends ExtensionContext

**Since:** 14

**System capability:** SystemCapability.Location.Location.Geofence

## Modules to Import

```TypeScript
import { FenceExtensionContext } from 'kits/@kit.LocationKit';
```

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

Starts a new service extension ability. If the target service extension ability is visible, you can start the target service extension ability; If the target service extension ability is invisible, you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to start target invisible service extension ability. If the target service extension ability is in cross-device, you need to apply for permission:ohos.permission.DISTRIBUTED_DATASYNC.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Location.Location.Geofence

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-application-under-control) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000019](../../apis-ability-kit/errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16200001](../../apis-ability-kit/errorcode-ability.md#16200001-caller-released) |
