# access

## access

```TypeScript
declare function access(path: string, mode?: number): Promise<void>
```

检查当前进程是否可访问某文件，使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:access](arkts-corefile-fileio-access-f.md#access)

<!--Device-unnamed-declare function access(path: string, mode?: number): Promise<void>--><!--Device-unnamed-declare function access(path: string, mode?: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待访问文件的应用沙箱路径。 |
| mode | number | No | 访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。&lt;br/&gt;确认当前进程是否具有对应权限：&lt;br/&gt;-?0：确认文件是否存在。&lt;br/&gt;-?1：确认当前进程 是否具有可执行权限。&lt;br/&gt;-?2：确认当前进程是否具有写权限。&lt;br/&gt;-?4：确认当前进程是否具有读权限。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


## access

```TypeScript
declare function access(path: string, callback: AsyncCallback<void>): void
```

检查当前进程是否可访问某文件，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:access](arkts-corefile-fileio-access-f.md#access)

<!--Device-unnamed-declare function access(path: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function access(path: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待访问文件的应用沙箱路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异步检查当前进程是否可访问某文件之后的回调。 |


## access

```TypeScript
declare function access(path: string, mode: number, callback: AsyncCallback<void>): void
```

检查当前进程是否可访问某文件，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:access](arkts-corefile-fileio-access-f.md#access)

<!--Device-unnamed-declare function access(path: string, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function access(path: string, mode: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待访问文件的应用沙箱路径。 |
| mode | number | Yes | 访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。&lt;br/&gt;确认当前进程是否具有对应权限：&lt;br/&gt;-?0：确认文件是否存在。&lt;br/&gt;-?1：确认当前进程 是否具有可执行权限。&lt;br/&gt;-?2：确认当前进程是否具有写权限。&lt;br/&gt;-?4：确认当前进程是否具有读权限。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异步检查当前进程是否可访问某文件之后的回调。 |

