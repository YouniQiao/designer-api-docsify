# fstat

## fstat

```TypeScript
declare function fstat(fd: number): Promise<Stat>
```

基于文件描述符获取文件状态信息，使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:stat](arkts-corefile-fileio-stat-f.md#stat)

<!--Device-unnamed-declare function fstat(fd: number): Promise<Stat>--><!--Device-unnamed-declare function fstat(fd: number): Promise<Stat>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 待获取文件状态的文件描述符。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Stat&gt; | Promise对象。返回表示文件状态的具体信息。 |


## fstat

```TypeScript
declare function fstat(fd: number, callback: AsyncCallback<Stat>): void
```

基于文件描述符获取文件状态信息，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:stat](arkts-corefile-fileio-stat-f.md#stat)

<!--Device-unnamed-declare function fstat(fd: number, callback: AsyncCallback<Stat>): void--><!--Device-unnamed-declare function fstat(fd: number, callback: AsyncCallback<Stat>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 待获取文件状态的文件描述符。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Stat&gt; | Yes | 异步获取文件状态信息之后的回调。 |

