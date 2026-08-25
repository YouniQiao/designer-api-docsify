# create

## Modules to Import

```TypeScript
import { floatingBall } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
function create(config: FloatingBallConfiguration): Promise<FloatingBallController>
```

Creates a floating ball controller. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [FloatingBallConfiguration](arkts-arkui-floatingball-floatingballconfiguration-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FloatingBallController](arkts-arkui-floatingball-floatingballcontroller-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
