# registerTraceListener

## registerTraceListener

```TypeScript
function registerTraceListener(callback: TraceEventListener): int
```

Registers a callback to notify whether the application trace capture is enabled. This API uses a synchronous callback to return the result. After the registration is successful, the callback is executed immediately. Subsequent callbacks are executed when the application trace capture status changes. Callbacks are stored in the application process. A maximum of 10 callbacks can be registered in a process. > **NOTE** > > If the callback contains time-consuming operations, the registration or deregistration will be blocked (waiting > for the callback execution to complete) when the callback is executed. > > Therefore, you are advised not to register or deregister callbacks containing time-consuming operations in the > main thread of the application to avoid application freeze.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-hiTraceMeter-function registerTraceListener(callback: TraceEventListener): int--><!--Device-hiTraceMeter-function registerTraceListener(callback: TraceEventListener): int-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Registered callback. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Callback registration status. |

**Example**

```TypeScript
// Define the registered callback.
let callback: hiTraceMeter.TraceEventListener = (traceStatus: boolean) => {
    if (traceStatus) {
        // Trace capture is enabled for the current application. The service process is as follows:
    } else {
        // Trace capture is disabled for the current application. The service process is as follows:
    }
};

// Register a callback to notify whether the application trace capture is enabled.
let index = hiTraceMeter.registerTraceListener(callback);
if (index < 0) {
    // Handle exceptions.
}
```

