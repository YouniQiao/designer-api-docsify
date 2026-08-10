# setUserOperation (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## setUserOperation

```TypeScript
function setUserOperation(operation: Operation, mac: string, params: string): void
```

设置用户操作

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CONNECT_MECHANIC_HARDWARE

<!--Device-mechanicManager-function setUserOperation(operation: Operation, mac: string, params: string): void--><!--Device-mechanicManager-function setUserOperation(operation: Operation, mac: string, params: string): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| operation | [Operation](../../apis-mdm-kit/arkts-apis/arkts-mdm-devicecontrol-operation-e.md) | Yes | 操作类型 |
| mac | string | Yes | MAC address. |
| params | string | Yes | Operation parameters. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |
| 33300001 | Service exception. |

## Examples

```TypeScript
console.info('User operate');
mechanicManager.setUserOperation(mechanicManager.Operation.CONNECT, "58:51:9e:e7:79:6d", "operatingParams");
console.info('User operation was successful');
```

