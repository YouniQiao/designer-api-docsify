# registerControlComponentResultCallback

## Modules to Import

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## registerControlComponentResultCallback

```TypeScript
export function registerControlComponentResultCallback(callback: ResultCallback): void
```

Registers the control component to simulate the click result callback. After registration, the result of each simulated click of the control component is returned through this callback. Only one callback can be registered in a process. Repeated registration overwrites the previously registered callback.

**Since:** 26.1.0

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used in both the stage model and FA model.

<!--Device-abilityToolAccessCtrl-export function registerControlComponentResultCallback(callback: ResultCallback): void--><!--Device-abilityToolAccessCtrl-export function registerControlComponentResultCallback(callback: ResultCallback): void-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ResultCallback](arkts-ability-abilitytoolaccessctrl-resultcallback-t.md) | Yes | Callback function for receiving the simulated click operation result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [24010000](../errorcode-abilityToolAccessCtrl-sys.md#24010000-invalid-parameter) | Invalid parameter. callback is invalid. |
| [24010001](../errorcode-abilityToolAccessCtrl-sys.md#24010001-system-service-abnormal) | Service is abnormal. Possible cause: IPC failed. |
| [24010002](../errorcode-abilityToolAccessCtrl-sys.md#24010002-internal-service-error) | Common internal error. Possible cause: dependent service unavailable, resource access failure, etc. |
