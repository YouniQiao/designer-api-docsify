# on_topSessionChange (System API)

## Modules to Import

```TypeScript
import { avSession } from 'avSession';
```

## on_topSessionChange

```TypeScript
function on(type: 'topSessionChange', callback: (session: AVSessionDescriptor) => void): void
```

Register top session changed callback

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-avSession-function on(type: 'topSessionChange', callback: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function on(type: 'topSessionChange', callback: (session: AVSessionDescriptor) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'topSessionChange' | Yes | Registration Type, top priority session change, 'topSessionChange' |
| callback | (session: AVSessionDescriptor) =&gt; void | Yes | Used to handle ('topSessionChange' command) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## Examples

```TypeScript
avSession.on('topSessionChange', (descriptor: avSession.AVSessionDescriptor) => {
  console.info(`on topSessionChange : isActive : ${descriptor.isActive}`);
  console.info(`on topSessionChange : type : ${descriptor.type}`);
  console.info(`on topSessionChange : sessionTag : ${descriptor.sessionTag}`);
});
```

