# open

## open

```TypeScript
declare function open(path: string, flags?: number, mode?: number): Promise<number>
```

打开文件，使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:open](arkts-corefile-fileio-open-f.md#open)

<!--Device-unnamed-declare function open(path: string, flags?: number, mode?: number): Promise<number>--><!--Device-unnamed-declare function open(path: string, flags?: number, mode?: number): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待打开文件的应用沙箱路径。 |
| flags | number | No | 打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开：&lt;br/&gt;-?0o0：只读打开。&lt;br/&gt;-?0o1：只写打开。&lt;br/&gt;-?0o2：读写打开。&lt;br/&gt;同时，也可 给定如下选项，以按位或的方式追加，默认不给定任何额外选项：&lt;br/&gt;-?0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数?mode。&lt;br/&gt;-?0o200：如果追加了0o100选项，且文件已经存在，则出错 。&lt;br/&gt;-?0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。&lt;br/&gt;-?0o2000：以追加方式打开，后续写将追加到文件末尾。&lt;br/&gt;-?0o4000：如果path指向FIFO、块特殊文件或字符特殊文件 ，则本次打开及后续?IO?进行非阻塞操作。&lt;br/&gt;-?0o200000：如果path不指向目录，则出错。&lt;br/&gt;-?0o400000：如果path指向符号链接，则出错。&lt;br/&gt;-?0o4010000：以同步IO的方式打开 文件。 |
| mode | number | No | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。&lt;br/&gt;-?0o660：所有者具有读、写权限，所有用户组具有读、写权限。&lt;br/&gt;-?0 o700：所有者具有读、写及可执行权限。&lt;br/&gt;-?0o400：所有者具有读权限。&lt;br/&gt;-?0o200：所有者具有写权限。&lt;br/&gt;-?0o100：所有者具有可执行权限。&lt;br/&gt;-?0o070：所有用户组具有读、写及可 执行权限。&lt;br/&gt;-?0o040：所有用户组具有读权限。&lt;br/&gt;-?0o020：所有用户组具有写权限。&lt;br/&gt;-?0o010：所有用户组具有可执行权限。&lt;br/&gt;-?0o007：其余用户具有读、写及可执行权限。&lt;br/&gt; -?0o004：其余用户具有读权限。&lt;br/&gt;-?0o002：其余用户具有写权限。&lt;br/&gt;-?0o001：其余用户具有可执行权限。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise对象。返回打开文件的文件描述符。 |


## open

```TypeScript
declare function open(path: string, callback: AsyncCallback<number>): void
```

打开文件，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:open](arkts-corefile-fileio-open-f.md#open)

<!--Device-unnamed-declare function open(path: string, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function open(path: string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待打开文件的应用沙箱路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 异步打开文件之后的回调，返回打开文件的文件描述符。 |


## open

```TypeScript
declare function open(path: string, flags: number, callback: AsyncCallback<number>): void
```

打开文件，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:open](arkts-corefile-fileio-open-f.md#open)

<!--Device-unnamed-declare function open(path: string, flags: number, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function open(path: string, flags: number, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待打开文件的应用沙箱路径。 |
| flags | number | Yes | 打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开：&lt;br/&gt;-?0o0：只读打开。&lt;br/&gt;-?0o1：只写打开。&lt;br/&gt;-?0o2：读写打开。&lt;br/&gt;同时，也可 给定如下选项，以按位或的方式追加，默认不给定任何额外选项：&lt;br/&gt;-?0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数?mode。&lt;br/&gt;-?0o200：如果追加了0o100选项，且文件已经存在，则出错 。&lt;br/&gt;-?0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。&lt;br/&gt;-?0o2000：以追加方式打开，后续写将追加到文件末尾。&lt;br/&gt;-?0o4000：如果path指向FIFO、块特殊文件或字符特殊文件 ，则本次打开及后续?IO?进行非阻塞操作。&lt;br/&gt;-?0o200000：如果path不指向目录，则出错。&lt;br/&gt;-?0o400000：如果path指向符号链接，则出错。&lt;br/&gt;-?0o4010000：以同步IO的方式打开 文件。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 异步打开文件之后的回调，返回打开文件的文件描述符。 |


## open

```TypeScript
declare function open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void
```

打开文件，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:open](arkts-corefile-fileio-open-f.md#open)

<!--Device-unnamed-declare function open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待打开文件的应用沙箱路径。 |
| flags | number | Yes | 打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开：&lt;br/&gt;-?0o0：只读打开。&lt;br/&gt;-?0o1：只写打开。&lt;br/&gt;-?0o2：读写打开。&lt;br/&gt;同时，也可 给定如下选项，以按位或的方式追加，默认不给定任何额外选项：&lt;br/&gt;-?0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数?mode。&lt;br/&gt;-?0o200：如果追加了0o100选项，且文件已经存在，则出错 。&lt;br/&gt;-?0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。&lt;br/&gt;-?0o2000：以追加方式打开，后续写将追加到文件末尾。&lt;br/&gt;-?0o4000：如果path指向FIFO、块特殊文件或字符特殊文件 ，则本次打开及后续?IO?进行非阻塞操作。&lt;br/&gt;-?0o200000：如果path不指向目录，则出错。&lt;br/&gt;-?0o400000：如果path指向符号链接，则出错。&lt;br/&gt;-?0o4010000：以同步IO的方式打开 文件。 |
| mode | number | Yes | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。&lt;br/&gt;-?0o660：所有者具有读、写权限，所有用户组具有读、写权限。&lt;br/&gt;-?0 o700：所有者具有读、写及可执行权限。&lt;br/&gt;-?0o400：所有者具有读权限。&lt;br/&gt;-?0o200：所有者具有写权限。&lt;br/&gt;-?0o100：所有者具有可执行权限。&lt;br/&gt;-?0o070：所有用户组具有读、写及可 执行权限。&lt;br/&gt;-?0o040：所有用户组具有读权限。&lt;br/&gt;-?0o020：所有用户组具有写权限。&lt;br/&gt;-?0o010：所有用户组具有可执行权限。&lt;br/&gt;-?0o007：其余用户具有读、写及可执行权限。&lt;br/&gt; -?0o004：其余用户具有读权限。&lt;br/&gt;-?0o002：其余用户具有写权限。&lt;br/&gt;-?0o001：其余用户具有可执行权限。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 异步打开文件之后的回调，返回打开文件的文件描述符。 |

