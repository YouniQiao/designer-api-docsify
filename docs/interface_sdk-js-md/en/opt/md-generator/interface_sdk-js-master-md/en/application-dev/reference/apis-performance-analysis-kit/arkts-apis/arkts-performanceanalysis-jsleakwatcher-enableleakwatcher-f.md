# enableLeakWatcher

## Modules to Import

```TypeScript
```

## enableLeakWatcher

```TypeScript
function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void
```

Enables the detection for JS object leaks. This function is disabled by default. This API can detect the JS object memory leak, which is simpler than the method that needs to call the **enable**, **watch**, **check**, and **dump** functions. If a memory leak occurs, the leaked file is returned through the callback.

**Since:** 26.1.0

<!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void--><!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | boolean | Yes |
| configs | Array & lt;string & gt; | Yes |
| callback | Callback & lt;Array & lt;string & gt; & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10801001](../errorcode-jsleakwatcher.md#10801001-invalid-isenabled) |
| [10801002](../errorcode-jsleakwatcher.md#10801002-invalid-config) |
| [10801003](../errorcode-jsleakwatcher.md#10801003-invalid-callback) |

**Examples**

```TypeScript
let config: Array<string> = ['XComponent'];
// Monitor the memory leak of the ArkTS object XComponent.
// If an empty array is passed, all objects are monitored.
jsLeakWatcher.enableLeakWatcher(true, config, (filePath: Array<string>) => {
    console.info('JsLeakWatcher leaklistFileName:' + filePath[0]);
    console.info('JsLeakWatcher heapDumpFileName:' + filePath[1]);
});
```


## enableLeakWatcher

```TypeScript
function enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void
```

Enables the ArkTS object leak detection. This API can detect memory leaks of ArkTS objects with a single call, which is simpler than the previous method that requires four functions (**enable**, **watch**, **check**, and **dump**). You can use the **configs** parameter to customize the properties of monitoring items, greatly improving the leak detection performance.

**Since:** 26.1.0

<!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void--><!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | boolean | Yes |
| configs | [LeakWatcherConfig](arkts-performanceanalysis-jsleakwatcher-leakwatcherconfig-i.md) | Yes |
| callback | Callback & lt;Array & lt;string & gt; & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10801001](../errorcode-jsleakwatcher.md#10801001-invalid-isenabled) |
| [10801002](../errorcode-jsleakwatcher.md#10801002-invalid-config) |
| [10801003](../errorcode-jsleakwatcher.md#10801003-invalid-callback) |

**Examples**

```TypeScript
// Detect memory leaks of the ArkTS objects CustomComponent and Window.
// If the value of an object type is null or false, the default value is used.
let config: jsLeakWatcher.LeakWatcherConfig = {
    monitorObjectTypes: jsLeakWatcher.MonitorObjectType.CUSTOM_COMPONENT | jsLeakWatcher.MonitorObjectType.WINDOW,
    objectUniqueIDs: [],
    checkInterval: 10000,
    fgLeakCountThreshold: 5,
    bgLeakCountThreshold: 3,
    maxStoredHeapDumps: 5,
    dumpHeapWaitTimeMs: 5000,
    exclusionList: []
};
jsLeakWatcher.enableLeakWatcher(true, config, (filePath : Array<string>) => {
    console.info('JsLeakWatcher leaklistFileName:' + filePath[0]);
    console.info('JsLeakWatcher heapDumpFileName:' + filePath[1]);
});
```
