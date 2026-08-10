# show

## show

```TypeScript
declare function show(uri: string, type: string): Promise<void>
```

异步打开URI对应的文件，使用promise形式返回结果。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

<!--Device-unnamed-declare function show(uri: string, type: string): Promise<void>--><!--Device-unnamed-declare function show(uri: string, type: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 待打开的文件URI |
| type | string | Yes | 待打开文件的类型 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise回调返回void表示成功打开文件（注：当前返回错误码） |


## show

```TypeScript
declare function show(uri: string, type: string, callback: AsyncCallback<void>): void
```

异步打开URI对应的文件，使用callback形式返回结果。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

<!--Device-unnamed-declare function show(uri: string, type: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function show(uri: string, type: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 待打开的文件URI |
| type | string | Yes | 待打开文件的类型 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异步打开uri对应文件（注：当前返回错误码） |

