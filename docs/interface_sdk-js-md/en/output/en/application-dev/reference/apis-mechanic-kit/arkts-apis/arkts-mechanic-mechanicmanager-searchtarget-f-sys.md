# searchTarget (System API)

## searchTarget

```TypeScript
function searchTarget(target: TargetInfo, params: SearchParams): Promise<SearchResult>
```

Searching for a specified target.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-mechanicManager-function searchTarget(target: TargetInfo, params: SearchParams): Promise<SearchResult>--><!--Device-mechanicManager-function searchTarget(target: TargetInfo, params: SearchParams): Promise<SearchResult>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Target infomation. |
| params | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameters to use when searching. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SearchResult&gt; | Promise that return the Search result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) | Device not connected. |
| [33300003](../errorcode-mechanic.md#33300003-function-not-supported) | Feature not supported. |
| 33300004 | Camera not opened. |

**Example**

```TypeScript
let targetInfo: mechanicManager.TargetInfo = {
    targetType: mechanicManager.TargetType.HUMAN_FACE
};
let searchParams: mechanicManager.SearchParams = {
    direction: mechanicManager.SearchDirection.DEFAULT
}
mechanicManager.searchTarget(targetInfo,
    searchParams).then((searchResult) => {
    console.info(`'result:' ${searchResult}`);
});
```

