# searchTarget (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## searchTarget

```TypeScript
function searchTarget(target: TargetInfo, params: SearchParams): Promise<SearchResult>
```

Searching for a specified target.

**Since:** 21

<!--Device-mechanicManager-function searchTarget(target: TargetInfo, params: SearchParams): Promise<SearchResult>--><!--Device-mechanicManager-function searchTarget(target: TargetInfo, params: SearchParams): Promise<SearchResult>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [TargetInfo](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-targetinfo-i.md) | Yes |
| params | [SearchParams](../../apis-arkui/arkts-apis/arkts-arkui-atomicservice-atomicservicesearch-searchparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SearchResult](arkts-mechanic-mechanicmanager-searchresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 33300004 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-system-error) |
| [33300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300002-device-not-connected) |
| [33300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300003-function-not-supported) |

## Examples

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
