# setUserOperation (System API)

## Modules to Import

```TypeScript
```

## setUserOperation

```TypeScript
function setUserOperation(operation: Operation, mac: string, params: string): void
```

Sets a user operation.

**Since:** 23

**Required permissions:** ohos.permission.CONNECT_MECHANIC_HARDWARE

<!--Device-mechanicManager-function setUserOperation(operation: Operation, mac: string, params: string): void--><!--Device-mechanicManager-function setUserOperation(operation: Operation, mac: string, params: string): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| operation | [Operation](../../apis-mdm-kit/arkts-apis/arkts-mdm-devicecontrol-operation-e.md) | Yes |
| mac | string | Yes |
| params | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |

**Examples**

```TypeScript
console.info('User operate');
mechanicManager.setUserOperation(mechanicManager.Operation.CONNECT, "58:51:9e:e7:79:6d", "operatingParams");
console.info('User operation was successful');
```
