# choose

## choose

```TypeScript
declare function choose(types?: string[]): Promise<string>
```

通过文件管理器选择文件，异步返回文件URI，使用promise形式返回结果。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

<!--Device-unnamed-declare function choose(types?: string[]): Promise<string>--><!--Device-unnamed-declare function choose(types?: string[]): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | string[] | No | 限定文件选择的类型 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | 异步返回文件URI（注：当前返回错误码） |


## choose

```TypeScript
declare function choose(callback: AsyncCallback<string>): void
```

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

<!--Device-unnamed-declare function choose(callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function choose(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 异步获取对应文件URI（注：当前返回错误码） |


## choose

```TypeScript
declare function choose(types: string[], callback: AsyncCallback<string>): void
```

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

<!--Device-unnamed-declare function choose(types: string[], callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function choose(types: string[], callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | string[] | Yes | 限定选择文件的类型 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 异步获取对应文件URI（注：当前返回错误码） |

