# SEService

**SEService** indicates the connection service used to connect to all available SEs in the system. You can use [createService](arkts-connectivity-omapi-createservice-f.md) to create an **SEService** instance.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

## Modules to Import

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## getReaders

```TypeScript
getReaders(): Reader[]
```

Obtains available SE readers, which include all the SEs on the device.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Reader](arkts-connectivity-omapi-reader-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## getVersion

```TypeScript
getVersion(): string
```

Obtains the version of the Open Mobile API (OMAPI) specification used.

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

## isConnected

```TypeScript
isConnected(): boolean
```

Checks whether this SE service is connected.

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

## shutdown

```TypeScript
shutdown(): void
```

Releases all SE resources allocated to this SE service. After that, [isConnected](#isconnected) returns **false**.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
