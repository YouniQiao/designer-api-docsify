# DisplaySync

An object that implements the setting of the frame rate and callback. It provides APIs for you to set the frame rate, register a callback, and start/stop the callback. Before calling any of the following APIs, you must use [displaySync.create()](arkts-arkgraphics2d-displaysync-create-f.md) to create a **DisplaySync** instance.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { displaySync } from 'kits/@kit.ArkGraphics2D';
```

## off('frame')

```TypeScript
off(type: 'frame', callback?: Callback<IntervalInfo>): void
```

Unsubscribes from change events of each frame.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'frame' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[IntervalInfo](arkts-arkgraphics2d-displaysync-intervalinfo-i.md)&gt; | No |

## on('frame')

```TypeScript
on(type: 'frame', callback: Callback<IntervalInfo>): void
```

Subscribes to change events of each frame.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'frame' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[IntervalInfo](arkts-arkgraphics2d-displaysync-intervalinfo-i.md)&gt; | Yes |

## setExpectedFrameRateRange

```TypeScript
setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange) : void
```

Sets the expected frame rate range.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rateRange | [ExpectedFrameRateRange](../../apis-arkui/arkts-components/arkts-arkui-expectedframeraterange-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## start

```TypeScript
start(): void
```

Starts callback for each frame.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stop

```TypeScript
stop(): void
```

Stops callback for each frame.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full
