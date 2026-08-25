# preloadApplication (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## preloadApplication

```TypeScript
function preloadApplication(bundleName: string, userId: number, mode: PreloadMode, appIndex?: number): Promise<void>
```

Preloads an application process. A successful call does not always mean that the preloading is successful. In other words, the target application process may not be created even if the API is successfully called. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.PRELOAD_APPLICATION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| userId | number | Yes |
| mode | [PreloadMode](arkts-ability-appmanager-preloadmode-e-sys.md) | Yes |
| appIndex | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16300005](../errorcode-ability.md#16300005-bundle-information-does-not-exist) |
