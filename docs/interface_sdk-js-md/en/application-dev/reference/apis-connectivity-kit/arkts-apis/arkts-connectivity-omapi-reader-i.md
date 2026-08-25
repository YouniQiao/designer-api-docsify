# Reader

Obtains the SE supported by the device. If eSE, SIM, and SIM2 are supported, three instances will be returned. SIM2 is supported since API version 22. You can use [SEService.getReaders](arkts-connectivity-omapi-seservice-i.md#getreaders) to obtain a **Reader** instance.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

## Modules to Import

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## closeSessions

```TypeScript
closeSessions(): void
```

Closes all sessions opened on this reader. All channels opened by these sessions will be closed.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |

## getName

```TypeScript
getName(): string
```

Obtains the name of this reader. The name is **SIM** for a SIM reader, **SIM2** for a SIM2 reader, and **eSE** for an eSE.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## isSecureElementPresent

```TypeScript
isSecureElementPresent(): boolean
```

Checks whether the SE corresponding to this reader is available.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |

## openSession

```TypeScript
openSession(): Session
```

Opens a session to connect to an SE in this reader. Multiple sessions can be opened on a reader at the same time.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Session](../../apis-camera-kit/arkts-apis/arkts-camera-camera-session-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |
