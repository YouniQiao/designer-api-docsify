# enableLeakWatcher

## Modules to Import

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## enableLeakWatcher

```TypeScript
function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void
```

ʹ��ArkTS����й©��⡣

�˽ӿ�ͨ��һ�ε��ü��ɼ��ArkTS������ڴ�й©����֮ǰ��Ҫ�����ĸ�������enable��watch��check��dump���ķ������Ӽ�ࡣ

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.1.0.

<!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void--><!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean | Yes | �Ƿ�ʹ��ArkTS�����ڴ�й©��⹦�ܡ�true������ArkTS�ڴ�й©��⹦�ܣ�false���ر�ArkTS�ڴ�й©��⹦�ܡ� |
| configs | Array&lt;string&gt; | Yes | �����������ÿ��Ԫ��Ϊ�������������͡�&lt;br&gt;�������������XComponent��NodeContainer��Window��CustomComponent ��Ability��&lt;br&gt;**˵��**���������������������ȫ������ |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;string&gt;&gt; | Yes | �ص����������ڽ���jsLeakWatcher.enableLeakWatcher�ӿڷ��ص��ڴ�й©�ļ��б���������ڴ�����ļ���&lt;br&gt;�ص������д���һ������ ��������0Ϊй©�б��ļ�������׺Ϊ.jsleaklist������1Ϊ������ڴ�����ļ�������׺Ϊ.rawheap�� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10801001 | The parameter isEnabled is invalid. |
| 10801002 | The parameter config is invalid. |
| 10801003 | The parameter callback is invalid. Input parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

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

ʹ��ArkTS����й©��⡣

�˽ӿ�ͨ��һ�ε��ü��ɼ��ArkTS������ڴ�й©����֮ǰ��Ҫ�����ĸ�������enable��watch��check��dump���ķ������Ӽ�ࣻͨ��configs��������������Զ������ü��������ԣ���Ƚ�֮ǰ����������й©������ܡ�

> **ע��**
> 
> ��ǰjsLeakWatcherй©������ܿ����ϴ󣬻ᵼ��Ӧ�ÿ��٣�������������ʱ�䣬���ٿ���Ƶ�ʡ�

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

<!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void--><!--Device-jsLeakWatcher-function enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean | Yes | �Ƿ�ʹ��ArkTS�����ڴ�й©��⹦�ܡ�&lt;br&gt;true������ArkTS�ڴ�й©��⹦�ܡ�&lt;br&gt;false���ر�ArkTS�ڴ�й©��⹦�ܡ� |
| configs | [LeakWatcherConfig](arkts-performanceanalysis-jsleakwatcher-leakwatcherconfig-i.md) | Yes | LeakWatcherConfig�������ͣ������а�����������ڴ�й©���Ŀ��������ԡ�&lt;br&gt;**˵��**�������в������ʹ����ֵ���ֵ�������������� ΪĬ��ֵ�� |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;string&gt;&gt; | Yes | �ص����������ڽ���й©���ĵ����ļ�·����&lt;br&gt;�ص������д���һ������ ��������0Ϊй©�б��ļ�������׺Ϊ.jsleaklist������1Ϊ������ڴ�����ļ�������׺Ϊ.rawheap�� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10801001 | The parameter isEnabled is invalid. |
| 10801002 | The parameter config is invalid. |
| 10801003 | The parameter callback is invalid. Input parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

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

