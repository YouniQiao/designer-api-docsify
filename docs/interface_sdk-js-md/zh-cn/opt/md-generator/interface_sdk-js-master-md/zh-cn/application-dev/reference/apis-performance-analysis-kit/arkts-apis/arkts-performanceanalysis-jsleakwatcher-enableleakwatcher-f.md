# enableLeakWatcher

## enableLeakWatcher

```TypeScript
function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void
```

ʹ��ArkTS����й©��⡣

�˽ӿ�ͨ��һ�ε��ü��ɼ��ArkTS������ڴ�й©����֮ǰ��Ҫ�����ĸ�������enable��watch��check��dump���ķ������Ӽ�ࡣ

**起始版本：** 20

<!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void--><!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean | 是 |
| configs | Array&lt;string&gt; | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10801001](../errorcode-jsleakwatcher.md#10801001--参数isenabled无效) |
| [10801002](../errorcode-jsleakwatcher.md#10801002--参数config无效) |
| [10801003](../errorcode-jsleakwatcher.md#10801003--参数callback无效) |

## 示例

```TypeScript
let config: Array<string> = ['XComponent'];
// 监测ArkTS对象XComponent的内存泄漏
// 传入空数组代表监测全部对象
jsLeakWatcher.enableLeakWatcher(true, config, (filePath: Array<string>) => {
    console.info('JsLeakWatcher leaklistFileName:' + filePath[0]);
    console.info('JsLeakWatcher heapDumpFileName:' + filePath[1]);
});
```


## enableLeakWatcher

```TypeScript
function enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void
```

ʹ��ArkTS����й©��⡣

�˽ӿ�ͨ��һ�ε��ü��ɼ��ArkTS������ڴ�й©����֮ǰ��Ҫ�����ĸ�������enable��watch��check��dump���ķ������Ӽ�ࣻͨ��configs��������������Զ������ü��������ԣ���Ƚ�֮ǰ����������й©������ܡ�

> **ע��**
> 
> ��ǰjsLeakWatcherй©������ܿ����ϴ󣬻ᵼ��Ӧ�ÿ��٣�������������ʱ�䣬���ٿ���Ƶ�ʡ�

**起始版本：** 24

<!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void--><!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean | 是 |
| configs | [LeakWatcherConfig](arkts-performanceanalysis-jsleakwatcher-leakwatcherconfig-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10801001](../errorcode-jsleakwatcher.md#10801001--参数isenabled无效) |
| [10801002](../errorcode-jsleakwatcher.md#10801002--参数config无效) |
| [10801003](../errorcode-jsleakwatcher.md#10801003--参数callback无效) |

## 示例

```TypeScript
// 监测ArkTS对象CustomComponent和Window的内存泄漏
// 对象中类型传入空值或假值代表该属性设置为默认值
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
