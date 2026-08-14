# off_sessionCreate (System API)

## Modules to Import

```TypeScript
import { avSession } from 'avSession';
```

## off_sessionCreate

```TypeScript
function off(type: 'sessionCreate', callback?: (session: AVSessionDescriptor) => void): void
```

Unregister session create callback

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-avSession-function off(type: 'sessionCreate', callback?: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function off(type: 'sessionCreate', callback?: (session: AVSessionDescriptor) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionCreate' | Yes | Registration Type, session creation, 'sessionCreate' |
| callback | (session: AVSessionDescriptor) =&gt; void | No | Used to unregister listener for ('sessionCreate') command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## Examples

```TypeScript
avSession.off('sessionCreate');
```

