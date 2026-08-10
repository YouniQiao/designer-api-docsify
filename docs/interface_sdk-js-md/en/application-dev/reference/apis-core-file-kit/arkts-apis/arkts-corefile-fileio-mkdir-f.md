# mkdir

## mkdir

```TypeScript
declare function mkdir(path: string, mode?: number): Promise<void>
```

创建目录，使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:mkdir](arkts-corefile-fileio-mkdir-f.md#mkdir)

<!--Device-unnamed-declare function mkdir(path: string, mode?: number): Promise<void>--><!--Device-unnamed-declare function mkdir(path: string, mode?: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待创建目录的应用沙箱路径。 |
| mode | number | No | 创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。&lt;br/&gt;-?0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。&lt;br/&gt;-?0o7 00：所有者具有读、写及可执行权限。&lt;br/&gt;-?0o400：所有者具有读权限。&lt;br/&gt;-?0o200：所有者具有写权限。&lt;br/&gt;-?0o100：所有者具有可执行权限。&lt;br/&gt;-?0o070：所有用户组具有读、写及可执行 权限。&lt;br/&gt;-?0o040：所有用户组具有读权限。&lt;br/&gt;-?0o020：所有用户组具有写权限。&lt;br/&gt;-?0o010：所有用户组具有可执行权限。&lt;br/&gt;-?0o007：其余用户具有读、写及可执行权限。&lt;br/&gt;-? 0o004：其余用户具有读权限。&lt;br/&gt;-?0o002：其余用户具有写权限。&lt;br/&gt;-?0o001：其余用户具有可执行权限。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


## mkdir

```TypeScript
declare function mkdir(path: string, callback: AsyncCallback<void>): void
```

创建目录，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:mkdir](arkts-corefile-fileio-mkdir-f.md#mkdir)

<!--Device-unnamed-declare function mkdir(path: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function mkdir(path: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待创建目录的应用沙箱路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异步创建目录操作完成之后的回调。 |


## mkdir

```TypeScript
declare function mkdir(path: string, mode: number, callback: AsyncCallback<void>): void
```

创建目录，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:mkdir](arkts-corefile-fileio-mkdir-f.md#mkdir)

<!--Device-unnamed-declare function mkdir(path: string, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function mkdir(path: string, mode: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待创建目录的应用沙箱路径。 |
| mode | number | Yes | 创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。&lt;br/&gt;-?0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。&lt;br/&gt;-?0o7 00：所有者具有读、写及可执行权限。&lt;br/&gt;-?0o400：所有者具有读权限。&lt;br/&gt;-?0o200：所有者具有写权限。&lt;br/&gt;-?0o100：所有者具有可执行权限。&lt;br/&gt;-?0o070：所有用户组具有读、写及可执行 权限。&lt;br/&gt;-?0o040：所有用户组具有读权限。&lt;br/&gt;-?0o020：所有用户组具有写权限。&lt;br/&gt;-?0o010：所有用户组具有可执行权限。&lt;br/&gt;-?0o007：其余用户具有读、写及可执行权限。&lt;br/&gt;-? 0o004：其余用户具有读权限。&lt;br/&gt;-?0o002：其余用户具有写权限。&lt;br/&gt;-?0o001：其余用户具有可执行权限。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异步创建目录操作完成之后的回调。 |

