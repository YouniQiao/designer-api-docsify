# on_sessionCreate (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## on('sessionCreate')

```TypeScript
function on(type: 'sessionCreate', callback: (session: AVSessionDescriptor) => void): void
```

Register session create callback

**Since:** 9

<!--Device-avSession-function on(type: 'sessionCreate', callback: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function on(type: 'sessionCreate', callback: (session: AVSessionDescriptor) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionCreate' | Yes | Registration Type, 'sessionCreate' |
| callback | (session: AVSessionDescriptor) =&gt; void | Yes | Used to handle ('sessionCreate' command) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

**Examples**

```TypeScript
avSession.on('sessionCreate', (descriptor: avSession.AVSessionDescriptor) => {
  console.info(`on sessionCreate : isActive : ${descriptor.isActive}`);
  console.info(`on sessionCreate : type : ${descriptor.type}`);
  console.info(`on sessionCreate : sessionTag : ${descriptor.sessionTag}`);
});
```

