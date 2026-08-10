# createWatcher

## createWatcher

```TypeScript
declare function createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher
```

监听文件或者目录的变化，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [@ohos.file.fs:createWatcher](arkts-corefile-fileio-createwatcher-f.md#createwatcher)

<!--Device-unnamed-declare function createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher--><!--Device-unnamed-declare function createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filename | string | Yes | 待监视文件的应用沙箱路径。 |
| events | number | Yes | ?1:?监听文件或者目录是否发生重命名。&lt;br/&gt;-?2：监听文件或者目录内容的是否修改。&lt;br/&gt;-?3：两者都有。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 每发生变化一次，调用一次此函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Watcher](arkts-corefile-watcher-t.md) | Promise对象。返回文件变化监听的实例。 |

