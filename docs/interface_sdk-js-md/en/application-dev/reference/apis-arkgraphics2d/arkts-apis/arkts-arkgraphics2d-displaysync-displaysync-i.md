# DisplaySync

An object that implements the setting of the frame rate and callback. It provides APIs for you to set the frame rate, register a callback, and start/stop the callback. Before calling any of the following APIs, you must use [displaySync.create()](arkts-arkgraphics2d-displaysync-create-f.md) to create a **DisplaySync** instance.

**Since:** 23

<!--Device-displaySync-interface DisplaySync--><!--Device-displaySync-interface DisplaySync-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { displaySync } from '@kit.ArkGraphics2D';
```

## offFrame

```TypeScript
offFrame(callback?: Callback<IntervalInfo>): void
```

Unsubscribes from change events of each frame.

**Since:** 23

<!--Device-DisplaySync-offFrame(callback?: Callback<IntervalInfo>): void--><!--Device-DisplaySync-offFrame(callback?: Callback<IntervalInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[IntervalInfo](arkts-arkgraphics2d-displaysync-intervalinfo-i.md)&gt; | No | Callback used for unsubscription. If no value is passed in, all subscriptions to the specified event are canceled. |

## off_frame('frame')

```TypeScript
off(type: 'frame', callback?: Callback<IntervalInfo>): void
```

Unsubscribes from change events of each frame.

**Since:** 11

<!--Device-DisplaySync-off(type: 'frame', callback?: Callback<IntervalInfo>): void--><!--Device-DisplaySync-off(type: 'frame', callback?: Callback<IntervalInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frame' | Yes | Event type. The value is fixed at **'frame'**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[IntervalInfo](arkts-arkgraphics2d-displaysync-intervalinfo-i.md)&gt; | No | Callback used for unsubscription. If no value is passed in, all subscriptions to the specified event are canceled. |

**Examples**

```TypeScript
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

backDisplaySync?.on("frame", callback)

// Unsubscribe from the event.
backDisplaySync?.off("frame", callback)
```

## onFrame

```TypeScript
onFrame(callback: Callback<IntervalInfo>): void
```

Subscribes to change events of each frame.

**Since:** 23

<!--Device-DisplaySync-onFrame(callback: Callback<IntervalInfo>): void--><!--Device-DisplaySync-onFrame(callback: Callback<IntervalInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[IntervalInfo](arkts-arkgraphics2d-displaysync-intervalinfo-i.md)&gt; | Yes | Callback used for subscription. |

## on_frame('frame')

```TypeScript
on(type: 'frame', callback: Callback<IntervalInfo>): void
```

Subscribes to change events of each frame.

**Since:** 11

<!--Device-DisplaySync-on(type: 'frame', callback: Callback<IntervalInfo>): void--><!--Device-DisplaySync-on(type: 'frame', callback: Callback<IntervalInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frame' | Yes | Event type. The value is fixed at **'frame'**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[IntervalInfo](arkts-arkgraphics2d-displaysync-intervalinfo-i.md)&gt; | Yes | Callback used for subscription. |

**Examples**

```TypeScript
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

// Subscribe to the event.
backDisplaySync?.on("frame", callback)
```

## setExpectedFrameRateRange

```TypeScript
setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange) : void
```

Sets the expected frame rate range.

**Since:** 23

<!--Device-DisplaySync-setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange) : void--><!--Device-DisplaySync-setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange) : void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rateRange | [ExpectedFrameRateRange](../../apis-na/arkts-apis/arkts-na-common-expectedframeraterange-i.md) | Yes | Expected frame rate range. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. or check if ExpectedFrameRateRange is valid. |

**Examples**

```TypeScript
let range : ExpectedFrameRateRange = {
  expected: 10,
  min:0,
  max:120
};

// Set the expected frame rate range.
backDisplaySync?.setExpectedFrameRateRange(range)
```

## start

```TypeScript
start(): void
```

Starts callback for each frame.

**Since:** 23

<!--Device-DisplaySync-start(): void--><!--Device-DisplaySync-start(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
let range : ExpectedFrameRateRange = {
  expected: 10,
  min:0,
  max:120
};

backDisplaySync?.setExpectedFrameRateRange(range)

let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

backDisplaySync?.on("frame", callback)

// Start callback for each frame.
backDisplaySync?.start()
```

```TypeScript
import { displaySync } from '@kit.ArkGraphics2D';
import { UIContext } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  // Create a DisplaySync instance.
  backDisplaySync: displaySync.DisplaySync = displaySync.create();

  aboutToAppear() {
    // Obtain a UIContext instance.
    let uiContext: UIContext = this.getUIContext();
    // Call start() in the current UI context.
    uiContext?.runScopedTask(() => {
      this.backDisplaySync?.start();
    })
  }

  build() {
    // ...
  }
}
```

## stop

```TypeScript
stop(): void
```

Stops callback for each frame.

**Since:** 23

<!--Device-DisplaySync-stop(): void--><!--Device-DisplaySync-stop(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
let range : ExpectedFrameRateRange = {
  expected: 10,
  min:0,
  max:120
};

backDisplaySync?.setExpectedFrameRateRange(range)

let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

backDisplaySync?.on("frame", callback)

backDisplaySync?.start()

// ...

// Stop callback for each frame.
backDisplaySync?.stop()
```

