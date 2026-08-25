# IPCSkeleton

Obtains IPC context, including the UID and PID, local and remote device IDs, and whether the method is invoked on the same device.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## flushCmdBuffer

```TypeScript
static flushCmdBuffer(object: IRemoteObject): void
```

Flushes all suspended commands from the specified **RemoteProxy** to the corresponding **RemoteObject**. This API is a static method. You are advised to call this API before performing any sensitive operation.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| object | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## flushCommands

```TypeScript
static flushCommands(object: IRemoteObject): number
```

Flushes all suspended commands from the specified **RemoteProxy** to the corresponding **RemoteObject**. This API is a static method. You are advised to call this API before performing any sensitive operation.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** static

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| object | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCallingDeviceID

```TypeScript
static getCallingDeviceID(): string
```

Obtains the ID of the device hosting the caller's process. This API is a static method.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getCallingPid

```TypeScript
static getCallingPid(): number
```

Obtains the PID of the caller. This API is a static method, which is invoked by the **RemoteObject** object in the **onRemoteRequest** method. If this method is not invoked in the IPC context (**onRemoteRequest**), the PID of the process will be returned.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCallingTokenId

```TypeScript
static getCallingTokenId(): number
```

Obtains the caller's token ID, which is used to verify the caller identity.

**Since:** 8

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCallingUid

```TypeScript
static getCallingUid(): number
```

Obtains the UID of the caller. This API is a static method, which is invoked by the **RemoteObject** object in the **onRemoteRequest** method. If this method is not invoked in the IPC context (**onRemoteRequest**), the UID of the process will be returned.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getContextObject

```TypeScript
static getContextObject(): IRemoteObject
```

Obtains the system capability manager. This API is a static method.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) |

## getLocalDeviceID

```TypeScript
static getLocalDeviceID(): string
```

Obtains the local device ID. This API is a static method.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## isLocalCalling

```TypeScript
static isLocalCalling(): boolean
```

Checks whether the peer process is a process of the local device. This API is a static method.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## resetCallingIdentity

```TypeScript
static resetCallingIdentity(): string
```

Resets the UID and PID of the remote user to those of the local user. This API is a static method and is used in scenarios such as identity authentication.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## restoreCallingIdentity

```TypeScript
static restoreCallingIdentity(identity: string): void
```

Restores the UID and PID of the remote user. This API is a static method. It is usually called after **resetCallingIdentity**, and the UID and PID of the remote user returned by **resetCallingIdentity** are required.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| identity | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setCallingIdentity

```TypeScript
static setCallingIdentity(identity: string): boolean
```

Sets the UID and PID of the remote user. This API is a static method. It is usually called after **resetCallingIdentity**, and the UID and PID of the remote user returned by **resetCallingIdentity** are required.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** static

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| identity | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
