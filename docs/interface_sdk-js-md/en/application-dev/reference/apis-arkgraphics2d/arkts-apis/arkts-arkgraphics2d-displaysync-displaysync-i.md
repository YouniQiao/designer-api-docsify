# DisplaySync

```TypeScript
interface DisplaySync
```

An instance for setting the expected frame rate and callback function. It is used to set the expected frame rate range, register the frame callback function, and start and stop the frame callback. Before calling any of the following APIs, you must use displaySync.create() to create a DisplaySync instance and then call the corresponding method through this instance.

**Since:** 11

<!--Device-displaySync-interface DisplaySync--><!--Device-displaySync-interface DisplaySync-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { displaySync } from '@kit.ArkGraphics2D';
```

## off('frame')

```TypeScript
off(type: 'frame', callback?: Callback<IntervalInfo>): void
```

Unsubscribes from change events of each frame. This API is used together with on('frame'). After the unsubscription succeeds, the callback function will no longer be triggered.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 26.0.1.

<!--Device-DisplaySync-off(type: 'frame', callback?: Callback<IntervalInfo>): void--><!--Device-DisplaySync-off(type: 'frame', callback?: Callback<IntervalInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frame' | Yes | Type of the callback to set (only 'frame' is supported). |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[IntervalInfo](arkts-arkgraphics2d-displaysync-intervalinfo-i.md)&gt; | No | Callback function registered when on('frame') is called, used to unsubscribe from the callback function. It must be used after the callback has been registered through on('frame'). |

**Examples**

```TypeScript
// Define the callback function.
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

// Register the callback function.
backDisplaySync?.on("frame", callback)

// Unregister the callback function.
backDisplaySync?.off("frame", callback)
```

## on('frame')

```TypeScript
on(type: 'frame', callback: Callback<IntervalInfo>): void
```

Subscribes to change events of each frame. After the callback function is registered, you must call start to start the DisplaySync object; only then will the system trigger the callback on each frame. This API is used together with off('frame') to unregister the callback function. The callback function is executed on the UI main thread. The callback frequency is affected by the frame rate range set by setExpectedFrameRateRange. If the callback takes too long to execute, frame freezing may occur. It is recommended that only lightweight business logic be performed in the callback.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 26.0.1.

<!--Device-DisplaySync-on(type: 'frame', callback: Callback<IntervalInfo>): void--><!--Device-DisplaySync-on(type: 'frame', callback: Callback<IntervalInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'frame' | Yes | Type of the callback to set (only 'frame' is supported). |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[IntervalInfo](arkts-arkgraphics2d-displaysync-intervalinfo-i.md)&gt; | Yes | Callback function for subscribing to frame changes. IntervalInfo contains two attributes: timestamp (the arrival time of the current frame) and targetTimestamp (the expected arrival time of the next frame), both in nanoseconds. |

**Examples**

```TypeScript
// Define the callback function.
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

// Register the callback function.
backDisplaySync?.on("frame", callback)

// Enable the callback function.
backDisplaySync?.start()
```

## setExpectedFrameRateRange

```TypeScript
setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange) : void
```

Sets the expected frame rate range. The expected frame rate range is used as a reference for system scheduling, and the system tries to adjust the drawing frame rate within this range. If this API is not called or ExpectedFrameRateRange(0, 0, 0) is passed in, the current frame rate of the application is followed. It is recommended to set the range before calling start so that it takes effect immediately. Setting the range after calling start also takes effect, but there may be a delay.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 26.0.1.

<!--Device-DisplaySync-setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange) : void--><!--Device-DisplaySync-setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange) : void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rateRange | ExpectedFrameRateRange | Yes | Sets the expected frame rate range of DisplaySync, which contains three fields: expected, min, and max, in frames per second (fps). The fields must be non-negative integers, with a value range of [0, the maximum frame rate of the device], and must satisfy min &lt;= expected &lt;= max. If the value is out of the valid range, error code 401 is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:                                                                 1. Mandatory parameters are left unspecified.                                                                 2. Incorrect parameter types.                                                                 3. Parameter verification failed. Or check if ExpectedFrameRateRange is valid. |

**Examples**

```TypeScript
// Define the expected frame rate range.
let range: ExpectedFrameRateRange = {
  expected: 10, // Expected frame rate
  min: 0, // Minimum frame rate
  max: 120 // Maximum frame rate
};

// Set the expected frame rate range for DisplaySync.
backDisplaySync?.setExpectedFrameRateRange(range)

// Apply the expected frame rate range.
backDisplaySync?.start()
```

## start

```TypeScript
start(): void
```

Makes the expected frame rate range set by setExpectedFrameRateRange take effect. If a callback function is registered through on('frame'), this API starts requesting VSync signals and triggers the registered callback once per frame. This API is used together with stop.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 26.0.1.

<!--Device-DisplaySync-start(): void--><!--Device-DisplaySync-start(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
// Define the expected frame rate range.
let range: ExpectedFrameRateRange = {
  expected: 10, // expected frame rate
  min: 0, // minimum frame rate
  max: 120 // maximum frame rate
};
// Set the expected frame rate range of DisplaySync.
backDisplaySync?.setExpectedFrameRateRange(range)

// Define the callback function.
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

// Register the callback function.
backDisplaySync?.on("frame", callback)

// Apply the expected frame rate range and start the per-frame callback.
backDisplaySync?.start()
```

> NOTE
> 
> The start() API associates the DisplaySync object with a UI context and window. If [start](#start) is called on a non-UI page or in an asynchronous callback, an incorrect UI context may be obtained, causing the [start](#start) function to work abnormally. As a result, the callback function cannot be executed and the expected frame rate range cannot take effect.In this case, you can use [runScopedTask](../apis-arkui/arkts-apis-uicontext-uicontext.md#runscopedtask) to specify the UI context and ensure that [start](#start) is executed in the correct context.

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

Closes the expected frame rate range and stops the callback for each frame. This method must be called after start. After it is stopped, the DisplaySync configurations (such as the expected frame rate range and callback function) are retained and can be restarted at any time through start. The stop method disassociates DisplaySync from the UI context and window, and usually no specific UI context is required.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 26.0.1.

<!--Device-DisplaySync-stop(): void--><!--Device-DisplaySync-stop(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
// Define the expected frame rate range.
let range: ExpectedFrameRateRange = {
  expected: 10, // Expected frame rate.
  min: 0, // Minimum frame rate.
  max: 120 // Maximum frame rate.
};

// Set the expected frame rate range of DisplaySync.
backDisplaySync?.setExpectedFrameRateRange(range)

// Define the callback function.
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

// Register the callback function.
backDisplaySync?.on("frame", callback)

// Apply the expected frame rate range and start the per-frame callback.
backDisplaySync?.start()

// ...

// Stop applying the expected frame rate range and stop the per-frame callback.
backDisplaySync?.stop()
```
