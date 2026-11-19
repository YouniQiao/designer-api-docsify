# unregisterControlComponentResultCallback

## Modules to Import

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## unregisterControlComponentResultCallback

```TypeScript
export function unregisterControlComponentResultCallback(): void
```

Callback of the simulated click result of the deregistration control component. Releases callback resources when a service ends.

**Since:** 26.1.0

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used in both the stage model and FA model.

<!--Device-abilityToolAccessCtrl-export function unregisterControlComponentResultCallback(): void--><!--Device-abilityToolAccessCtrl-export function unregisterControlComponentResultCallback(): void-End-->

**System capability:** SystemCapability.Security.Asset

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [24010001](../errorcode-abilityToolAccessCtrl-sys.md#24010001-system-service-abnormal) | Service is abnormal. Possible cause: IPC failed. |
| [24010002](../errorcode-abilityToolAccessCtrl-sys.md#24010002-internal-service-error) | Common internal error. Possible cause: dependent service unavailable, resource access failure, etc. |
