# stopCasting (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## stopCasting

```TypeScript
function stopCasting(session: SessionToken, callback: AsyncCallback<void>): void
```

Stop current cast and disconnect device connection.

**Since:** 23

**Deprecated since:** -1

<!--Device-avSession-function stopCasting(session: SessionToken, callback: AsyncCallback<void>): void--><!--Device-avSession-function stopCasting(session: SessionToken, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| session | [SessionToken](arkts-avsession-avsession-sessiontoken-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600109](../errorcode-avsession.md#6600109-remote-session-does-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let myToken: avSession.SessionToken = {
  sessionId: sessionId,
}
avSession.stopCasting(myToken, () => {
    console.info('Succeeded in stopping casting.');
});
```


## stopCasting

```TypeScript
function stopCasting(session: SessionToken): Promise<void>
```

Stop current cast and disconnect device connection.

**Since:** 23

**Deprecated since:** -1

<!--Device-avSession-function stopCasting(session: SessionToken): Promise<void>--><!--Device-avSession-function stopCasting(session: SessionToken): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| session | [SessionToken](arkts-avsession-avsession-sessiontoken-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600109](../errorcode-avsession.md#6600109-remote-session-does-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let myToken: avSession.SessionToken = {
  sessionId: sessionId,
}
avSession.stopCasting(myToken).then(() => {
  console.info('Succeeded in stopping casting.');
});
```
